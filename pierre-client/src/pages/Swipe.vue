<template>
  <div class="wrap">
    <Navbar :title="title"></Navbar>
    <div v-show="active = offers_ids[0]" 
         v-touch:swipeleft="dislike"
         v-touch:swiperight="like"
         class="cards">
      <Card v-for="id in offers_ids" 
          :offer_id="id" 
          :key="id"
          class="cards_item"
          :class="{
            'cards_item--active': active == id,
          }"
          v-touch:swipeleft="dislike" >
      </Card>  
    </div>
    <div class="actions"> 
      <button class="button dislike" v-on:click.prevent="dislike"></button>
      <button class="button like" v-on:click.prevent="like"></button>
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
        offers_ids: ['1', '2', '3']
      }
    },
    methods: {
      get_offers_ids: function () {
        let url = 'profile/offers_to_show/'
        this.$http.get(url).then(function (data) {
          this.offers_ids = data.body.map(offer => offer.id.toString())
        })
      },
      like: function () {
        let url = 'offers/' + this.offers_ids[0] + '/accept/'
        this.$http.post(url).then(function (data) {
          console.log(data)
        })
        this.offers_ids.shift()
      },
      dislike: function () {
        let url = 'offers/' + this.offers_ids[0] + '/refuse/'
        this.$http.post(url).then(function (data) {
          console.log(data)
        })
        this.offers_ids.shift()
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
  max-width: 320px;
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
