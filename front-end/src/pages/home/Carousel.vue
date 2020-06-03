<template>
  <el-card class="card-carousel">
    <el-carousel  class="push" :interval="4000" arrow="always">
      <el-carousel-item v-for="item in items" :key="item.id">
        <a :href=item.link target="_blank">
          <img :src=item.img alt="" class="carousel_img">
        </a>
        <h3>{{ item.title }}</h3>
      </el-carousel-item>
    </el-carousel>
  </el-card>
</template>

<script>
export default {
  name: 'Carousel',
  data: function () {
    return {
      items: [
        {
          id: 1,
          title: '光明城豆瓣小站',
          img: '../../../static/img/carousel/luminocity.jpg',
          link: 'https://site.douban.com/246052/'
        },
        {
          id: 2,
          title: 'Der Zug 豆瓣小站',
          img: '../../../static/img/carousel/derzug.jpg',
          link: 'https://site.douban.com/249336/?ref=similar_sites'
        }
      ]
    }
  }
}
</script>

<style>
.el-carousel__item h3 {
  color: black;
  font-size: 15px;
  /*line-height: 300px;*/
  bottom: 43px;
  float: left;
  position: relative;
}
.card-carousel {
  /*margin: 0 auto;*/
  margin-left: 20px;
  width: 680px;
  height: 320px;
}
.push {
  /*margin-left: -15px;*/
}
.el-carousel__item:nth-child(2n) {
  background: black;
}
.el-carousel__item:nth-child(2n+1) {
  background: black;
}
.carousel_img {
  height: 100%;
  /* width: 100%; */
  text-align: center;
}
</style>
