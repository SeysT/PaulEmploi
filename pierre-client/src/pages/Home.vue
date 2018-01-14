<template>
  <div class="container">
    <Navbar :title="title"></Navbar>
    <div class="msg">{{ msg }}</div>
    <button class="btn btn-success" v-on:click.prevent="swipe()">Start & swipe the best offers!</button>
    <br>
    <router-link to="/profile/my_offers" class="btn btn-info my-offers">My Offers</router-link>
    <br>
    <br>
    <router-link to="/profile/my_formations" class="btn btn-info my-offers">My Formations</router-link>
  </div>
</template>

<script>
  import Navbar from '../components/Navbar.vue'

  export default {
    name: 'Home',
    components: {
      Navbar
    },
    data () {
      return {
        title: 'Home',
        msg: ''
      }
    },
    methods: {
      swipe: function () {
        this.$router.push({ name: 'Swipe' })
      },
      set_msg: function () {
        if (this.$route.params.msg !== null) {
          this.msg = this.$route.params.msg
        }
      }
    },
    created: function () {
      this.set_msg()
    }
  }
</script>

<style scoped>
.my-offers {
  position: relative;
  top: 30px;
}
.msg {
  color: green;
  margin-bottom: 1em;
}
</style>
