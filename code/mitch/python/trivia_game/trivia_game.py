# Mini-Capstone - Trivia Game
# Mitch Chapman

import requests
from question_organizer import Question
from trivia_functions import TriviaMaster


parameters = {
    "amount": 5,
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

print(question_list)

quiz = TriviaMaster(question_list)

quiz.initiate_window()
