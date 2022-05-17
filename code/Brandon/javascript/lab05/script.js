const App = {
  data() {
    return {
      message: "welcome to Vue",
      inputText: "",
      listItems: [],
      complete: true,
    };
  },
  methods: {
    clickButton() {
      inputText = this.inputText;
      this.listItems.push(inputText);
    },
    deleteItem(e) {
      var elem = document.getElementById("del");
      elem.parentNode.remove(elem);
      return false;
    },
    completeItem() {
      this.complete = !this.complete;
    },
  },
};

const app = Vue.createApp(App);
app.mount("#app");
