import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: HomeView
    },
    {
      path: '/home',
      name: 'home',
      component: () => import('../views/UserPageView.vue')
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
      path: '/users/:user_id',
      name: 'userprofiles',
      component: () => import('../views/UserProfileView.vue')
    },
    {
      path: '/profiles/new',
      name: 'createprofile',
      component: () => import('../views/CreateProfileView.vue')
    }
  ]
})

export default router
