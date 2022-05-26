const app = Vue.createApp({
    data() {
      return {
        query: null,
        data: [],
        select: "",
        selections: ['Keyword','Author', 'Tag'],
        option: "",
      }

    },
    methods: {
        async getData(){

          if (this.select === 'Author'){
            this.option = '&type=author';
          }
          else if (this.select === 'Tag'){
            this.option = '&type=tag';
          }
          // console.log(this.select)
          // console.log(this.option)
            await axios.get(('https://favqs.com/api/quotes/?filter='+ 
              this.query + 
              this.option), {
              
                headers: {
                'Authorization': 'Token token="dfd15da739458b8342b029922062323d"'
              }
            })
            .then((response)=>{
                this.data = response.data.quotes
                console.log(this.data)
            })
            .catch((error)=>{
                console.log(error)
            })
            // this.$refs.aQuery.reset();        
        },
        async startData(){
            await axios.get(('https://favqs.com/api/quotes/'), {
              
                headers: {
                'Authorization': 'Token token="dfd15da739458b8342b029922062323d"'
              }
            })
            .then((response)=>{
                this.data = response.data.quotes
                console.log(this.data)
            })
            .catch((error)=>{
                console.log(error)
            })       
        },

    },
    beforeMount(){
      this.startData();
    },

  })



app.mount('#app')