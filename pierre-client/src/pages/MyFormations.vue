<template>
  <div class="container">
    <Navbar :title="title"></Navbar>
    <div class="wrap">
      <div class="cards">
        <Card v-for="id in my_ids" 
          :card_id="id" 
          :is_formation=true 
          :key="id"
          class="cards_item"></Card>
    </div>
    </div>
  </div>
</template>

<script>
  import Card from '../components/Card.vue'
  import Navbar from '../components/Navbar.vue'

  export default {
    name: 'MyFormations',
    components: {
      Card,
      Navbar
    },
    data () {
      return {
        title: 'My Formations',
        my_ids: ['1', '2', '3']
      }
    },
    methods: {
      get_my_ids: function () {
        let url = 'api/profile/kept_formations'
        this.$http.get(url).then(function (resp) {
          this.my_ids = resp.body.map(formation => formation.id.toString())
        })
      }
    },
    created: function () {
      this.get_my_ids()
    }
  }
</script>

<style scoped>
.cards_item{
  visibility: visible;
  position: relative;
  margin: 15px;
}
</style>
