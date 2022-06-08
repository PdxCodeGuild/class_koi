// you don't need an HTML file to run javascript
// if you have node installed, you can run a javascript file like this:
// node fileName.js

console.log('hello world')
// these won't work, the DOM is not here, since
// this is just being run without an associated HTML file
// alert is undefined, and so is window
// alert('hello world')
// window.alert('hello world')

const plants = [
	'alocasia',
	'angel wing begonia',
	'pothos',
	'lilies',
	'monstera',
	'snake plant',
	'aloe',
	'string of pearls'
]

// forEach: an alternative to the javascript for loop
// for loop
for (let i=0; i<plants.length; i++) {
	const plant = plants[i]
	console.log(plant)
	// plants[i] = plant.toUpperCase() // modifying the array
}

// forEach: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach

plants.forEach(plant => console.log(plant))

// you could also declare a function elsewhere...
function iLike (thing) {
	console.log('i like ' + thing)
}
// then pass that funciton to the forEach method
plants.forEach(iLike)

// parameters for js array method callback functions
// if there is just one parameter, it is the element
// if there is a second parameter, that is the index of that element
// if there is a third parameter, that is the array itself

plants.forEach((plant, index, arr) => {
	console.log(plant, index, arr)
	// if you want to capitalize each plant:
	arr[index] = plant.toUpperCase()
})

// array.map returns a new array
// filled with the values that the callback function returns
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map

const emojiPlants = plants.map(plant => `🌿${plant}🌱`)

console.log(emojiPlants)

// array.map is used a lot in react
// react uses JSX, where functions can return html
const divPlants = emojiPlants.map(plant => `<div>${plant}</div>`)
console.log(...divPlants)

// ... is the spread operator https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax
// it's used to unpack an array to its values
// for instance...
const colors = ['red', 'green', 'blue']
// this logs the whole array
console.log(colors)
// this logs the individual values
console.log(...colors)
// as though console.log(['red', 'green', 'blue']) is the code that was written

// array.filter, like map, returns a new array
// however, it only includes elements for which the callback function
// returns a truthy value
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter

const multiWordPlants = plants.filter(plant => plant.includes(' '))
console.log(multiWordPlants)

// chaining array methods
// this is similar to chaining QuerySet and/or Object Manager methods together in Django:
// Todo.objects.filter(completed=True).order_by('-creation_date')

const ff7Characters = [
	{ name: 'Tifa', attackStyle: 'short range' },
	{ name: 'Cloud', attackStyle: 'short range' },
	{ name: 'Barret', attackStyle: 'long range' },
	{ name: 'Aerith', attackStyle: 'long range' },
]

const shortRange = ff7Characters.filter(character => character.attackStyle === 'short range').map(character => `${character.name} is a short range fighter`)
console.log(shortRange)

// since whitespace doesn't matter the way it does in python,
// for ease of reading, these methods can be chained on multiple lines
const longRange = ff7Characters
	.filter(character => character.attackStyle === 'long range')
	.map(character => character.name + ' is a long range fighter.')

console.log(longRange)