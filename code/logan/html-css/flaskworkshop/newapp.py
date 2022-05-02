from asyncore import read
from flask import Flask, render_template
app = Flask(__name__)
import json

@app.route('/')
def index():
    with open("data.json", "r") as f:
        data = json.load(f)
    return render_template("index.html")

app.run(debug=True)