from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    with open('data.json', 'r') as f:
        data = (f.read())
        print(data)

    body = [
        'paragrtaph 1',
        'paragraph 2',
    ]
    return render_template(
        'index.html',
         name=data.get('name'), 
         quote = data.get('quote'),
         )
app.run(debug=False)