<template>
  <div>
    <div v-if="expand">
      <button disabled>Gauche</button>
      <Offer></Offer>
      <button v-on:click.prevent="toggle()">Droite</button>
    </div>
    <div v-else>
      <button v-on:click.prevent="toggle()">Gauche</button>
      <OfferExpand></OfferExpand>
      <button disabled>Droite</button>
    </div>
  </div>
</template>

<script>
  import Offer from './Offer.vue'
  import OfferExpand from './OfferExpand.vue'

  export default {
    components: {
      Offer,
      OfferExpand
    },
    name: 'card',
    data () {
      return {
        expand: false
      }
    },
    methods: {
      toggle: function () {
        this.expand = !this.expand
      }
    }
  }
</script>

<style scoped>

</style>
