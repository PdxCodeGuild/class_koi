const btn = document.querySelector('#btn')
const outputParagraph = document.getElementById('output-text')
const form = document.querySelector('form')
const colorInput = document.querySelector('#color')

// console.log(btn)


btn.innerText = 'Click Me Pretty Please...'

const colors = [
	'rebeccapurple',
	'aliceblue',
	'bisque',
	'burlywood',
	'cornflowerblue',
	'coral',
	'mediumseagreen',
	'springgreen'
]

function randomColor () {
	const randomFloat = Math.random() * colors.length // random float between 0 and 7 (upper-bound exclusive)
	const randomInteger = Math.floor(randomFloat) // float rounded down to an integer (range 0-6)
	const color = colors[randomInteger] // color accessed from array with integer
	return color
	return colors[Math.floor(Math.random() * colors.length)]
}

btn.addEventListener('click', function () {
	// alert('you clicked the button')
	// element.innerText is a writeable property
	// you can assign it to be the new text inside of the element
	btn.innerText = 'you clicked me'
	btn.style.textDecoration = 'line-through'
	outputParagraph.innerText = 'you clicked the button'
	document.body.style.backgroundColor = randomColor()
})

form.addEventListener('submit', function (event) {
	event.preventDefault() // preventDefault will stop the default outcome of the event
	// in this case, that is the page refresh on form submission
	console.log(event)
	outputParagraph.innerText = 'form submitted'
	console.log(colorInput.value)
	// an input element has a .value property, which can be used to extract whatever the
	// user has entered into the input
	document.body.style.backgroundColor = colorInput.value
	// input.value is also a writeable property, to reset the input
	// element to be empty you can do this:
	colorInput.value = ''
})