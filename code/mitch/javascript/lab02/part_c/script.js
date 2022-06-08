

let conversion_ratios = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254,
}


const App = {
    
    data () {
        return {
            output:'',       
            number_input:0,
            input_unit:'ft',
            output_unit:'ft',
		}
	},

	methods: {
		goButton () { 
            let number = this.number_input
            let meters_output = number * conversion_ratios[this.input_unit]
            let output = meters_output / conversion_ratios[this.output_unit]
        
            this.output = `${number} ${this.input_unit} is equal to ${output.toPrecision(3)} ${this.output_unit}`
        }
	}
}


const app = Vue.createApp(App)
app.mount('#app')
