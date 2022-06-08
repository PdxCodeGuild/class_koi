const app = Vue.createApp({
    data() {
        return {
            title: 'todo list',
            tasks: [
                {name: 'test 1', delete: false},
                {name: 'test 2', delete: false},
                {name: 'test 3', delete: false},
                {name: 'test 4', delete: false},
                {name: 'test 5', delete: false},
                {name: 'test 6', delete: false},
                {name: 'test 7', delete: false},
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
        delItem(index) {
            // this.delete(this.tasks, index);
            // this.tasks.splice(index, 1);
            // this.tasks.splice(this.tasks.indexOf(task), 1);
            this.tasks.splice(index, 1);
            // delete this.tasks[(this.tasks.indexOf(task))];
            console.log(this.tasks);
        }
    }
})

app.mount('#app')