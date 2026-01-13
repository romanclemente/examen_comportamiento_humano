import tkinter as tk

# from examen_comportamiento_humano.main import main, PATH
from tkinter import (
    ttk,
    StringVar,
    OptionMenu,
    Y,
    Scrollbar,
    RIGHT,
    LEFT,
    BOTH,
)
from backend import BBDD_backend


class Revision_Examen:
    def __init__(self, dct_exam, main):
        self.master = tk.Tk()
        self.main = main
        self.master.title("Revisión de Respuestas")
        self.master.geometry("400x600")

        self.dct_exam = dct_exam
        self.questions = list(self.dct_exam.keys())

        # Crear contenedor con scrollbar usando Canvas
        container = tk.Frame(self.master)
        container.pack(fill=BOTH, expand=True)

        canvas = tk.Canvas(container)
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.answer_vars = {}

        for idx, question_num in enumerate(self.questions):
            question_data = self.dct_exam[question_num]

            question_frame = tk.Frame(
                scrollable_frame, bd=2, relief="groove", padx=10, pady=5
            )
            question_frame.pack(fill="x", padx=5, pady=5)

            tk.Label(question_frame, text=f"Pregunta {question_num }:").pack(anchor="w")
            tk.Label(
                question_frame,
                text=f"Tu respuesta actual: {question_data['mi_respuesta']}",
            ).pack(anchor="w")
            opciones = [question_data["respuesta_verdadera"]] + question_data[
                "otras_respuestas"
            ]
            if question_data["mi_respuesta"] not in opciones:
                opciones.append(question_data["mi_respuesta"])
            self.answer_vars[question_num] = StringVar(
                value=question_data["mi_respuesta"]
            )
            dropdown = OptionMenu(
                question_frame, self.answer_vars[question_num], *opciones
            )
            dropdown.pack(fill="x")
        tk.Button(
            self.master, text="Guardar Cambios y Cerrar", command=self.guardar_y_cerrar
        ).pack(pady=10)

        self.master.mainloop()

    def guardar_y_cerrar(self):
        for question_num, var in self.answer_vars.items():
            self.dct_exam[question_num]["mi_respuesta"] = var.get()
        dct = self.main.conteo_puntos()
        VentanaCorreccion(dct=dct, main1=self.main, main2=self.master)


