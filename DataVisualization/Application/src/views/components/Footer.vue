<template>
  <el-footer height="100px">
    <div class="footer_link">
      <span>
        <p style="color: #a6a9ad; font-weight: bold; font-size: 13px;">
          By Group 7: Peng Hou <a href="mailto:phou001@fiu.edu">phou001@fiu.edu</a>, Hongjing Wang <a href="mailto:hwang064@fiu.edu">hwang064@fiu.edu</a>, Zheya Wu <a href="mailto:zwu014@fiu.edu">zwu014@fiu.edu</a>,
          Yan Xiao <a href="mailto:yxiao001@fiu.edu">yxiao001@fiu.edu</a>, Linlin Zhou <a href="mailto:lzhou012@fiu.edu">lzhou012@fiu.edu</a>
        </p>

        <p style="color: #a6a9ad; font-weight: bold; font-size: 13px;">Professor: Giri Narasimhan</p>
        <p style="color: #a6a9ad; font-weight: bold; font-size: 13px;">Fall 2019 Data Science.</p>
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
