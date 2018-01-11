<template>
  <div class="container">
    <div>
      <div class="msg">{{ msg }}</div>
      <div class="container">
      <div class="row">
      <div class="col-md-6 col-md-offset-3">
        <div class="panel panel-login">
          <div class="panel-heading">
            <div class="row">
              <div class="col-xs-6">
                <a v-on:click='login_link_click()' ><router-link to="/login" class="active" id="login-form-link">Login</router-link></a>
              </div>
              <div class="col-xs-6">
                <a v-on:click='register_link_click()'><router-link to="/login"  id="register-form-link">Register</router-link></a>
              </div>
            </div>
            <hr>
          </div>
          <div class="panel-body">
            <div class="row">
              <div class="col-lg-12">
                <form id="login-form" method="post" role="form" style="display: block;">
                  <div class="form-group">
                    <input type="text" name="username" id="username" tabindex="1" class="form-control" placeholder="Username"
                    value="" v-model='username'>
                  </div>
                  <div class="form-group">
                    <input type="password" name="password" id="password" tabindex="2" class="form-control" placeholder="Password"
                    v-model='password'>
                  </div>
                  <div class="form-group text-center">
                    <input type="checkbox" tabindex="3" class="" name="remember" id="remember">
                    <label for="remember"> Remember Me</label>
                  </div>
                  <div class="form-group">
                    <div class="row">
                      <div class="col-sm-6 col-sm-offset-3">
                        <input type="submit" name="login-submit" id="login-submit" tabindex="4" class="form-control btn btn-login" value="Log In" v-on:click.prevent='login()'>
                      </div>
                    </div>
                  </div>
                  <div class="form-group">
                    <div class="row">
                      <div class="col-lg-12">
                        <div class="text-center">
                          <a tabindex="5" class="forgot-password"><router-link to="/recover">Forgot Password?</router-link></a>
                        </div>
                      </div>
                    </div>
                  </div>
                </form>
                <form id="register-form" method="post" role="form" style="display: none;">
                  <div class="form-group">
                    <input type="text" name="username" id="username" tabindex="1" class="form-control" placeholder="Username" value="">
                  </div>
                  <div class="form-group">
                    <input type="email" name="email" id="email" tabindex="1" class="form-control" placeholder="Email Address" value="">
                  </div>
                  <div class="form-group">
                    <input type="password" name="password" id="password" tabindex="2" class="form-control" placeholder="Password">
                  </div>
                  <div class="form-group">
                    <input type="password" name="confirm-password" id="confirm-password" tabindex="2" class="form-control" placeholder="Confirm Password">
                  </div>
                  <div class="form-group">
                    <div class="row">
                      <div class="col-sm-6 col-sm-offset-3">
                        <input type="submit" name="register-submit" id="register-submit" tabindex="4" class="form-control btn btn-register" value="Register Now" v-on:click.prevent='register()'>
                      </div>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
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
        },
        register: function () {
          console.log('register\'s working')
        },
        login_link_click: function (e) {
          $('#login-form').delay(100).fadeIn(100)
          $('#register-form').fadeOut(100)
          $('#register-form-link').removeClass('active')
          $('#login-form-link').addClass('active')
          e.preventDefault()
        },
        register_link_click: function (e) {
          $('#register-form').delay(100).fadeIn(100)
          $('#login-form').fadeOut(100)
          $('#login-form-link').removeClass('active')
          $('#register-form-link').addClass('active')
          e.preventDefault()
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
