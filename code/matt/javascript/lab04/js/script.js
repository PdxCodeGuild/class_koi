// generate app
const { createApp } = Vue
createApp({
    data () {
        return {
            // set up variables
            pageTitle: 'Ayyy Another To-Do List!',
            warning: '',
            showWarning: 'none',
            itemInput: '',
            toDoList: [],
            completedList: [],
        }
    },
    created () {
        if (localStorage.getItem('toDoList')) {
            this.toDoList = JSON.parse(localStorage.getItem('toDoList'))
        }
        if (localStorage.getItem('completedList')) {
            this.completedList = JSON.parse(localStorage.getItem('completedList'))
        }
    },
    methods: {
        addItem () {
            if (this.itemInput) {
                this.toDoList.push(this.itemInput)
                this.itemInput = ''
                this.saveToLocal()
                this.warning = ''
                this.showWarning = 'none'

            } else {
                this.warning = 'Ayyy you didn\'t type anything!'
                this.showWarning = 'block'
            }
        },
        deleteItem (item, listName) {
            listName.splice(listName.indexOf(item),1)
            this.saveToLocal()
        },
        toggleItem (item, listName) {
            listName.splice(listName.indexOf(item),1)
            if (listName == this.toDoList) {
                this.completedList.push(item)
            } else {
                this.toDoList.push(item)
            }
            this.saveToLocal()
        },
        saveToLocal () {
            const parsedToDo = JSON.stringify(this.toDoList)
            localStorage.setItem('toDoList', parsedToDo)
            const parsedComplete = JSON.stringify(this.completedList)
            localStorage.setItem('completedList', parsedComplete)
        }
    }
}).mount('#app')