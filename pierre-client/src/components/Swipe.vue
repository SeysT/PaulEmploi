<template>
  <div>
    <Card v-for="id in offers_ids" :offer_id="id" :key="id"></Card>
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
        let url = 'users/' + '2' + '/offers_to_show'
        this.$http.get(url).then(function (data) {
          console.log(data)
          this.offers_ids = data.body.map(offer => offer.id)
        })
      }
    },
    created: function () {
      this.get_offers_ids()
    }
  }
</script>

<style scoped>

</style>
