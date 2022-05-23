const App = {
	data () {
		return {
			test: 'Hello World',
            headline: 'Vue Quotes',
            faveQ: "",
            qAuthor: "",
            qotdURL: "https://favqs.com/api/qotd",
			baseURL: "https://favqs.com/api/quotes/",
            fQuotes: [],
            searchTerm: "",
			error: ""

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
				console.log({ 'this in .then': this }) // this is the Window if not in an arrow function
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
			url: this.baseUrl + 'filter=' + `${searchTerm}` + "&type=tag",
			headers: { Accept: 'application/json' },
			params: { term: this.searchTerm }
		}).then(res => {
			// throw new Error('Something went wrong. Please try again.')
			console.log(res.data)
			this.jokes = res.data.results
		}).catch(err => this.error = err.message) // .catch will run if an error occurs
		.finally(() => alert('finally ran')) // .finally is always going to run},
	}
}
}

const app = Vue.createApp(App)
app.mount('#app')