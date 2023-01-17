class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.q_list = q_list
        self.score = 0

    def still_have_questions(self):
        return self.question_number < len(self.q_list)

    def next_question(self):
        curr_question = self.q_list[self.question_number]
        self.question_number += 1
        userans = input(f"Q.{self.question_number}: {curr_question.text} (True/False)?: ")
        self.check_answer(userans, curr_question.answer)

    def check_answer(self, userans, current_answer):
        if userans.lower() == current_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer is {current_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")
