<template>
  <div>
    <familiar></familiar>
    <div class="separator"></div>
    <books></books>
    <about></about>
    <lumi-footer></lumi-footer>
    <router-view/>
  </div>
</template>

<script>
import Familiar from './home/Familiar'
import Books from './home/Books'
import About from './home/About'
import LumiFooter from './home/LumiFooter'

export default {
  name: 'Luminocity',
  components: {
    Familiar,
    Books,
    About,
    LumiFooter,
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

.separator {
  display: block;
  position: relative;
	padding-top: 90px;
}

</style>
