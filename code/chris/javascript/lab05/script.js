// Vue ToDo

const App = {
    data () {
        return {
            entryLabel: 'Please enter conversion information below:',
            units: {
                feet: {unit: 'feet', coefficient: .3048},
                miles: {unit: 'miles', coefficient: 1609.34},
                meters: {unit: 'meters', coefficient: 1},
                kilometers: {unit: 'kilometers', coefficient: 1000},
                yards: {unit: 'yards', coefficient: .9144},
                inches: {unit: 'inches', coefficient: .0254}, // must be a better way to do this
            },
            userInput: 0,
            inputUnit: undefined,
            outputUnit: undefined,
            output: ''
        }
    },

    methods: {
        convertUnit () {
            let toMetersCoeff = this.units[this.inputUnit].coefficient
            meterValue = this.userInput * toMetersCoeff
            let outputCoeff = this.units[this.outputUnit].coefficient
            outputValue = meterValue / outputCoeff
            this.output = `${outputValue}`
        }
    },
}

const app = Vue.createApp(App)
app.mount('#app')