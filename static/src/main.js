import Vue from 'vue'
import VueX from 'vuex'
import routes from './config/PageRoutes'
window.axios = require('axios');
window.moment = require('moment');
window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

// plugins
import VueRouter from 'vue-router'
import VueBootstrap from 'bootstrap-vue'
import VueInsProgressBar from 'vue-ins-progress-bar'
import Vueditor from '@agametov/vueditor'
import VueHljs from 'vue-hljs'
import VueSweetalert2 from 'vue-sweetalert2'
import VueNotification from 'vue-notification'
import VuePanel from './plugins/panel/'
import VueSelect from 'vue-select'
import VueInputTag from 'vue-input-tag'
import VueGoodTable from 'vue-good-table';
import VeeValidate, {Validator} from 'vee-validate';
import Loading from 'vue-loading-overlay';
import es from 'vee-validate/dist/locale/es';

// plugins css
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'vue-hljs/dist/vue-hljs.min.css'
import '@agametov/vueditor/dist/style/vueditor.min.css'
import 'simple-line-icons/css/simple-line-icons.css'
import 'flag-icon-css/css/flag-icon.min.css'
import 'bootstrap-social/bootstrap-social.css'
import 'ionicons/dist/css/ionicons.min.css'
import 'vue-good-table/dist/vue-good-table.css'

// color admin css
import './assets/css/apple/style.min.css'
import './assets/css/apple/style-responsive.min.css'
import './assets/css/apple/theme/default.css'
import './assets/css/style.css'

import App from './App.vue'

Vue.config.productionTip = false

Vue.use(VueX)
Vue.use(VueRouter)
Vue.use(VeeValidate);
Vue.use(Loading, {
    color: 'red',
    loader: 'bars',
    width: 64,
    height: 64,
    backgroundColor: 'black',
    opacity: 0.5,
});
Vue.use(VueBootstrap)
Vue.use(Vueditor)
Vue.use(VueHljs)
Vue.use(VueSweetalert2)
Vue.use(VueNotification)
Vue.use(VuePanel)
Vue.use(VueGoodTable)
Vue.use(VueInsProgressBar, {
  position: 'fixed',
  show: true,
  height: '3px'
})
Vue.component('v-select', VueSelect);
Vue.component('input-tag', VueInputTag);

let token = document.getElementById("csrf-token").content;

if (token) {
    window.axios.defaults.headers.common['X-CSRFToken'] = token;
}

Validator.localize('es', es);

const router = new VueRouter({
  mode: 'history',
	routes
})

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
