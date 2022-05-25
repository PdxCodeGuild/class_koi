Vue.createApp({
	data () {
		return {
			allTodos: [
				{ text: 'wash the car', completed: false, id: 0 },
				{ text: 'walk the dog',  completed: false, id: 1 },
				{ text: 'butter the cat', completed: true, id: 2 }
			],
			newTodo: '',
			id: 3
		}
	},

	computed: { // computed properties, like data object properties,
		// are properties of the vue app, defined by what they return
		// however, they are going to listen to any other propert
		todos () {
			return this.allTodos.filter(todo => todo.completed === false)
		},

		todones () {
			return this.allTodos.filter(todo => todo.completed === true)
		}
	},

	methods: {
		addTodo () {
			// console.log(this.todos, this.newTodo)
			this.allTodos.push({ text: this.newTodo, completed: false, id: this.id })
			this.newTodo = ''
			this.id++
		},

		deleteTodo (id) {
			console.log(id)
			// this filter will give us all todos with that id
			// there is only one todo, so we will access the 0th element
			const todo = this.allTodos.filter(todo => todo.id === id)[0]
			const index = this.allTodos.indexOf(todo)
			console.log(index)
			this.allTodos.splice(index, 1)
			
			// console.log('delete', i)
			// splice docs: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice
			// array.spice(indexToDelete, numberOfItemsToDelete)
			// this.allTodos.splice(i, 1)
		},

		toggleCompleteTodo (todo) {
			console.log(todo)
			todo.completed = !todo.completed
		}
	}
}).mount('#app')