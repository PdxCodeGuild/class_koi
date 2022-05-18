// Axios example w/o VUE
// this code is not necessary for the vue app or any axios calls in it to work

axios({ // in JavaScript, it is common that a function will take an options/config
	// objects, sometimes as the sole parameter
	url: 'https://icanhazdadjoke.com',
	method: 'get',
	headers: {
		Accept: 'application/json'
	} // the axios(optionsObj) call will return a Promise
	// a Promise is an object representing the eventual fullfillment or rejection
	// of an AJAX Request.  You can use .then on a promise and pass in a callback function
	// to be performed when the promise is resolved
}).then(res => console.log(res.data))

// python version:
// import requests
// res = requests.get('https://icanhazdadjoke.com', headers={'Accept': 'application/json'})
// print(res) # <Response[200]>
// data = res.json()
// print(data) # the dictionary with the joke


// VUE

const App = {
	data () {
		return {
			dadJoke: '',
			searchTerm: '',
			baseUrl: 'https://icanhazdadjoke.com/',
			jokes: []
		}
	},

	created () { // the created method will run automatically when the
		// page first loads
		this.getDadJoke()
	},

	methods: {
		getDadJoke () {
			console.log({ 'this in getDadJoke': this }) // this is the vue app
			// this.dadJoke = 'Dad joke incoming...'
			axios({ // this entire thing will return a promise
				url: this.baseUrl,
				headers: { Accept: 'application/json' },
				method: 'get'
			}).then(res => {
				console.log({ 'this in .then': this }) // this is the Window if not in an arrow function
				// this will still be the vue app if in an arrow function
				this.dadJoke = res.data.joke
			})
		},

		searchDadJokes () {
			axios({
				method: 'get',
				url: this.baseUrl + 'search',
				headers: { Accept: 'application/json' },
				params: { term: this.searchTerm }
			}).then(res => {
				console.log(res.data)
				this.jokes = res.data.results
			})
		}
	}
}

// python search for multiple jokes
// import requests
// term = input('what jokes do you want to see? )
// headers = {'Accept': 'application/json'}
// params = {'term': term}
// res = requests.get('https://icanhazdadjoke.com/search, headers=headers, params=params)
// print(res.json()['results']) # list of jokes

// in a Node Environment you would import just what you need, like this:
// import { createApp } from 'vue' // python: from vue import create_app

const app = Vue.createApp(App)

app.mount('#app')