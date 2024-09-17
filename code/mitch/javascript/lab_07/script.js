


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
    
    created() {
        this.getAllMakes()
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
                this.userYear = this.output.ModelYear
                this.userMake = this.output.Make
                this.userModel = this.output.Model
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
        searchByMakeAndYear () {
            if (this.userMake === "") return
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
        undo (userObject) {
            if (userObject == "year") {
                this.userYear = ""
                this.userMake = ""
                this.userModel =""
                this.modelList = []
            }else if (userObject == "make") {
                this.userMake = ""
                this.userModel =""
                this.modelList = []
            }else if (userObject == "model") {
                this.userModel = ""
            }
        },
	}
}

const app = Vue.createApp(App)


app.component('vue-select', VueNextSelect)
app.mount('#app')
