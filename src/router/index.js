import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },

    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path:'/logout',
      name:'logout',
      component:() => import('../views/LogoutView.vue')
    },
    {
      path: '/users/:user_id',
      name: 'userprofiles',
      component: () => import('../views/UserProfileView.vue')
    },
    {
      path: '/profiles/new',
      name: 'createprofile',
      component: () => import('../views/CreateProfileView.vue')
    },
    {
      path: '/profiles/:profile_id',
      name: 'profile-details',
      component: () => import('../views/ProfileView.vue')
    },
    // USED FOR THE MATCH ME
    {
      path: '/profiles/favourites',
      name: 'report',
      component: () => import('../views/FavouritesView.vue')
    },
    //TO BE REMOVED
    // {
    //   path: '/matches/:profile_id',
    //   name: 'MatchMeView',
    //   component: () => import('../views/MatchMeView.vue')
    // }
   
  ]
})

export default router
