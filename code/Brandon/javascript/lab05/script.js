const App = {
  data() {
    return {
      message: "welcome to Vue",
      inputText: "",
      listItems: [],
    };
  },
  methods: {
    clickButton() {
      this.listItems.push({
        task: this.inputText,
        complete: false,
      });
      inputText = "";
    },
    deleteItem() {
      var elem = document.getElementById("del");
      elem.parentNode.remove(elem);
    },
  },
};

const app = Vue.createApp(App);
app.mount("#app");
