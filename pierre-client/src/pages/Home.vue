<template>
  <div class="container">
    <Navbar :title="title"></Navbar>
    <button class="btn btn-success" v-on:click.prevent="swipe()">Start & swipe the best offers!</button>
    <br>
    <router-link to="/profile/my_offers" class="btn btn-info my-offers">My Offers</router-link>
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
        title: 'Home'
      }
    },
    methods: {
      swipe: function () {
        this.$router.push({ name: 'Swipe' })
      }
    }
  }
</script>

<style scoped>
.my-offers{
  position: relative;
  top: 30px;
}
</style>
