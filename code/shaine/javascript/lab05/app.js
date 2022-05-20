const app = Vue.createApp({
    data() {
        return {
            title: 'todo list',
            tasks: []
        }
    },
    methods:{
        newItem() {
            if (!this.tasks.name) {
                return
            }
            this.tasks.push ({
                name: this.tasks.name,
                del: ''
            });
            this.tasks.name = "";
        },
        delItem(task) {
            this.tasks.splice(this.tasks.indexOf(task), 1)
        }
    }
})

app.mount('#app')