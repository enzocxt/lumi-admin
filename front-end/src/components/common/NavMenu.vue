<template>
  <el-menu
    :default-active="'currentPath'"
    router
    mode="horizontal"
    background-color="white"
    text-color="#222"
    active-text-color="red"
  >
    <!-- style="min-width: 1300px" -->
    <!-- router attribute indicates whether 'vue-router' mode is activated -->
    <!-- If true, index will be used as 'path' to activate the route action -->
    <el-menu-item v-for="(item, i) in navList" :key="i" :index="item.name">
      {{ item.navItem }}
    </el-menu-item>
    <span style="position: absolute;padding-top: 20px;right: 43%;font-size: 20px;font-weight: bold">光明城</span>
    <el-input
      placeholder="快速搜索..."
      prefix-icon="el-icon-search"
      size="medium"
      style="width: 200px;position:absolute;margin-top: 12px;right: 18%"
      v-model="keywords"
    >
    </el-input>
  </el-menu>
</template>

<script>
export default {
  name: 'NavMenu',
  data () {
    return {
      navList: [
        {name: '/index', navItem: '首页'},
        {name: '/jotter', navItem: '笔记本'},
        {name: '/library', navItem: '书目'},
        // {name: '/admin/dashboard', navItem: '管理中心'}
        {name: '/admin', navItem: '管理中心'}
      ],
      keywords: ''
    }
  },
  computed: {
    hoverBackground () {
      return '#ffd04b'
    },
    currentPath () {
      var x = this.$route.path.indexOf('/', 1)
      if (x !== -1) {
        return this.$route.path.substring(0, x)
      } else {
        return this.$route.path
      }
    }
  },
  methods: {}
}
</script>

<style scoped>
a{
  text-decoration: none;
}

span {
  pointer-events: none;
}
</style>

