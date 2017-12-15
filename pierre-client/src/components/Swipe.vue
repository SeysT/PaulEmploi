<template>
  <div>
    <Card></Card>
    <button v-on:click.prevent="like()">Like</button>
    <button v-on:click.prevent="dislike()">Dislike</button>
  </div>
</template>

<script>
  import Card from './Card.vue'

  export default {
    name: 'swipe',
    components: {
      Card
    },
    methods: {
      like: function () {
        return null
      },
      dislike: function () {
        return null
      }
    }
  }
</script>

<style scoped>

</style>
