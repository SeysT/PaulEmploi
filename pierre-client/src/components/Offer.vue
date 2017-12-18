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
      props: {
        offer_id: {
          type: String,
          default: '1'
        }
      },
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
        get_offer: function (id) {
          let url = 'offers/' + id
          this.$http.get(url).then(function (data) {
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
        this.get_offer(this.offer_id)
      }
    }
</script>
