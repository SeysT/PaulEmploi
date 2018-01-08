<template>
  <div class="container">
    <Navbar :title="title"></Navbar>
    <router-link to="/profile/my_offers">My Offers</router-link>
    <form>
      <br>
      <div class="well">
        <label>Location:</label>
          <input type='text' class="form-control" placeholder="Paris" v-model="location">
          <!-- TODO: Ajouter de la validation-->
        <label>Interests:</label>
          <select class="form-control" v-model="interests" multiple>
            <option v-for="interest in available_interests">{{ interest }}</option>
          </select>
        <label>Degrees:</label>
          <select class="form-control" v-model="degrees" multiple>
            <option v-for="degree in available_degrees">{{ degree }}</option>
          </select>
        <label>Skills:</label>
          <select class="form-control" v-model="skills" multiple>
            <option v-for="skill in available_skills">{{ skill }}</option>
          </select>
        <label>Languages :</label>
          <select class="form-control" v-model="languages" multiple>
            <option v-for="language in available_languages">{{ language }}</option>
          </select>
        <label>Minimum salary (K euros):</label>
          <input class="form-control" type="number" v-model="min_salary">
        <label>Maximum salary (K euros):</label>
          <input class="form-control" type="number" v-model="max_salary">
        <label>Contract type:</label>
          <select class="form-control" v-model="contract">
            <option v-for="contract in available_contracts">{{ contract }}</option>
          </select>
          <br>
          <button name='save' class="btn btn-large btn-block btn-primary" v-on:click.prevent="save_profile()">Save</button>
      </div>
    </form>
  </div>
</template>

<script>
  import Navbar from '../components/Navbar.vue'

  export default {
    name: 'Profile',
    components: {
      Navbar
    },
    data () {
      return {
        title: 'Profile',
        available_interests: [],
        available_degrees: [],
        available_skills: [],
        available_languages: [],
        available_contracts: [],
        location: 'Paris',
        interests: [],
        degrees: [],
        skills: [],
        languages: [],
        min_salary: 0,
        max_salary: 0,
        contract: ''
      }
    },
    methods: {
      my_offers: function () {
        this.$router.push({ path: '/profile/my_offers' })
      },
      get_available: function () {
        let url = 'fields/'
        this.$http.get(url).then(function (data) {
          this.available_interests = data.body.interests_names
          this.available_degrees = data.body.degrees_names
          this.available_skills = data.body.skills_names
          this.available_languages = data.body.languages_names
          this.available_contracts = data.body.contract_types_names
        })
      },
      get_profile: function () {
        let url = 'profile/'
        this.$http.get(url).then(function (data) {
          this.location = data.body.desired_location
          this.interests = data.body.interests
          this.degrees = data.body.degrees
          this.skills = data.body.skills
          this.languages = data.body.languages
          this.min_salary = data.body.desired_min_salary
          this.max_salary = data.body.desired_max_salary
          this.contract = data.body.desired_contract
        })
      },
      save_profile: function () {
        let url = 'profile/'
        let body = {
          desired_location: this.location,
          desired_contract: this.contract,
          interests: this.interests,
          degrees: this.degrees,
          skills: this.skills,
          languages: this.languages,
          desired_min_salary: this.min_salary,
          desired_max_salary: this.max_salary
        }
        this.$http.put(url, body)
      }
    },
    created: function () {
      this.get_available()
      this.get_profile()
    }
  }
</script>

<style scoped>

</style>
