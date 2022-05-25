


const App = {
    data () {
        return {
            output: '',
			userVIN: '',
            userYear: '',
            userMake: '',
            userModel: '',
            makeList: [],
            modelList: [],
			baseUrl: 'https://vpic.nhtsa.dot.gov/api/vehicles/',
		}
	},
    
    
	methods: {
        searchByVIN () {
            axios({
                url: this.baseUrl + "DecodeVinValues/" + this.userVIN,
				method: 'get',
                headers: {
                    Accept: 'application/json'
                },
				params: { 
                    format: 'json',
                },
			}).then(response => {
                console.log(response)
				this.output = response.data.Results[0]
			})
		},
        getAllMakes () {
            axios({
                url: this.baseUrl + "GetAllMakes/",
				method: 'get',
                headers: {
                    Accept: 'application/json'
                },
				params: { 
                    format: 'json',
                },
			}).then(response => {
                console.log(response)
				this.makeList = response.data.Results
			})
		},
        searchByManAndYear () {
            axios({
                url: this.baseUrl + "GetModelsForMakeYear/make/" + this.userMake + "/modelyear/" + this.userYear,
				method: 'get',
                headers: {
                    Accept: 'application/json'
                },
				params: { 
                    format: 'json',
                },
			}).then(response => {
                console.log(response)
				this.modelList = response.data.Results
			})
		},
	}
}

const app = Vue.createApp(App)


app.component('vue-select', VueNextSelect)
app.mount('#app')
