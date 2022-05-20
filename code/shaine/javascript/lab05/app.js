const app = Vue.createApp({
    data() {
        return {
            title: 'todo list',
            tasks: [
                {name: 'test 1'},
                {name: 'test 2'},
                {name: 'test 3'},
        ]
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
            this.tasks.splice(this.tasks.indexOf(task), 1);
        }
    }
})

app.mount('#app')