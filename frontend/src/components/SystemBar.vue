<template>
  <div class="systemBar">
    <v-system-bar height="30" light>
      <span>Клиент базы данных</span>
      <v-spacer></v-spacer>
      <span>{{apiUrl}}</span>
      <!--<v-icon>{{connected ? 'mdi-check-circle-outline' : 'mdi-cancel'}}</v-icon>
      <span>{{connected ? 'подключен' : 'не подключен'}}</span>-->
    </v-system-bar>
  </div>
</template>

<script>
export default {
  name: 'SystemBar',
  props: {
    connected: Boolean,
    apiUrl: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
