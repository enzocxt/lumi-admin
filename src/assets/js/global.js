/**
 * Global properties, variables, methods...
 **/
import Vue from 'vue'
import store from '@/vuex/index.js'
// import "@/assets/css/init.scss" // initial styles
import ElementUI from 'element-ui' // element-ui
import { Loading, Message, MessageBox, Notification } from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import 'echarts/theme/macarons.js'
// import echarts from 'echarts' // baidu echarts
// import 'echarts-gl'; //百度GL
// import world from 'echarts/map/js/world.js'; //百度echarts 相关
// import api from '@/api/api.js'; //公共的请求
import axios from '@/api/api.js'

// import EN from '@/assets/language/en.js' //英语
// import ZH_CN from '@/assets/language/zh_cn.js' //简体中文

Vue.use(ElementUI)
Vue.use(Loading.directive)
Vue.use(mavonEditor)

Vue.prototype.$loading = Loading.service
Vue.prototype.$msgbox = MessageBox
Vue.prototype.$alert = MessageBox.alert
Vue.prototype.$confirm = MessageBox.confirm
Vue.prototype.$prompt = MessageBox.prompt
Vue.prototype.$notify = Notification
Vue.prototype.$message = Message
// Vue.prototype.$echarts = echarts
Vue.prototype.getViewportSize = getViewportSize
// Vue.prototype.$api = api
Vue.prototype.$axios = axios //???
// Vue.prototype.$setRouter = setRouter
Vue.prototype.$vuex = store
// Vue.prototype.$bus = Bus()
Vue.prototype.$sysTheme = sysTheme
Vue.config.productionTip = false
// Vue.prototype.$lang = setLanguage

function Bus() {
	return new Vue()
}

/**
 * 语言国际化
 * 自定义: EN --> 表示英文
 * 自定义: ZH_CN --> 简体中文
 */
function setLanguage() {
	let language = localStorage.getItem('language') || 'ZH_CN';
	var langObj = {
		'EN': EN,
		'ZH_CN': ZH_CN,
	}
	return langObj[language];
}

/**
 * 全局三位分隔过滤器
 */
Vue.filter('dollarShape', function(value) {
	if(!value) return '0';
	var intPart = Number(value).toFixed(0) // 获取整数部分
	var intPartFormat = intPart.toString().replace(/(\d)(?=(?:\d{3})+$)/g, '$1,') // 将整数部分逢三一断
	return intPartFormat;
});

// Get window width and height
function getViewportSize() {
	return {
		width: window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth,
		height: window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight
	};
}

// System default theme
function sysTheme() {
	let obj = {};
	obj.theme_color = '#5474B7';
	obj.level2_bg_color = '#333333'; //二级菜单背景色
	obj.level2_txt_color = '#ffffff';
	let theme = localStorage.getItem('sysTheme') || null;
	if(theme) {
		try {
			theme = JSON.parse(theme);
			obj.theme_color = theme.theme_color;
			obj.level2_bg_color = theme.level2_bg_color;
		} catch(err) {}
	}
	return obj;
}