<template>
    <div>
      <h1>Offer</h1>
      <p>Title: {{ title }}</p>
      <p>Company: {{ company }}</p>
      <p>Language: {{ language }}</p>
      <p>Location: {{ location }}</p>
      <p>Degree: {{ degree }}</p>
      <p>Minimum Salary: {{ min_salary }}</p>
      <p>Maximum Salary: {{ max_salary }}</p>
      <p>Contract Type: {{ contract_type }}</p>
    </div>
</template>

<script>
    export default {
      name: 'Offer',
      data () {
        return {
          title: '',
          company: '',
          language: '',
          location: '',
          degree: '',
          min_salary: 0,
          max_salary: 0,
          contract_type: ''
        }
      },
      methods: {
        get_offer: function (i) {
          let link = 'offers/'
          link += i
          this.$http.get(link).then(function (data) {
            console.log(data)
            this.title = data.body.title
            this.company = data.body.company
            this.language = data.body.language
            this.location = data.body.location
            this.degree = data.body.degree
            this.contract_type = data.body.contract_type
          })
        }
      },
      created: function () {
        this.get_offer('1')
      }
    }
</script>
