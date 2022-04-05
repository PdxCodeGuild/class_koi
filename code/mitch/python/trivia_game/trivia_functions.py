
import random


class TriviaMaster:

    def __init__(self, question_list:list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        self.current_question = None

    def are_there_more_questions(self):
        """Returns True if there are more questions left in the quiz and False if there is not."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Uses the current question positon to retrieve the current trivia question from the question list, then tics the question counter. 
        Labels quesion and answers and shuffles answers. Asks for an input from the user, input must be the string of the answer. Calls the check answer func."""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = self.current_question.text
        answers = [self.current_question.answer, self.current_question.incorrect_1, self.current_question.incorrect_2, self.current_question.incorrect_3]
        random.shuffle(answers)
        
        user_answer = input(f"\nQ.{self.question_number}: {question_text}\nAnswers:\n{' or '.join(answers)}: ")
        self.check_answer(user_answer)

    def check_answer(self, user_answer:str):
        """Compares the user answer against the correct answer. Provides appropriate feedback and awards a point if correct."""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print(f"That's wrong.\nThe correct answer was {correct_answer}")

        print(f"Your current score is: {self.score}/{self.question_number}\n")

