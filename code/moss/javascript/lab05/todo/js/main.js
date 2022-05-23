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
            completedTasks :[

            ]
        }
    },
    
    methods: {
        addTask() {
            console.log(this.newTask)
            // this.tasks.push({ id: id++, text: this.newTask })
            this.incompleteTasks.push(this.newTask)
            this.newTask = ''
        },

        removeTask(task) {
            this.incompleteTasks = incompleteTasks.filter((t) => t !== incompleteTasks)   
            // this.completeTasks.push(t)
            
        },  

        checkTask() {
            this.completeTasks.push(this.incompleteTasks)

        },
    },
}


const app = Vue.createApp(App)
app.mount('#app')
