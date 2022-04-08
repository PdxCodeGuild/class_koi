# Mini-Capstone - Trivia Now
# Mitch Chapman

import requests
from question_organizer import Question
from trivia_functions import TriviaMaster

# Parameters for the API Call. "Ammount"=number of trivia questions. "Type"=type of trivia game.
parameters = {
    "amount": 10,
    "type": "multiple"
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()  # Returns an HTTPError object if an error has occurred during the process. (Nice for debugging API response).
data = response.json()
question_data = data["results"]


question_list = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    incorrect_answers = question["incorrect_answers"]
    new_question = Question(question_text, question_answer, incorrect_answers) # Sends the parsed data to the question organizer for ... more parsing/organizing and unescaping HTML.
    question_list.append(new_question)


quiz = TriviaMaster(question_list)

quiz.initiate_window()
