<template>
  <el-container>
    <el-aside style="width: 200px;margin-top: 20px">
      <switch></switch>
      <SideMenu @indexSelect="listByCategory" ref="sideMenu"></SideMenu>
    </el-aside>
    <el-main>
      <books class="books-area" ref="booksArea"></books>
    </el-main>
  </el-container>
</template>

<script>
import SideMenu from './SideMenu'
import Books from './Books'

export default {
  name: 'AppLibrary',
  components: {
    SideMenu,
    Books
  },
  methods: {
    listByCategory () {
      // api[GET]: /api/category/<cid>/book
      // 子组件 SideMenu 触发（$emit）indexSelect 事件执行 listByCategory()
      // 通过 this.$refs.sideMenu.cid 获取子组件的 data
      var _this = this
      var cid = this.$refs.sideMenu.cid
      // 与后端 URL 的构造方式对应（"/api/category/{cid}/books"）
      var url = `category/${cid}/books`
      this.$axios.get(url).then(resp => {
        if (resp && resp.status === 200) {
          _this.$refs.booksArea.books = resp.data
        }
      })
    }
  }
}
</script>

<style scoped>
.books-area {
  width: 900px;
  margin-left: auto;
  margin-right: auto;
}
</style>