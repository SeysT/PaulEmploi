<template>
  <div class="container">
    <Navbar :title="title"></Navbar>
    <div class="msg">{{ msg }}</div>
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
        password: '',
        msg: '',
        redirected: false
      }
    },
    methods: {
      set_msg: function () {
        if (this.$route.params.errors === 401) {
          this.redirected = true
          this.msg = 'You have to login to see this page.'
        }
      },
      login: function () {
        let url = 'auth/get-token/'
        let body = {
          username: this.$data.username,
          password: this.$data.password
        }
        this.$http.post(url, body).then(function (resp) {
          this.$cookies.set('token', resp.body.token)
          if (this.redirected) {
            this.$router.go(-1)
          } else {
            this.$router.push({ name: 'Swipe' })
          }
        })
      }
    },
    created: function () {
      this.set_msg()
    }
  }
</script>

<style scoped>
.msg {
  color: red;
}
</style>
