from question_model import Question
from data import question_data

Question_Bank = []
for question in question_data:
    q_text = question["text"]
    a_answer = question["answer"]
    new_question = Question(q_text, a_answer)
    Question_Bank.append(new_question)
