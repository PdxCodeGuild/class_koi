// Vue To Do

const App = {
    data() {
        return {
            toDoList: [],
            descriptionInput: '',
            done: undefined,
            deleted: undefined,
        }
    },
    mounted () {
        this.toDoList = localStorage.getItem('items') ? JSON.parse(localStorage.getItem('items')) : []
    },
    methods: {
        addItem() {
            this.toDoList.push({ itemDescription: this.descriptionInput, done: false, deleted: false })
            localStorage.setItem('items', JSON.stringify(this.toDoList))
        },
        updateList() {
            for (i = 0; i < this.toDoList.length; i++) {
                if (this.toDoList[i].deleted === true) {
                    this.toDoList.splice(i, 1)
                    i--
                }
            }
            console.log(this.toDoList)
            localStorage.setItem('items', JSON.stringify(this.toDoList))
        }
    }
}

const app = Vue.createApp(App)
app.mount('#app')