let page = 1
let keyword = 'dog'

// axios({
// 	url: `https://favqs.com/api/quotes/?page=${page}&filter=${keyword}`,
// 	method: 'get',
// 	headers: {
// 		Accept: 'application/json',
//         Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'
// 	}
// }).then(res => console.log(res.data))



// generate app
const { createApp } = Vue
createApp({
    data () {
        return {
            // set up variables
            quotesObj: '',
            currentPage: 1,
            lastPage: '',
            searchTypes: ['keyword','tag','author'],
            searchType: 'keyword',
            searchTermField: '',
            searchTerm: '',
        }
    },
    created () {
        this.getRandomQuotes()
    },
    methods: {
        getRandomQuotes () {
            axios({
                url: `https://favqs.com/api/quotes/`,
                method: 'get',
                headers: {
                    Accept: 'application/json',
                    Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'
                }
            }).then(res => {
                this.quotesObj = res.data.quotes
                this.lastPage = res.data.last_page
            })
        },
        getQuotes () {
            axios({
                url: `https://favqs.com/api/quotes/?page=${this.currentPage}&filter=${this.searchTerm}`,
                method: 'get',
                headers: {
                    Accept: 'application/json',
                    Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'
                }
            }).then(res => {
                this.quotesObj = res.data.quotes
                this.lastPage = res.data.last_page
            })
        },
        updateSearchTerm () {
            this.searchTerm = this.searchTermField
        },
        resetPage() {
            this.currentPage = 1
        },
        nextPage () {
            this.currentPage++
        },
        prevPage () {
            this.currentPage--
        }
    }
}).mount('#app')