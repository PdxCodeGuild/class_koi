from msilib import add_stream
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') # http://127.0.0.1:5000
def index():
    return 'Hello World'

@app.route('/goodbye') 
def goodbye():
    return 'Goodbye World'

@app.route('/random-message')
def random_message():
    from random import choice
    messages = [
        'Flask is fun',
        'CSS is fun',
        'HTML is fun'
    ]
    return choice(messages)
    
@app.route('/template')
def template():
    from random import choice
    messages = [
        'Flask is fun',
        'CSS is fun',
        'HTML is fun'
    ]
    view_message = choice(messages)
    programmer = 'Adam'
    framework = 'Flask'
    return render_template('index.html',
    template_message=view_message, programmer=programmer,
    framework=framework)

app.run(debug=True)
