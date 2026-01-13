import os
import tkinter as tk


def buscar_jsons(ruta_base):
    rutas_json = []
    for root, _, files in os.walk(ruta_base):
        for file in files:
            if file.endswith(".json"):
                rutas_json.append(os.path.join(root, file))
    return rutas_json


def seleccionar_json(rutas_json):
    ruta_seleccionada = None

    def on_select():
        nonlocal ruta_seleccionada
        seleccion = lista_archivos.curselection()
        if seleccion:
            nombre_archivo = lista_archivos.get(seleccion[0])
            ruta_seleccionada = rutas_dict[nombre_archivo]
            ventana.quit()  # <- Sal del loop, pero no destruyas la ventana aún

    ventana = tk.Tk()
    ventana.title("Selecciona un archivo JSON")
    ventana.geometry("600x400")

    lista_archivos = tk.Listbox(ventana, width=80, height=20)
    lista_archivos.pack(padx=10, pady=10)

    rutas_dict = {}
    for ruta in rutas_json:
        nombre = os.path.basename(ruta)
        lista_archivos.insert(tk.END, nombre)
        rutas_dict[nombre] = ruta

    boton = tk.Button(ventana, text="Seleccionar", command=on_select)
    boton.pack(pady=10)

    ventana.mainloop()
    ventana.destroy()

    return ruta_seleccionada


def main_json_find():
    ruta_base = r"C:\Users\roman\Desktop\Universidad"
    rutas_json = buscar_jsons(ruta_base)

    if not rutas_json:
        print("No se encontraron archivos JSON.")
        return None

    return seleccionar_json(rutas_json)

