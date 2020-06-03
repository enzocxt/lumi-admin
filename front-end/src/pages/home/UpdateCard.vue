<template>
  <el-card class="box-card">
    <div slot="header" class="clearfix">
      <span style="font-weight: bold;font-size: 20px">公告</span>
      <!--<el-button style="float: right; padding: 3px 0" type="text">修改</el-button>-->
    </div>
    <div class="block">
      <el-timeline>
        <el-timeline-item v-for="item in items" :key="item.id"
          timestamp="item.ct.slice(0, 10)" placement="top">
          <el-card>
            <h4>{{ item.title }}</h4>
            <p>
              <a :href=item.href>{{ item.author }}</a>
              提交于 {{ item.ct }}
            </p>
          </el-card>
        </el-timeline-item>
      </el-timeline>
    </div>
  </el-card>
</template>

<script>
export default {
  name: 'UpdateCard',
  data () {
    return {
      items: [
        {
          'id': 1,
          'title': '读书御寒双十一：光明城经典好书全场5折起，折后更享满减',
          'href': "https://www.douban.com/people/131903450/",
          'author': '晃膀子的',
          'ct': '2017-11-09 20:21:46',
        }, 
        {
          'id': 2,
          'title': '招聘 | 千里路 · 万卷书 · 一座城',
          'href': "https://www.douban.com/people/131903450/",
          'author': '晃膀子的',
          'ct': '2017-03-07 09:03:05',
        }, 
        {
          'id': 3,
          'title': '招聘 | 光明城期待您的加入',
          'href': "https://www.douban.com/people/46912750/",
          'author': '王琦瑶',
          'ct': '2015-07-01 15:24:27',
        }
      ]
    }
  }
}
</script>

<style scoped>
.box-card {
  margin-top: 5px;
  width: 988px;
  height: 1050px;
  text-align: left;
}
</style>