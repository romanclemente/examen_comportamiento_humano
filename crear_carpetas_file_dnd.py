import os

ruta_base = r"C:\Users\roman\Desktop\dnd"

if not os.path.exists(ruta_base):
    print(f"La ruta {ruta_base} no existe.")
else:
    for i in range(23, 101):
        carpeta = os.path.join(ruta_base, str(i))
        try:
            os.makedirs(carpeta, exist_ok=True)
            txt_path = os.path.join(carpeta, "enlace.txt")
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write("")
            print(f"Carpeta y archivo creados: {txt_path}")
        except Exception as e:
            print(f"Error creando la carpeta o archivo en {carpeta}: {e}")