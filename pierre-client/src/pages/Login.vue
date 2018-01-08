<template>
  <div class="container">
    <Navbar :title="title"></Navbar>
    <form>
      <div class="well">
        <label>Username:</label>
        <input type='text' class="form-control" placeholder="Username" name='username' v-model='username'>
        <label>Password:</label>
        <input type='password' class="form-control" placeholder="Password" name='password' v-model='password'><br>
        <button type='submit' name='submit' class="btn btn-large btn-block btn-primary" v-on:click.prevent='login()'>Log In</button>
      </div>
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
