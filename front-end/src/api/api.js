import axios from 'axios'
// var axios = require('axios')
// import Qs from 'qs'

// 设置反向代理，前端请求默认发送到 http://localhost:8088/api

axios.defaults.timeout = 60000 // request timeout
// 为了让前端能够带上 cookie，需要通过 axios 主动开启 withCredentails 功能
axios.defaults.withCredentials = true
// axios.defaults.baseURL = 'http://localhost:8088/api'
// Configure DEVELOP ENV and PRODUCT ENV
if (process.env.NODE_ENV == 'development') {
	axios.defaults.baseURL = 'http://localhost:8088/api'
} else if (process.env.NODE_ENV == 'production') {
	axios.defaults.baseURL = window.location.origin + '/api'
}

// http response 拦截器
// axios.interceptors.response.use(
//   response => {
//     return response
//   },
//   error => {
//     if (error) {
//       store.commit('logout')
//       router.replace('/login')
//     }
//     // 返回接口返回的错误信息
//     return Promise.reject(error)
//   }
// )

export default axios