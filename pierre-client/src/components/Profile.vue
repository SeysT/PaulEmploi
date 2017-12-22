<template>
  <div>
    <h1>Profile</h1>
    <p>Location : {{ location }}</p>
    <p>Interests :</p>
    <ul>
      <li v-for="interest in interests">{{ interest }}</li>
    </ul>
    <p>Interests :</p>
    <ul>
      <li v-for="degree in degrees">{{ degree }}</li>
    </ul>
    <p>Skills :</p>
    <ul>
      <li v-for="skill in skills">{{ skill }}</li>
    </ul>
    <p>Languages :</p>
    <ul>
      <li v-for="language in languages">{{ language }}</li>
    </ul>
    <p>Minimum salary : {{ min_salary }}</p>
    <p>Maximum salary : {{ max_salary }}</p>
    <p>Contract type : {{ contract }}</p>
  </div>
</template>

<script>
  export default {
    name: 'profile',
    data () {
      return {
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
      }
    },
    created: function () {
      this.get_profile()
    }
  }
</script>

<style scoped>

</style>
