<template>
  <div class="telephoneView">
    <v-container fluid>
      <div class="ma-2">
        <h3>Телефонный справочник</h3>
      </div>
      <v-data-table
        :headers="table_headers"
        :items="table_persons"
        :items-per-page="all"
        class="elevation-3"
      >
        <template v-slot:item.telephone="{ item }">
          {{item.telephone}}
        </template>
        <template v-slot:item.email="{ item }">
          <a :href="'mailto:' + item.email">{{item.email}}</a>
        </template>
      </v-data-table>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'TelephoneView',
  props: {
    table_headers: Array,
    table_persons: Array
  },
  data () {
    return {
      bd_title: 'bd_practic_telephone',
      phone: "+7(800) 5553535"
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
