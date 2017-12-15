import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import Bucketlist from '@/components/Bucketlist'
import HelloWorld from '@/components/HelloWorld'
import Offer from '@/components/Offer'
import OfferExpand from '@/components/OfferExpand'

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
      path: '/offer',
      name: 'Offer',
      component: Offer
    },
    {
      path: '/offer/expand',
      name: 'OfferExpand',
      component: OfferExpand
    }
  ]
})
