const App = {
    // the data property is a function that returns an object
    data() {
      return {
        headline: 'Hello World',
        toDoInc: [],
        toDoComp: [],
        txtInput: "",
        toDoTask: undefined

      }
    },

    methods: {
        addTask () {
          input = this.txtInput
          toDoTask = document.createElement("li")
          toDoTask.innerText = input
          this.toDoInc.push(toDoTask)
          // //

          let toDoRemove = document.createElement("button")
          let toDoComplete = document.createElement("button")
          toDoRemove.innerText = "Remove"
          toDoComplete.innerText = "Complete"
          toDoComplete.
          toDoTask.appendChild(toDoRemove)
          toDoTask.appendChild(toDoComplete)
          


          // //

        },
        compTask () {


        },
        remTask () {},


    }






}
Vue.createApp(App).mount('#app')