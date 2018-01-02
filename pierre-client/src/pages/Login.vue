<template>
  <div>
    <Navbar :title="title"></Navbar>
    <form>
      Username: <br>
      <input type='text' name='username' v-model='username'><br>
      Password: <br>
      <input type='password' name='password' v-model='password'><br><br>
      <input type='submit' name='submit' v-on:click.prevent='login()'>
    </form>
  </div>
</template>

<script>
  import Navbar from '../components/Navbar.vue'

  export default {
    name: 'Login',
    components: {
      Navbar
    },
    data () {
      return {
        title: 'Login',
        username: '',
        password: ''
      }
    },
    methods: {
      login: function () {
        this.$http.post(
          'http://localhost:8000/auth/get-token/',
           { username: this.$data.username, password: this.$data.password }
        ).then(function (data) {
          this.$cookies.set('token', data.body.token)
          this.$router.push({ path: '/swipe' })
        })
      }
    }
  }
</script>

<style scoped>

</style>
