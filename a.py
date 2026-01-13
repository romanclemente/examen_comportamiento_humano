from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json
import time
from urllib.parse import urljoin

BASE_URL = "https://darksouls.wiki.fextralife.com"
MAIN_URL = f"{BASE_URL}/Weapons"


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Comenta esta línea para ver el navegador
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )


def get_weapons_section(driver):
    driver.get(MAIN_URL)
    time.sleep(3)  # Esperar a que cargue JavaScript
    soup = BeautifulSoup(driver.page_source, "html.parser")

    start_tag = soup.find(
        "h2", class_="titlearea", string=lambda t: "armas" in t.lower()
    )
    end_tag = soup.find("div", class_="row gallery")

    content = []
    current = start_tag
    while current and current != end_tag:
        content.append(current)
        current = current.find_next_sibling()
    content.append(end_tag)

    return content


def extract_weapons(section):
    # Solo procesamos la galería
    soup = BeautifulSoup("".join(str(tag) for tag in section), "html.parser")
    gallery = soup.find("div", class_="row gallery")
    weapons = {}

    for div in gallery.find_all("div", class_="col-xs-6 col-sm-2"):
        a = div.find("a", class_="wiki_link", href=True)
        if not a:
            continue

        name = a.get("title") or a.text.strip()
        href = a["href"]
        url = urljoin(BASE_URL, href)

        # Evita enlaces a categorías (que luego cargan más armas)
        if (
            "Weapons" in href
            or "weapon" in name.lower()
            or name.lower().startswith("dark souls")
        ):
            continue  # 🔥 Esto filtra cosas como "Dark Souls Daggers"

        weapons[name] = {"url": url}

    return weapons


def get_weapon_details(driver, url):
    driver.get(url)
    time.sleep(1.5)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # --- Procesar tabla ---
    table_data = {}
    table = soup.find("table", class_="wiki_table")
    if table:
        current_key = None
        for row in table.find_all("tr"):
            cols = row.find_all("td")
            if not cols:
                continue
            images = [img["alt"] for img in row.find_all("img", alt=True)]
            texts = [
                col.get_text(strip=True) for col in cols if col.get_text(strip=True)
            ]

            # Caso: imagen y valor => clave: imagen alt, valor: texto
            if images and texts:
                for i, img in enumerate(images):
                    value = texts[i] if i < len(texts) else ""
                    table_data[img] = value

            # Caso: fila con texto tipo clave-valor
            elif len(texts) == 2:
                table_data[texts[0]] = texts[1]

            # Caso: lista de valores sin clave
            elif len(texts) > 2:
                table_data[f"Fila {len(table_data)+1}"] = texts

    # --- Procesar descripción ---
    description = ""
    content = soup.find("div", class_="wiki-content")
    if content:
        paragraphs = content.find_all(["p", "font"], recursive=True)
        for p in paragraphs:
            text = p.get_text(strip=True)
            if (
                len(text) > 30
                and "wikidot" not in text
                and "back to" not in text.lower()
            ):
                description = text
                break

    return {"tabla": table_data, "descripcion": description}


def main():
    driver = setup_driver()
    try:
        section = get_weapons_section(driver)
        weapons = extract_weapons(section)

        print(f"Encontradas {len(weapons)} armas. Procesando...")

        for name, data in weapons.items():
            print(f"- {name}")
            try:
                details = get_weapon_details(driver, data["url"])
                weapons[name].update(details)
            except Exception as e:
                print(f"  Error en {name}: {e}")
            time.sleep(1.5)  # Evitar bloqueo

        with open("dark_souls_weapons.json", "w", encoding="utf-8") as f:
            json.dump(weapons, f, ensure_ascii=False, indent=2)

        print("✅ Datos guardados en 'dark_souls_weapons.json'")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
