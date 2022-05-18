
const App = {
	data () {
		return {
                quoteSearchTerm: '',
                quotes: [],
                searchType: ''
		}
	},

    created () {
        this.getQuotes()
    },

	methods: {
        getQuotes () {
			axios({
				method: 'get',
				url: 'https://favqs.com/api/quotes/',
				headers: { 
                    Accept: 'application/json',
                    Authorization: 'Token token="bd5ff2c92ebe246e003253c172340874"'
                },

			}).then(res => {
				this.quotes = res.data.quotes
			})
		},
		searchQuotes () {
			axios({
				method: 'get',
				url: 'https://favqs.com/api/quotes/',
				headers: { 
                    Accept: 'application/json',
                    Authorization: 'Token token="bd5ff2c92ebe246e003253c172340874"'
                },

                if (_searchType === "Keyword") {
				    params: { filter: this.quoteSearchTerm }
                }
                elif (this.searchType === "Author") {
				    params: { filter: this.quoteSearchTerm + "%type=author" }
                }
                elif (this.searchType === "Tag") {
				    params: { filter: this.quoteSearchTerm  + "%type=tag"}
                }
			}).then(res => {
				console.log(res.data)
				this.quotes = res.data.quotes
			})
		}
	}
}

const app = Vue.createApp(App)

app.mount('#app')


