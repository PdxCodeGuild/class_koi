
const App = {
    data() {
        return {
            test: 'IT WORKS',
            baseUrl: 'https://favqs.com/api/quotes',
            quotes: '',
            userSearch: '',
            checkedName: ''
        }
    },

    created() {
        this.getQuote()
    },

    methods: {
        getQuote() {
            axios({
                url:this.baseUrl,
                headers: {
                    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"',
                    // Accept: 'application/json'
                },
                method: 'get'
            }).then(res => {
                this.quotes = res.data.quotes
            })
        },

        searchQuote(checkedName) {
            console.log(checkedName)
            if(checkedName == 'keyword') {
                axios({
                    url:this.baseUrl,
                    headers: {
                        'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
                    },
                    params: { filter: this.userSearch },
                    method: 'get'
                }).then(res => {
                    this.quotes = res.data.quotes
                })
            }
            else {
                axios({
                    url:this.baseUrl,
                    headers: {
                        'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
                    },
                    params: {
                        filter: this.userSearch,
                        type: checkedName
                    },
                    method: 'get'
                }).then(res => {
                    this.quotes = res.data.quotes
                })
            }
        }
    }
}

const app = Vue.createApp(App)

app.mount('#app')