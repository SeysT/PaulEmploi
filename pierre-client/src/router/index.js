import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import Bucketlist from '@/components/Bucketlist'
import HelloWorld from '@/components/HelloWorld'
// import Offer from '@/components/Offer'
// import OfferExpand from '@/components/OfferExpand'
import Swipe from '@/components/Swipe'

Vue.use(VueRouter)
Vue.use(VueResource)
Vue.http.options.root = 'http://localhost:8000/api/'

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
    },
    {
      path: '/swipe',
      name: 'Swipe',
      component: Swipe
    }
  ]
})
