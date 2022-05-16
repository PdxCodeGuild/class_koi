const App = {
	data () {
		return {
			message: 'welcome to Vue',
			inputText: '', //  this was required so that the <input v-model="inputText"> would work
			colors: ['red', 'green', 'blue']
		}
	},
	methods: {
		clickButton () { // this event will run when an element
			// with v-on:click="clickButton" is clicked
			// alert('the button was clicked')
			// this.message is the message property from the data object
			// this.alertPopUp is the alertPopUp method from the methods object
			this.message += ' will this work?'
			this.message += ' and thank you so much for clicking the button'
			this.alertPopUp()
			this.inputText = 'you clicked the button'
			// console.log(this) // this is the Vue app
		},
		alertPopUp () {
			alert('this is the alert popup')
		}
	}
}

const app = Vue.createApp(App)
app.mount('#app')


// def index(request):
//     context = {'message': 'welcome to Vue'}
//     return render(request, 'index.html', context)

// const button = document.querySelector('button')
// const p = document.querySelector('p')
// button.addEventListener('click', function () {
// 	alert('the button was clicked')
// 	p.innerText = 'this one was from vanilla dom manipulation'
// })

// const input = document.querySelector('input')
// const output = document.querySelector('#output')
// input.addEventListener('change', function (event) {
// 	output.innerText = 'Vanilla DOM Manipuation version: ' + event.target.value
// })