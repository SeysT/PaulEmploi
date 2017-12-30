<template>
  <div>
    <Card v-for="id in offers_ids" :offer_id="id" :key="id"></Card>
    <button v-on:click.prevent="like()">Like</button>
    <button v-on:click.prevent="dislike()">Dislike</button>
  </div>
</template>

<script>
  import Card from './Card.vue'

  export default {
    name: 'swipe',
    components: {
      Card
    },
    data () {
      return {
        offers_ids: ['1', '2', '3']
      }
    },
    methods: {
      get_offers_ids: function () {
        let url = 'profile/offers_to_show/'
        this.$http.get(url).then(function (data) {
          this.offers_ids = data.body.map(offer => offer.id.toString())
        })
      },
      like: function () {
        let url = 'offers/' + this.offers_ids[0] + '/accept/'
        this.$http.post(url).then(function (data) {
          console.log(data)
        })
        this.offers_ids.shift()
      },
      dislike: function () {
        let url = 'offers/' + this.offers_ids[0] + '/refuse/'
        this.$http.post(url).then(function (data) {
          console.log(data)
        })
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
