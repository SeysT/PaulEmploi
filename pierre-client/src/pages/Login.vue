<template>
  <div>
    <Navbar :title="title"></Navbar>
    <div class="msg">{{ msg }}</div>
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
