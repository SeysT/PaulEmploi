<template>
  <div class="container">
    <Navbar :title="title"></Navbar>
    <div class="wrap">
      <div class="cards">
        <Card v-for="card_id in cards_ids"
            :card_id="card_id"
            :key="card_id.toString()+isFormation.toString()"
            :is_formation="isFormation"
            class="cards_item"
            :class="{
              'cards_item--active': cards_ids[0] === card_id,
            }" >
        </Card>
        <div>
          <p class='msg'>
            {{ msg }}
          </p>
        </div>
        <div class="cards_item">
          <p class="background-text">No more cards to swipe!<br/><br/>But you're welcome to come back tomorrow! :)</p>
        </div>
      </div>
      <div class="actions">
        <button class="button dislike" v-on:click.prevent="action(like=true)"></button>
        <button class="button like" v-on:click.prevent="action(like=false)"></button>
      </div>
    </div>
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
        cards_ids: ['1', '2', '3'],
        isFormation: false,
        msg: ''
      }
    },
    methods: {
      get_ids: function (url) {
        this.$http.get(url).then(
          function (resp) {
            this.cards_ids += resp.body.map(card => card.id.toString())
          },
          function (resp){
            this.msg = resp.statusText
          }
        )
      },
      get_offers_ids: function () {
        let url = 'api/profile/offers_to_show/'
        this.cards_ids = []
        this.get_ids(url)
      },
      get_formations_ids: function () {
        let url = 'api/profile/formations_to_show/'
        this.get_ids(url)
      },
      action: function (like) {
        let cardId = this.cards_ids[0]
        let urlStart = this.isFormation ? 'api/formations/' : 'api/offers/'
        let urlEnd = this.isFormation
          ? like
            ? '/keep/' : '/drop/'
          : like
            ? '/accept/' : '/refuse/'
        if (this.cards_ids.length === 1 && !this.isFormation) {
          this.isFormation = true
          this.get_formations_ids()
        }
        this.$http.post(urlStart + cardId + urlEnd)
        this.cards_ids.shift()
      }
    },
    created: function () {
      this.get_offers_ids()
    }
  }
</script>

<style scoped>
.background-text {
  position: relative;
  top: 8em;
  z-index: -12;
  visibility: visible;
}
</style>
