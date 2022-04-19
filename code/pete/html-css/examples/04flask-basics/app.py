from flask import Flask, render_template
app = Flask(__name__)

# @app.route is a decorator, it gives additional instructions to the function which is defined next
# this decorator makes it so when a request is sent to it's path (/), it will execute this view function
@app.route('/') # http://127.0.0.1:5000/
def index():
    return 'Hello World'

@app.route('/goodbye') # http://127.0.0.1:5000/goodbye
def goodbye():
    return 'Goodbye World'

@app.route('/random-message') # https://127.0.0.1:5000/random-message
def random_message():
    from random import choice
    messages = [
        'Flask is fun',
        'CSS is fun',
        'HTML is fun',
    ]
    return choice(messages)

@app.route('/template') # http://127.0.0.1:5000/template
def template():
    from random import choice
    messages = [
        'Flask is fun',
        'CSS is fun',
        'HTML is fun',
    ]
    # this is a view function, calling this var view_message
    view_message = choice(messages)
    programmer = 'Pete'
    framework = 'Flask'
    return render_template('index.html', template_message=view_message, programmer="programmer", framework=framework)

app.run(debug=True)