// Vue Conversions

const App = {
    data () {
        return {
            entryLabel: 'Please enter conversion information below.',
            units: {
                feet: {unit: 'feet', coefficient: .3048},
                miles: {unit: 'miles', coefficient: 1609.34},
                meters: {unit: 'meters', coefficient: 1},
                kilometers: {unit: 'kilometers', coefficient: 1000},
                yards: {unit: 'yards', coefficient: .9144},
                inches: {unit: 'inches', coefficient: .0254},
                lightyears: {unit: 'lightyears', coefficient: 946100000000000},
            },
            userInput: 0,
            inputUnit: undefined,
            outputUnit: undefined,
            output: ''
        }
    },

    methods: {
        convertUnit () {
            console.log(this.inputUnit)
            let toMetersCoeff = this.units[this.inputUnit].coefficient
            console.log(toMetersCoeff)
            console.log(this.userInput)
            meterValue = this.userInput * toMetersCoeff
            console.log(meterValue)
            let outputCoeff = this.units[this.outputUnit].coefficient
            outputValue = (meterValue / (outputCoeff))
            console.log(outputValue)
            this.output = `${outputValue}`
        }
    },
}

const app = Vue.createApp(App)
app.mount('#app')