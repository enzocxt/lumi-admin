<template>
  <div>
    <familiar></familiar>
    <router-view/>
  </div>
</template>

<script>
import Familiar from './home/Familiar'

export default {
  name: 'Luminocity',
  components: {
    Familiar,
  }
}
</script>

<style scoped>
html {
  position: relative;
}
body, html {
	/* width:100%; */
  min-width: 1280px;
	/*height:100%;*/
}
body {
  height: 100%;
	margin:0;
	padding:0;
  background: linear-gradient(to bottom,#f2d7d2,#ffffff,#f2d7d2,#ffffff,#f2d7d2,#ffffff,#f2d7d2,#ffffff,#f2d7d2);
  background-repeat:no-repeat
}
/* 通用的　*/
/* 鼠标移动到元素上面显示效果 */
.pointer {
  cursor: pointer;
}
/* 不显示拥有该CSS类的元素 */
.cls-hide {
  display: none;
}
</style>
