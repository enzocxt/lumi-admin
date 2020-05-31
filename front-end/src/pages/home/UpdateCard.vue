<template>
  <el-card class="box-card">
    <div slot="header" class="clearfix">
      <span style="font-weight: bold;font-size: 20px">公告</span>
      <!--<el-button style="float: right; padding: 3px 0" type="text">修改</el-button>-->
    </div>
    <div class="block">
      <el-timeline>
        <el-timeline-item timestamp="2017/11/09" placement="top">
          <el-card>
            <h4>读书御寒双十一：光明城经典好书全场5折起，折后更享满减</h4>
            <p>
              <a href="https://www.douban.com/people/131903450/">晃膀子的</a>
              提交于 2017-11-09 20:21:46
            </p>
          </el-card>
        </el-timeline-item>
        <el-timeline-item timestamp="2017/03/07" placement="top">
          <el-card>
            <h4>招聘 | 千里路 · 万卷书 · 一座城</h4>
            <p>
              <a href="https://www.douban.com/people/131903450/">晃膀子的</a>
              提交与 2017-03-07 09:03:05
            </p>
          </el-card>
        </el-timeline-item>
        <el-timeline-item timestamp="2015/07/01" placement="top">
          <el-card>
            <h4>招聘 | 光明城期待您的加入</h4>
            <p>
              <a href="https://www.douban.com/people/46912750/">王琦瑶</a>
              提交于 2015-07-01 15:24:27</p>
          </el-card>
        </el-timeline-item>
      </el-timeline>
    </div>
  </el-card>
</template>

<script>
export default {
  name: 'UpdateCard'
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