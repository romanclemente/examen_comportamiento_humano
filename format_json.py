import os
import json
import hashlib

# Archivo para almacenar los hashes de los JSON procesados
PROCESSED_FILES_LOG = "processed_files.log"


def get_file_hash(file_path):
    """Genera un hash único para un archivo dado."""
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        hasher.update(f.read())
    return hasher.hexdigest()


def is_file_processed(file_hash):
    """Verifica si un archivo ya ha sido procesado."""
    if not os.path.exists(PROCESSED_FILES_LOG):
        return False
    with open(PROCESSED_FILES_LOG, "r") as f:
        return file_hash in f.read()


def mark_file_as_processed(file_hash):
    """Marca un archivo como procesado escribiendo su hash en el log."""
    with open(PROCESSED_FILES_LOG, "a") as f:
        f.write(file_hash + "\n")


def wrap_text(text, max_length=75):
    """Elimina saltos de línea previos y añade saltos de línea con guion en palabras largas."""
    text = text.replace("\n", " ").strip()  # Elimina saltos de línea existentes
    wrapped = []
    while len(text) > max_length:
        split_point = max_length
        if text[split_point] != " ":
            while split_point > 0 and text[split_point] not in (" ", "\t"):
                split_point -= 1
            if (
                split_point == 0
            ):  # Si no encuentra espacio, corta en el límite y añade guion
                split_point = max_length
                wrapped.append(text[:split_point] + "-")
            else:
                wrapped.append(text[:split_point])
        else:
            wrapped.append(text[:split_point])
        text = text[split_point:].lstrip()
    wrapped.append(text)
    return "\n".join(wrapped)


def process_json_file(file_path):
    """Procesa un archivo JSON para añadir saltos de línea en strings largos, incluidas las claves."""
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"Error al decodificar JSON en: {file_path}")
            return False

    def process_value(value):
        if isinstance(value, str):
            return wrap_text(value)
        elif isinstance(value, list):
            return [process_value(v) for v in value]
        elif isinstance(value, dict):
            return {wrap_text(k): process_value(v) for k, v in value.items()}
        return value

    processed_data = process_value(data)

    # Sobrescribe el archivo JSON con el contenido modificado
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=4)
    return True


def process_directory(directory):
    """Busca y procesa todos los archivos JSON en un directorio y sus subdirectorios."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                file_hash = get_file_hash(file_path)

                if is_file_processed(file_hash):
                    print(f"Archivo ya procesado: {file_path}")
                    continue

                print(f"Procesando archivo: {file_path}")
                if process_json_file(file_path):
                    mark_file_as_processed(file_hash)
                    print(f"Archivo procesado con éxito: {file_path}")
                else:
                    print(f"Fallo al procesar el archivo: {file_path}")


def limpiar_respuestas_duplicadas_en_json_recursivo(ruta_base):
    for root, _, files in os.walk(ruta_base):
        for archivo in files:
            if archivo.endswith(".json"):
                ruta_completa = os.path.join(root, archivo)
                try:
                    with open(ruta_completa, "r", encoding="utf-8") as f:
                        datos = json.load(f)

                    modificado = False
                    for pregunta, contenido in datos.items():
                        if not isinstance(contenido, dict):
                            continue
                        correcta = contenido.get("v")
                        falsas = contenido.get("f", [])

                        if isinstance(falsas, list) and correcta in falsas:
                            contenido["f"] = [
                                resp for resp in falsas if resp != correcta
                            ]
                            modificado = True
                        if isinstance(correcta, list):
                            contenido["e_count"] = 10
                            contenido["v"] = contenido["v"][0]
                            modificado = True

                    if modificado:
                        with open(ruta_completa, "w", encoding="utf-8") as f:
                            json.dump(datos, f, ensure_ascii=False, indent=4)
                        print(f"Corregido: {ruta_completa}")

                except Exception as e:
                    print(f"Error al procesar {ruta_completa}: {e}")


# USO


if __name__ == "__main__":
    # limpiar_respuestas_duplicadas_en_json_recursivo(r"C:\Users\roman\Desktop\Apuntes")
    process_directory(r"C:\Users\roman\Desktop\Apuntes")
