<template>
  <div class="container">
    <div class="row">
      <div class="col-md-6 col-md-offset-3">
        <div class="panel panel-login">
          <div class="panel-heading">
            <div class="row">
              <div class="col-xs-12">
                <a class="active" >Recover Account</a>
              </div>
            </div>
          </div>
          <div class="panel-body">
            <div class="row">
              <div class="col-lg-12">
                <form id="login-form" method="post" role="form" style="display: block;">
                  <div class="form-group">
                    <input type="text" name="recover" id="recover" tabindex="1" class="form-control" placeholder="Email Address" 
                    v-model='mail'>
                  </div>
                  <div class="form-group">
                    <div class="row">
                      <div class="col-sm-6 col-sm-offset-3">
                        <input type="submit" name="register-submit" id="register-submit" tabindex="4" class="form-control btn btn-register" value="Recover Account" v-on:click.prevent='recover()'>
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
</template>

<script>
  export default {
    name: 'recover',
    data () {
      return {
        mail: ''
      }
    },
    methods: {
      recover: function () {
        console.log(this.$data.mail)
      }
    }
  }
</script>

<style scoped>
  
</style>