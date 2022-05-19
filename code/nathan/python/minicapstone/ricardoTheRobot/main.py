import requests
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'],'/slack/events',app)
# YOU HAVE TO UPDATE SLACK REQUEST URL AFTER EACH NGROK SESSION
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call('auth.test')['user_id']
# challenges = requests.get('http://api.bonillaproject.com/api/challenges', verify=False)
# challenges_data = challenges.json()
COUNT = 0
ARRAYS_AND_STRINGS = 0
LINKED_LISTS = 0
STACKS_AND_QUEUES = 0
TREES_AND_GRAPHS = 0
RECURSION_AND_DYNAMIC_PROGRAMMING = 0
OBJECT_ORIENTED_DESIGN = 0
BIT_MANIPULATION = 0
MATH_AND_LOGIC_PUZZLES = 0



def get_challenge():
    challenges = requests.get('http://api.bonillaproject.com/api/challenges', verify=False)
    challenges_data = challenges.json()
    global COUNT
    output = f"""
    {challenges_data['challenges'][COUNT]['section']}
*{challenges_data['challenges'][COUNT]['name']}*: {challenges_data['challenges'][COUNT]['description']}'"""
    COUNT += 1
    return output

'''
@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if(BOT_ID != user_id):
        client.chat_postMessage(channel=channel_id, text=text)
        '''

@app.route('/ricardo-the-robot', methods=['POST'])
def ricardo_the_robot():
    data = request.form

    channel_id = data.get('channel_id')
    client.chat_postMessage(channel=channel_id, text=f"""I am Ricardo the Robot!
Try me out!  My commands are:
/daily-challenge
/show-sections
/get-from-section
/get-random""")
    return 'okay'

@app.route('/daily-challenge', methods=['POST'])
def daily_challenge():
    data = request.form

    channel_id = data.get('channel_id')
    client.chat_postMessage(channel=channel_id, text=get_challenge())
    return 'okay'

@app.route('/show-sections', methods=['POST'])
def show_sections():
    data = request.form
    channel_id = data.get('channel_id')
    sections = requests.get('http://api.bonillaproject.com/api/sections', verify=False)
    sections_data = sections.json()
    sections_keys = sections_data['sections'].keys()
    for section in sections_keys:
        client.chat_postMessage(channel=channel_id, text=section)

@app.route('/get-from-section', methods=['POST'])
def get_from_section():
    data = request.form
    channel_id = data.get('channel_id')
    section = data.get('text')
    from_section = requests.get('http://api.bonillaproject.com/api/sections', verify=False)
    sections_data = from_section.json()
    output = sections_data['sections'][section]
    def format_output(challenge, count):
        return f"""
{section}
*{challenge[count]['name']}*: {challenge[count]['description']}"""

    if(section == 'Arrays and Strings'):
        global ARRAYS_AND_STRINGS
        client.chat_postMessage(channel=channel_id, text=format_output(output, ARRAYS_AND_STRINGS))
        ARRAYS_AND_STRINGS += 1
    elif(section == 'Linked Lists'):
        global LINKED_LISTS
        client.chat_postMessage(channel=channel_id, text=format_output(output, LINKED_LISTS))
        LINKED_LISTS += 1
    elif(section == 'Stacks and Queues'):
        global STACKS_AND_QUEUES
        client.chat_postMessage(channel=channel_id, text=format_output(output, STACKS_AND_QUEUES))
        STACKS_AND_QUEUES += 1
    elif(section == 'Trees and Graphs'):
        global TREES_AND_GRAPHS
        client.chat_postMessage(channel=channel_id, text=format_output(output, TREES_AND_GRAPHS))
        TREES_AND_GRAPHS += 1
    elif(section == 'Recursion and Dynamic Programming'):
        global RECURSION_AND_DYNAMIC_PROGRAMMING
        client.chat_postMessage(channel=channel_id, text=format_output(output, RECURSION_AND_DYNAMIC_PROGRAMMING))
        RECURSION_AND_DYNAMIC_PROGRAMMING += 1
    elif(section == 'Object-Oriented Design'):
        global OBJECT_ORIENTED_DESIGN
        client.chat_postMessage(channel=channel_id, text=format_output(output, OBJECT_ORIENTED_DESIGN))
        OBJECT_ORIENTED_DESIGN += 1
    elif(section == 'Bit Manipulation'):
        global BIT_MANIPULATION
        client.chat_postMessage(channel=channel_id, text=format_output(output, BIT_MANIPULATION))
        BIT_MANIPULATION += 1
    elif(section == 'Math and Logic Puzzles'):
        global MATH_AND_LOGIC_PUZZLES
        client.chat_postMessage(channel=channel_id, text=format_output(output, MATH_AND_LOGIC_PUZZLES))
        MATH_AND_LOGIC_PUZZLES += 1
    else:
        client.chat_postMessage(channel=channel_id, text="Unrecognized secion.  Run '/show-sections to see what is available")
    
    return 'okay'

'''
@app.route('/get-random', methods=['POST'])
def get_random():
    data = request.form

    channel_id = data.get('channel_id')
    client.chat_postMessage(channel=channel_id, text=get_challenge())
    return 'okay'
'''

if __name__ == "__main__":
    app.run(debug=True)