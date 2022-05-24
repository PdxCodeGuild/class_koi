const App = {
    // the data property is a function that returns an object
    data() {
      return {
        headline: 'The Amazing Vue Change Device!',
        dollarAmount: 0,
        dollarAdj: 0,
        running_total: 0,
        quarters: 0,
        dimes: 0,
        nickels: 0,
        pennies: 0,
        output: "",
        
      }
    },

    methods: {
        makeChange () {
            const input = parseFloat(this.dollarAmount)
            this.dollarAdj = parseInt((input * 100))
            this.quarters = Math.floor((this.dollarAdj / 25 ))
            this.running_total = (this.dollarAdj % 25)
            this.dimes = Math.floor((this.running_total / 10))
            this.running_total = (this.running_total % 10)
            this.nickels = Math.floor((this.running_total / 5))
            this.pennies = (this.running_total % 5)
            
            this.output = `That's ${this.quarters} quarters, ${this.dimes} dimes, ${this.nickels} nickels, and ${this.pennies} pennies.`

        }

    }






}
Vue.createApp(App).mount('#app')