
const App = {
    data() {
        return {
            // object
            works: 'APP WORKS',
            task: '',
            completed: false,
            todoList: [],
            completedList: []
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

        completeTodo(todo) {
            const todoList = this.todoList
            const todoIndex = todoList.indexOf(todo)
            const completedList = this.completedList

            completedList.push(todo)
            todoList.splice(todoIndex, 1)
        },

        removeCompleted(todo) {
            const completedList = this.completedList
            const todoIndex = completedList.indexOf(todo)

            completedList.splice(todoIndex, 1)
        }
    }
}

const app = Vue.createApp(App)
app.mount('#app')