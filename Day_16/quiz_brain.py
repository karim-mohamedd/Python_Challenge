class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
    def nex_question(self, ):
        current_question = self.question_list[self.question_num]
        self.question_num = 1
