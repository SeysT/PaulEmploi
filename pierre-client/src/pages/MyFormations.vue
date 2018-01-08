<template>
  <div>
    <Card v-for="id in my_ids" :card_id="id" :is_formation=true :key="id"></Card>
  </div>
</template>

<script>
  import Card from '../components/Card.vue'

  export default {
    name: 'MyFormations',
    components: {
      Card
    },
    data () {
      return {
        my_ids: ['1', '2', '3']
      }
    },
    methods: {
      get_my_ids: function () {
        let url = 'profile/kept_formations'
        this.$http.get(url).then(function (data) {
          this.my_ids = data.body.map(formation => formation.id.toString())
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
