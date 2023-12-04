<template>
    
    <div id="show_movies">
    <h1>Please input your favourite movies</h1>
    <h2>Add at least 3 movies</h2>
    </div>

    <!-- REFERENCE: Stack Overflow. (n.d.). javascript - Search bar vue.js. [online] Available at: https://stackoverflow.com/questions/69287834/search-bar-vue-js -->
    <input class="searchbar" type ="text" v-model ="search" placeholder="Seach movies">
    <div v-for="movie in filteredMovies" :key="movie.id">
          <p>{{ movie.id }}</p>
          <h3>{{ movie.title }}</h3>
          <p><b>Plot:</b><i>{{ movie.plot_outline}}</i></p>
          <small><b>Genre:</b> {{ movie.genres}}</small>&nbsp
          <small><b>Happy:</b> {{ movie.happy}}</small>&nbsp
          <small><b>Angry:</b> {{ movie.angry}}</small>&nbsp
          <small><b>Sad:</b> {{ movie.sad}}</small>&nbsp
          <br>
          <br>
          <button @click="addMovie(movie.title)" >Select</button>

    </div>

    
</template>

<script lang="js">
  export default {
      data() {
        return{
          userid: 0,
          movies: [],
          search:"",
          title: [],
        }
      },

    // first time user inputs, get movies before or during component loads
      created(){
        this.getMovies()
      },
    //   for every user input, get movies updates
      updated(){
        this.getMovies()
      },
      
      computed: {
        filteredMovies() {
            console.log(this.movies)
            return this.movies.filter(movie => {
                return movie.title.toLowerCase().indexOf(this.search.toLowerCase()) != -1;
      });
    }
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

        async getMovies(){
            let response = await fetch(("http://localhost:8000/movies"),{
                method: "GET",
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
            })
            let data = await response.json()
            this.movies = data.movies
            console.log(this.movies)
        },

        async addMovie(currentmovie){   
            let response = await fetch(("http://localhost:8000/addmovies"),{
                method: 'POST', 
                credentials: "include",
                mode: "cors",   
                referrerPolicy: "no-referrer",
                body:JSON.stringify({
                    title:currentmovie,
                    userid:this.userid
                })
            })
            let data = await response.json()
            this.movies = data.movies
            console.log(this.movies)
            alert('Movie selected')
        },

      },

        async mounted(){
            this.getUserSessionId()
            this.getMovies()
            }
    }

</script>

<style>
.searchbar:hover{
    background-color: #b6b6e1;
    
}
.searchbar{
    color:#7375e2;
    width: 500px;
    height:30px;
    padding:5px;
    margin:5px;
    border-radius: 10px;
}

</style>