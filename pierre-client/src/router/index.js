import Vue from 'vue'

import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import VueCookies from 'vue-cookies'

import Swipe from '@/pages/Swipe'
import Login from '@/pages/Login'
import Profile from '@/pages/Profile'
import Home from '@/pages/Home'
import MyOffers from '@/pages/MyOffers'
import Recover from '@/pages/Recover'
import NotFound from '@/pages/NotFound'

Vue.use(VueRouter)

Vue.use(VueCookies)

Vue.use(VueResource)
Vue.http.options.root = 'https://germoon.nebulae.co/' // Si Django tourne en local : 'http://localhost:8000/api/'
Vue.http.interceptors.push(function (request, next) {
  if (Vue.cookies.get('token') !== null) {
    request.headers.set('Authorization', 'Token ' + Vue.cookies.get('token'))
  }
  next(function (resp) {
    if (resp.status === 401) {
      this.$router.push({ name: 'Login', params: { errors: 401 } })
    }
  })
})

export default new VueRouter({
  routes: [
    {
      path: '*',
      name: 'NotFound',
      component: NotFound
    },
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/recover',
      name: 'Recover',
      component: Recover
    },
    {
      path: '/swipe',
      name: 'Swipe',
      component: Swipe
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile
    },
    {
      path: '/profile/my_offers',
      name: 'MyOffers',
      component: MyOffers
    }
  ]
})
