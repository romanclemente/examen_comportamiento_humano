import random
import json
import os

LAST_EXAM = None


class BBDD_backend:
    def __init__(
        self,
        path,
        lenght_exam=10,
        only_fails=False,
        repetir=False,
        news_quest=True,
        difficulty=None,
    ) -> None:
        self.lenght_exam = lenght_exam
        self.lenght_exam = float(int(self.lenght_exam))
        self.path = path
        self.path_desarrollo = None
        self.repetir = repetir
        self.only_fails = only_fails
        self.all_questions = self.get_preguntas(path=path)
        if news_quest:
            self.questions = self.preguntas_nuevas()
        else:
            if difficulty is None:
                self.questions = self.preguntas_normales()
            else:
                self.questions = self.preguntas_examen(difficulty=difficulty)
        print(difficulty)
        self.total_points = 0.0
        self.points_per_question = 10 / len(list(self.questions))

    def remove_question(self, question):
        self.questions.pop(question, None)
        self.all_questions.pop(question, None)
        if self.questions:
            self.points_per_question = 10 / len(self.questions)
        else:
            self.points_per_question = 0

        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(self.all_questions, file, ensure_ascii=False, indent=4)

    def get_all_fail_questions(self):
        total_questions = len(self.all_questions)
        answered_questions = 0
        error = 0
        accurate = 0
        failed_questions = {}

        for key, data in self.all_questions.items():
            has_error = "e_count" in data
            has_correct = "c_count" in data

            if has_error or has_correct:
                answered_questions += 1
                error += data.get("e_count", 0)
                accurate += data.get("c_count", 0)

                if has_error:
                    failed_questions[key] = data

        sorted_failed_questions = dict(
            sorted(failed_questions.items(), key=lambda item: item[1]["e_count"], reverse=True)
        )

        return sorted_failed_questions, answered_questions, total_questions, error, accurate

    def get_preguntas(self, path):
        with open(
            path,
            "r",
            encoding="utf-8",
        ) as file:
            datos = json.load(file)
        return datos

    def get_preguntas_desarrollo(self, path):
        with open(
            path,
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
        self.write_in_preguntas(self.path)

    def sum_points(self, current_question):
        # Aseguramos que la key sea string, por si vienen como enteros
        current_question = str(current_question)
        c_q = self.all_questions.get(current_question, {})

        # Sumamos 1 a c_count
        c_q["c_count"] = int(c_q.get("c_count", 0)) + 1

        # Restamos 1 a e_count si existe
        if "e_count" in c_q:
            c_q["e_count"] = int(c_q["e_count"]) - 1
            if c_q["e_count"] <= 0:
                c_q.pop("e_count")

        # Guardamos los cambios de vuelta al diccionario general
        self.all_questions[current_question] = c_q

        # Sumamos puntos
        self.total_points += self.points_per_question

        # Escribimos en el JSON
        self.write_in_preguntas(self.path)

    def quit_points(self, current_question):
        current_question = str(current_question)
        c_q = self.all_questions.get(current_question, {})

        # Sumamos 1 a e_count
        c_q["e_count"] = int(c_q.get("e_count", 0)) + 1

        # Restamos 1 a c_count si existe
        if "c_count" in c_q:
            c_q["c_count"] = int(c_q["c_count"]) - 1
            if c_q["c_count"] <= 0:
                c_q.pop("c_count")

        # Guardamos los cambios
        self.all_questions[current_question] = c_q

        # Restamos puntos
        self.total_points -= self.points_per_question * 0.2

        # Escribimos en el JSON
        self.write_in_preguntas(self.path)

    def write_in_preguntas(self, path):
        with open(
            path,
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(self.all_questions, file, ensure_ascii=False, indent=4)

    def preguntas_normales(self):
        bank = self.all_questions
        dct = {}

        total = int(self.lenght_exam)

        # Separamos las preguntas en nuevas (sin e_count ni c_count) y ya salidas
        nuevas = [
            key
            for key, data in bank.items()
            if isinstance(data, dict)
            and "e_count" not in data
            and "c_count" not in data
        ]
        salidas = [key for key in bank if key not in nuevas]

        # De las salidas, separamos en e_count y c_count
        e_keys = [key for key in salidas if "e_count" in bank[key]]
        c_keys = [key for key in salidas if "c_count" in bank[key]]

        # Ordenamos: e_count descendente (más usados primero), c_count ascendente (menos usados primero)
        e_keys.sort(key=lambda k: bank[k]["e_count"], reverse=True)
        c_keys.sort(key=lambda k: bank[k]["c_count"])

        # Calculamos cuántas preguntas queremos de cada grupo
        n_salidas = int(round(total * 0.50))
        n_nuevas = total - n_salidas  # El 50%

        n_e = int(round(n_salidas * 0.90))
        n_c = n_salidas - n_e  # El 10%

        # Ajustamos para no pasarnos si hay menos preguntas disponibles de las necesarias
        e_seleccionadas = e_keys[: min(n_e, len(e_keys))]
        c_seleccionadas = c_keys[: min(n_c, len(c_keys))]
        nuevas_seleccionadas = random.sample(nuevas, min(n_nuevas, len(nuevas)))

        # Si faltan preguntas por no haber suficientes disponibles, intentamos compensar
        faltan = total - (
            len(e_seleccionadas) + len(c_seleccionadas) + len(nuevas_seleccionadas)
        )
        if faltan > 0:
            # Rellenar con nuevas si quedan
            restantes = list(set(nuevas) - set(nuevas_seleccionadas))
            nuevas_extra = random.sample(restantes, min(faltan, len(restantes)))
            nuevas_seleccionadas.extend(nuevas_extra)
            faltan -= len(nuevas_extra)

        if faltan > 0:
            # Rellenar con más salidas en general, priorizando e_keys y luego c_keys restantes
            restantes_e = list(set(e_keys) - set(e_seleccionadas))
            restantes_c = list(set(c_keys) - set(c_seleccionadas))
            e_extra = restantes_e[: min(faltan, len(restantes_e))]
            e_seleccionadas.extend(e_extra)
            faltan -= len(e_extra)

            if faltan > 0:
                c_extra = restantes_c[: min(faltan, len(restantes_c))]
                c_seleccionadas.extend(c_extra)

        # Unimos todas las claves seleccionadas
        seleccionadas = e_seleccionadas + c_seleccionadas + nuevas_seleccionadas

        # Creamos el dict final con contenido incluido
        for key in seleccionadas:
            data = bank[key]
            dct[key] = data.copy()

            contenido = self.leer_contenido_si_fichero(key)
            if contenido is not None:
                dct[key]["enunciado"] = contenido

        return dct

    def preguntas_nuevas(self):
        bank = self.all_questions
        dct = {}
        preguntas_validas = [
            key
            for key, data in bank.items()
            if isinstance(data, dict)
            and "e_count" not in data
            and "c_count" not in data
        ]
        if len(preguntas_validas) < self.lenght_exam:
            self.lenght_exam = len(preguntas_validas)

        # Elegimos aleatoriamente sin repetición
        seleccionadas = random.sample(preguntas_validas, int(self.lenght_exam))

        for key in seleccionadas:
            data = bank[key]
            dct[key] = data.copy()

            contenido = self.leer_contenido_si_fichero(key)
            if contenido is not None:
                dct[key]["enunciado"] = contenido

        return dct

    def leer_contenido_si_fichero(self, path):
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        return None

    def preguntas_examen(self, difficulty):
        global LAST_EXAM

        if self.repetir:
            return LAST_EXAM

        dct = {}
        index = 0
        fails = 0
        sorted_dct, _, _, _, _ = self.get_all_fail_questions()
        list_only_fails = list(sorted_dct)
        all_keys = list(self.all_questions)

        # Número de preguntas fallidas totales a incluir
        if self.only_fails:
            preguntas_fallidas = self.lenght_exam
        else:
            preguntas_fallidas = round(self.lenght_exam / 3)

        # Número de "más fallidas" según dificultad
        if difficulty == "Facil":
            mas_fallidas = round(self.lenght_exam * 0.25)
        elif difficulty == "Medio":
            mas_fallidas = round(self.lenght_exam * 0.50)
        elif difficulty == "Dificil":
            mas_fallidas = round(self.lenght_exam * 0.75)
        elif difficulty is None:
            mas_fallidas = round(self.lenght_exam * 0.1)
        else:
            mas_fallidas = self.lenght_exam

        x = -1
        # Incluir preguntas más fallidas
        while preguntas_fallidas > 0:
            try:
                if mas_fallidas == 0:
                    x = random.randrange(0, len(list_only_fails) - 1)
                else:
                    mas_fallidas -= 1
                    x += 1

                key = list_only_fails[x]
                data = self.all_questions[key]
                dct[key] = data.copy() if isinstance(data, dict) else data

                contenido = self.leer_contenido_si_fichero(key)
                if contenido:
                    dct[key]["enunciado"] = contenido

                preguntas_fallidas -= 1
                index += 1

            except Exception:
                break

        # Rellenar hasta completar el examen
        if not self.only_fails:
            while index < self.lenght_exam:
                key = random.choice(all_keys)
                data = self.all_questions[key]

                if "e_count" not in data:
                    dct[key] = data.copy() if isinstance(data, dict) else data

                    contenido = self.leer_contenido_si_fichero(key)
                    if contenido:
                        dct[key]["enunciado"] = contenido

                    index += 1
                elif fails >= 100:
                    break
                else:
                    fails += 1

        # Si se pasa del número total, recortar
        exceso = len(dct) - self.lenght_exam
        if exceso > 0:
            for key in list(dct.keys())[:exceso]:
                dct.pop(key)

        LAST_EXAM = dct
        return dct

    def get_points(self):
        return round(self.total_points, 2)
