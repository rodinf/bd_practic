import Vue from 'vue'
import App from './App.vue'
import vuetify from '@/plugins/vuetify' // path to vuetify export
import '@mdi/font/css/materialdesignicons.css'
import VueTelInput from 'vue-tel-input';
import 'vue-tel-input/dist/vue-tel-input.css'

Vue.use(VueTelInput);

Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(App),
}).$mount('#app')
