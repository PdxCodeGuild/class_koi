axios({
    url: 'https://lldev.thespacedevs.com/2.2.0/spacecraft',
    method: 'get',
    headers: {
        Accept: 'application/json'
    }
}).then(res => {
    console.log(res.data.next)
})

const App = {
    data () {
        return {
            searchTerm: '',
            baseUrl: 'https://lldev.thespacedevs.com/2.2.0/',
            imageUrl: '',
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
            //console.log(res.data.results[0])
            axios({
                url: this.baseUrl + 'spacecraft/', // url: this.url,
                headers: { Accept: 'application/json' },
                method: 'get',
                // params: { limit: 10, offset: 0 }
            }).then(res=> {
                console.log(res.data)
                this.spacecraft = res.data.results
                console.log(this.spacecraft)
                this.imageUrl = res.data.results[0].spacecraft_config.image_url
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
                params: { search: this.searchTerm },
                method: 'get',
            }).then(res=> {
                console.log(res.data)
                console.log(res.data.results[0].name)
                this.spacecraft = res.data.results
                this.nextUrl = res.data.next
                this.previousUrl = res.data.previous
            })
        }
            
    }
}

const app = Vue.createApp(App)
app.mount('#app')