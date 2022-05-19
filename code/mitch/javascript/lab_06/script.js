
const App = {
	data () {
		return {
                quoteSearchTerm: null,
                quotes: [],
                searchType: '',
                page: 1,
                lastPage: false,
                
		}
	},

    mounted() {
        this.$refs.input.focus()
    },

    created () {
        this.searchQuotes()
    },

    updated() {
        this.$refs.input.focus()
    },

	methods: {
 
        scrollToTop() {
            window.scrollTo(0,0);
        },
          
        searchQuotes () {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: { 
                    Accept: 'application/json',
                    Authorization: 'Token token="bd5ff2c92ebe246e003253c172340874"'
                },
                params: {
                    filter:this.quoteSearchTerm, 
                    type:this.searchType,
                    page: this.page
                }
            }).then(res => {
                console.log(res.data)
                this.quotes = res.data.quotes
                this.page = res.data.page
                this.lastPage = res.data.last_page
            })
        }
    }
}


const app = Vue.createApp(App)

app.mount('#app')


