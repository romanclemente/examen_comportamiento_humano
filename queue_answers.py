import random
import os
import json


class BBDD_backend:
    def __init__(self) -> None:
        self.all_questions = self.get_preguntas()
        self.questions = self.preguntas_examen()
        self.total_points = 0.0
        self.points_per_question = 10 / len(list(self.questions))

    def get_preguntas(self):
        with open(
            "lote_preguntas/p_a_2_0.json",
            "r",
            encoding="utf-8",
        ) as file:
            datos = json.load(file)
        return datos

    def sum_points(self, current_question):
        c_q = self.all_questions[current_question]
        if "c_count" in c_q:
            c_q["c_count"] = 1 + int(c_q["c_count"])
        else:
            c_q["c_count"] = 1
        self.total_points += self.points_per_question
        self.write_in_preguntas()

    def quit_points(self, current_question):
        c_q = self.all_questions[current_question]
        if "e_count" in c_q:
            c_q["e_count"] = 1 + int(c_q["e_count"])
        else:
            c_q["e_count"] = 1
        self.total_points -= self.points_per_question
        self.write_in_preguntas()

    def preguntas_examen(self):
        asks = list(self.all_questions)
        dct = {}
        index = 0
        for x in asks:
            if (
                "e_count" in self.all_questions[x]
                and int(self.all_questions[x]["e_count"]) > 0
            ):
                if "c_count" not in self.all_questions[x] or (
                    "c_count" in self.all_questions[x]
                    and int(self.all_questions[x]["c_count"]) <= 4
                ):
                    index += 1
                    dct[x] = self.all_questions[x]
                    if index >= 10:
                        return dct

        ask_exam = 10 - len(list(dct))
        
        for item in range(ask_exam):
            r = random.randint(0, len(asks) - 1)
            question_key = asks[r]
            if question_key not in dct:
                if "c_count" not in self.all_questions[question_key] or (
                    "c_count" in self.all_questions[question_key]
                    and int(self.all_questions[question_key]["c_count"]) <= 3
                ):
                    dct[question_key] = self.all_questions[question_key]
        return dct

    def get_points(self):
        return self.total_points

    def write_in_preguntas(self):
        with open(
            "lote_preguntas/p_a_2_0.json",
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(self.all_questions, file, ensure_ascii=False, indent=4)
