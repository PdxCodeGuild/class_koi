axios({
    url: 'https://favqs.com/api',
    method: 'get',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Token token="620fbf04812832502f434c92105e70da"' //'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
    }
}).then(res => console.log(res.data.body))

const App = {
    data () {
        return {
            favQuote: '',
            favQAuthor: '',
            searchTerm: '',
            quotes: [],
            authorTrue: false,
            tagTrue: false,
            searchParams: { filter: undefined, type: undefined, type: undefined, page: undefined },
            qSearched: false,
            qPageNumber: 1,
            qLastPage: undefined
        }
    },
    created() {
        this.getFavQ()
    },
    watch: {
        searchTerm(newSearch, oldSearch) {
            if (newSearch.length >= 0) {
                this.qSearched = false
                this.authorTrue = false
                this.qPageNumber = 1
                this.qLastPage = true
            }
        }
    },
    methods: {
        getFavQ () {
            this.favQuote = 'Quote incoming...',
            axios({
                url: 'https://favqs.com/api/qotd',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Token token="620fbf04812832502f434c92105e70da"'
                },
                method: 'get',
            }).then(res => {
                this.favQuote = res.data.quote.body
                this.favQAuthor = res.data.quote.author
                console.log(res.data.quote)
                console.log(this.favQuote)
                console.log(this.favQAuthor)
            })

        },
        searchFavQ () {
            this.searchParams = { filter: this.searchTerm, page: this.qPageNumber}
            // console.log(this.authorTrue)
            // console.log(this.tagTrue)
            if (this.authorTrue || this.tagTrue) {
                if (this.authorTrue) {
                    this.searchParams = { filter: this.searchTerm, type: 'author', page: this.qPageNumber }
                }
                if (this.tagTrue) {
                    this.searchParams = { filter: this.searchTerm, type: 'tag', page: this.qPageNumber }
                }
                
            }
            console.log(this.searchParams)
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Token token="620fbf04812832502f434c92105e70da"'
                },
                params: this.searchParams // { filter: this.searchTerm, type: 'author', type: 'tag' }
            }).then(res => {
                this.qPageNumber = res.data.page
                this.qLastPage = res.data.last_page
                this.qSearched = true
                console.log(this.qLastPage)
                this.quotes = res.data.quotes
                // this.quotes = res.data.quote
                // console.log(this.quotes)
            })
        },
        nextQPage () {
            this.qPageNumber++
            this.searchFavQ()
        },
        previousQPage () {
            this.qPageNumber--
            this.searchFavQ()
        }
    }
}

const app = Vue.createApp(App)
app.mount('#app')

        // this.qKeyword = whatever
            // this.qTag = whatever
            // equivocate the checkbox to the searchTerm (maybe?) so the filter can filter by that..
            /*[Log] Object (script.js, line 38)
            author: "Georges Bataille"
            author_permalink: "georges-bataille"
            body: "A judgment about life has no meaning except the truth of the one who speaks last, and the mind is at ease only at the moment when everyon…"
            dialogue: false
            downvotes_count: 0
            favorites_count: 1
            id: 59022
            private: false
            tags: ["truth"] (1)
            upvotes_count: 0
            url: "https://favqs.com/quotes/georges-bataille/59022-a-judgment-ab-" */