<template>
  <div id="id-books">
    <div id="id-thumb-wrapper">
      <div class="thumb"
        v-for="item in books" :key="item.id"
        v-if="item.img"
      >
        <img class="bks shadow" :src="item.img.url" :alt="item.abbr"
          :width="computeWidthOrHeight(item.img.width)"
          :height="computeWidthOrHeight(item.img.height)"
        >
        <a class="ellipsis" :href="'#/books/'+item.abbr">
          {{ item.title }}
        </a>
      </div>
		</div>
  </div>
</template>

<script>
export default {
  name: 'Books',
  components: {},
  data () {
    return {
      proportion: 0.25,
      books: []
    }
  },
  mounted () {
    this.loadBooks()
  },
  methods: {
    loadBooks () {
      // api[GET]: /api/books
      // 从后端获得所有图书信息
      let _this = this
      _this.$axios.get('/books').then(resp => {
        console.log('books response:', resp)
        if (resp && resp.status === 200) {
          _this.books = resp.data
          this.adjustCovers()
          // this.filterBooks()
          console.log('books:', _this.books)
        }
      })
    },
    adjustCovers () {
      // 调整封面图片大小
      let _this = this
      _this.books.forEach(book => {
        // 图片对象[套路]
        let img = new Image()
        img.src = _this.getCoverUrl(book.abbr)
        img.onload = function () {
          let imgInfo = {}
          _this.$set(imgInfo, 'url', img.src)
          _this.$set(imgInfo, 'width', img.width)
          _this.$set(imgInfo, 'height', img.height)
          _this.$set(book, 'img', imgInfo)
        }
      })
    },
    filterBooks () {
      this.books = this.books.filter(book => {
        return typeof book.img !== undefined
      })
    },
    getCoverUrl (abbr) {
      const baseUrl = "http://localhost:8088/api/file"
      return `${baseUrl}/${abbr}/${abbr}00.jpg`
    },
    computeWidthOrHeight (ele) {
      return ele * this.proportion + 'px'
    }
  }
}
</script>

<style scoped>
#id-books {
  position: relative;
  padding-top: 90px;
}

/* book thumb */
#id-thumb-wrapper {
  position: relative;
  overflow: hidden;
  padding: 45px 60px 45px 60px;
}

div.thumb {
  position: relative;
  cursor: pointer;
  float: left;
  overflow: hidden;
  width: 240px;
  height: 270px;
}

.bks {
  position: absolute !important;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.shadow {
  position: relative;
  box-shadow: 12px 12px 0 #C0C0C0 !important;
}

div.thumb a {
  font-family: 'Noto Sans TC', sans-serif;
  font-weight: 700;
  z-index: 998;
  color: #000000;
  font-size: 12px;

  display: none;
  position: absolute;
  /* float: left; */
  width: 100%;

  text-decoration: none;
  text-align: center;

  bottom: 12px;
  height: 18px;
  overflow: hidden;
}

.ellipsis {
  white-space: nowrap;
  overflow: hidden;
}
</style>
