<template>
  <div id="id-familiar">
  </div>
</template>

<script>
export default {
  name: 'Books',
  components: {},
  data () {
    return {
      books: []
    }
  },
  mounted () {
    this.getBooks()
  },
  methods: {
    getBooks () {
      // api[GET]: /api/books
      // 从后端获得所有图书信息
      let _this = this
      _this.$axios.get('/books').then(resp => {
        console.log('books response:', resp)
        if (resp && resp.status === 200) {
          _this.books = resp.data
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
