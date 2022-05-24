const App = {
    // the data property is a function that returns an object
    data() {
      return {
        message: 'Cats! (under construction)',
        baseURL: " https://api.thecatapi.com/v1/images/search",
        breedURL: "https://api.thecatapi.com/v1/breeds",
        catFetch: undefined,
        urlFetch: undefined,
        imgObj: undefined,
        searchTerm: "",
        imgURLs: [],
        breedData: undefined,
        breedList: [],
        breedIDList: [],
        breedDict: {},
        shortDict: {},
        // newKey: undefined,
        // newVal: undefined,
        // select: document.getElementById("selectBreed"),
        
      }
    },
    created () {
      this.breedGrab()
    //   for(let i = 0; i < this.breedList.length; i++) {
    //     var opt = this.breedList[i];
    //     var el = document.createElement("option");
    //     el.textContent = opt;
    //     el.value = opt;
    //     this.select.appendChild(el);
    // }
    // didn't work
      let i = 0 // under construction might not work



      },

    methods: {
      getCat () {
        axios({
          url: this.baseURL,
          headers: { Accept: 'application/json', Authorization:"9bf907ff-5c70-40c1-93a1-16d55b35d6bb" },
          method: 'get',
  
        }).then(res => {
                  this.catFetch = res.data // 
                  this.urlFetch = this.catFetch[0].url
                  this.imgObj = {"url": this.urlFetch}
                  this.imgURLs.push(this.imgObj)



    })},







      searchCat () {
			  axios({
        url: this.baseURL,
				headers: { Accept: 'application/json', Authorization:"9bf907ff-5c70-40c1-93a1-16d55b35d6bb" },
				method: 'get',
        parameters: "",

			}).then(res => {


	})},

      breedGrab () {
        axios({
        url: this.breedURL,
        headers: { Accept: 'application/json', Authorization:"9bf907ff-5c70-40c1-93a1-16d55b35d6bb" },
        method: 'get',

      }).then(res => {
        this.breedData = res.data
        let i = 0
        while (i < this.breedData.length) {
        this.breedList.push(this.breedData[i].name)
        i++}
        i = 0
        while (i < this.breedData.length) {
        this.breedIDList.push(this.breedData[i].id)
        i++}
    

  })},



    },


  }
  // this is how you create & mount the app in Vue 3:
  Vue.createApp(App).mount('#app')