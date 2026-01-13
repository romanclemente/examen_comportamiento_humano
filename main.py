import tkinter as tk
from tkinter import ttk
from ventana_examen import Examen_App
from vistas import VentanaEstadisticas
from tkinter import StringVar
from cargar_json import main_json_find


class Main_App:
    def __init__(self, master, json_path):
        self.count_down_spinner = 0
        self.only_fails = False
        self.master = master
        self.master.title("Menú Principal")
        self.json_path = json_path
        if not self.json_path:
            tk.messagebox.showerror("Error", "No se seleccionó ningún archivo JSON.")
            self.master.destroy()
            return
        self.master.geometry("500x400")
        self.master.configure(bg="#f0f0f0")
        self.difficulty = None
        self.spinbox = None
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=6)
        style.configure("TLabel", font=("Helvetica", 14))

        title = ttk.Label(self.master, text="Seleccione una opción")
        title.pack(pady=30)

        self.button_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.button_frame.pack()

        self._add_main_buttons()

    def _add_main_buttons(self):
        ttk.Button(
            self.button_frame,
            text="Examen normal",
            width=30,
            command=self.setup_questions,
        ).pack(pady=10)
        ttk.Button(
            self.button_frame,
            text="Todos mis fallos anteriores",
            width=30,
            command=self.all_fail,
        ).pack(pady=10)
        ttk.Button(
            self.button_frame,
            text="Ver Tabla de Fallos",
            width=30,
            command=self.see_score,
        ).pack(pady=10)

    def see_score(self):
        app = VentanaEstadisticas(self.master, json_path=self.json_path)
        app.see_score()

    def setup_questions(self):
        self.new_window = tk.Toplevel(self.master)
        self.new_window.title("Configurar Preguntas")
        self.new_window.geometry("300x300")
        self.new_window.configure(bg="#ffffff")

        frame = ttk.LabelFrame(self.new_window, text="Configuración del Examen")
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        ttk.Label(frame, text="Cantidad de preguntas:").pack(pady=5)
        self.num_questions = tk.IntVar(value=10)
        self.spinbox = ttk.Spinbox(
            frame, from_=1, to=300, textvariable=self.num_questions, width=10
        )
        self.spinbox.pack(pady=5)

        self.checkbox_var = tk.IntVar(value=0)
        self.checkbox_preguntas_nuevas_val = tk.IntVar(value=0)

        ttk.Checkbutton(
            frame, text="¿Limpiar aciertos y fallos?", variable=self.checkbox_var
        ).pack(pady=5)

        ttk.Checkbutton(
            frame,
            text="¿Preguntas nuevas?",
            variable=self.checkbox_preguntas_nuevas_val,
        ).pack(pady=5)

        ttk.Button(frame, text="Iniciar Examen", command=self.start_exam).pack(pady=10)

    def all_fail(self):
        def set_difficulty():
            selected = clicked.get()
            mapping = {"Facil": 10, "Medio": 13, "Dificil": 15, "Hard": 20}
            self.num_questions = mapping.get(selected, 10)
            self.difficulty = selected
            self.start_exam()

        self.new_window = tk.Toplevel(self.master)
        self.new_window.title("Recordando fallos")
        self.new_window.geometry("300x200")
        self.new_window.configure(bg="#ffffff")

        self.checkbox_var = False
        self.only_fails = True

        frame = ttk.LabelFrame(self.new_window, text="Selecciona Dificultad")
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        options = ["Facil", "Medio", "Dificil", "Hard"]
        clicked = StringVar(self.new_window)
        clicked.set(options[0])

        option_menu = ttk.OptionMenu(frame, clicked, options[0], *options)
        option_menu.pack(pady=10)

        ttk.Button(frame, text="Iniciar Examen", command=set_difficulty).pack(pady=10)

    def start_exam(self):
        try:
            self.spinbox.update()
            if self.spinbox.get() == "":
                num_questions = 10
            else:
                num_questions = int(self.spinbox.get())

            checkbox_value = self.checkbox_var.get()
            checkbox_value_preguntas_nuevas = self.checkbox_preguntas_nuevas_val.get()
            self.crear_examen(
                cantidad_preguntas=num_questions,
                limpiar_historial_preguntas=checkbox_value,
                solo_preguntas_nuevas=checkbox_value_preguntas_nuevas,
            )
        except (AttributeError, tk.TclError):
            self.crear_examen(
                cantidad_preguntas=self.num_questions,
                limpiar_historial_preguntas=False,
                solo_preguntas_nuevas=False,
                solo_fallos=True,
            )

    def crear_examen(
        self,
        cantidad_preguntas=10,
        limpiar_historial_preguntas=False,
        solo_preguntas_nuevas=True,
        solo_fallos=False,
    ):
        try:
            self.new_window.destroy()
        except Exception:
            pass

        self.master.destroy()
        root = tk.Tk()

        Examen_App(
            root,
            path=self.json_path,
            num_questions=cantidad_preguntas,
            clean_ddbb=(
                bool(limpiar_historial_preguntas),
                bool(solo_preguntas_nuevas),
            ),
            difficulty=self.difficulty,
            only_fail=solo_fallos,
        )
        root.mainloop()


def main(path):
    root = tk.Tk()
    Main_App(root, json_path=path)
    root.mainloop()


if __name__ == "__main__":
    main(main_json_find())
