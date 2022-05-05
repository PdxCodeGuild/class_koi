from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route('/')
def index():
    with open('data.json', 'r') as f:
        data = json.load(f)
        print(data)

    return render_template('lab01')





