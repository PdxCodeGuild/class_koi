const App = {
    // the data property is a function that returns an object
    data() {
      return {
        headline: 'Hello World',
        toDoInc: ["run", "water plants"],
        toDoComp: [],
        txtInput: ""

      }
    },

    methods: {
        addTask () {
          input = this.txtInput
          this.toDoInc.push(input)
        },
        compTask () {},
        remTask () {},


    }






}
Vue.createApp(App).mount('#app')