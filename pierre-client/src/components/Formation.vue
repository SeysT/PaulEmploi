<template>
  <div>
    <h1>Formation</h1>
    <p>Name: {{ name }}</p>
    <p>Acquired skills:</p>
      <ul>
        <li v-for="skill in acquired_skills">{{ skill }}</li>
      </ul>
    <p>Acquired degree: {{ acquired_degree }}</p>
    <p>Duration: {{ duration }}</p>
    <p>Location: {{ location }}</p>
    <p>Language: {{ language }}</p>
  </div>
</template>

<script>
  export default {
    name: 'Formation',
    props: {
      formation_id: {
        type: String,
        default: '1'
      }
    },
    data () {
      return {
        name: '',
        acquired_skills: [],
        acquired_degree: '',
        duration: '',
        location: '',
        language: ''
      }
    },
    methods: {
      get_formation: function (id) {
        let url = 'api/formations/' + id + '/'
        this.$http.get(url).then(function (resp) {
          this.name = resp.body.name
          this.acquired_skills = resp.body.acquired_skills.name
          this.acquired_degree = resp.body.acquired_degree.name
          this.duration = resp.body.duration
          this.location = resp.body.location
          this.language = resp.body.language
        })
      }
    },
    created: function () {
      this.get_formation(this.formation_id)
    }
  }
</script>

<style scoped>

</style>
