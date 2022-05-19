// Vanilla JavaScript Without Interacting with the HTML

// Comments:
// this is commented out
// so is this
/*
this is
multi-
line
comment
*/

// output and feedback via alert and console.log
// alert will display the message in a dialog box in the browser
// alert('hello world')
// console.log is more like Python's print, it will log to the web browser's console
console.log('I was gonna say that but not make a big deal out of it.')

// getting input from the user, in place of python's input, use prompt
// let message = prompt('type somethin\'')
// alert('you typed ' + message)


/* Declaring Variables */
// in JavaScript, variables can be assigned with var, let & const
// let
// let allows the variable to be reassigned

let x = 10
console.log(x) // 10
x += 5
console.log(x) // 15

// const
// const does not allow variable reassignment
const y = 10
console.log(y) // 10
// y += 5
// console.log(y) // TypeError: attempt to assign to readonly property

const numbers = [1, 2, 3, 4, 5]
numbers.push(6) // this works because numbers is not being redefined, the numbers array is using its push method to modfiy itself
console.log(numbers)
numbers.push('hello')
console.log(numbers)
// numbers = [1, 2, 3, 4, 5, 6, 7]

/* Arrays */
// A JavaScript Array is like a Python List... but different

// Python List
// colors = ['red', 'green', 'blue']
// colors.append('yellow')
// print(colors)
// colors[2] = 'purple'
// print(len(colors))

// JavaScript Array
let colors = ['red', 'green', 'blue']
colors.push('yellow')
console.log(colors)
colors[2] = 'purple'
console.log(colors)
console.log(colors.length)

/* Objects */
// A JavaScript Object is like a Python Dictionary AND a Python Object

// Python Dictionary
// teacher_dictionary = {'name': 'Pete', 'role': 'Instructor'}
// print(teacher_dictionary['name'])
// teacher_dictionary['class_type'] = 'day'


// JavaScript Object
let teacherObject = { name: 'Pete', role: 'Instructor' }
console.log(teacherObject['name'])
console.log(teacherObject.name) // in JavaScript, you can use dot notation with objects
teacherObject.classType = 'day'
console.log(teacherObject)


// you can chain dot notation together for nested objects
// here is a complex data structure with objects, arrays, strings, and numbers
let apiResponse = {
	data: {
		location: {
			city: 'Portland',
			state: 'OR'
		},
		forecast: [
			{
				date: 'May 10th',
				high: 60,
				low: 40
			},
			{
				date: 'May 11th',
				high: 65,
				low: 45
			}
		]
	}
}
// tomorrowsHigh is declared using dot notation for objects, and bracket notation for arrays
let tomorrowsHigh = apiResponse.data.forecast[1].high
console.log("Tomorrow's high is " + tomorrowsHigh)

// you can use quotes for string property names, and you have to in some cases:
irregularPropertyNames = {
	'test': 1,
	'XCSRF-Token': '153jkl;j4k3l21;jkl;23',
	'1moreThing': '123',
	0: 'does this work'
}

console.log(irregularPropertyNames.test)
console.log(irregularPropertyNames['test'])

/* Random */
// There is no random module in JavaScript, readily available like Python's
// There is, however, Math.random, a function you can use whenever you need it
// to get a random value between 0 and 1

// get a random element from an list/array in Python/JavaScript
// Python
// # colors is already defined
// import random
// print(random.choice(colors)) # prints out a random color

// from random import random
// from math import floor
// colors[floor(random() * len(colors))] # this ends up being the same as the javascript version

// JavaScript
console.log(colors)
// console.log(Math.random(), colors.length) // Math.random() returns a random float between 0 and 1, colors.length is the number of elements in the colors array
// console.log(Math.random() * colors.length) // this gives us a random float between 0 and the length of the array (4)
// console.log(Math.floor(Math.random() * colors.length)) // this gives us an integer from 0 to the length of the array (0-3)
console.log(colors[Math.floor(Math.random() * colors.length)])

/* Functions */
// the syntax is different
// whitespace and indentations don't matter the same way as they do in python
// you will use curly braces {} for the scope of functions, as well as conditionals and for loops

// Python
// def add(x, y):
//   return x + y

// JavaScript
function add(x, y) {
	return x + y
}
console.log(add(4, 6))

let subtract = function(x, y) { // another way of defining a function
	return x - y
}
console.log(subtract(7, 4))

// Python Lambda function
// multiply = lambda x, y: x * y

// JavaScript Arrow Function
// returns what comes after the fat arrow =>
let multiply = (x, y) => x * y
console.log(multiply(7, 11))

// you can use curly braces as well for a more comlex function
let randomElementFromArray = (array) => {
	let randomNumber = Math.random() * array.length
	let randomIndex = Math.floor(randomNumber)
	let randomElement = array[randomIndex]
	return randomElement
}

console.log(randomElementFromArray(colors))

/* Strings and Numbers */

// python fstring... JavaScipt Template Literal (aka) Sting Interpolation
// Python: message = f'Hello {name}, thanks for coming to {event}.'

// Javascript
let guest = 'Bud'
let eventName = 'Annual Gathering of the Buds'
let message = `Hello ${guest}, thanks for coming to ${eventName}.`
console.log(message)

// Type Conversion in Python
// number = int(input('Please enter a number: '))

// you can use parseInt and parseFloat to get a number out of a numeric string
let number = prompt('Please enter a number: ')
console.log(number)
console.log(typeof number)
number = parseInt(number)
console.log(number)
console.log(typeof number)

// automatic type conversion
// Python would give you a type error for '1' + 2
// Javascript just makes it work
let w = '1'
let z = 2
console.log(w + z) // '12'
console.log(z + w) // '21'

/* For Loops */
// Python
// for color in colors:
//   print(color)

console.log(colors) // ['red', 'green', 'purple', 'yellow']
for (let i=0; i<colors.length; i++) {
	console.log(i)
	console.log(colors[i])
}

// You can think of this for loop like a Python while loop:
// colors = ['red', 'green', 'blue']
// i = 0
// while i < len(colors):
//     print(colors[i])
//     i += 1

// Using the forEach array method to console.log each element of the array
// colors.forEach(color => console.log(color))

/* Conditionals */

// == vs ===
// == will attempt type coercion, === will not
// rule of thumb: always use ===

console.log(1 == 1) // true
console.log(1 === 1) // true
console.log(1 == '1') // true
console.log(1 === '1') // false

// and: &&
let temperature = 60
let sky = 'clear'
if (temperature > 60 && sky === 'clear') { // will execute code in {} if both conditionals are true
	console.log('nice day')
} else if (temperature < 60 || sky === 'cloudy') {
	console.log('not so nice day')
} else {
	console.log('dunno about the weather')
}

