# Programming 102 Labs Redux

Create a Flask app that performs at least 2 of the following Programming 102 labs.

- [Unit Converter](https://github.com/PdxCodeGuild/Programming102/blob/master/labs/lab3.md)
- [Anagram Checker](https://github.com/PdxCodeGuild/Programming102/blob/master/labs/lab4.md)
- [User Login](https://github.com/PdxCodeGuild/Programming102/blob/master/labs/lab5.md)

Instead of using URL converters, use forms with inputs and post requests to get user input.  You may use one view for each lab, or multiple views.  You can also use a single template for each lab, or use redirects for POST requests vs GET requests.

```py
from flask import Flask, render_template, request, redirect
app = Flask(__app__)

# like 101 Redux, serve an index page where users can find links to the labs
@app.route('/')
def index():
	return render_template('index.html')


# single view
@app.route('/unit-converter/', methods=['GET', 'POST'])
def unit_converter():
	if request.method == 'POST':
		print(request.form) # see what was submitted in the form
		# extract the necessary data from request.POST
		# do the Python stuff
		result = '42 meters' # or whatever the result is
		# for POST requests, render a template that shows the results
		return render_template('unit-converter-result.html', result=result)
	# for GET requests, render a template with a form for submitting data
	return render_template('unit-converter.html')


# multiple views
@app.route('/anagram/') # if the methods= kwarg is missing, the route will only accept GET requests
def anagram():
	# the GET request to /anagram just renders the template
	return render_template('anagram.html')

@app.route('/anagram/', methods=['POST']) # same endpoint, but a POST request
def anagram_check():
	print(request.form) # see what was submitted in the form
	# extract the necessary data from request.POST
	# do the python stuff
	word1 = 'Jim Morrison' # or whatever word1 was
	word2 = 'Mr. Mojo Risin' # or whatever word2 was
	anagram_check = True # or False
	# render the same template as the GET request, but pass in the kwargs
	return render_template('anagram.html', word1=word1, word2=word2, anagram_check=anagram_check)


# using redirects
@app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.METHOD == 'POST':
		# do the python stuff
		success = True # or False, depending on the post request
		if success:
			# redirect user to success page
			return redirect('/login/success/)
		# redirect user to failure page
		return redirect('/login/failure/')
	# for get requests (aka: initial page load),
	# render the login template with the form
	return render_template('login.html')

# Note: this is missing the success and failure views, be sure to add those!
```

Make sure each template has a links to any other appropriate pages.
