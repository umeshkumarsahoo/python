from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for i in question_data:
    question_bank.append(Question(i["question"],i["correct_answer"]))

quiz=QuizBrain(question_bank)
while quiz.still_has_qus():
    quiz.next_question()
else:
    print("you completed the quiz.")
    print(f"your score is:{quiz.score}/{len(question_bank)}")
