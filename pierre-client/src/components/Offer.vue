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
    data() {
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
        let url = 'api/offers/' + id + '/'
        this.$http.get(url).then(function (resp) {
          this.title = resp.body.title
          this.company = resp.body.company
          this.language = resp.body.language
          this.location = resp.body.location
          this.degree = resp.body.degree
          this.contract_type = resp.body.contract_type
        })
      }
    },
    created: function () {
      this.get_offer(this.offer_id)
    }
  }
</script>
