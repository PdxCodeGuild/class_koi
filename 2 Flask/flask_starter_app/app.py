from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    var1 = 'Banana'
    var2 = 'Orange Soda'
    var3 = 'Donkey Kong'
    var4 = 'Godzilla'
    return render_template('index.html', var1=var1, var2=var2, var3=var3, var4=var4)

app.run(debug=True)