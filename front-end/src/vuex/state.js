// import EN from '@/assets/language/en.js' //英语
// import ZH_CN from '@/assets/language/zh_cn.js' //简体中文

// function setLanguage() {
// 	let language = localStorage.getItem('language') || 'ZH_CN'
// 	var langObj = {
// 		'EN': EN,
// 		'ZH_CN': ZH_CN,
// 	}
// 	return langObj[language]
// }

const user = window.localStorage.getItem('user' || '[]')
const state = {
  user: {
    username: user == null ? '' : JSON.parse(user).username
  },
  adminMenus: []
	// navList: [],
	// setLanguage: setLanguage,
	// langObj: setLanguage(),
}
export default state;