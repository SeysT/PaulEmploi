<template>
  <div>
    <Navbar :title="title"></Navbar>
    <Card v-for="id in offers_ids" :offer_id="id" :key="id"></Card>
    <button v-on:click.prevent="like()">Like</button>
    <button v-on:click.prevent="dislike()">Dislike</button>
  </div>
</template>

<script>
  import Card from '../components/Card.vue'
  import Navbar from '../components/Navbar.vue'

  export default {
    name: 'Swipe',
    components: {
      Card,
      Navbar
    },
    data () {
      return {
        title: 'Swipe',
        offers_ids: ['1', '2', '3']
      }
    },
    methods: {
      get_offers_ids: function () {
        let url = 'api/profile/offers_to_show/'
        this.$http.get(url).then(function (resp) {
          this.offers_ids = resp.body.map(offer => offer.id.toString())
        })
      },
      like: function () {
        let url = 'api/offers/' + this.offers_ids[0] + '/accept/'
        this.$http.post(url)
        this.offers_ids.shift()
      },
      dislike: function () {
        let url = 'api/offers/' + this.offers_ids[0] + '/refuse/'
        this.$http.post(url)
        this.offers_ids.shift()
      }
    },
    created: function () {
      this.get_offers_ids()
    }
  }
</script>

<style scoped>

</style>
