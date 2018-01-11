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
        isFormation: false
      }
    },
    methods: {
      get_ids: function (url) {
        this.$http.get(url).then(function (resp) {
          this.cards_ids += resp.body.map(card => card.id.toString())
        })
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
.wrap{
  width: 100%;
  height: 100%;
  max-width: 520px;
  padding: 0 16px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.cards{
  position: relative;
  padding: 0;
  margin: 0;
  height: 450px;

  list-style-type: none;
}

.cards_item {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;

  height: 450px;
  overflow: auto;

  border: 2px solid #96b7ff;
  border-radius: 4px;
  background-color: #eff4ff;

  visibility: hidden;
}

.cards_item--active {
  z-index: 1;
  visibility: visible;
  transition: all .4s .1s cubic-bezier(.87,-.41,.19,1.44);
}

.actions {
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 20px 15px;
}

.button {
  display: flex;
  justify-content: space-around;
  align-items: center;
  padding: 20px 0;
  display: block;
  width: 63px;
  height: 63px;

  background-color: white;
  background-size: 100%;
  background-repeat: no-repeat;
  background-position: center;
  border: 0;
  outline: 0;
  cursor: pointer;

  transition: all .3s;
}

.like {
  background-image: url(../assets/like.png);
}

.dislike {
  background-image: url(../assets/dislike.png);
}

.background-text {
  position: relative;
  top: 8em;
  z-index: -12;
  visibility: visible;
}
</style>
