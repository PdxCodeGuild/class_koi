const app = Vue.createApp({
    data() {
        return {
            apiKey: "4c5d0a1cc7ce77b5205f548273305589",
            searchInput: "",
            metric: true,
            f: [],
            c: [],
            mph: [],
            kph: [],
            roundKph: [],
        }
    },
    methods: {
        toggleMetric() {
            this.metric = !this.metric
        },
        fetchWeather(city) {
            fetch("https://api.openweathermap.org/data/2.5/weather?q=" 
            + city 
            + "&units=imperial&appid=" 
            + this.apiKey
            )
            .then((response) => response.json())
            .then((data) => this.displayWeather(data));
        },
        displayWeather(data) {
            const { name } = data;
            const { icon, description } = data.weather[0];
            const { temp, humidity } = data.main;
            const { speed } = data.wind;
            document.querySelector(".city").innerText = "Weather in " + name;
            document.querySelector(".icon").src =
                "https://openweathermap.org/img/wn/" + icon + ".png";
            document.querySelector(".description").innerText = description;
            this.f.splice(0,1,(Math.round(temp)));
            this.c.splice(0,1,Math.round((temp-32)*.5556));
            document.querySelector(".temp").innerText = Math.floor(temp) + "°F";
            document.querySelector(".humidity").innerText = "Humidity: " + humidity + "%";
            document.querySelector(".wind").innerText = "Wind speed: " + speed + " mph";
            this.mph.splice(0,1,speed);
            this.kph.splice(0,1,((speed*1.609344).toFixed(2)));
            document.querySelector(".weather").classList.remove("loading");
            document.body.style.backgroundImage = "url('https://source.unsplash.com/1600x900/?" + name + "-landscape')";
        },
        search()  {
            this.fetchWeather(this.searchInput);
        },

    },
    beforeMount() {
        this.fetchWeather("Sedona");
      },

})

app.mount('#app')
