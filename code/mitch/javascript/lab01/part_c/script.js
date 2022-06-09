

const App = {

	data () {
		return {
            average: '',
            nums: [],
            running_sum: 0,        
		}
	},

	methods: {
		goButton () { 
            let number = number_input.value
            this.nums.push(parseInt(number))
            this.running_sum += parseInt(number)
            this.average = this.running_sum / this.nums.length;
            this.average = this.average.toPrecision(3)
        }
	}
}


const app = Vue.createApp(App)
app.mount('#app')





