axios({
  url: "https://favqs.com/api/qotd",
  method: "get",
  header: {
    Accept: "application/json",
  },
}).then((res) => console.log(res.data));

// alert(API_KEY);

const App = {
  data() {
    return {
      qotd: "",
      searchQuotes: "",
      searchTerm: "",
      searchType: "",
      randomQuote:"",
      baseUrl: "https://favqs.com/api/",
    };
  },

  created() {
    this.getQotd();
    this.getRandomQuotes();
    this.getSearchQuotes()
  },

  methods: {
    getQotd() {
      console.log({ "this in getQotd": this });
      axios({
        url: this.baseUrl + "qotd/",
        headers: {
          Accept: "application/json",
        },
        method: "get",
      }).then((res) => {
        console.log({ "this in .then": this });
        this.qotd = res.data.quote;
      });
    },
    getSearchQuotes() {
      this.error = "";
      axios({
        url: this.baseUrl + "quotes",
        headers: { Accept: "application/json" ,
        "Authorization": `Token token="461af7a6a1ab9c45a31e7ce2b03dd8de"`},
        params: { filter: this.searchTerm, type: this.searchType}, 
      }).then((res) => {
        console.log(res.data);
        this.searchQuotes = res.data.quotes;
      });
    },
    getRandomQuotes() {
      axios({
        url: this.baseUrl + "quotes/",
        headers: { Accept: "application/json",
        "Authorization": `Token token="461af7a6a1ab9c45a31e7ce2b03dd8de"`},
        method: "get",
      }).then((res) => {
        console.log({ "this in .then": this });
        this.randomQuote = res.data.quotes;
      });
    },
  },
};

const app = Vue.createApp(App);

app.mount("#app");
