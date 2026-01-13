import tkinter as tk
from tkinter import ttk, messagebox
from vistas import Revision_Examen
from backend import BBDD_backend
import random


class Examen_App:
    def __init__(
        self,
        master,
        path,
        num_questions,
        difficulty=None,
        clean_ddbb=False,
        only_fail=False,
    ):
        self.answer_var = tk.StringVar(value="")
        self.Revision_Examen = None
        self.previous_ask = ""
        self.dct_exam = {}
        self.index_actual_question = 1
        self.aciertos = 0
        self.errores = 0
        self.ask_route = None
        self.master = master
        self.master.title("Examen")
        self.master.geometry("1200x800")
        self.master.resizable(True, True)

        style = ttk.Style(self.master)
        style.configure("Answer.TButton", font=("Helvetica", 16), padding=10)
        style.configure(
            "Danger.TButton",
            font=("Helvetica", 14),
            foreground="black",
            background="red",
        )
        style.map("Danger.TButton", background=[("active", "#cc0000")])

        # Scrollable frame
        self.container = ttk.Frame(self.master)
        self.canvas = tk.Canvas(self.container, borderwidth=0, background="#f0f0f0")
        self.scrollbar = ttk.Scrollbar(
            self.container, orient="vertical", command=self.canvas.yview
        )
        self.scrollable_frame = ttk.Frame(self.canvas)

        # Frame centrado dentro del scrollable_frame
        self.inner_frame = ttk.Frame(self.scrollable_frame, padding=20)
        self.inner_frame.pack()

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        self.canvas.create_window(
            (0, 0), window=self.scrollable_frame, anchor="n", tags="frame"
        )
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", self._center_frame)  # ← Centrado dinámico

        self.container.pack(fill="both", expand=True)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Backend
        if isinstance(clean_ddbb, tuple) and clean_ddbb[1]:
            self.back = BBDD_backend(
                path=path,
                lenght_exam=num_questions,
                only_fails=only_fail,
                news_quest=clean_ddbb[1],
                difficulty=difficulty,
            )
        else:
            self.back = BBDD_backend(
                path=path,
                lenght_exam=num_questions,
                news_quest=clean_ddbb[1],
                only_fails=only_fail,
                difficulty=difficulty,
            )

        if isinstance(clean_ddbb, tuple) and clean_ddbb[0]:
            self.back.clean_bbdd()

        self.questions = self.back.questions

        # UI widgets
        self.question_label = ttk.Label(
            self.inner_frame,
            text="",
            wraplength=1100,
            justify="left",
            font=("Helvetica", 22),
        )
        self.question_label.pack(pady=(20, 10))

        self.image_labels = []
        self.E1 = None
        self.submit_button = None
        self.back_button = None
        self.radio_buttons = []

        self.selected_label = ttk.Label(
            self.inner_frame,
            text="Opción seleccionada: Ninguna",
            font=("Helvetica", 22),
            foreground="green",
        )
        self.selected_label.pack(pady=(0, 20))

        self.load_question()

    def _center_frame(self, event):
        canvas_width = event.width
        self.canvas.itemconfig("frame", width=canvas_width)

    def conteo_puntos(self):
        tmp = {}
        try:
            for q_id, q_data in self.dct_exam.items():
                correcta = q_data.get("respuesta_verdadera")
                usuario = q_data.get("mi_respuesta")
                if correcta is None or usuario is None:
                    continue
                if correcta == usuario:
                    self.aciertos += 1
                    self.back.sum_points(q_id)
                else:
                    self.errores += 1
                    self.back.quit_points(q_id)
                    tmp[q_id] = self.dct_exam[q_id]
            return tmp
        except Exception as ex:
            messagebox.showerror("Error en conteo de puntos", str(ex))

    def correccion_examen(self):
        self.Revision_Examen = Revision_Examen(self.dct_exam, self)

    def load_question(self, back=None):
        salto_de_linea = " "
        if not self.questions:
            self.correccion_examen()
            return

        # Elegir pregunta
        self.current_question = back or random.choice(list(self.questions))

        data = self.questions.get(self.current_question)
        if not data:
            messagebox.showerror("Error", "Pregunta mal definida o no encontrada.")
            return
        if "enunciado" in data.keys() or (
            "enunciado" not in data.keys() and ".txt" in self.current_question
        ):
            salto_de_linea = "\n\n\n"

            if "enunciado" in data.keys():
                self.ask_route = self.current_question
                self.current_question = data["enunciado"]
            else:
                self.ask_route = self.current_question
                self.current_question = f"{self.back.leer_contenido_si_fichero(
                    self.current_question
                )}"

        self.question_label.config(
            text=f"{self.index_actual_question}º{salto_de_linea}{self.current_question}",
            justify="left",
            anchor="w",
        )

        # Mostrar posibles respuestas o entrada libre
        try:
            answers = [data["v"]] + data["f"]
            random.shuffle(answers)
            self.create_radio_buttons(answers)
        except (KeyError, TypeError):
            self.E1 = ttk.Entry(self.scrollable_frame, font=("Helvetica", 25))
            self.E1.pack(pady=10)

        self.configure_buttons()

    def configure_buttons(self):
        if not self.submit_button or not self.submit_button.winfo_exists():
            self.submit_button = tk.Button(
                self.scrollable_frame,
                text="✅ Siguiente",
                command=self.check_answer,
                font=("Helvetica", 18, "bold"),
                bg="#4CAF50",  # verde fuerte
                fg="white",
                activebackground="#45a049",
                padx=20,
                pady=15,
            )
            self.submit_button.pack(pady=20, fill="x")

        if not self.back_button or not self.back_button.winfo_exists():
            self.back_button = tk.Button(
                self.scrollable_frame,
                text="🔙 Atrás",
                command=self.previous_question,
                font=("Helvetica", 18, "bold"),
                bg="#2196F3",  # azul fuerte
                fg="white",
                activebackground="#1976D2",
                padx=20,
                pady=15,
            )
            self.back_button.pack(pady=10, fill="x")

        if not hasattr(self, "delete_button") or not self.delete_button.winfo_exists():
            delete_frame = ttk.Frame(self.scrollable_frame)
            delete_frame.pack(
                pady=50, anchor="e", fill="x", padx=20
            )  # Lo empuja a la derecha con margen
            self.delete_button = ttk.Button(
                delete_frame,
                text="Eliminar esta pregunta",
                command=self.confirm_delete_question,
                style="Danger.TButton",
            )
            self.delete_button.pack(anchor="e")

    def confirm_delete_question(self):
        if not self.current_question:
            return
        confirm = messagebox.askyesno(
            "¿Eliminar pregunta?",
            "¿Estás seguro de que deseas eliminar esta pregunta del examen y del archivo JSON?",
        )
        if confirm:
            self.delete_question()

    def delete_question(self):
        try:
            pregunta = self.current_question
            if not pregunta:
                return

            # Eliminar de preguntas actuales y archivo
            self.back.remove_question(pregunta)

            # Eliminar de diccionario de preguntas del examen
            self.questions.pop(pregunta, None)
            self.dct_exam.pop(pregunta, None)

            self.remove_old_question()
            self.index_actual_question += 1
            self.answer_var.set("")

            self.load_question()
        except Exception as ex:
            messagebox.showerror("Error eliminando pregunta", str(ex))

    def set_val(self, value):
        self.answer_var.set(value)
        self.selected_label.config(text=f"Opción seleccionada: {value}")

    def create_radio_buttons(self, answers):
        for rb in self.radio_buttons:
            rb.destroy()
        self.radio_buttons.clear()

        for answer in answers:
            btn = ttk.Button(
                self.inner_frame,  # ← usa el frame centrado
                text=answer,
                command=lambda val=answer: self.set_val(val),
                style="Answer.TButton",  # ← estilo personalizado
            )
            btn.pack(
                fill="x", padx=40, pady=10
            )  # ← márgenes laterales y separación vertical
            self.radio_buttons.append(btn)

    def enable_submit(self):
        if self.submit_button and self.submit_button.winfo_exists():
            self.submit_button.config(state=tk.NORMAL)
        if self.back_button and self.back_button.winfo_exists():
            self.back_button.config(state=tk.NORMAL)

    def check_answer(self):
        selected_answer = self.answer_var.get()
        if selected_answer:
            try:
                self.index_actual_question += 1
                self.previous_ask = self.current_question

                self.dct_exam[self.current_question] = {
                    "mi_respuesta": selected_answer,
                    "respuesta_verdadera": self.questions[self.current_question]["v"],
                    "otras_respuestas": self.questions[self.current_question]["f"],
                }

                self.questions.pop(self.current_question, None)
                self.remove_old_question()
                self.answer_var.set("")
                self.load_question()
            except Exception as ex:
                self.index_actual_question += 1
                self.previous_ask = self.current_question

                self.dct_exam[self.ask_route] = {
                    "mi_respuesta": selected_answer,
                    "respuesta_verdadera": self.questions[self.ask_route]["v"],
                    "otras_respuestas": self.questions[self.ask_route]["f"],
                }
                self.questions.pop(self.ask_route, None)
                self.ask_route = None
                self.remove_old_question()
                self.answer_var.set("")
                self.load_question()
        else:
            messagebox.showwarning(
                "Advertencia", "Selecciona una respuesta antes de continuar."
            )

    def previous_question(self):
        if self.index_actual_question > 1 and self.previous_ask in self.dct_exam:
            self.index_actual_question -= 1
            self.remove_old_question()
            self.questions[self.previous_ask] = {
                "v": self.dct_exam[self.previous_ask]["respuesta_verdadera"],
                "f": self.dct_exam[self.previous_ask]["otras_respuestas"],
            }
            self.answer_var.set(self.dct_exam[self.previous_ask]["mi_respuesta"])
            self.load_question(back=self.previous_ask)
        else:
            messagebox.showinfo("Info", "No hay pregunta anterior.")

    def remove_old_question(self):
        self.current_question = ""
        self.question_label.config(text="")

        for rb in self.radio_buttons:
            rb.destroy()
        self.radio_buttons.clear()

        if self.E1:
            self.E1.destroy()
            self.E1 = None

        if self.submit_button:
            self.submit_button.destroy()
            self.submit_button = None
        if self.back_button:
            self.back_button.destroy()
            self.back_button = None

        for img in self.image_labels:
            img.destroy()
        self.image_labels.clear()
