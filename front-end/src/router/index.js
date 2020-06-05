import Vue from 'vue'
import Router from 'vue-router'
import Luminocity from '@/components/Luminocity'
import Home from '@/pages/Home'

Vue.use(Router)

// export const viewURL = [
let viewURL = [
  {
    path: '/',
    name: 'Luminocity',
    component: Luminocity
  }, {
    path: 'backend',
    name: 'Backend',
    redirect: '/index'
  }, {
    path: '/home',
    name: 'Home',
    component: Home,
    // home page serves as parent component of other components
    redirect: '/index',
    meta: {
      title: 'Home',
    },
    children: [
      {
        path: '/index',
        name: 'AppIndex',
        // component: () => import('@/pages/home/AppIndex')
        component: resolve => require(['@/pages/home/AppIndex'], resolve)
      }, {
        path: '/jotter',
        name: 'Jotter',
        component: () => import('@/pages/jotter/Articles')
      }, {
        path: '/jotter/article',
        name: 'Article',
        component: () => import('@/pages/jotter/ArticleDetails')
      }, {
        path: '/admin/content/editor',
        name: 'Editor',
        component: () => import('@/pages/admin/content/ArticleEditor'),
        meta: {
          requireAuth: true
        }
      }, {
        path: '/library',
        name: 'Library',
        component: () => import('@/pages/library/LibraryIndex')
      }
    ]
  }, {
    path: '/admin',
    name: 'Admin',
    component: () => import('@/pages/admin/AdminIndex'),
    meta: {
      title: 'Admin Home',
      requireAuth: true
    },
    children: [
      {
        path: '/admin/dashboard',
        name: 'Dashboard',
        component: () => import('@/pages/admin/dashboard/index'),
        meta: {
          requireAuth: true
        }
      }
    ]
  },  {
    path: '/login',
    name: 'Login',
    component: () => import('@/pages/Login')
  }, {
    path: '/register',
    name: 'Register',
    component: () => import('@/pages/Register')
  }, {
    path: '/404',
    component: () => import('@/components/Error404')
  }, {
    path: '*',  // NOTE: put at the end
    component: () => import('@/components/Error404')
  }
]

/*
// second level routes
let childrenRouter = []
viewRUL.forEach((x) => {
  if (x.children && x.children.length) {
    childrenRouter.push(...x.children)
  } else {
    childrenRouter.push(x)
  }
})

// first level routes
let firstRouter = [
  {
    path: '/',
    component: HelloWorld,
    // redirect: '/home',
    children: childrenRouter
  }, {
    path: '/login',
    name: 'Login',
    component: () => import('@/pages/Login')
  }, {
    path: '/register',
    name: 'Register',
    component: () => import('@/pages/Register')
  }, {
    path: '/404',
    component: () => import('@/components/Error404')
  }, {
    path: '*',  // NOTE: put at the end
    component: () => import('@/components/Error404')
  }
]
*/

let router = new Router({
  mode: 'history',
  routes: viewURL
})
console.log(viewURL)
export default router

// for creating default routes
export const createRouter = routes => new Router({
  mode: 'history',
  routes: viewURL
})
