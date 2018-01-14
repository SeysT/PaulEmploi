<template>
  <div>
    <nav class="navbar navbar-default">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target='#myNavbar'>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/"><strong>Paul Emploi</strong></a>
        </div>
        <div class="collapse navbar-collapse" id="myNavbar">
          <div class="navbar-text"><strong>{{ title }}</strong></div>
          <ul class="nav navbar-nav navbar-right">
            <li><router-link to="/profile/my_offers">My Offers</router-link></li>
            <li><router-link to="/profile/my_formations">My Formations</router-link></li>
            <li><router-link to="/profile">Profile</router-link></li>
            <li class="navbar-btn btn btn-danger" v-on:click.prevent="logout()">Logout</li>
          </ul>
        </div>
      </div>
    </nav>
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
      logout: function () {
        let url = 'auth/logout'
        this.$http.get(url).then(function () {
          this.$cookies.remove('token')
          this.$router.push({ name: 'Home', params: { msg: 'You have been successfully logged out.' } })
        })
      }
    }
  }
</script>

<style scoped>

</style>
