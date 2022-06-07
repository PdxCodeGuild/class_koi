axios({
    url: 'https://lldev.thespacedevs.com/2.2.0/launch/?mode=list&search=SpaceX',
    method: 'get',
    headers: {
        Accept: 'application/json'
    }
}).then(res => {
    console.log(res.data)
})

const App = {
    data () {
        return {
            searchType: '',
            searchTerm: '',
            baseUrl: 'https://lldev.thespacedevs.com/2.2.0/',
            spacecraft: [],
            allSpacecraft: [],
            searchCraft: '',
            nextUrl:'',
            previousUrl: '',
            url: 'https://lldev.thespacedevs.com/2.2.0/spacecraft/',
            limit: 10,
            offset: 0, // methods that do this.offset += 10 or this.offset -= 10
            upcomingLaunches: [],
            upcomingLaunchesAll: [],
            previousUrlLaunch: '',
            previousUrlLaunchSearch: '',
            nextUrlLaunch: '',
            nextUrlLaunchSearch: '',
            searchLaunch: '',
            launchesSearched: [],
        }
    },

    methods: {
        getCraft () {
            //console.log(res.data)
            axios({
                url: this.baseUrl + 'spacecraft/', // url: this.url,
                headers: { Accept: 'application/json' },
                method: 'get',
                params: { status: this.searchType} //limit: 10, offset: 0
            }).then(res=> {
                console.log(res.data.results)
                console.log(this.searchType)
                this.spacecraft = res.data.results
                // this.spacecraft = this.allSpacecraft[Math.floor(Math.random()*this.allspacecraft.length)]
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
                // this.nextUrlLaunch = res.data.next
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
                    // this.previousUrl = res.data.previous
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
                this.spacecraft = res.data.results
                this.nextUrl = res.data.next
                this.previousUrl = res.data.previous
            })
        },

        launchSearch() {
            axios({
                url: 'https://lldev.thespacedevs.com/2.2.0/launch/?mode=list&search=' + this.launchSearch,
                headers: { Accept: 'application/json' },
                params: { search: this.searchLaunch },
                method: 'get',                
            }).then(res=> {
                console.log(this.searchLaunch)
                console.log(res.data)
                this.launchesSearched = res.data.results
                this.nextUrlLaunchSearch = res.data.next
                this.previousUrlLaunchSearch = res.data.previous
                console.log(this.nextUrlLaunchSearch)
            })
        },

        getLaunch() {
            axios({
                url: 'https://lldev.thespacedevs.com/2.2.0/launch/upcoming',
                headers: { Accept: 'application/json'},
                method: 'get',
            }).then(res=> {
                this.nextUrlLaunch = res.data.next
                this.previousUrlLaunch = res.data.previous
                this.upcomingLaunches = res.data.results
            })
        },

        nextPageLaunch() {
            axios({
                url: this.nextUrlLaunch,
                headers: { Accept: 'application/json' },
                method: 'get',
            }).then(res=> {
                this.upcomingLaunches = res.data.results
                this.nextUrlLaunch = res.data.next
                this.previousUrlLaunch = res.data.previous
                console.log(res.data)
            })
        },
        
        previousPageLaunch() {
            axios({
                url: this.previousUrlLaunch,
                method: 'get',
                headers: { Accept: 'application/json' },
                }).then(res=> {
                    this.upcomingLaunches = res.data.results
                    this.nextUrlLaunch = res.data.next
                    this.previousUrlLaunch = res.data.previous
                    console.log(res.data)
                    console.log(res.data.next)
                })
            },

        nextPageLaunchSearch() {
            axios({
                url: this.nextUrlLaunchSearch,
                headers: { Accept: 'application/json' },
                method: 'get',
            }).then(res=> {
                this.launchesSearched = res.data.results
                this.nextUrlLaunchSearch = res.data.next
                this.previousUrlLaunchSearch = res.data.previous
                console.log(res.data)
            })
        },

        previousPageLaunchSearch() {
            axios({
                url: this.previousUrlLaunchSearch,
                method: 'get',
                headers: { Accept: 'application/json' },
                }).then(res=> {
                    this.launchesSearched = res.data.results
                    this.nextUrlLaunchSearch = res.data.next
                    this.previousUrlLaunchSearch = res.data.previous
                    console.log(res.data)
                    console.log(res.data.next)
                })
            },
        
    }
}

const app = Vue.createApp(App)
app.mount('#app')