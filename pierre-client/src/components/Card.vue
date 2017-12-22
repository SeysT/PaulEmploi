<template>
  <div>
    <div v-if="isExpanded">
      <button disabled>Gauche</button>
      <Offer :offer_id="offer_id"></Offer>
      <button v-on:click.prevent="toggle()">Droite</button>
    </div>
    <div v-else>
      <button v-on:click.prevent="toggle()">Gauche</button>
      <OfferExpand :offer_id="offer_id"></OfferExpand>
      <button disabled>Droite</button>
    </div>
    <button v-on:click.prevent="like()">Like</button>
    <button v-on:click.prevent="dislike()">Dislike</button>
  </div>
</template>

<script>
  import Offer from './Offer.vue'
  import OfferExpand from './OfferExpand.vue'

  export default {
    name: 'card',
    components: {
      Offer,
      OfferExpand
    },
    props: {
      offer_id: {
        type: String,
        default: '1'
      }
    },
    data () {
      return {
        isExpanded: false
      }
    },
    methods: {
      toggle: function () {
        this.isExpanded = !this.isExpanded
      },
      like: function () {
        return null
      },
      dislike: function () {
        return null
      }
    }
  }
</script>

<style scoped>

</style>
