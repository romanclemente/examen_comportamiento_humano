import random
import os
import json


class BBDD_backend:
    def __init__(self, lenght_exam, only_fails=False) -> None:
        self.lenght_exam = lenght_exam
        self.only_fails = only_fails
        self.all_questions = self.get_preguntas()
        self.questions = self.preguntas_examen()
        self.total_points = 0.0
        self.points_per_question = 10 / len(list(self.questions))

    def get_all_fail_questions(self):
        asks = list(self.all_questions)
        dct = {}
        for x in asks:
            if "e_count" in self.all_questions[x]:
                dct[x] = self.all_questions[x]
        sorted_dct = dict(
            sorted(dct.items(), key=lambda item: item[1]["e_count"], reverse=True)
        )
        index, length, error, accurate = self.get_amount_question_total()
        return sorted_dct, index, length, error, accurate

    def get_amount_question_total(self):
        asks = list(self.all_questions)
        index = 0
        error = 0
        accurate = 0
        for x in asks:
            if "e_count" in self.all_questions[x] or "c_count" in self.all_questions[x]:
                if "e_count" in self.all_questions[x]:
                    error += 1
                else:
                    accurate += 1
                index += 1

        return index, len(asks), error, accurate

    def get_preguntas(self):
        with open(
            "examen_comportamiento_humano/lote_preguntas/p_a_2_0.json",
            "r",
            encoding="utf-8",
        ) as file:
            datos = json.load(file)
        return datos

    def clean_bbdd(self):
        lt = list(self.all_questions)
        for x in lt:
            if "c_count" in self.all_questions[x]:
                del self.all_questions[x]["c_count"]
            if "e_count" in self.all_questions[x]:
                del self.all_questions[x]["e_count"]
        self.write_in_preguntas()

    def sum_points(self, current_question):
        c_q = self.all_questions[current_question]
        if "c_count" in c_q:
            c_q["c_count"] = 1 + int(c_q["c_count"])
            if "e_count" in c_q:
                c_q["e_count"] = int(c_q["e_count"]) - 1
                if int(c_q["e_count"]) <= 0:
                    del self.all_questions[current_question]["e_count"]
        else:
            c_q["c_count"] = 1
        self.total_points += self.points_per_question
        self.write_in_preguntas()

    def quit_points(self, current_question):
        c_q = self.all_questions[current_question]
        if "e_count" in c_q:
            c_q["e_count"] = 1 + int(c_q["e_count"])
            if "c_count" in c_q:
                c_q["c_count"] = int(c_q["c_count"]) - 1
                if int(c_q["c_count"]) <= 0:
                    del self.all_questions[current_question]["c_count"]
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
                    and int(self.all_questions[x]["c_count"]) <= 2
                ):
                    index += 1
                    dct[x] = self.all_questions[x]
                    if index >= self.lenght_exam:
                        return dct
        if not self.only_fails:
            ask_exam = self.lenght_exam - len(list(dct))

            for item in range(ask_exam):
                r = random.randint(0, len(asks) - 1)
                question_key = asks[r]
                if question_key not in dct:
                    if "c_count" not in self.all_questions[question_key]:
                        dct[question_key] = self.all_questions[question_key]
                    elif (
                        "c_count" in self.all_questions[question_key]
                        and int(self.all_questions[question_key]["c_count"]) <= 2
                    ):
                        in_dct = True
                        for i in asks:
                            if "c_count" not in self.all_questions[i]:
                                in_dct = False
                                dct[i] = self.all_questions[i]
                                break
                        if in_dct:
                            dct[question_key] = self.all_questions[question_key]
        return dct

    def get_points(self):
        return self.total_points

    def write_in_preguntas(self):
        with open(
            "examen_comportamiento_humano/lote_preguntas/p_a_2_0.json",
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(self.all_questions, file, ensure_ascii=False, indent=4)
