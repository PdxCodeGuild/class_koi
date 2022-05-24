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
      baseUrl: "https://api.weather.gov/",
    };
  },

  created() {
    this.getAlerts();
  },

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
      });
    },
  },
};

const app = Vue.createApp(App);

app.mount("#app");
