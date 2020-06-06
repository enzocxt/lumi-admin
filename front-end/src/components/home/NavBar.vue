<template>
  <div id="nav">
    <div class="nav-wrapper" @mouseenter="setNavBar()" @mouseleave="setNavBar()">
      <img src="../../assets/logo.png" width="104px">
      <span class="nd">img/Logo.gif</span>
      <ul id="menu" v-show="showNavBar">
        <li>
          <a href="#/books">图书</a>
        </li>
        <!--
        <li>
          <a href="#/products">产品</a>
        </li>
        -->
        <li>
          <a href="LUMINOCITY_catalogue_spring_2016_EN.pdf" target="_blank">书目下载</a>
        </li>
        <li>
          <a href="#/about">关于我们</a>
        </li>
        <li id="id-purchase-nav">
          <a>购买</a>
          <ul id="id-purchase-menu">
            <li>
              <a href="https://tjdxcbs.tmall.com/shop/view_shop.htm?spm=a230r.7195193.1997079397.2.PTcaWU" target="_blamk">天猫</a>
            </li>
            <li>
              <a href="https://weidian.com/item_classes.html?userid=208102218&c=77739198&des=%E5%85%89%E6%98%8E%E5%9F%8E%E7%B3%BB%E5%88%97&from=timeline&isappinstalled=0" target="_blank">微店</a>
            </li>
          </ul>
        </li>
        <li>
          <a href="#/english">English</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
  components: {},
  data () {
    return {
      showNavBar: false,
    }
  },
  mounted () {
  },
  methods: {
    setNavBar () {
      console.log(this.showNavBar)
      this.showNavBar = !this.showNavBar
    }
  }
}
</script>

<style scoped>
#nav {
	z-index: 9999;
	position: fixed;
  padding: 0 0 0 1.25%;
  top: 6.25%;
  /*padding: 18px 0 0 8px;*/
	/*left: 68px;
	top: 78px;*/
}

.nd {
	display: none;
}

.nav-wrapper img {
	display: block;
  padding-bottom: 45px;
}

.nav-wrapper img:hover{
  cursor: pointer;
}

/* menu */
#menu {
	/* display: none; */
  position: fixed;
}

#menu li {
  list-style-type: none;
}

#menu a {
  font-family: "Noto Sans TC", sans-serif;
	font-size: 12px;
	line-height: 22.5px;
  word-spacing: 100%;
	text-decoration: none;
  color: #000000;
}

#menu:hover {
  cursor: pointer;
}

#menu a:hover {
	font-style: italic !important;
}

#menu .selected {
	font-style: italic;
}

#nav ul {
  margin-top: 0;
  padding-left: 27px; /* nav 最左侧轴线距离最外层padding还有8px */
}

#id-purchase-menu {
  display: none;
}

#id-purchase-nav ul {
  padding-left: 13.5px;
}
/* menu end*/

#p-featured {
	margin-bottom: 82px;
}

.mb {margin-bottom: 18px;}
.mt {margin-top: 18px;}
.mr {margin-right: 17px;}
</style>
