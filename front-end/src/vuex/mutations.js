// import { NAVLIST } from './mutation-types.js'
// import { SWITCH_LANGUAGE } from './mutation-types.js'


export default {
  // [NAVLIST](state, res) {
	// 	state.navList = res;
	// },
	// [SWITCH_LANGUAGE](state, res) {
	// 	state.langObj = state.setLanguage();
	// },
  login (state, user) {
    state.user = user
    window.localStorage.setItem('user', JSON.stringify(user))
  },
  logout (state) {
    state.user = []
    window.localStorage.removeItem('user')
  },
  initAdminMenu (state, menus) {
    state.adminMenus = menus
  }
}