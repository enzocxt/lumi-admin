<template>
  <div id="id-footer">
    <div class="footer-wrapper">
      <div class="unknown">
        <div class="qrimg-wrapper">
          <img class="qr-img" src="../../assets/qrwechat.jpg" alt="qr-wechat">
        </div>
        <div class="frame-wrapper">
          <a href="http://218.242.124.22:8081/businessCheck/verifKey.do?showType=extShow&serial=9031000020190422145209000004579464-SAIC_SHOW_310000-4028e4cb6493ac2c0164c8bbe7bd20ac746&signData=MEUCIQCuP5msdgoXJ++cBNha526WBeW3ja8voMbbyiuvRcNBIgIgH+TDcGnXPyIA3zFEcYelAJr1OUm7agYNmhxy3yHkR7U=" target="_blank">
            <img class="frame-img" src="../../assets/logo.png" alt="logo-frame">
          </a>
        </div>
      </div>
      <div class="qr-code">
        <div id="icp-wrapper">
          <p>
            <a class="email" href="mailto:info@luminocity.cn" target="_blank">写邮件</a>
            <a class="douban" href="https://site.douban.com/246052/" target="_blank">去豆瓣小站</a>
            <a class="wechat" href="../../assets/qrwechat.jpg" target="_blank">微信公众号</a>
          </p>
          <p class="address-cn">北京市海淀区安宁庄西路1号上第MOMA 18-2-202  邮编 100085</p>
          <p class="icpback-cn">版权所有 © 同济大学出版社光明城 2016 沪ICP备11031396号-2</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LumiFooter',
  components: {},
  data () {
    return {
    }
  },
  mounted () {
  },
  methods: {
  }
}
</script>

<style scoped>
#id-footer {
    position: relative;
    /* margin: 0 60px 0px 180px; */
    margin-left: 180px;
}

.unknown {
    position: relative;
    overflow: hidden;
    height: 135px;
}

.qrimg-wrapper{
    position: relative;
    display: inline;
    height: 100px;
    width: 100px;
}
.qr-img {
    position: relative;
    /* display: none; */
    height: 100px;
    width: 100px;
    vertical-align: bottom;
}

.frame-wrapper {
    position: relative;
    float: right;
    display: inline;
}
.frame-img {
    position: relative;
    height: 70px;
    vertical-align: top;
}
.footer-img {
    position: relative;
    display: inline;
    width: 180px;
    height: 135px;
    float: right;
    vertical-align: bottom;
}

.qr-code {
    position: relative;
    left: 0px;
    overflow: hidden;
}
p {
	margin: 0;
}
.icp-wrapper {
    display: block;
    position: relative;
}
.icpback-cn{
    display: flex;
    align-items: flex-end;
    position: relative;
    bottom: 0;
    font-family: "source-han-sans-simplified-c","Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    font-size: 11px;
    letter-spacing:2px
}

a.douban:link {
	color:#807f80;
	text-decoration:none;
}
a.douban:visited {
	color:#807f80;
	text-decoration:none;
}
a.douban:hover {
	color:white;
	text-decoration:underline;
}

a.email:link {
	color:#807f80;
	text-decoration:none;
}
a.email:visited {
	color:#807f80;
	text-decoration:none;
}
a.email:hover {
	color:white;
	text-decoration:underline;
}

a.wechat:link {
    color:#807f80;
    text-decoration:none;
}
a.wechat:visited {
    color:#807f80;
    text-decoration:none;
}
a.wechat:hover {
    color:white;
    text-decoration:underline;
}

p.address-cn{
	position: relative;
	font-family:"source-han-sans-simplified-c","Hiragino Sans GB", "Microsoft YaHei",sans-serif;
	font-size: 11px;
	letter-spacing:2px
}
a.email {
	position: relative;
	font-family:"source-han-sans-simplified-c","Hiragino Sans GB", "Microsoft YaHei", sans-serif;
	font-size:11px;
	letter-spacing:2px
}
a.douban {
	position: relative;
	font-family:"source-han-sans-simplified-c","Hiragino Sans GB", "Microsoft YaHei", sans-serif;
	font-size: 11px;
	letter-spacing:2px
}
a.wechat {
    position: relative;
    font-family:"source-han-sans-simplified-c","Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    font-size: 11px;
    letter-spacing:2px
}
</style>
