class QuizBrain:
    def __init__(self,question_list):
        self.question_no=0
        self.question_list=question_list
        self.score=0

    def still_has_qus(self):
        if self.question_no<len(self.question_list):
            return True

    def next_question(self):
        curr_question=self.question_list[self.question_no]
        self.question_no+=1
        user_ans=input(f"Q.{self.question_no}:{curr_question.text}(True/False): ").capitalize()
        self.check_ans(user_ans,curr_question.answer)

    def check_ans(self,answer,correct):
        if answer==correct:
            self.score+=1
        else:
            print("wrong answer. ")
        print(f"correct answer to the qus is {correct}")
        print(f"your current score is: {self.score}/{self.question_no}")
