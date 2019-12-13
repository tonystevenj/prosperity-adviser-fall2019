<template>
  <el-footer height="100px">
    <div class="footer_link">
      <span>
        <el-link type="info" style="margin-left:10px;">Privacy Policy</el-link>
        <el-link type="info" style="margin-left:10px;">Terms of Use</el-link>
        <el-link type="info" style="margin-left:10px;">About</el-link>
        <p style="color: #a6a9ad; font-weight: bold; font-size: 13px;">@2019</p>
      </span>
    </div>
  </el-footer>
</template>

<script>
export default {
  name: "Footer",
  components: {}
};
</script>

<style scoped>
.el-footer {
  background-color: rgb(240, 240, 240);
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  border-top: 1px solid rgb(228, 228, 228);
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
.el-footer .footer_link {
  margin-top: 20px;
  text-align: center;
}
</style>
