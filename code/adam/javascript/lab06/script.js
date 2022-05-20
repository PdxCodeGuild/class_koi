axios({
    url: 'https://favqs.com/api/qotd',
    method: 'get',
    headers: {
        Accept: 'application/json'
    }
}).then(res => console.log(res.data))

const App = {
    data () {
        return {
            quote: '',
            author: '',
            searchTerm: '',
            searchType: '',
            baseUrl: 'https://favqs.com/api/',
            quotes: [],
            message: ''

        }
    },

    created () {
        this.getQuote()
    },

    methods: {
        getQuote () {
            this.quote = 'Quote incoming...'
            axios({
                methods: 'get',
                url: this.baseUrl + 'qotd/',
                headers: {'Accept': 'application/json'},
            }).then(res => {
                this.quote = res.data.quote.body
                this.author = res.data.quote.author
                console.log(res.data)
                console.log(res.data.quote.body)
                console.log(res.data.quote.author)
            })
        },

        searchQuote () {
            axios({
                method: 'get',
                url: this.baseUrl + 'quotes/?filter=' + this.searchTerm,
                headers: { 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"' },
                params: { filter: this.searchTerm }
            }).then(res => {
                console.log(res.data.quotes)
                this.quotes = res.data.quotes
                this.message = this.quotes.length + " Quotes about " + this.searchTerm
                console.log(this.searchType)
                if (this.searchType === 'keyword') {
                    this.searchTerm = this.searchTerm
                }
                else if (this.searchType === 'author') {
                    console.log(this.searchTerm)
                }
                else {
                    this.searchTerm = this.searchTerm + '&type=tag'
                    console.log(searchTerm)
                }
            })
        },

        getQuoteList () {
            axios({
                method: 'get',
                url: this.baseUrl + 'quotes/',
                headers: { 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"' },

            }).then(res => {
                console.log(res.data.quotes)
                console.log(res.data.quotes[0].body)
                console.log(res.data.quotes[0].author)
                this.quotes = res.data.quotes
                this.message = "25 Random Quotes"
                console.log(this.message)
            })
        }
    }
}

const app = Vue.createApp(App)
app.mount('#app')