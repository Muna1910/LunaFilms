<template>
    <h1><b>Your recommendations:</b></h1>
    <p v-if="findrecs == false && emptyrecs == true"> You need to add movies first </p>
    <p v-else-if="findrecs == true"> Loading ... </p>
  
    <p v-for="movie in recs">
    {{ movie }}
    </p>
  </template>
  
  <script lang="js">
    export default {
        data() {
          return{
            userid: 0,
            recs : [],
            findrecs: false,
            emptyrecs: true
          }
        },
        created() {
          this.getRecommendation()
        },
        methods: {
          async getUserSessionId() {
              let response = await fetch(("http://localhost:8000/session"),{
                  method: "GET",
                  credentials: "include",
                  mode: "cors",
                  referrerPolicy: "no-referrer",
              })
  
              let data = await response.json()
              this.userid = data.user_id
              console.log("This is the user logged in ",this.userid)
          },
  
          async getRecommendation() {
            this.findrecs = true 
            console.log(this.movies)
            let response = await fetch(("http://localhost:8000/recommendation"),{
                method: "GET",
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
            })

            let data = await response.json()
            this.recs = data.recs
            if(this.recs.length> 0){
              this.emptyrecs = false
            }
            
            this.findrecs = false
            console.log("The recommendations are: ",this.recs) 
          }
        },
  
        async mounted(){
          this.getUserSessionId()
          this.getRecommendation()

        }
      }
  
  </script>
  
  <style>
  
  </style>