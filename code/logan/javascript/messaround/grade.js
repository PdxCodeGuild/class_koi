let userScore = parseInt(prompt("Please enter a numeric score (0-100):  "))
// if I put a + before prompt, it would auto-convert it to a number.

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