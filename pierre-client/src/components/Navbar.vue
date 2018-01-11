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
            <a class="navbar-brand" href="home">Paul Emploi</a>
          </div>
          <div class="collapse navbar-collapse" id="myNavbar">
            <ul class="nav navbar-nav">
              <li><router-link to="/">Home</router-link></li>
              <li><router-link to="profile">Profile</router-link></li>
            </ul>
          </div>
        </div>
    </nav>      
    <!-- <router-link to="/">Home</router-link> -->
    <!-- <router-link to="profile">Profile</router-link> -->
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
    }
  }
</script>

<style scoped>

</style>
