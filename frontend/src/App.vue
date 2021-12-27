<template>
  <div id="app">
    <v-app>
      <v-main>
        <SystemBar :apiUrl="this.DBApi.params.proto + '://' + this.DBApi.params.host + ':' + this.DBApi.params.port + '/' + this.DBApi.params.baseDir"/>
        <!--<Login />-->
        <TelephoneView :table_headers="DBData.headers" :table_persons="DBData.persons"/>
      </v-main>
    </v-app>
  </div>
</template>

<script>
//import Login from './components/Login.vue'\

import axios from 'axios'
import SystemBar from './components/SystemBar.vue'
import TelephoneView from './components/TelephoneView.vue'

export default {
  name: 'App',
  components: {
    //Login,
    SystemBar,
    TelephoneView
  },
  data() {
    return {
      DBApi: {        
        params: {
          proto: "http",
          host: "localhost",
          port: "8000",
          baseDir: "bd/api/"
        }
      },
      DBData: {
        headers: [
          {
            text: 'ID',
            align: 'start',
            sortable: true,
            value: 'id',
          },
          { text: 'Фамилия', value: 'lastname' },
          { text: 'Имя', value: 'firstname' },
          { text: 'Отчество', value: 'surname' },
          { text: 'Телефон', value: 'telephone' },
          { text: 'Электропочта', value: 'email' },
          { text: 'Адрес', value: 'address' }
        ],
        persons: [
          
        ],
      }
    }
  },

  methods: {
    fetchAll() {
      axios
        .get(this.DBApi.params.proto + "://" + this.DBApi.params.host + ":" + this.DBApi.params.port + "/" + this.DBApi.params.baseDir +
        "query")
        .then((response) => {
          this.DBData.persons = response.data
          console.log(this.DBData.persons)
        })
        .catch((error) => {
          console.log(error)
        })
    }    
  },

  mounted() {
    this.fetchAll()
  }
}
</script>

<style>
/*#app {
  background: #eee;
}*/
</style>
