<template>
  <div>
    <Navbar :title="title"></Navbar>
    <button v-on:click.prevent="my_offers()">My Offers</button>
    <form>
      <p>
        Location :
        <input v-model="location">
        <!-- TODO: Ajouter de la validation-->
      <p>
        Interests :
        <select v-model="interests" multiple>
          <option v-for="interest in available_interests">{{ interest }}</option>
        </select>
      </p>
      <p>
        Degrees :
        <select v-model="degrees" multiple>
          <option v-for="degree in available_degrees">{{ degree }}</option>
        </select>
      </p>
      <p>
        Skills :
        <select v-model="skills" multiple>
          <option v-for="skill in available_skills">{{ skill }}</option>
        </select>
      </p>
      <p>
        Languages :
        <select v-model="languages" multiple>
          <option v-for="language in available_languages">{{ language }}</option>
        </select>
      </p>
      <p>
        Minimum salary :
        <input type="number" v-model="min_salary">
      </p>
      <p>
        Maximum salary :
        <input type="number" v-model="max_salary">
      </p>
      <p>
        Contract type :
        <select v-model="contract">
          <option v-for="contract in available_contracts">{{ contract }}</option>
        </select>
      </p>
      <button v-on:click.prevent="save_profile()">Save</button>
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
        let url = 'api/fields/'
        this.$http.get(url).then(function (resp) {
          this.available_interests = resp.body.interests_names
          this.available_degrees = resp.body.degrees_names
          this.available_skills = resp.body.skills_names
          this.available_languages = resp.body.languages_names
          this.available_contracts = resp.body.contract_types_names
        })
      },
      get_profile: function () {
        let url = 'api/profile/'
        this.$http.get(url).then(function (resp) {
          this.location = resp.body.desired_location
          this.interests = resp.body.interests
          this.degrees = resp.body.degrees
          this.skills = resp.body.skills
          this.languages = resp.body.languages
          this.min_salary = resp.body.desired_min_salary
          this.max_salary = resp.body.desired_max_salary
          this.contract = resp.body.desired_contract
        })
      },
      save_profile: function () {
        let url = 'api/profile/'
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
