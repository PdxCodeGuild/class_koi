from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():


app.run(debug=True)