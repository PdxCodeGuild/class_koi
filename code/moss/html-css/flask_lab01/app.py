from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route('/')
def index():
    with open('jmkovic.json') as f:
        data = json.load(f)
        print(data)
        print(type(data)
    )

    return render_template(
        'index.html',
        name = data.get('name'),
        bio = data.get('bio'),
        link1 = data.get('link1'),
        link2 = data.get('link2'),
        img = data.get('img'),
        places_lived = data.get('places_lived'),
        quote = data.get('quote'),
    )

app.run(debug=True)