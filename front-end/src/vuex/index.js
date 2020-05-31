import Vue from 'vue'
import Vuex from 'vuex'
import state from './state'
import mutations from './mutations'
// import actions from './action'
// import getters from './getters'

Vue.use(Vuex)

// const uname = window.localStorage.getItem('user' || '[]')
export default new Vuex.Store({
  state,
  // getters,
  // actions,
  mutations
})
