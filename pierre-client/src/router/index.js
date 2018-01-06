import Vue from 'vue'

import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import VueCookies from 'vue-cookies'

import Swipe from '@/pages/Swipe'
import Login from '@/pages/Login'
import Profile from '@/pages/Profile'
import Home from '@/pages/Home'
import MyOffers from '@/pages/MyOffers'

Vue.use(VueRouter)

Vue.use(VueCookies)

Vue.use(VueResource)
Vue.http.options.root = 'http://localhost:8000/api/' // Si Django tourne en local : 'http://germoon.nebulae.co/api/'
Vue.http.interceptors.push(function (request, next) {
  if (Vue.cookies.get('token') !== null) {
    request.headers.set('Authorization', 'Token ' + Vue.cookies.get('token'))
  }
  next()
})

var VueTouch = require('vue-touch')
Vue.use(VueTouch, {name: 'v-touch'})

export default new VueRouter({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
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
