import tkinter as tk
from tkinter import messagebox
import random
from queue_answers import BBDD_backend
from PIL import Image, ImageTk


class TestApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Examen")
        self.master.attributes("-fullscreen", True)
        self.canvas = tk.Canvas(self.master)
        self.scrollbar = tk.Scrollbar(
            self.master, orient="vertical", command=self.canvas.yview
        )
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.back = BBDD_backend()
        self.questions = self.back.questions

        self.question_label = tk.Label(
            self.scrollable_frame, text="", wraplength=1200, justify="left"
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
            if answer.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                image = self.load_image(answer)
                radio_button = tk.Radiobutton(
                    self.scrollable_frame,
                    variable=self.answer_var,
                    value=answer,
                    indicator=0,
                    background="light blue",
                    image=image,
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
                )
            radio_button.pack(fill=tk.X, ipady=5)
            self.radio_buttons.append(radio_button)

    def load_image(self, path):
        image = Image.open(path)
        image = image.resize((550, 400), Image.LANCZOS)
        return ImageTk.PhotoImage(image)

    def load_question(self):
        if not self.questions:
            messagebox.showinfo("Nota Final", f"Tienes un {self.back.get_points()}")
            self.master.quit()
            return

        index_ask = random.randint(0, len(self.questions) - 1)
        self.current_question = list(self.questions)[index_ask]
        question_text = self.current_question

        for label in self.image_labels:
            label.destroy()
        self.image_labels.clear()

        # Reemplazar las rutas de imágenes en el enunciado con las imágenes
        if (
            "images" in self.questions[self.current_question]
            and "Images" in self.current_question
        ):
            images = self.questions[self.current_question]["images"]
            for img_path in images:
                img = self.load_image(img_path)
                img_label = tk.Label(self.scrollable_frame, image=img)
                img_label.image = img
                question_text = question_text.replace(img_path, "")
                self.question_label.config(text=question_text)
                img_label.pack()
                self.image_labels.append(img_label)
        else:
            self.question_label.config(text=question_text)

        try:
            v_answers = self.questions[self.current_question]["v"]
            f_answers = self.questions[self.current_question]["f"]
            correct_answer = v_answers
            sample_size = min(3, len(f_answers))
            answers = [correct_answer] + random.sample(f_answers, sample_size)
            random.shuffle(answers)
            self.create_radio_buttons(answers)
        except TypeError:
            self.E1 = tk.Entry(self.scrollable_frame, bd=5)
            self.E1.pack(side=tk.BOTTOM)

        if self.submit_button is None:
            self.submit_button = tk.Button(
                self.scrollable_frame, text="Submit", command=self.check_answer
            )
            self.submit_button.pack()

    def enable_submit(self):
        self.submit_button.config(state=tk.NORMAL)

    def check_answer(self):
        try:
            correct_answer = self.questions[self.current_question]["v"]
            selected_answer = self.answer_var.get()
            if selected_answer == correct_answer:
                messagebox.showinfo("Respuesta", "¡Correcto!")
                self.back.sum_points()
            else:
                messagebox.showerror(
                    "Respuesta",
                    f"Incorrecto. La respuesta correcta es: {correct_answer}",
                )
                self.back.quit_points()
            self.questions.pop(self.current_question)
            self.remove_old_question()
        except TypeError:
            correct_answer = self.questions[self.current_question]
            if str(self.E1.get()).lower() == correct_answer.lower():
                messagebox.showinfo("Respuesta", "¡Correcto!")
                self.back.sum_points()
            else:
                messagebox.showerror(
                    "Respuesta",
                    f"Incorrecto. La respuesta correcta es: {correct_answer}",
                )
                self.back.quit_points()
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


def main():
    root = tk.Tk()
    app = TestApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
