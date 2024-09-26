axios({
  url: "https://api.weather.gov/",
  method: "get",
  header: {
    Accept: "application/json",
  },
}).then((res) => console.log(res.data));

const App = {
  data() {
    return {
      alerts: "",
      searchTerm: "",
      state: "",
      baseUrl: "https://api.weather.gov/",
    };
  },

  created() {},

  methods: {
    getAlerts() {
      console.log({ "this in getAlerts": this });
      axios({
        url: this.baseUrl + "alerts",
        headers: {
          Accept: "application/json",
        },
        method: "get",
      }).then((res) => {
        console.log({ "this in .then": this });
        this.alerts = res.data.features;
        this.searchTerm = "the US";
      });
    },

    getState() {
      console.log({ "this in getAlerts": this });
      axios({
        url: this.baseUrl + "alerts/active",
        headers: {
          Accept: "application/json",
        },
        params: { area: this.searchTerm },
      }).then((res) => {
        console.log({ "this in .then": this });
        this.alerts = res.data.features;
      });
    },
  },
};

const app = Vue.createApp(App);

app.mount("#app");
