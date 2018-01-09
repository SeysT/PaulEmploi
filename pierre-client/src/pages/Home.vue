<template>
  <div class="container">
    <Navbar :title="title"></Navbar>
    <button class="btn btn-primary" v-on:click.prevent="swipe()">Start & swipe the best offers!</button>
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

</style>
