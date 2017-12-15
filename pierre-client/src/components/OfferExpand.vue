<template>
  <div>
    <router-link to="/offer">Retour</router-link>
    <h1>Detailled Offer</h1>
    <p>Company Description: {{ company_description }}</p>
    <p>Company Website: {{ website }}</p>
    <p>Skill: {{ skill }}</p>
    <p>Offer Description: {{ offer_description }}</p>
    <p>Weekly Work Time: {{ weekly_work_time }}</p>
    <p>Experience Name: {{ experience_name }}</p>
  </div>
</template>

<script>
  export default {
    name: 'Offer',
    data () {
      return {
        company_description: '',
        website: '',
        skill: '',
        offer_description: '',
        weekly_work_time: 0,
        experience_name: 0
      }
    },
    methods: {
      get_detailed_offer: function (i) {
        let link = 'offers/' + i + '/expand'
        this.$http.get(link).then(function (data) {
          console.log(data)
          this.company_description = data.body.company.description
          this.website = data.body.company.url
          this.skill = data.body.skill
          this.offer_description = data.body.description
          this.weekly_work_time = data.body.weekly_work_time
          this.experience_name = data.body.experience_name
        })
      }
    },
    created: function () {
      this.get_detailed_offer('1')
    }
  }
</script>
