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
            baseUrl: 'https://favqs.com/api/',
            quotes: [],

        }
    },

    methods: {
        getQuote () {
            this.quote = 'Quote incoming...'
            axios({
                methods: 'get',
                url: this.baseUrl + 'qotd/',
                headers: {'Accept': 'application/json'},
            }).then(res => {
                this.quote = '"' + res.data.quote.body + '"'
                this.author = '-- ' + res.data.quote.author
                console.log(res.data)
                console.log(res.data.quote.body)
                console.log(res.data.quote.author)
            })
        },

        searchQuote () {
            axios({
                method: 'get',
                url: this.baseUrl + 'search',
                headers: { 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"' },
                params: { term: this.searchTerm }
            }).then(res => {
                console.log(res.data.quotes)
                this.quotes = res.data.quotes
            })
        },

        getQuoteList () {
            axios({
                method: 'get',
                url: this.baseUrl + 'quotes/',
                headers: { 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"' },

            }).then(res => {
                console.log(res.data.quotes[0].author)
                this.quotes = res.data.quotes
            })
        }
    }
}

const app = Vue.createApp(App)
app.mount('#app')