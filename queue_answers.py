from lote_preguntas.p_a import questions


class BBDD_backend:
    def __init__(self) -> None:
        self.questions = questions
        self.total_points = 0
        self.points_per_question = 10 / len(list(self.questions))

    def sum_points(self):
        self.total_points += self.points_per_question

    def quit_points(self):
        self.total_points -= self.points_per_question

    def get_points(self):
        return self.total_points
