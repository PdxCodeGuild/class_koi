from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/templates')
def template():
    return render_template('index.html')

app.run(debug=True)