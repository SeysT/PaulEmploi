<template>
  <div class="container">
    <Navbar :title="title"></Navbar>
    <Card v-for="id in my_ids" :offer_id="id" :key="id"></Card>
  </div>
</template>

<script>
  import Card from '../components/Card.vue'
  import Navbar from '../components/Navbar.vue'

  export default {
    name: 'MyOffers',
    components: {
      Card,
      Navbar
    },
    data () {
      return {
        title: 'My Offers',
        my_ids: ['1', '2', '3']
      }
    },
    methods: {
      get_my_ids: function () {
        let url = 'api/profile/accepted_offers'
        this.$http.get(url).then(function (resp) {
          this.my_ids = resp.body.map(offer => offer.id.toString())
        })
      }
    },
    created: function () {
      this.get_my_ids()
    }
  }
</script>

<style scoped>

</style>
