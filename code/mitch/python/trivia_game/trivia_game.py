# Mini-Capstone - Trivia Game
# Mitch Chapman

import requests
from question_organizer import Question
from trivia_functions import TriviaMaster


quiz_length = int(input("How many questions would you like the quiz to have? (1 - 50): "))

parameters = {
    "amount": quiz_length,
    "type": "multiple"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)

response.raise_for_status()
data = response.json()
question_data = data["results"]


question_list = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    incorrect_answers = question["incorrect_answers"]
    new_question = Question(question_text, question_answer, incorrect_answers)
    question_list.append(new_question)


quiz = TriviaMaster(question_list)


while quiz.are_there_more_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")