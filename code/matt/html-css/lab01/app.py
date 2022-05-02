import json
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = contents['name']
    bio = contents['bio']
    link = contents['link']
    photo = contents['photo']
    places_lived = contents['places_lived']
    quote = contents['quote']
    extraphoto1 = contents['extraphoto1']
    extraphoto2 = contents['extraphoto2']
    extraphoto3 = contents['extraphoto3']
    extraphoto4 = contents['extraphoto4']
    return render_template('index.html', name=name, bio=bio, link=link, photo=photo, places_lived=places_lived, quote=quote, extraphoto1=extraphoto1, extraphoto2=extraphoto2, extraphoto3=extraphoto3, extraphoto4=extraphoto4)

contents = open('./code/matt/html-css/lab01/data.json')
contents = json.load(contents)

app.run(debug=True)