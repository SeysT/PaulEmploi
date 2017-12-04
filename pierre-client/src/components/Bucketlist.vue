<template>
  <div>
    <div>Test : {{ test }}</div>
    <div>My Bucketlist : {{ my_bucketlist }}</div>
    <ul>Liste de bucketlists :
      <li v-for="bucketlist in bucketlists">{{ bucketlist.name }}</li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: 'bucket',
    data () {
      return {
        test: 'Test de bucket',
        my_bucketlist: '',
        bucketlists: []
      }
    },
    methods: {
      set_my_bucketlist: function (id) {
        this.$http.get('bucketlists/' + id).then(response => {
          this.my_bucketlist = response.body.name
        })
      },
      set_bucketlists: function () {
        this.$http.get('bucketlists/').then(response => {
          this.bucketlists = response.body
        })
      }
    },
    created: function () {
      this.set_my_bucketlist('2')
      this.set_bucketlists()
    }
  }
</script>

<style scoped>

</style>
