from flask import Blueprint
from src.database import db
from src.database import Challenge
from collections import defaultdict
from src.build_db import import_challenges

api = Blueprint("api", __name__)

@api.route('/challenges')
def get_challenges():
    challenges = Challenge.query.all()
    output = []
    for challenge in challenges:
        challenge_data = {'id': challenge.id, 'section': challenge.get_topic(challenge.section), 'name': challenge.name, 'description': challenge.description}

        output.append(challenge_data)

    return {'challenges': output}

@api.route('/challenges/random')
def random_challenges():
    return f"Return a random challenge based on specified section"

@api.route('/sections')
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

@api.route('/sections/random')
def random_sections():
    return f"Return a random challenge based on specified section"
    
@api.route('/challenges/<id>')
def get_challenge(id):
    challenge = Challenge.query.get_or_404(id)
    return {'section': challenge.get_topic(challenge.section), 'name': challenge.name, 'description': challenge.description}

@api.route('/challenge/add')
def user_add_challenge():
    return f"Allow user to add a challenge (MAYBE)"

@api.route('/db/drop')
def drop():
    db.drop_all()
    db.create_all()
    return "Dropped and Created"

@api.route('/db/build')
def build():
    def add_challenges(challenge_list):
        for i in challenge_list:
            db.session.add(Challenge(section=i[0], name=i[1], description=i[2]))
            db.session.commit()
    add_challenges(import_challenges())
    return "Built"
