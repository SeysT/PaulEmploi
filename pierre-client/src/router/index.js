import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import Bucketlist from '@/components/Bucketlist'
import HelloWorld from '@/components/HelloWorld'

Vue.use(VueRouter)
Vue.use(VueResource)
Vue.http.options.root = 'http://localhost:8000/'

export default new VueRouter({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/bucket',
      name: 'Bucketlist',
      component: Bucketlist
    }
  ]
})
