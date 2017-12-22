<template>
  <div>
    <h1>Detailed Offer</h1>
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
    name: 'OfferExpand',
    props: {
      offer_id: {
        type: String,
        default: '1'
      }
    },
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
      get_expanded_offer: function (id) {
        let url = 'offers/' + id + '/expand/'
        this.$http.get(url).then(function (data) {
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
      this.get_expanded_offer(this.offer_id)
    }
  }
</script>
