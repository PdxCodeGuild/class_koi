from collections import defaultdict
from build_db import import_challenges
from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

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

@app.route('/')
def index():
    return 'Hello'

@app.route('/challenges')
def get_challenges():
    challenges = Challenge.query.all()
    output = []
    for challenge in challenges:
        challenge_data = {'id': challenge.id, 'section': challenge.get_topic(challenge.section), 'name': challenge.name, 'description': challenge.description}

        output.append(challenge_data)

    return {'challenges': output}

@app.route('/challenges/random')
def random_challenges():
    return f"Return a random challenge based on specified section"

@app.route('/sections')
def get_sections():
    challenges = Challenge.query.all()
    output = defaultdict(list)
    # section_list = []
    # temp_list = []
    # for i, challenge in enumerate(challenges):
    #     section_data = {'id': challenge.id, 'section': challenge.get_topic(challenge.section), 'name': challenge.name, 'description': challenge.description}
    #     temp_list.append(section_data)
    #     # section_list.append(section_data)
    #     if(i + 1 == len(challenges)):
    #         # section_list = temp_list.copy()
    #         output.update({challenge.get_topic(challenge.section): temp_list})
    #         # temp_list.clear()
    #     elif(challenges[i].section != challenges[i + 1].section and i > 0):
    #         # section_list = temp_list.copy()
    #         output.update({challenge.get_topic(challenge.section): temp_list})
    #         # temp_list.clear()

    for challenge in challenges:
        section_data = {'id': challenge.id, 'name': challenge.name, 'description': challenge.description}
        output[challenge.get_topic(challenge.section)].append(section_data)

    return {'sections' : output}

@app.route('/sections/random')
def random_sections():
    return f"Return a random challenge based on specified section"
    
@app.route('/challenges/<id>')
def get_challenge(id):
    challenge = Challenge.query.get_or_404(id)
    return {'section': challenge.get_topic(challenge.section), 'name': challenge.name, 'description': challenge.description}

@app.route('/challenge/add')
def user_add_challenge():
    return f"Allow user to add a challenge (MAYBE)"

@app.route('/db/drop')
def drop():
    db.drop_all()
    db.create_all()
    return 1

@app.route('/db/build')
def build():
    def add_challenges(challenge_list):
        for i in challenge_list:
            db.session.add(Challenge(section=i[0], name=i[1], description=i[2]))
            db.session.commit()
    add_challenges(import_challenges())
    return 1

