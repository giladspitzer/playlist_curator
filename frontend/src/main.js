import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/fontawesome'
import './plugins/bootstrap-vue'
import App from './App.vue'
import router from './router'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

Vue.config.productionTip = false
Vue.config.devtools = true
library.add(faUserSecret)
Vue.component('font-awesome-icon', FontAwesomeIcon)
new Vue({
  devtools: true,
  router,
  render: h => h(App),
}).$mount('#app')
