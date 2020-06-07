<template>
  <div id="id-book-display">
    <div class="prev-next">
      <a class="prev-book">上一本</a>
      <a></a>
      <a class="next-book">下一本</a>
    </div>
    <div id="id-book-content">
      <!-- <div id="id-book-slideshow" class="pointer"> -->
      <el-carousel id="id-book-slideshow" class="pointer" 
        :interval="3000" 
        indicator-position="none"
        arrow="never"
      >
        <el-carousel-item v-for="item in pages" :key="item.id">
          <img :src="item.img" alt="">
        </el-carousel-item>
      </el-carousel>
      <!-- </div> -->
      <div id="id-book-description">
        <div class='brief'>
          <div class='brief-wrapper'>
            <div class='book-name'>
              <p>{{ item.name }}</p>
            </div>
            <div class='extend'>
              <a href='#'>展开介绍</a>
            </div>
          </div>
        </div>
        <div class="detail">
          <div class="book-info">
            <p>
              {{ item.author }}
              <br>
              {{ item.publish_date }}出版
              <br>
              {{ item.binding_style }} {{ item.size }} cm
              <br>
              {{ item.num_of_pages }}页 {{ item.num_of_bw_images }}张黑白图片，{{ item.num_of_color_images }}张彩色图片
              <br>
              ISBN {{ item.ISBN }}
              <br>
              {{ item.price }}元
            </p>
          </div>
          <div class="abstract">
            <p>{{ item.abstract }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import BookDisplay from './BookDisplay.vue'

export default {
  name: 'BookDisplay',
  components: {},
  props: {
    item: Object,
  },
  data () {
    return {
      pages: [],
    }
  },
  watch: {
    item: function () {
      console.log("当前图书:", this.item)
    }
  },
  mounted () {
  },
  methods: {
  }
}
</script>

<style scoped>
#id-book-display {
  padding: 67.5px 60px 0 180px;
	display: block;
}

div.prev-next {
    position: relative;
    float: right;
    margin-right: 20px;
    height: 22.5px;
}

.prev-next a:link {
    color:#807f80;
    text-decoration:none;
}
.prev-next a:visited {
    color:#807f80;
    text-decoration:none;
}
.prev-next a:hover {
    cursor: pointer;
    color:white;
}

.prev-next a {
    position: relative;
    font-family:"source-han-sans-simplified-c","Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    font-size: 11px;
    letter-spacing:2px
}


#id-book-slideshow {
    position: relative;
    /*padding-top: 67.5px;*/
    overflow: hidden;
    width: 840px;
    height: 540px;
}

#id-book-slideshow img {
    position: absolute;  /* 这里改成relative会造成fadeOut()执行后页面跳动问题 */
    top: 0;
    left: 0;
    width: 100%;
    display: none;
}

#id-book-slideshow img:first-child {
    display: block;
}

/* book brief info */
.brief {
    position: relative;
    overflow: hidden;
    width: 840px;
    /*height: 67.5px;*/
    padding-bottom: 22.5px;
}

.brief-wrapper {
    position: relative;
    padding-top: 6.25px;
    overflow: hidden;
}

.author {
    position: relative;
    width: 290px;
    float: left;
}

div.author p {
    font-family: "FangSong", sans-serif;
    font-size: 12px;
    line-height: 22.5px;
    letter-spacing:2px;
}

.book-name {
    position: relative;
    width: 430px;
    float: left;
    padding-left: 290px;
}

div.book-name p {
    font-family: "Noto Sans TC", sans-serif;
    font-weight: 700;
    font-size: 12px;
    line-height: 22.5px;
}

.extend {
    position: relative;
    float: right;
    width: 60px;
}

div.extend a {
    float: right;

    font-family: "Noto Sans TC", sans-serif;
    font-size: 12px;
    text-decoration: none;
    color: #000000;
}

/* book details */
.detail {
    position: relative;
    display: none;

    width: 840px;
    height: auto;
    overflow: hidden;
}

.book-info {
    position: relative;
    width: 290px;
    float: left;
}

div.book-info p {
    font-family: "FangSong", sans-serif;
    font-size: 12px;
    line-height: 22.5px
}

.abstract {
    position: relative;
    width: 550px;
    float: left;
}

div.abstract p {
    font-family: "SimSun", sans-serif;
    font-size: 12px;
    line-height: 22.5px
}
</style>
