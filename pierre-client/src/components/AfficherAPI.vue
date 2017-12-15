<template>
    <div>
      <h1>AfficherAPI</h1>
      <button v-on:click.prevent="get(1)">Montrez-moi une offre</button>
      <div v-if="submitted">
          <p>Title: {{title}}</p>
          <p>Offer: {{offer}}</p>
          <button v-on:click.prevent="more_details">See more details</button>
          <div v-if="see_more_detail">Detail: {{details}}</div>
          <button v-on:click.prevent="get(2)">Accept</button>

          <button v-on:click.prevent="get(3)">Refuse</button>
      </div>
    </div>

</template>

<script>
    export default {
      name: 'AfficherAPI',
      data () {
        return {
          title: '',
          offer: '',
          id: '',
          offerslist: [],
          submitted: false,
          see_more_detail: false,
          details : ''
        }
    },
      methods: {
          get: function (i) {
              var link = "https://jsonplaceholder.typicode.com/comments/"
              link = link + i
              this.$http.get(link).then(function(data){
                  console.log(data)
                  this.submitted=true
                  this.title = data.body.name
                  this.offer = data.body.email
                  this.id = data.body.id
                  this.details = data.body.body
              })
            },  
          more_details: function(){
              this.see_more_detail = true  

          }   

          }
      } 

    </script>