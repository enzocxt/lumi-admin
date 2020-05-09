import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Home from '@/views/Home'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    }, {
      path: 'backend',
      name: 'Backend',
      redirect: '/index',
    }, {
      path: '/home',
      name: 'Home',
      component: Home,
      // home 页面并不需要被访问，只是作为其它组件的父组件
      redirect: '/index',
      children: [
        {
          path: '/index',
          name: 'AppIndex',
          component: () => import('@/views/home/AppIndex')
        }, {
          path: '/jotter',
          name: 'Jotter',
          component: () => import('@/views/jotter/Articles')
        }, {
          path: '/jotter/article',
          name: 'Article',
          component: () => import('@/views/jotter/ArticleDetails')
        }, {
          path: '/admin/content/editor',
          name: 'Editor',
          component: () => import('@/views/admin/content/ArticleEditor'),
          meta: {
            requireAuth: true
          }
        }, {
          path: '/library',
          name: 'Library',
          component: () => import('@/views/library/LibraryIndex')
        }
      ]
    }, {
      path: '/login',
      name: 'Login',
      component: () => import('@/views/Login')
    }, {
      path: '/register',
      name: 'Register',
      component: () => import('@/views/Register')
    }, {
      path: '/admin',
      name: 'Admin',
      component: () => import('@/views/admin/AdminIndex'),
      meta: {
        requireAuth: true
      },
      children: [
        {
          path: '/admin/dashboard',
          name: 'Dashboard',
          component: () => import('@/views/admin/dashboard/index'),
          meta: {
            requireAuth: true
          }
        }
      ]
    }, {
      path: '*',
      component: () => import('@/components/Error404')
    }
  ]
})

// 用于创建默认路由
export const createRouter = routes => new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    }, {
      path: '/home',
      name: 'Home',
      component: Home,
      // home 页面并不需要被访问，只是作为其它组件的父组件
      redirect: '/index',
      children: [
        {
          path: '/index',
          name: 'AppIndex',
          component: () => import('@/views/home/AppIndex')
        }, {
          path: '/jotter',
          name: 'Jotter',
          component: () => import('@/views/jotter/Articles')
        }, {
          path: '/jotter/article',
          name: 'Article',
          component: () => import('@/views/jotter/ArticleDetails')
        }, {
          path: '/admin/content/editor',
          name: 'Editor',
          component: () => import('@/views/admin/content/ArticleEditor'),
          meta: {
            requireAuth: true
          }
        }, {
          path: '/library',
          name: 'Library',
          component: () => import('@/views/library/LibraryIndex')
        }
      ]
    }, {
      path: '/login',
      name: 'Login',
      component: () => import('@/views/Login')
    }, {
      path: '/register',
      name: 'Register',
      component: () => import('@/views/Register')
    }, {
      path: '/admin',
      name: 'Admin',
      component: () => import('@/views/admin/AdminIndex'),
      meta: {
        requireAuth: true
      },
      children: [
        {
          path: '/admin/dashboard',
          name: 'Dashboard',
          component: () => import('@/views/admin/dashboard/index'),
          meta: {
            requireAuth: true
          }
        }
      ]
    }, {
      path: '*',
      component: () => import('@/components/Error404')
    }
  ]
})