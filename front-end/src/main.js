// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import '@/assets/js/global.js'
import router from './router'
import store from './vuex'

router.beforeEach((to, from, next) => {
  if (store.state.user.username && to.path.startsWith('/admin')) {
    console.log(store.state.user)
    initAdminMenu(router, store)
  }
  // if already login, accessing login page is redirected to backend page
  if  (store.state.user.username && to.path.startsWith('/login')) {
    next({
      path: 'admin/dashboard'
    })
  }
  // 如果前端没有登录信息则直接拦截，如果有则判断后端是否正常登录（防止构造参数绕过）
  if (to.meta.requireAuth) {
    if (store.state.user.username) {
      // 访问每个页面前都向后端发送一个请求
      // 经由拦截器验证服务器端的登录状态，防止伪造参数绕过前端的路由限制
      // axios.get('/authentication').then(resp => {
      Vue.prototype.$axios.get('/authentication').then(resp => {
        if (resp.data) {
          next()
        } else {
          // next({
          //   path: 'login',
          //   query: {redirect: to.fullPath}
          // })
        }
      })
    } else {
      next({
        path: 'login',
        query: {redirect: to.fullPath}
      })
    }
  } else {
    next()
  }
})

// 执行请求，调用格式化方法并向路由表中添加信息
const initAdminMenu = (router, store) => {
  // 如果 store 里有菜单数据，说明是正常跳转，无需重新加载
  if (store.state.adminMenus.length > 0) {
    console.log(store.state.adminMenus)
    return
  }
  // 第一次进入或进行刷新时需要重新加载
  // axios.get('/menu').then(resp => {
  Vue.prototype.$axios.get('/menu').then(resp => {
    console.log('initAdminMenu:', resp)
    if (resp && resp.status === 200) {
      var fmtRoutes = formatRoutes(resp.data)
      // var fmtRoutes = formatRoutes(resp.data.result)
      router.addRoutes(fmtRoutes)
      store.commit('initAdminMenu', fmtRoutes)
    }
  })
}

const formatRoutes = (routes) => {
  let fmtRoutes = []
  routes.forEach(route => {
    if (route.children) {
      route.children = formatRoutes(route.children)
    }

    let fmtRoute = {
      path: route.path,
      component: resolve => {
        require([`./pages/admin/${route.component}.vue`], resolve)
      },
      name: route.name,
      nameZh: route.nameZh,
      iconCls: route.iconCls,
      meta: {
        requireAuth: true
      },
      children: route.children
    }
    fmtRoutes.push(fmtRoute)
  })
  return fmtRoutes
}

/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App), // ???
  router,
  store,
  components: { App },
  template: '<App/>'
})
