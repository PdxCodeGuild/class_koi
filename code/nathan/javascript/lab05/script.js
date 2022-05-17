
const App = {
    data() {
        return {
            // object
            works: 'APP WORKS',
            task: '',
            completed: false,
            todoList: []
        }
    },

    methods: {
        addTodo() {
            const newTask = this.task
            const todoList = this.todoList
            
            todoList.push(newTask)
        },

        removeTodo(todo) {
            const todoList = this.todoList
            const todoIndex = todoList.indexOf(todo)

            todoList.splice(todoIndex, 1)
        },

        completeTodo(todo, index) {
            const todoList = this.todoList
            const todoIndex = todoList.indexOf(todo)
            const completeButton = document.getElementById("complete-button" + index)
            const todoItem = document.getElementById(todo + index)

            completeButton.style.display = "none"
            todoItem.style.textDecoration = "line-through"
        }
    }
}

const app = Vue.createApp(App)
app.mount('#app')