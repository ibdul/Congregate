import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  
  // EVENTS
  {
    path: '/host',
    name: 'host',
    component: () => import('../views/events/Host.vue')
  },
  {
    path: '/join',
    name: 'join',
    component: () => import('../views/events/Join.vue')
  },
  {
    path: '/manage',
    name: 'manage',
    component: () => import('../views/events/Manage.vue')
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
