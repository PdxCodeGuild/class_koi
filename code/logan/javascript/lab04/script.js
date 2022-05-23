const App = {
	data () {
		return {
			test: 'Hello World',
            headline: 'Vue Quotes',
            faveQ: "",
            qAuthor: "",
            qotdURL: "https://favqs.com/api/qotd",
			baseURL: "https://favqs.com/api/quotes/",
            fQuotes: undefined,
            searchTerm: "",
			error: "",

		}
	},
    
    created () {
        this.getQuote()
    },

	methods: {
		// heavily indebted to that Pete code
        getQuote () {
			// console.log({ 'this in getDadJoke': this }) // this is the vue app
			// this.dadJoke = 'Dad joke incoming...'
			axios({ // this entire thing will return a promise
				// url: this.baseUrl,
                url: this.qotdURL,
				headers: { Accept: 'application/json' },
				method: 'get'
			}).then(res => {
				// console.log({ 'this in .then': this }) // this is the Window if not in an arrow function
				// this will still be the vue app if in an arrow function

                this.faveQ = res.data.quote.body
                this.qAuthor = res.data.quote.author

                // alert(this.faveQ)
	})},
		// heavily indebted to that Pete code
        searchQuote () {
			this.error = ''
		axios({
			method: 'get',
			url: this.baseURL,
			headers: { Accept: 'application/json', Authorization: "Token token=75781e1e8edbf2eb68848384abbbd2bb"}, // doesn't work
			params: { filter: this.searchTerm },
		}).then(res => {
			// throw new Error('Something went wrong. Please try again.')
			console.log(res.data)
			this.fQuotes = res.data.quotes // might need to fool with this .results
		}).catch(err => this.error = err.message) // .catch will run if an error occurs
		// alert(this.fQuotes)
		// .finally(() => alert('finally ran')) // .finally is always going to run},
	}
}
}

const app = Vue.createApp(App)
app.mount('#app')