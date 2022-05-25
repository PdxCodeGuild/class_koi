const App = {
    // the data property is a function that returns an object
    data() {
      return {
        message: 'CAT JUDGMENT',
        baseURL: " https://api.thecatapi.com/v1/images/search",
        breedURL: "https://api.thecatapi.com/v1/breeds",
        breedSearchURL: "https://api.thecatapi.com/v1/breeds/search",
        breedParam: undefined,
        catFetch: undefined,
        urlFetch: undefined,
        imgObj: undefined,
        searchTerm: "",
        imgURLs: [],
        hallOfFame: [],
        hallOfShame: [],
        breedData: undefined,
        breedList: [],
        breedIDList: [],
        breedDict: {},
        shortDict: {},
        clickCheck: false,
        desc: undefined,
        // newKey: undefined,
        // newVal: undefined,
        // select: document.getElementById("selectBreed"),
        
      }
    },
    created () {
      this.breedGrab()

      },

    methods: {
      getCat () {
        this.imgURLs = []
        this.clickCheck=true
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







      searchCat (breed) {
        this.imgURLs = []
        let i = this.breedList.indexOf(breed)
        this.breedParam = this.breedIDList[i]
        // alert(this.breedParam)
        this.clickCheck=true


			  axios({
        url: this.breedSearchURL,
        // url: this.baseURL,
				headers: { Accept: 'application/json', Authorization:"9bf907ff-5c70-40c1-93a1-16d55b35d6bb" },
				method: 'get',
        parameters: {q:this.breedParam},

			}).then(res => {
        this.catFetch = res.data //
        alert(this.catFetch)
        // this.urlFetch = this.catFetch[0].url
        // this.imgObj = {"url": this.urlFetch}
        // this.imgURLs.push(this.imgObj)


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
    rFame () {
      this.hallOfFame.push(this.imgObj)

    },

    rShame () {
      this.hallOfShame.push(this.imgObj)

    },



    },


  }
  // this is how you create & mount the app in Vue 3:
  Vue.createApp(App).mount('#app')