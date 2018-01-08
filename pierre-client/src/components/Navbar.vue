<template>
  <div>
    <button v-on:click.prevent="home()">Home</button>
    <h1>{{ title }}</h1>
    <button v-on:click.prevent="profile()">Profile</button>
  </div>
</template>

<script>
  export default {
    name: 'Navbar',
    props: {
      title: {
        type: String,
        default: ''
      }
    },
    methods: {
      home: function () {
        this.$router.push({ name: 'Home' })
      },
      profile: function () {
        this.$router.push({ name: 'Profile' })
      }
    }
  }
</script>

<style scoped>

</style>
