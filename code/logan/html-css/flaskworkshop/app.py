from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route("/daamn")
def daamn():
    return "daamn"

@app.route("/rando")
def rando():
    messages = ["your head asplode", "eh, steve!!"]
    from random import choice
    return choice(messages)

@app.route("/template")
def template():
    descartes = "Descartes"
    return render_template("index.html", philosopher=descartes)

app.run(debug=True)