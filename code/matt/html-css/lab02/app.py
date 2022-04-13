"""
PDX Code Guild - Class Koi
HTML Lab 02 - Blog
Matt Walsh
"""


#
import json
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    pagename = contents['pagename']
    posts = contents['posts']
    
    return render_template('index.html', pagename=pagename, posts=posts, authors=authors)

contents = open('./code/matt/html-css/lab02/data.json')
contents = json.load(contents)

authors = []
for posts in contents['posts']:
    authors.append(posts['author'])
authors = list(set(authors))
authors.sort()

for author in authors:
    @app.route(f'/{author}')
    def author():
        pagename = contents['pagename']
        posts = contents['posts']
        return render_template(f'{author}.html', pagename=pagename, posts=posts, authors=authors)

app.run(debug=True)