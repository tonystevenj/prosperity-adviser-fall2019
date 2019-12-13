<template>
  <div class="banner">
    <div>
      <coverflow></coverflow>
    </div>
    <div class="banner_content">
      <el-card class="box-card">
        <div slot="header" class="clearfix test">
          <span style="font-weight: bold;">Assistant for Restaurant Site Selection</span>
        </div>
        <div>ARSS（Assistant of Restaurant Site Selection）is a web-based service that helps restaurant businesses to make better location-based decisions. Based on comprehensive databases and advanced big data processing technology; ARSS is totally committed to assists every restaurant owner to determine businesses location, accomplish cooperation target, and create value.</div>
      </el-card>
    </div>
  </div>
</template>

<script>
import coverflow from "./coverflow";

export default {
  name: "Banner",
  components: {
    coverflow
  }
};
</script>

<style>
.banner_content .el-card__header {
  border-bottom-color: rgba(0, 0, 0, 0.6);
}
</style>

<style scoped>
.swiper-container {
  float: left;
  width: 70%;
  height: 360px;
  margin-top: 40px;
  margin-left: 30px;
}
.banner {
  width: 100%;
  height: 400px;
  background: url("../../../static/banner_1.jpg") no-repeat center top;
  background-size: cover;
  -moz-background-size: 100% 100%;
}
.banner_content {
  float: right;
  width: 24%;
  height: 360px;
  background-color: rgba(0, 0, 0, 0.5);
  border-color: black;
  margin-top: 20px;
  margin-right: 30px;
  border-radius: 8px;
}
.banner_content .box-card {
  background: none;
  border: none;
  margin: 20px;
  color: #dddddd;
  box-shadow: none;
}
</style>

