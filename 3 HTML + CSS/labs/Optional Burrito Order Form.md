

# Lab 06: Burrito Order Form


Create a Flask app that serves a burrito order form template with the following inputs. Try to incorporate some images and semantic elements. Below are some recommended fields, feel free to use your own.

The input elements should all be inside a `<form>` element with `action="/"` and `method="POST"` attributes.  Feel free to change things up a bit (i.e.: use a `<select>` dropdown with `<option>`s instead of radio buttons) but include at least this much data 

- Name (text input)
- Password (password input)
- Tortilla (radio buttons)
  - White Flour
  - Wheat Flour
  - Spinach
  - Corn
- Rice (radio buttons)
  - White Rice
  - Brown Rice
- Beans (radio buttons)
  - Black Beans
  - Pinto Beans
- Protein (radio buttons)
  - Carnitas
  - Chicken
  - Sofritas
  - None
- Additional Ingredients (check boxes)
  - Cheese
  - Sour Cream
- Delivery Instructions (textarea)

Use the starter code below if you like.  Only Version 1 (print the order info in the terminal) is required.

```py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		form_data = dict(request.form)
		print(form_data)
		# extract the order info from form_data

		# Version 1:
		# print an order summary in the terminal

		# Version 2 (optional):
		# render a confirmation page
		# return render_template('confirmation', confirmation_data=???)

		# Version 3 (optional):
		# redirect to another view, sending the form_data info along
		# https://sodocumentation.net/flask/topic/6856/redirect
		# return redirect(url_for('confirmation', confirmation_data=???))

	return render_template('index.html') # index.html is the template with the form

@app.route('/confirmation/<confirmation_data>/')
def confirmation(confirmation_data):
	...
```