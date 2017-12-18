import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import Swipe from '@/components/Swipe'

Vue.use(VueRouter)
Vue.use(VueResource)
Vue.http.options.root = 'http://localhost:8000/api/'

export default new VueRouter({
  routes: [
    {
      path: '/swipe',
      name: 'Swipe',
      component: Swipe
    }
  ]
})
