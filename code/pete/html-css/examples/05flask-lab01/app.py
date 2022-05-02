from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route('/')
def index():
    with open('merri-cat.json', 'r') as f:
        data = json.load(f)
        print(data)
        print(type(data)) # <class 'dict'>
        # contents = f.read()
        # print(contents)
        # print(type(contents)) # <class 'str'>
    


    quote = 'this is the quote'
    body = [
        'paragraph1',
        'paragraph2',
        'paragraph3',
    ]
    return render_template(
        'lab01_bio_v1.html',
        name=data.get('name'),
        quote=data.get('quote'),
        body=data.get('body'),
        places_lived=data.get('places_lived'),
        image1=data.get('image1'),
        image2=data.get('image2'),
    )

app.run(debug=True)