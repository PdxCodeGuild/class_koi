from turtle import title
from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route('/')
def index():
    with open('blog_items.json', 'r') as f:
        data = json.load(f)
        
    return render_template(
        
        'index.html',
        
       title = data.get('items'),
    #    date = data['items'][0]['blog_date'],
    #    author = data['items'][0]['blog_author'],
    #    paragraph = data['items'][0]['blog_paragraph'],
        )
    
#@app.route('/about')
#def about():
 #   return render_template('about.html')
    
#@app.route('/post')
#def post():
 #  return render_template('post.html')
    
if __name__== '__main__':
    app.run(debug=True)
    
    