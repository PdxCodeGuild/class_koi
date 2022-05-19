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
            fullURL: ``,
            quotesObj: '',
            currentPage: 1,
            firstPage: true,
            lastPage: true,
            searchTypes: {
                keyword: '',
                tag: 'tag',
                author: 'author',
            },
            searchType: 'keyword',
            searchTermField: null,
            searchTerm: null,
            baseURL: 'https://favqs.com/api/quotes/',
            wasSearch: false,
        }
    },
    created () {
        this.getQuotes()
    },
    methods: {
        getQuotes () {
            axios({
                url: this.baseURL,
                method: 'get',
                headers: {
                    Accept: 'application/json',
                    Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'
                },
                params: {
                    page: this.currentPage,
                    filter: this.searchTerm,
                    type: this.searchTypes[this.searchType],
                }
            }).then(res => {
                this.quotesObj = res.data.quotes
                if (this.wasSearch){
                    if (res.data.page == 1) {
                        this.firstPage = false
                    } else {
                        this.firstPage = true
                    }
                    if (res.data.last_page) {
                        this.lastPage = false
                    } else {
                        this.lastPage = true
                    }
                } else {
                    this.firstPage = true
                    this.lastPage = true
                }
            })
        },
        clearSearchField () {
            this.searchTermField = null
            this.searchTerm = null
        },
        wasSearchTrue() {
            this.wasSearch = true
        },
        wasSearchFalse () {
            this.wasSearch = false
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