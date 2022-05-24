const App = {
    // the data property is a function that returns an object
    data() {
      return {
        message: 'Hello World',
        baseURL: "https://imsea.herokuapp.com//api/1?q=",
        imgFetch: undefined,
        searchTerm: "",
        
      }
    },

    methods: {
        getImg () {
			axios({ 
                method: 'get',
                url: this.baseURL + this.searchTerm,
				headers: { Accept: 'application/json', },
				method: 'get',
                params: null,

			}).then(res => {
				// console.log({ 'this in .then': this }) // this is the Window if not in an arrow function
				// this will still be the vue app if in an arrow function

                this.imgFetch = res.data // hmmm data
	})},





    },


  }
  // this is how you create & mount the app in Vue 3:
  Vue.createApp(App).mount('#app')