
// document.querySelector is a method that, when passed a valid css selector as string,
// will return the first occurence of an element that matches that selector
const button = document.querySelector('#button-1')
// another method that would work just as well is:
// const button = document.getElementById('button')
const p = document.querySelector('p')
const form = document.getElementById('color-form')
const colorInput = document.querySelector('#color')
const h1 = document.querySelector('.header')
console.log(form)

// you can set events using element.onclick, element.onsubmit,
// but it's better to use element.addEventListener
// h1.onclick = function () { alert('you clicked the h1') }
function clickH1 () {
	alert('you clicked the h1')
}

const colors = [
	'red',
	'orange', 
	'yellow',
	'green',
	'blue',
	'indigo',
	'violet'
]

function randomColor () {
	return colors[Math.floor(Math.random() * colors.length)]
}

button.innerText = "Please Click Me 🥺" // element.innerText is a writeable property which will change the text inside of an element

p.innerText = 'hello'

button.addEventListener('click', function () {
	// element.style.propertyName is a writeable property. You can dynamically set inline styling this way
	button.style.textDecoration = 'underline'
	p.innerText = 'the button has been clicked'
	document.body.style.backgroundColor = randomColor()

	// you can even have nested event listeners that won't be set until the function
	// that they are in has run
	p.addEventListener('click', function () {
		p.innerText = 'The button has been clicked AND then I was clicked'
	})
})

form.addEventListener('submit', function (event) {
	// if adding a submit event to a form, pass in the event to the callback function
	// and use event.preventDefault() to keep the page from refreshing
	event.preventDefault()
	// console.log(event)
	// console.log(colorInput, colorInput.type)

	// an input has a .value property which can be used to extract what the user has typed into it
	console.log(colorInput.value)
	document.body.style.backgroundColor = colorInput.value
	// the value of an input element is writeable as well, to clear the form field
	// you can just set it to an empty string
	colorInput.value = ''
	p.innerText = 'the form was submitted'
})