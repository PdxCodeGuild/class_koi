const input = document.querySelector('#input')
const button = document.querySelector('#button')
const output = document.querySelector('#output')

button.addEventListener('click', function () {
	const percentage = +input.value // using the + before this will make it interpret the value as a number, if possible
	// console.log(percentage)
	let letterGrade

	if (percentage < 60) {
		letterGrade = 'F'
	} else if (percentage < 70) {
		letterGrade = 'D'
	} else if (percentage < 80) {
		letterGrade = 'C'
	} else if (percentage < 90) {
		letterGrade = 'B'
	} else {
		letterGrade = 'A'
	}

	// ternary operator
	// let aOrAn = (letterGrade === 'F' || letterGrade === 'A')
	let aOrAn = ['A', 'F'].includes(letterGrade)
		? 'an'
		: 'a'

	output.innerText = `Your Grade is ${aOrAn} ${letterGrade}.`
})