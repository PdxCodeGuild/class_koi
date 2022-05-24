// let nums = []
// let total = 0
// let avg = 0

const App = {
    // the data property is a function that returns an object
    data() {
      return {
        headline: 'The Amazing Vue Average Device!',
        inputNumber: 0,
        output: "",
        // totalMessage: `Total value ${total}`,
        // avgMessage: `Total value ${avgMessage}`,
        nums: [],
        total: 0,
        avg: 0
      }
    },
    methods: {
        compAvg () {

            const input = parseInt(this.inputNumber)
            this.total += input
            this.nums.push(input)
            this.avg = (this.total/this.nums.length)

            this.output = `Total: ${this.total} Avg: ${this.avg}`
            // alert(total)

        }
    }
  }
  // this is how you create & mount the app in Vue 3:
  Vue.createApp(App).mount('#app')