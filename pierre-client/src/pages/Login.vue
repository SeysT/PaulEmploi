<template>
  <div class="container">
    <Navbar :title="title"></Navbar>
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
  .panel-login {
  border-color: #ccc;
  -webkit-box-shadow: 0px 2px 3px 0px rgba(0,0,0,0.2);
  -moz-box-shadow: 0px 2px 3px 0px rgba(0,0,0,0.2);
  box-shadow: 0px 2px 3px 0px rgba(0,0,0,0.2);
}
.panel-login>.panel-heading {
  color: #00415d;
  background-color: #fff;
  border-color: #fff;
  text-align:center;
}
.panel-login>.panel-heading a{
  text-decoration: none;
  color: #666;
  font-weight: bold;
  font-size: 15px;
  -webkit-transition: all 0.1s linear;
  -moz-transition: all 0.1s linear;
  transition: all 0.1s linear;
}
.panel-login>.panel-heading a.active{
  color: #029f5b;
  font-size: 18px;
}
.panel-login>.panel-heading hr{
  margin-top: 10px;
  margin-bottom: 0px;
  clear: both;
  border: 0;
  height: 1px;
  background-image: -webkit-linear-gradient(left,rgba(0, 0, 0, 0),rgba(0, 0, 0, 0.15),rgba(0, 0, 0, 0));
  background-image: -moz-linear-gradient(left,rgba(0,0,0,0),rgba(0,0,0,0.15),rgba(0,0,0,0));
  background-image: -ms-linear-gradient(left,rgba(0,0,0,0),rgba(0,0,0,0.15),rgba(0,0,0,0));
  background-image: -o-linear-gradient(left,rgba(0,0,0,0),rgba(0,0,0,0.15),rgba(0,0,0,0));
}
.panel-login input[type="text"],.panel-login input[type="email"],.panel-login input[type="password"] {
  height: 45px;
  border: 1px solid #ddd;
  font-size: 16px;
  -webkit-transition: all 0.1s linear;
  -moz-transition: all 0.1s linear;
  transition: all 0.1s linear;
}
.panel-login input:hover,
.panel-login input:focus {
  outline:none;
  -webkit-box-shadow: none;
  -moz-box-shadow: none;
  box-shadow: none;
  border-color: #ccc;
}
.btn-login {
  background-color: #59B2E0;
  outline: none;
  color: #fff;
  font-size: 14px;
  height: auto;
  font-weight: normal;
  padding: 14px 0;
  text-transform: uppercase;
  border-color: #59B2E6;
}
.btn-login:hover,
.btn-login:focus {
  color: #fff;
  background-color: #53A3CD;
  border-color: #53A3CD;
}
.forgot-password {
  text-decoration: underline;
  color: #888;
}
.forgot-password:hover,
.forgot-password:focus {
  text-decoration: underline;
  color: #666;
}

.btn-register {
  background-color: #1CB94E;
  outline: none;
  color: #fff;
  font-size: 14px;
  height: auto;
  font-weight: normal;
  padding: 14px 0;
  text-transform: uppercase;
  border-color: #1CB94A;
}
.btn-register:hover,
.btn-register:focus {
  color: #fff;
  background-color: #1CA347;
  border-color: #1CA347;
}
</style>
