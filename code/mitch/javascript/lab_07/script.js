


const App = {
	data () {
		return {
			output: '',
			userVIN: '',
            userYear: '',
            userMake: '',
            userModel: '',
            makeList: ["A","B","C",],
            modelList: [],
			baseUrl: 'https://vpic.nhtsa.dot.gov/api/vehicles/',
			error: ''
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
                    data: this.userVIN
                },
			}).then(response => {
				console.log(response)
				this.output = response.data.Results[0]
			})
		},
        getAllMakes () {
			axios({
				url: this.baseUrl + "GetMakesForManufacturerAndYear/" + this.userYear,
				method: 'get',
                headers: {
                    Accept: 'application/json'
                },
				params: { 
                    format: 'json',
                    data: this.userYear
                },
			}).then(response => {
				console.log(response)
				this.makeList = response.data.Results[0]
			})
		},
        searchByYear () {
			axios({
				url: this.baseUrl + "GetMakesForManufacturerAndYear/" + this.userYear,
				method: 'get',
                headers: {
                    Accept: 'application/json'
                },
				params: { 
                    format: 'json',
                    data: this.userYear
                },
			}).then(response => {
				console.log(response)
				this.makeList = response.data.Results[0]
			})
		},
	}
}

const app = Vue.createApp(App)

app.mount('#app')