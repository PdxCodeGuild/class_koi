from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/laugh')
def laugh():
    return 'HAHAHAHAHA'

@app.route('/random_msg')
def random_msg():
    from random import choice
    messages = [
        'Flask is  fun',
        'CSS is fun',
        'HTML is fun',
    ]
    return choice(messages)

@app.route('/template')
def template():
    from random import choice
    messages = [
        'Flask is  fun',
        'CSS is fun',
        'HTML is fun',
    ]
    view_message = choice(messages)
    programmer = "Moss"
    framework = "Flask"
    return render_template('index.html', 
    template_message = view_message, programmer = programmer,
    framework = framework)

app.run(debug=True)