import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/views/Index'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(Router)

axios.defaults.headers.post['Content-type'] = 'application/json'
// axios.defaults.baseURL = '/'
Vue.use(VueAxios, axios);

export default new Router({
  mode: 'hash',
  base: '/',
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    }
  ]
})
