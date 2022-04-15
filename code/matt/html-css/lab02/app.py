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
    main_page = True
    return render_template('index.html', pagename=pagename, posts=posts, authors=authors, main_page=main_page)

@app.route('/by/<string:author>')
def posts_by(author):
    author_page = True
    author_bio = contents['bios'][author.title()]
    author_posts = []
    for post in posts:
        if post['author'].lower() == author.lower():
            author_posts.append(post)
    return render_template('index.html',pagename=pagename, posts=author_posts, authors=authors, author_page=author_page, author_bio=author_bio)

@app.route('/posts/<string:slug>')
def single_post(slug):
    post_page = True
    this_post = []
    for post in posts:
        if post['slug'] == slug:
            this_post.append(post)
    return render_template('index.html',pagename=pagename, posts=this_post, authors=authors, post_page=post_page)

contents = open('./code/matt/html-css/lab02/data.json')
contents = json.load(contents)

authors = []
for posts in contents['posts']:
    authors.append(posts['author'])
authors = list(set(authors))
authors.sort()

pagename = contents['pagename']
posts = contents['posts']

post_page = False
main_page = False
author_page = False

app.run(debug=True)