class VentanaEstadisticas:
    def __init__(self, master, json_path):
        self.master = master
        self.json_path = json_path

    def see_score(self):
        self.new_window = tk.Toplevel(self.master)
        self.new_window.title("Tabla de Estadísticas")
        self.new_window.geometry("1000x600")
        self.new_window.configure(bg="white")
        self.new_window.resizable(True, True)  # Hacemos la ventana redimensionable

        # Marco contenedor con scroll
        container = tk.Frame(self.new_window)
        container.pack(fill=tk.BOTH, expand=True)

        columns = ("Fallos", "Aciertos", "Pregunta", "Respuesta Correcta")
        tree = ttk.Treeview(container, columns=columns, show="headings")

        # Scrollbars
        vsb = ttk.Scrollbar(container, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(container, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        hsb.pack(side=tk.BOTTOM, fill=tk.X)
        tree.pack(fill=tk.BOTH, expand=True)

        # Estilos
        style = ttk.Style()
        style.configure(
            "Treeview",
            font=("Arial", 12),
            rowheight=30,
            background="white",
            fieldbackground="white",
            foreground="#333333",
        )
        style.configure(
            "Treeview.Heading",
            font=("Arial", 13, "bold"),
            foreground="white",
            background="#007acc",
        )
        style.map("Treeview", background=[("selected", "#cce6ff")])
        tree.tag_configure("oddrow", background="#f2f2f2")
        tree.tag_configure("evenrow", background="#ffffff")

        # Encabezados y tamaños
        tree.heading("Fallos", text="Fallos")
        tree.heading("Aciertos", text="Aciertos")
        tree.heading("Pregunta", text="Pregunta")
        tree.heading("Respuesta Correcta", text="Respuesta Correcta")

        tree.column("Fallos", anchor=tk.CENTER, width=80)
        tree.column("Aciertos", anchor=tk.CENTER, width=80)
        tree.column("Pregunta", anchor=tk.W, width=400, stretch=True)
        tree.column("Respuesta Correcta", anchor=tk.W, width=300, stretch=True)

        # Cargar datos desde backend
        back = BBDD_backend(path=self.json_path, lenght_exam=1, only_fails=False)
        dct_fails, index, length, error, accurate = back.get_all_fail_questions()

        # Resumen estadístico
        summary = (
            f"Preguntas contestadas: {index} de {length} | "
            f"Aciertos: {accurate} | Fallos: {error} | "
        )
        try:
            ratio = round((accurate / (accurate + error)) * 100, 2)
            summary += f"Tasa de acierto: {ratio}%"
        except ZeroDivisionError:
            summary += "Tasa de acierto: N/A"

        summary_label = tk.Label(
            self.new_window,
            text=summary,
            font=("Arial", 13, "bold"),
            bg="white",
            fg="#333333",
            justify="left",
        )
        summary_label.pack(pady=(10, 0), anchor="w", padx=10)

        # Añadir datos a la tabla
        row_counter = 0
        for pregunta, datos in dct_fails.items():
            e_count = int(datos.get("e_count", 0))
            c_count = int(datos.get("c_count", 0))
            if e_count > 0 or c_count > 0:
                tag = "evenrow" if row_counter % 2 == 0 else "oddrow"
                tree.insert(
                    "",
                    "end",
                    values=(e_count, c_count, pregunta, datos.get("v", "")),
                    tags=(tag,),
                )
                row_counter += 1


class VentanaCorreccion:
    def __init__(self, main1, main2, dct):
        self.master = tk.Toplevel()  # ← CAMBIO CLAVE
        self.main1 = main1
        self.main2 = main2
        self.dct = dct or {}
        self.keys = list(self.dct.keys())
        self.index = 0

        self.resultado = self.main1.back.get_points()
        self.master.title("Corrección")
        self.master.geometry("400x600")
        self.master.configure(bg="white")

        self.question_label = tk.Label(
            self.master,
            text="",
            font=("Arial", 16, "bold"),
            justify="center",
            bg="white",
        )
        self.question_label.pack(pady=20, fill="both", expand=True)

        self.error_label = tk.Label(
            self.master,
            text="",
            font=("Arial", 14),
            bg="#ffcccc",
            pady=10,
            wraplength=350,
            justify="center",
        )
        self.error_label.pack(pady=10, fill="both", expand=True)

        self.correct_label = tk.Label(
            self.master, text="", font=("Arial", 14), bg="white", justify="center"
        )
        self.correct_label.pack(pady=5, fill="both", expand=True)

        self.correct_answer_label = tk.Label(
            self.master,
            text="",
            font=("Arial", 14),
            bg="#ccffcc",
            pady=10,
            wraplength=350,
            justify="center",
        )
        self.correct_answer_label.pack(pady=10, fill="both", expand=True)

        self.siguiente_button = tk.Button(
            self.master,
            text="Siguiente",
            font=("Arial", 12, "bold"),
            bg="#007bff",
            fg="white",
            width=20,
            command=self.siguiente,
        )
        self.siguiente_button.pack(pady=20)

        self.master.bind("<Configure>", self.adjust_wraplength)

        # Mostrar la primera pregunta
        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        if self.index < len(self.keys):
            current_key = self.keys[self.index]
            current_data = self.dct.get(current_key, {})

            mi_respuesta = current_data.get("mi_respuesta", "Respuesta no registrada")
            respuesta_verdadera = current_data.get(
                "respuesta_verdadera", "No disponible"
            )

            self.question_label.config(
                text=f"Has sacado un {self.resultado}, has tenido {self.main1.errores}/{self.main1.aciertos + self.main1.errores} errores en el test\n\nPara la pregunta:\n\n{current_key}\n\nelegiste:"
            )
            self.error_label.config(text=mi_respuesta)
            self.correct_label.config(text="Pero la respuesta correcta es:")
            self.correct_answer_label.config(text=respuesta_verdadera)
        else:
            self.question_label.config(
                text=f"¡Fin de la corrección!, has sacado un {self.resultado}, has tenido {self.main1.errores}/{self.main1.aciertos + self.main1.errores} errores en el test"
            )
            self.error_label.config(text="")
            self.correct_label.config(text="")
            self.correct_answer_label.config(text="")
            self.siguiente_button.config(text="Cerrar", command=self.cerrar_todo)

    def siguiente(self):
        self.index += 1
        self.mostrar_pregunta()

    def cerrar_todo(self):
        if self.main1.master.winfo_exists():
            self.main1.master.destroy()
        if self.main2.winfo_exists():
            self.main2.destroy()
        self.master.destroy()

    def adjust_wraplength(self, event):
        new_wraplength = int(event.width * 0.9)
        self.question_label.config(wraplength=new_wraplength)
        self.error_label.config(wraplength=new_wraplength)
        self.correct_answer_label.config(wraplength=new_wraplength)
