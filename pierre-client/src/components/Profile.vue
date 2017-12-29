<template>
  <div>
    <h1>Profile</h1>
    <form>
      <p>
        Location :
        <input v-model="location">
        <!-- TODO: Ajouter de la validation-->
      <p>
        Interests :
        <select v-model="interests" multiple>
          <option v-for="interest in available.interests">{{ interest }}</option>
        </select>
      </p>
      <p>
        Degrees :
        <select v-model="degrees" multiple>
          <option v-for="degree in available.degrees">{{ degree }}</option>
        </select>
      </p>
      <p>
        Skills :
        <select v-model="skills" multiple>
          <option v-for="skill in available.skills">{{ skill }}</option>
        </select>
      </p>
      <p>
        Languages :
        <select v-model="languages" multiple>
          <option v-for="language in available.languages">{{ language }}</option>
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
          <option v-for="contract in available.contracts">{{ contract }}</option>
        </select>
      </p>
      <button v-on:click.prevent="save_profile()">Save</button>
    </form>
  </div>
</template>

<script>
  export default {
    name: 'profile',
    data () {
      return {
        // TODO: Charger available en fonction de ce qu'il y a dans la BDD (faire une route)
        available: {
          interests: ['informatique', 'électronique', 'mathématiques'],
          degrees: ['CAP', 'Bac', 'Bac+2', 'Bac+3', 'Bac+4', 'Bac+5'],
          skills: ['back-end', 'front-end', 'devops', 'data science'],
          languages: ['Français', 'Anglais'],
          contracts: ['CDI', 'CDD', 'Stage']
        },
        location: '',
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
      get_profile: function () {
        let url = 'profile/'
        this.$http.get(url).then(function (data) {
          console.log(data)
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
      this.get_profile()
    }
  }
</script>

<style scoped>

</style>
