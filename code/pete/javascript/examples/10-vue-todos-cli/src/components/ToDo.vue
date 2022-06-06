<template>
  <li>{{ text }}</li>
</template>

<script>
export default {
  name: 'ToDo',
  props: {
    text: String
  }
}
</script>

<style scoped>
li {
  font-size: x-large;
}
</style>