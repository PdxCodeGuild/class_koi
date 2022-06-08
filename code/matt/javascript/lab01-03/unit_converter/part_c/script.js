// generate app
const { createApp } = Vue
createApp({
    data () {
        return {
            // create converter object and other variables
            converter: {
                in: .0254,
                ft: .3048,
                yd: .9144,
                mi: 1609.34,
                m: 1,
                km: 1000,
            },
            startDistance: 1,
            startUnit: '',
            endUnit: '',
            results: '',
        }
    },
    methods: {
        // method for button click
        clickButton () {
            if ((this.startUnit == '') || (this.endUnit == '')) {
                // return an error if start/end unit not selected
                this.results = 'Please select start and end units.'
            } else {
                // calculate results and return if input is valid
                endDistance = +parseFloat(this.startDistance * this.converter[this.startUnit] / this.converter[this.endUnit]).toPrecision(3)
                this.results = `${this.startDistance} ${this.startUnit} is equal to ${endDistance} ${this.endUnit}`
            }
        }
    }
}).mount('#app')