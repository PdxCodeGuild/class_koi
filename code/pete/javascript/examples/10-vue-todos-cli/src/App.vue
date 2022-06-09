<template>
  <h1 id="todos-header">ToDos</h1>
  <form @submit.prevent="addNewTodo">
    <label for="new-todo">New Todo:</label>
    <input v-model="newTodo" id="new-todo" />
    <button type="submit">Add New Todo</button>
  </form>
  <ul>
    <ToDo v-for="(todo, i) in todos" :text="todo" :key="i" />
  </ul>

</template>

<script>
import ToDo from './components/ToDo.vue'
export default {
  name: 'App',
  components: {
    ToDo
  },
  data () {
    return {
      todos: [
        'wash the car',
        'walk the dog',
        'butter the cat'
      ],
      newTodo: ''
    }
  },
  methods: {
    addNewTodo () {
      this.todos.push(this.newTodo)
      this.newTodo = ''
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
h1 {
  text-align: center;
}
</style>
