// var myHtml = document.getElementById('myHtml').innerHTML;


const App = {
    // the data property is a function that returns an object
    data() {
      return {
        // test:"jabberwocky",
        // test2: {name:"jabberwocky"},
        headline: 'To Dos',
        toDoInc: [],
        toDoComp: [],
        txtInput: "",
        toDoTask: undefined,
        incompInput: "",
        compInput: "",
        remInput: "",
        toDo: ""


      }
    },

    methods: {
        addTask () {
          input = this.txtInput
          toDoTask = {
            name:input,
          }
          // toDoTask.innerText = input
          this.toDoInc.push(toDoTask)
          // //
          // let toDoRemove = document.createElement("button")
          // let toDoComplete = document.createElement("button")
          // toDoRemove.innerText = "Remove"
          // toDoComplete.innerText = "Complete"
          // // toDoComplete.
          // toDoTask.appendChild(toDoRemove)
          // toDoTask.appendChild(toDoComplete)
          
          


          // //

        },


        compTask () {
          // let parent = undefined
          // let index = toDoInc.indexOf(parent)
          // this.toDoInc.splice(index, 1)
          let input = this.compInput
          let i = 0
          while (i < this.toDoInc.length) {
          if (this.toDoInc[i].name == input)
          {this.toDoComp.push(this.toDoInc[i])
            this.toDoInc.splice(i, 1)}
          i++
        }

          


        },

        incompTask () {
          // let parent = undefined
          // let index = toDoInc.indexOf(parent)
          // this.toDoInc.splice(index, 1)
          let input = this.compInput
          let i = 0
          while (i < this.toDoComp.length) {
          if (this.toDoComp[i].name == input)
          {this.toDoInc.push(this.toDoComp[i])
            this.toDoComp.splice(i, 1)}
          i++
        }

          


        },



        remTask () {
          let input = this.remInput
          let i = 0
          while (i < this.toDoInc.length) {
            if (this.toDoInc[i].name == input)
            // {this.toDoComp.push(this.toDoInc[i])
              {this.toDoInc.splice(i, 1)}
            i++



          }
          i = 0
          while (i < this.toDoComp.length) {
            if (this.toDoComp[i].name == input)
            // {this.toDoComp.push(this.toDoInc[i])
              {this.toDoComp.splice(i, 1)}
            i++



          }
  
  



          /// no luck
          // const parent = parentNode.name
          // alert(parent)
          // let index = toDoInc.indexOf(parent)
          // toDoInc.splice(index, 1)

        },

        compTaskAlt (toDo) {
          
          let i = this.toDoInc.indexOf(toDo)
          this.toDoComp.push(this.toDoInc[i])
          this.toDoInc.splice(i, 1)

        },

        remTaskAlt (toDo) {
          // fix
          let i = 0
          while (i < this.toDoInc.length) {
            if (this.toDoInc[i] == toDo)
            // {this.toDoComp.push(this.toDoInc[i])
              {this.toDoInc.splice(i, 1)}
            i++
          }

          i = 0
          while (i < this.toDoComp.length) {
            if (this.toDoComp[i] == toDo)
            // {this.toDoComp.push(this.toDoInc[i])
              {this.toDoComp.splice(i, 1)}
            i++
          }

    },

        incompTaskAlt (toDo) {
          let i = this.toDoComp.indexOf(toDo)
          this.toDoInc.push(this.toDoComp[i])
          this.toDoComp.splice(i, 1)

  },
}
}
Vue.createApp(App).mount('#app')