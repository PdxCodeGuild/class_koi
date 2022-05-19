from flask import Flask, render_template, request
from random import choice

app = Flask(__name__)

@app.route('/')
def index():
    names = ['baby', 'friend-o', 'pal']
    name = choice(names)

    return render_template('index.html', name=name, possible_names=names)

    # this will return a string and just display this text simply on the page
    return f'Hello, it\'s Flask time, {name}!'

@app.route('/form', methods=['GET', 'POST']) # GET is allowed by default, now it will take GET and POST requests
def form():
    message = ''
    if request.method == 'POST':
        print(request.form) # ImmutableMultiDict -- a dictionary-like object that has the info from the form
        print(request.form.get('message')) # you can use dictionary operators and methods on the ImmutableMultiDict
        message = request.form.get('message')
    return render_template('form.html', message=message)

app.run(debug=True)

