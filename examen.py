import tkinter as tk
from tkinter import messagebox
import random
from queue_answers import BBDD_backend
from PIL import Image, ImageTk
import sys


class TestApp:
    def __init__(
        self,
        master,
        num_questions,
        clean_ddbb=False,
        to_the_fail=False,
        only_fail=False,
    ):
        self.to_the_fail = to_the_fail
        self.master = master
        self.master.title("Examen")
        self.master.attributes("-fullscreen", False)
        self.container = tk.Frame(self.master)
        self.container.pack(fill="both", expand=True)
        self.canvas = tk.Canvas(self.container)
        self.scrollbary = tk.Scrollbar(
            self.container,
            activebackground="red",
            bg="blue",
            orient="vertical",
            command=self.canvas.yview,
        )
        self.scrollbarx = tk.Scrollbar(
            self.container,
            activebackground="red",
            bg="blue",
            orient="horizontal",
            command=self.canvas.xview,
        )
        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbary.set)
        self.canvas.configure(xscrollcommand=self.scrollbarx.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbary.pack(side="right", fill="y")
        self.scrollbarx.pack(side="bottom", fill="x")

        self.back = BBDD_backend(lenght_exam=num_questions, only_fails=only_fail)
        if clean_ddbb:
            self.back.clean_bbdd()
        self.questions = self.back.questions

        self.index_actual_question = 1
        self.aciertos = 0
        self.errores = 0

        self.question_label = tk.Label(
            self.scrollable_frame,
            text="",
            wraplength=2000,
            justify="left",
            font=("Helvetica", 20),
        )
        self.question_label.pack()
        self.image_labels = []
        self.E1 = None
        self.answer_var = tk.StringVar()
        self.answer_var.set(None)
        self.submit_button = None
        self.radio_buttons = []
        self.load_question()

    def create_radio_buttons(self, answers):
        for answer in answers:
            if answer.lower().endswith((".png", ".jpg", ".jpeg")):
                image = self.load_image(answer)
                radio_button = tk.Radiobutton(
                    self.scrollable_frame,
                    variable=self.answer_var,
                    value=answer,
                    indicator=0,
                    background="light blue",
                    image=image,
                    font=("Helvetica", 20),
                )
                radio_button.image = image
            else:
                radio_button = tk.Radiobutton(
                    self.scrollable_frame,
                    text=answer,
                    variable=self.answer_var,
                    value=answer,
                    indicator=0,
                    background="light blue",
                    font=("Helvetica", 20),
                )
            radio_button.pack(fill=tk.X, ipady=10)
            self.radio_buttons.append(radio_button)

    def load_image(self, path):
        image = Image.open(path)
        image = image.resize((1100, 800), Image.LANCZOS)
        return ImageTk.PhotoImage(image)

    def load_question(self):
        if not self.questions:
            messagebox.showinfo("Nota Final", f"Tienes un {self.back.get_points()}")
            self.master.quit()
            sys.exit()
        elif self.to_the_fail:
            if self.errores >= 5:
                points_per_question = 10 / self.index_actual_question
                positive = points_per_question * self.aciertos
                negative = points_per_question * -1 * self.errores
                messagebox.showinfo("Nota Final", f"Tienes un {positive + negative}")
                self.master.quit()
                sys.exit()

        index_ask = random.randint(0, len(self.questions) - 1)
        self.current_question = list(self.questions)[index_ask]
        question_text = self.current_question

        for label in self.image_labels:
            label.destroy()
        self.image_labels.clear()

        if (
            "images" in self.questions[self.current_question]
            and "Image" in self.current_question
            and self.current_question.lower().endswith((".png", ".jpg", ".jpeg"))
        ):
            images = self.questions[self.current_question]["images"]
            for img_path in images:
                img = self.load_image(img_path)
                img_label = tk.Label(self.scrollable_frame, image=img)
                img_label.image = img
                question_text = question_text.replace(img_path, "")
                self.image_labels.append(img_label)
                img_label.pack()

        self.question_label.config(
            text=f"{self.index_actual_question}º {question_text}"
        )

        try:
            v_answers = self.questions[self.current_question]["v"]
            f_answers = self.questions[self.current_question]["f"]
            correct_answer = v_answers
            sample_size = min(3, len(f_answers))
            answers = [correct_answer] + random.sample(f_answers, sample_size)
            random.shuffle(answers)
            self.create_radio_buttons(answers)
        except TypeError:
            self.E1 = tk.Entry(self.scrollable_frame, bd=5, font=("Helvetica", 20))
            self.E1.pack(side=tk.BOTTOM)

        if self.submit_button is None:
            self.submit_button = tk.Button(
                self.scrollable_frame,
                text="Submit",
                command=self.check_answer,
                font=("Helvetica", 20),
            )
            self.submit_button.pack()

    def enable_submit(self):
        self.submit_button.config(state=tk.NORMAL)

    def check_answer(self):
        self.index_actual_question += 1
        try:
            correct_answer = self.questions[self.current_question]["v"]
            selected_answer = self.answer_var.get()
            if selected_answer == correct_answer:
                self.aciertos += 1
                self.back.sum_points(self.current_question)
                if self.to_the_fail:
                    messagebox.showinfo(
                        "Respuesta",
                        f"¡Correcto!",
                    )
                else:
                    messagebox.showinfo(
                        "Respuesta",
                        f"¡Correcto! llevas hasta ahora:\n{self.aciertos} aciertos y \n {self.errores} fallo/s\n por tanto llevas una nota de {float(self.back.get_points())}",
                    )
            else:
                self.errores += 1
                self.back.quit_points(self.current_question)
                if self.to_the_fail:
                    messagebox.showerror(
                        "Respuesta",
                        f"Incorrecto. La respuesta correcta es:\n{correct_answer}",
                    )
                else:
                    messagebox.showerror(
                        "Respuesta",
                        f"Incorrecto. La respuesta correcta es:\n{correct_answer}, llevas hasta ahora:\n {self.aciertos} acierto/s y \n {self.errores} fallo/s\n por tanto llevas una nota de {float(self.back.get_points())}",
                    )
            self.questions.pop(self.current_question)
            self.remove_old_question()
        except TypeError:
            correct_answer = self.questions[self.current_question]
            if str(self.E1.get()).lower() == correct_answer.lower():
                messagebox.showinfo("Respuesta", "¡Correcto!")
                self.back.sum_points(self.current_question)
            else:
                messagebox.showerror(
                    "Respuesta",
                    f"Incorrecto. La respuesta correcta es: {correct_answer}",
                )
                self.back.quit_points(self.current_question)
            self.E1.delete(0, tk.END)
            self.E1.destroy()
            if self.submit_button:
                self.submit_button.destroy()
                self.submit_button = None
            self.questions.pop(self.current_question)
        self.load_question()

    def remove_old_question(self):
        self.current_question = ""
        self.question_label.config(text="")
        for radio_button in self.radio_buttons:
            radio_button.destroy()
        self.radio_buttons.clear()
        if self.submit_button:
            self.submit_button.destroy()
            self.submit_button = None
        for label in self.image_labels:
            label.destroy()
        self.image_labels.clear()


class StartApp:
    def __init__(self, master):
        self.only_fails = False
        self.to_the_fail = False
        self.master = master
        self.master.title("Inicio")
        self.master.geometry("400x300")

        self.label = tk.Label(
            self.master, text="Seleccione una opción", font=("Helvetica", 16)
        )
        self.label.pack(pady=20)

        self.button1 = tk.Button(
            self.master, text="Examen normal", command=self.setup_questions
        )
        self.button1.pack(pady=10)

        self.button2 = tk.Button(
            self.master, text="Preguntas al fallo", command=self.to_the_fail_mode
        )
        self.button2.pack(pady=10)

        self.button3 = tk.Button(
            self.master, text="Todos mis fallos anteriores", command=self.all_fail
        )
        self.button3.pack(pady=10)

    def setup_questions(self):
        self.new_window = tk.Toplevel(self.master)
        self.new_window.title("Configurar Preguntas")
        self.new_window.geometry("300x200")

        self.label = tk.Label(
            self.new_window, text="Seleccione la cantidad de preguntas"
        )
        self.label.pack(pady=10)

        self.num_questions = tk.IntVar(value=5)
        self.spinbox = tk.Spinbox(
            self.new_window, from_=5, to=100, textvariable=self.num_questions
        )
        self.spinbox.pack(pady=10)

        self.checkbox_var = tk.IntVar()
        self.checkbox = tk.Checkbutton(
            self.new_window,
            text="¿Limpiar aciertos y fallos?",
            variable=self.checkbox_var,
        )
        self.checkbox.pack(pady=10)

        self.start_button = tk.Button(
            self.new_window, text="Iniciar Examen", command=self.start_exam
        )
        self.start_button.pack(pady=10)

    def start_exam(self):
        try:
            num_questions = self.num_questions.get()
        except Exception:
            num_questions = self.num_questions

        try:
            checkbox_value = self.checkbox_var.get()
        except Exception:
            checkbox_value = self.checkbox_var

        self.new_window.destroy()
        self.master.destroy()
        root = tk.Tk()
        app = TestApp(
            root,
            num_questions,
            bool(checkbox_value),
            to_the_fail=self.to_the_fail,
            only_fail=self.only_fails,
        )
        root.mainloop()

    def to_the_fail_mode(self):
        self.to_the_fail = True
        back = BBDD_backend(lenght_exam=5)
        self.num_questions = len(back.all_questions)
        self.new_window = tk.Toplevel(self.master)
        self.new_window.title("Preguntas al fallo")
        self.new_window.geometry("300x200")

        self.label = tk.Label(
            self.new_window,
            text="Preguntas de examen hasta llegar al máximo de 5 errores",
        )
        self.label.pack(pady=10)

        self.checkbox_var = tk.IntVar()
        self.checkbox = tk.Checkbutton(
            self.new_window,
            text="¿Limpiar aciertos y fallos?",
            variable=self.checkbox_var,
        )
        self.checkbox.pack(pady=10)

        self.start_button = tk.Button(
            self.new_window, text="Iniciar Examen", command=self.start_exam
        )
        self.start_button.pack(pady=10)

    def all_fail(self):
        self.new_window = tk.Toplevel(self.master)
        self.new_window.title("Recordando fallos")
        self.new_window.geometry("300x200")
        self.num_questions = 200
        self.checkbox_var = False
        self.only_fails = True
        self.start_button = tk.Button(
            self.new_window, text="Iniciar Examen", command=self.start_exam
        )
        self.start_button.pack(pady=10)


def main():
    root = tk.Tk()
    app = StartApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
