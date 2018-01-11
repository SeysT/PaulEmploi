<template>
  <div>
    <div v-if="!is_formation">
      <div v-if="!isExpanded">
        <Offer :offer_id="card_id"></Offer>
        <button v-on:click.prevent="toggle()" class="button details"></button>
      </div>
      <div v-else>
        <OfferExpand :offer_id="card_id"></OfferExpand>
        <button v-on:click.prevent="toggle()" class="button back"></button>
      </div>
    </div>
    <div v-else>
      <Formation :formation_id="card_id"></Formation>
    </div>
  </div>
</template>

<script>
  import Offer from './Offer.vue'
  import OfferExpand from './OfferExpand.vue'
  import Formation from './Formation.vue'

  export default {
    name: 'Card',
    components: {
      Offer,
      OfferExpand,
      Formation
    },
    props: {
      card_id: {
        type: String,
        default: '1'
      },
      is_formation: {
        type: Boolean,
        default: false
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
      }
    }
  }
</script>

<style scoped>
.button {
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 20px 0;
  display: block;
  width: 35px;
  height: 35px;
  margin: 0 auto;

  background-color:#eff4ff;
  background-size: 100%;
  background-repeat: no-repeat;
  background-position: center;
  border: 0;
  outline: 0;
  cursor: pointer;
  /* transition: all .3s; */
}
.details {
  background-image: url(../assets/question.png);
  }
.back{
  background-image: url(../assets/back.png);
}
</style>
