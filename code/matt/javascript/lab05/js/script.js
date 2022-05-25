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
            hasQuotes: true,
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
                // set firstPage and lastPage booleans for pagination if a search occured
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
                    // prevent currentPage from exceeding actual current page if too many clicks happen before response
                    this.currentPage = res.data.page
                // hide pagination if random quote was selected
                } else {
                    this.firstPage = false
                    this.lastPage = false
                }
                // set booleans if no results were found
                if (res.data.quotes[0].body == 'No quotes found') {
                    this.hasQuotes = false
                    this.lastPage = false
                } else {
                    this.hasQuotes = true
                }
                // console.log(res.data)
            })
        },
        // clear search field and stored term
        clearSearchField () {
            this.searchTermField = null
            this.searchTerm = null
        },
        // set boolean to true if a search occurred
        wasSearchTrue() {
            this.wasSearch = true
        },
        // set boolean to false if no search ocurred
        wasSearchFalse () {
            this.wasSearch = false
        },
        // set search term from field when run (to avoid typing in field interfering with paginated results)
        updateSearchTerm () {
            this.searchTerm = this.searchTermField
        },
        // reset page counter
        resetPage() {
            this.currentPage = 1
        },
        // increment page counter
        nextPage () {
            this.currentPage++
        },
        // decrement page counter
        prevPage () {
            this.currentPage--
        },
        // scroll to top of page
        toTop () {
            window.scrollTo(0,0)
        },
    }
}).mount('#app')