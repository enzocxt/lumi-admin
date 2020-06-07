<template>
  <div id="site">
    <div id="site-wrapper">
      <nav-bar></nav-bar>
      <div id="logo" @mouseenter="setShowIntro()" @mouseleave="setShowIntro">
        <img class="logo-cn" src="../assets/logo_cn.png">
      </div>
      <familiar ref="familiar"></familiar>
      <div class="separator"></div>
      <books></books>
      <about></about>
      <lumi-footer></lumi-footer>
      <router-view/>
    </div>
  </div>
</template>

<script>
import NavBar from './home/NavBar'
import Familiar from './home/Familiar'
import Books from './home/Books'
import About from './home/About'
import LumiFooter from './home/LumiFooter'

export default {
  name: 'Luminocity',
  components: {
    NavBar,
    Familiar,
    Books,
    About,
    LumiFooter,
  },
  data () {
    return {
    }
  },
  methods: {
    setShowIntro () {
      let tmp = this.$refs.familiar.showIntro
      this.$refs.familiar.showIntro = !tmp
    }
  }
}
</script>

<style scoped>
@import url(http://fonts.googleapis.com/earlyaccess/notosanstc.css);
@font-face{
  font-family: 'FC';
  src: url( 'http://fnt.webink.com/wfs/?drawer=2FF99E2B-FAF5-4EAB-9ED4-8A4BC2755E92&font=79FFD680-777D-F4B0-8FFE-043ABAB4969A');
  font-weight:normal;font-style:normal;
}
@font-face{
  font-family: 'FC';
  src: url( 'http://fnt.webink.com/wfs/?drawer=2FF99E2B-FAF5-4EAB-9ED4-8A4BC2755E92&font=2AA35A4E-ED48-3B8D-3C79-2764EFAD2C9E');
  font-weight:normal;font-style:italic;
}

html {
  position: relative;
}
body, html {
  min-width: 1280px;
	/* width: 100%; */
	/* height: 100%; */
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
/* 分隔块 */
.separator {
  display: block;
  position: relative;
	padding-top: 90px;
}

#site {
	width: 1280px;
  margin: 0 auto 0 auto;
}
#site-wrapper {
	/*padding: 60px 120px 60px 60px;*/
  padding: 3.5% 9.375% 3.5% 4.6875%;
}

#logo {
	z-index: 9999;
	position: fixed;
	padding: 0 35px 0 35px;
  bottom: 9.275%;
	/* width: 45px; */
}
.logo-cn {
  width: 45px;
}
#logo:hover {
  cursor: pointer;
}
</style>
