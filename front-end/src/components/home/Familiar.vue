<template>
  <div id="id-familiar">
    <div id="id-familiar-wrapper">
      <div id="id-familiar-slideshow" class="pointer">
      </div>
      <div id="intro">
        <a>光明城是同济大学出版社城市、建筑、设计专业出版品牌，由群岛工作室负责策划及出版。致力以更新的出版理念、更敏锐的视角、更积极的态度，回应今天中国城市、建筑、设计领域的问题。</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Familiar',
  components: {}
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
#id-familiar-slideshow img {
  position: relative;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

#intro {
  z-index: 9999;
  position: relative;
  display: none;
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
