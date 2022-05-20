axios({
    url: 'https://favqs.com/api/qotd',
    method: 'get',
    headers: {
        Accept: 'application/json'
    }
})//.then(res => console.log(res.data))

const App = {
    data () {
        return {
            quote: '',
            author: '',
            searchTerm: '',
            searchType: '',
            page: 1,
            lastPage: 'true',
            baseUrl: 'https://favqs.com/api/',
            quotes: [],
            message: '',
            listStart: 1,

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
            })
        },

        searchQuote () {
            axios({
                method: 'get',
                url: this.baseUrl + 'quotes/',
                headers: { 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"' },
                params: { filter: this.searchTerm, type: this.searchType, page: this.page}
            }).then(res => {
                this.quotes = res.data.quotes
                this.lastPage = res.data.last_page
                this.page = res.data.page
                console.log(res.data)
                if (this.searchType === 'keyword') {
                    console.log(res.data.quotes)
                    this.message = this.quotes.length + " Quotes containing the word " + "'" + this.searchTerm + "'"
                }
                else if (this.searchType === 'author') {
                    this.message = this.quotes.length + " Quotes by " + this.quotes[0].author
                }
                else {
                    this.message = this.quotes.length + " Quotes tagged with " + "'" + this.searchTerm + "'"
                }
            })
        },

        nextPage() {
            this.page++
            this.searchQuote()
            this.listStart += 25

        },

        getQuoteList () {
            axios({
                method: 'get',
                url: this.baseUrl + 'quotes/',
                headers: { 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"' },

            }).then(res => {
                this.quotes = res.data.quotes
                this.message = "25 Random Quotes"
                this.lastPage = true
            })
        }
    }
}

const app = Vue.createApp(App)
app.mount('#app')