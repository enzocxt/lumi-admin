<template>
  <div id="id-familiar">
    <div id="id-familiar-wrapper">
      <!-- <div id="id-familiar-slideshow" class="pointer"> -->
      <!-- </div> -->
      <!-- <el-card id="id-familiar-slideshow"> -->
      <el-carousel id="id-familiar-slideshow" :interval="3000" 
        indicator-position="none"
        arrow="never"
      >
        <el-carousel-item v-for="item in familiars" :key="item.id">
          <img :src="item.img" alt="">
        </el-carousel-item>
      </el-carousel>
      <!-- </el-card> -->
      <div id="intro" v-show="showIntro">
        <a>光明城是同济大学出版社城市、建筑、设计专业出版品牌，由群岛工作室负责策划及出版。致力以更新的出版理念、更敏锐的视角、更积极的态度，回应今天中国城市、建筑、设计领域的问题。</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Familiar',
  components: {},
  data () {
    return {
      showIntro: false,
      familiars: [
        {
          id: 1,
          img: '../../../static/img/familiars/FP00_HBBP.jpg'
        }, 
        {
          id: 2,
          img: '../../../static/img/familiars/FP01_DSL.jpg'
        }, 
        {
          id: 3,
          img: '../../../static/img/familiars/FP02_HY.jpg'
        }, 
        {
          id: 4,
          img: '../../../static/img/familiars/FP03_SZJS.jpg'
        }, 
        {
          id: 5,
          img: '../../../static/img/familiars/FP04_RHGF.jpg'
        }
      ]
    }
  },
  mounted () {
    // this.getFamiliars()
  },
  methods: {
    getFamiliars () {
      // api[GET]: /api/familiar
      // 从后端获得所有 familiar 图片
      let _this = this
      _this.$axios.get('/familiar').then(resp => {
        console.log('familiar response:', resp)
        if (resp && resp.status === 200) {
          _this.familiars = resp.data
        }
      })
    }
  }
}
</script>

<style scoped>
#id-familiar {
  position: relative;
	margin-top: 97.5px;
  margin-bottom: 225px;
}
#id-familiar-wrapper {
  position: relative;
}
#id-familiar-slideshow {
	position: relative;
  overflow: hidden; /* 添加这行导致margin-right增大至最大值 */
  width: 600px;
  height: 427.5px;
	margin: 0 auto 44px 240px;
}
.el-carousel__item {
  width: 100%;
  height: 427.5px;
}
.el-carousel__item img {
  position: relative;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

#intro {
  z-index: 9999;
  position: relative;
  /* display: none; */
  width: 780px;
  margin-left: 240px;
}
#intro a{
  font-family: "SimSun", sans-serif;
  font-size: 12px;
  /*letter-spacing:2px;*/
  line-height: 22.5px
}
</style>
