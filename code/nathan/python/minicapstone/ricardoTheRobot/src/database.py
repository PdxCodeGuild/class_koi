from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.String(50))
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(500))

    def __repr__(self):
        return f"{self.id} {self.section} {self.name} {self.description}"
    
    def get_topic(self, section):
        topic_list = {
            '1': 'Arrays and Strings',
            '2': 'Linked Lists',
            '3': 'Stacks and Queues',
            '4': 'Trees and Graphs',
            '5': 'Bit Manipulation',
            '6': 'Math and Logic Puzzles',
            '7': 'Object-Oriented Design',
            '8': 'Recursion and Dynamic Programming',
        }

        if(self.section[0] in topic_list):
            return topic_list[self.section[0]]
        
        return self.section