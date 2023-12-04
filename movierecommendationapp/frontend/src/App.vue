<script setup>
import { RouterView, RouterLink } from 'vue-router';
</script>

<script>
export default {
  name: 'App',
  methods: {
    async user_logout() {
      let response = await fetch(('http://localhost:8000/logout'), {
        method: 'GET',
        credentials: 'include',
        mode: 'cors',
        referrerPolicy: 'no-referrer'
      })
        .then(response => {
          // clear session data on client-side
          sessionStorage.clear();
          // redirect  user to  login page
          window.location.href = 'http://localhost:8000';
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>



<!-- RouterView goes to the index.js to check the defined routes rules -->
<template>

  <main>
    <div class="bar">
      <div class="navlinks">
      <RouterLink active-class="active" to="/">Home</RouterLink>
      <RouterLink active-class="active" to="/recommendations">Recommendations</RouterLink>
      <button v-on:click="user_logout">Logout</button>
    </div>


    </div>
    <RouterView />
  </main>
</template> 

<style scoped>

.navlinks{
  display: flex;
  flex-direction: row;
  padding: 15px
}
.navlinks a{
  margin: 0 10px;
}
.active{
  font-weight: bold;
  color:#7375e2
}
.bar{
  background-color: #97a9ff;
}

button {
  color:#f1f2f9;
  background-color:#7375e2;
}

</style>


