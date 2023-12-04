// References:
// www.youtube.com. (n.d.). Vue 3 Routing - Beginner to Advanced. [online] Available at: https://www.youtube.com/watch?v=PBqQO-keR1s&ab_channel=LaithAcademy
import {createRouter, createWebHistory} from "vue-router";
import HomePage from "../views/HomePage.vue";
import RecommendationPage from  "../views/RecommendationPage.vue";

// to determine which pages to render for each correspoinding path
const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomePage
        },

        {
            path: '/recommendations',
            name: 'recommendations',
            component: RecommendationPage 
        },


    ]
})

export default router