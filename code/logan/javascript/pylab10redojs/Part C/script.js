const App = {
    // the data property is a function that returns an object
    data() {
      return {
        headline: 'The Amazing Vue ROT13 Device!',
        inputMessage: "",
        output: "",
        standard_s: "abcdefghijklmnopqrstuvwxyz",
        rot13_s: "nopqrstuvwxyzabcdefghijklm",
        txtInput:"",
        encodedString: ""
      }
    },

    methods: {
        encMessage () {
            const string = this.txtInput
            for (let i=0; i<string.length; ++i) {
                // if (string[i] in standard_s == true) {
                if (this.standard_s.includes(string[i]) == true) {
                    let newLetInd = this.standard_s.indexOf(string[i])
                    this.encodedString = this.encodedString.concat(this.rot13_s[newLetInd])
            
                }
                else {
                    this.encodedString = this.encodedString.concat(string[i])
                }
            
            
            }

        }
    }
  }
  // this is how you create & mount the app in Vue 3:
  Vue.createApp(App).mount('#app')