from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/goodbye')
def goodbye():
    return 'Goodbye World' 

@app.route('/template')
def template():
    return render_template('index.html')

app.run(debug=True)

# index.html should be in 'templates' directory

