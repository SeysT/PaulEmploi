import Vue from 'vue'

import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import VueCookies from 'vue-cookies'

import Swipe from '@/components/Swipe'
import Login from '@/components/Login'

Vue.use(VueRouter)

Vue.use(VueCookies)

Vue.use(VueResource)
Vue.http.options.root = 'http://localhost:8000/api/'
Vue.http.headers.common['Authorization'] = (
  Vue.cookies.get('token') !== null ? 'Token ' + Vue.cookies.get('token') : undefined
)

export default new VueRouter({
  routes: [
    {
      path: '/swipe',
      name: 'Swipe',
      component: Swipe
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ]
})
