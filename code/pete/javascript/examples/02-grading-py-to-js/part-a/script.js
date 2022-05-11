let userScore = prompt('Please enter the numeric grade (0-100):')
// console.log(userScore, typeof userScore)
userScore = parseInt(userScore)
// console.log(userScore, typeof userScore)

// use parseInt and prompt on one line to get a number
// let userScore = parseInt(prompt('Please enter the numeric grade (0-100):'))
// use the + operator before prompt to have it evaluate the prompt string into a number
// let userScore = +prompt('Please enter the numeric grade (0-100):')

let letterGrade

if (userScore < 60) {
	letterGrade = 'F'
} else if (userScore < 70) {
	letterGrade = 'D'
} else if (userScore < 80) {
	letterGrade = 'C'
} else if (userScore < 90) {
	letterGrade = 'B'
} else {
	letterGrade = 'A'
}

alert(`${userScore}% is a ${letterGrade}`)


