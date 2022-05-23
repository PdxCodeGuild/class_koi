const App = {
	data () {
		return {
			test: 'Hello World',
            headline: 'Vue Quotes',
            faveQ: "",
            qAuthor: "",
            qotdURL: "https://favqs.com/api/qotd",
            fQuotes: [],
            searchTerm: "",

		}
	},
    
    created () {
        this.getQuote()
    },

	methods: {
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

        searchQuote () {},


}}


const app = Vue.createApp(App)
app.mount('#app')