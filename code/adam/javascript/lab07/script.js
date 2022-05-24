axios({
    url: 'https://lldev.thespacedevs.com/2.2.0/launch',
    method: 'get',
    headers: {
        Accept: 'application/json'
    }
}).then(res => {
    console.log(res.data.results)
})

const App = {
    data () {
        return {
            searchType: '',
            searchTerm: '',
            baseUrl: 'https://lldev.thespacedevs.com/2.2.0/',
            spacecraft: [],
            searchCraft: '',
            nextUrl:'',
            previousUrl: '',
            url: 'https://lldev.thespacedevs.com/2.2.0/spacecraft/',
            limit: 10,
            offset: 0 // methods that do this.offset += 10 or this.offset -= 10
        }
    },

    methods: {
        getCraft () {
            //console.log(res.data)
            axios({
                url: this.baseUrl + 'spacecraft/', // url: this.url,
                headers: { Accept: 'application/json' },
                method: 'get',
                params: { status: this.searchType,} //limit: 10, offset: 0
            }).then(res=> {
                console.log(res.data)
                console.log(this.searchType)
                this.spacecraft = res.data.results
                console.log(this.spacecraft[0].spacecraft_config.in_use)
                this.nextUrl = res.data.next
                console.log(res.data.next)
                // this.url = res.data.next
            })
        },
        nextPage() {
            axios({
                url: this.nextUrl,
                headers: { Accept: 'application/json' },
                method: 'get',
            }).then(res=> {
                this.spacecraft = res.data.results
                this.nextUrl = res.data.next
                this.previousUrl = res.data.previous
                console.log(res.data)
                console.log('nextUrl '+this.nextUrl)
                console.log('previousUrl '+this.previousUrl)
            })
        },
        previousPage() {
            axios({
                url: this.previousUrl,
                method: 'get',
                headers: { Accept: 'application/json' },
                }).then(res=> {
                    this.spacecraft = res.data.results
                    this.nextUrl = res.data.next
                    this.previousUrl = res.data.previous
                    console.log(res.data)
                    console.log(res.data.next)
            })
        },
        searchKeyword() {
            axios({
                url: this.baseUrl + 'spacecraft/',
                headers: { Accept: 'application/json' },
                params: { search: this.searchTerm, status: this.searchType },
                method: 'get',
            }).then(res=> {
                console.log(res.data)
                console.log(res.data.results[0].name)
                console.log(res.data.results[0].spacecraft_config.in_use)
                this.spacecraft = res.data.results
                this.nextUrl = res.data.next
                this.previousUrl = res.data.previous
            })
        },

        getLaunch() {
            axois({
                url: this.baseUrl + 'launch/',
                headers: { Accept: 'application/json'},
                method: 'get',
            }).then(res=> {
                console.log(res.data)
            })
        }
            
    }
}

const app = Vue.createApp(App)
app.mount('#app')