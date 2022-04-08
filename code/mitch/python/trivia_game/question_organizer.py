
import html

class Question:
    def __init__(self, question_text:str, question_answer:str, incorrect_answers:list):
        """Breaks up the question data from the web API to be used by the trivia functions. Also converts HTML to characters."""
        self.text = html.unescape(question_text)
        self.answer = html.unescape(question_answer)
        self.incorrect_1 = html.unescape(incorrect_answers[0])
        self.incorrect_2 = html.unescape(incorrect_answers[1])
        self.incorrect_3 = html.unescape(incorrect_answers[2])



