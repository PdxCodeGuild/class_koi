// alert('all hooked up!')

// setTimeout is given a callback function and a number of milliseconds
// that it should wait before performing the callback
setTimeout(function () {
	alert('all hooked up... after 2 seconds')
}, 2000)

// setInterval is like setTimeout, but the function will keep repeating
// itself every 5000 (or another value) milliseconds
const intervalId = setInterval(function () {
	const userInput = prompt('5 seconds have passed. would you like to wait 5 more seconds?')
	if (userInput.toLowerCase() == 'no') {
		clearInterval(intervalId)
	} 
}, 5000)

alert('i wait for no timeout...')