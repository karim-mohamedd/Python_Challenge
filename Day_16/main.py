from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#Question Bank is a list of objects
Question_Bank = []
for question in question_data:
    q_text = question["text"]
    a_answer = question["answer"]
    new_question = Question(q_text, a_answer)
    Question_Bank.append(new_question)

quiz = QuizBrain(Question_Bank)   

while quiz.still_has_question():
        quiz.next_question()

print("You have completed the quiz")
print(f"You total score is {quiz.score}/{quiz.question_number}")



