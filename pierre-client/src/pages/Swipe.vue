<template>
  <div class="container">
    <Navbar :title="title"></Navbar>
    <div class="wrap">
      <div v-show="active = offers_ids[0]"
          class="cards">
        <Card v-for="card in cards"
            :card_id="card.id"
            :key="card.id.toString()+card.isFormation.toString()"
            :is_formation="card.isFormation"
            class="cards_item"
            :class="{
              'cards_item--active': offers_ids[0] == id,
            }" >
        </Card>
      </div>
      <div class="actions">
        <button class="button dislike" v-on:click.prevent="dislike()"></button>
        <button class="button like" v-on:click.prevent="like()"></button>
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
        cards: [
          {
            id: '1',
            isFormation: false
          },
          {
            id: '2',
            isFormation: false
          },
          {
            id: '3',
            isFormation: true
          }
        ]
      }
    },
    methods: {
      get_cards_ids: function () {
        let url = 'profile/cards_to_show/'
        this.$http.get(url).then(function (resp) {
          this.cards = resp.body.map(function (card) {
            return {
              id: card.id.toString(),
              isFormation: card.isFormation
            }
          })
        })
      },
      like: function () {
        let card = this.cards[0]
        let url = ''
        if (card.isFormation) {
          url = 'api/formations/' + card.id + '/keep/'
        } else {
          url = 'api/offers/' + card.id + '/accept/'
        }
        this.$http.post(url)
        this.cards.shift()
      },
      dislike: function () {
        let card = this.cards[0]
        let url = ''
        if (card.isFormation) {
          url = 'api/formations/' + card.id + '/drop/'
        } else {
          url = 'api/offers/' + card.id + '/refuse/'
        }
        this.$http.post(url)
        this.cards.shift()
      }
    },
    created: function () {
      this.get_cards_ids()
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

.actions{
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
.dislike{
  background-image: url(../assets/dislike.png);
  }


</style>
