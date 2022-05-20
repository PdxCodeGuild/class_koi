const App = {
    data () {
        // let id = 0

       return {
            newTask : '',
            incompleteTasks :[
                'Django Library',
                'Django Chirp',
                'Javascript Vue ToDo',
                'Javascript Vue Quotes',
            ],
            completeTasks :[

            ]
        }
    },
    
    methods: {
        addTask() {
            console.log(this.newTask)
            // this.tasks.push({ id: id++, text: this.newTask })
            this.tasks.push(this.newTask)
        },

        removeTask(tasks) {
            this.incompleteTasks = tasks.value.filter((t) => t !== task)   
        },  this.completeTasks
    },
}

const app = Vue.createApp(App)
app.mount('#app')
