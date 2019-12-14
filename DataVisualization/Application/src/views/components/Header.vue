<template>
  <el-header>
    <el-menu
      :default-active="activeIndex"
      @select="headerSelect"
      mode="horizontal"
      background-color="#f6f6f6"
    >
      <el-menu-item class="logo"><a href="#/">ARSS</a></el-menu-item>
      <el-menu-item index="/">
        <i class="el-icon-house" style="width:65%;">HOME</i>
      </el-menu-item>
      <!-- <el-menu-item index="/">
        <i class="el-icon-discover" style="width:65%;">GUIDE</i>
      </el-menu-item>-->
      <el-menu-item index="/introduction">
        <i class="el-icon-postcard" style="width:65%;">INTRODUCTION</i>
      </el-menu-item>
    </el-menu>
  </el-header>
</template>

<script>
export default {
  name: "Header",
  components: {},
  data() {
    return {
      activeIndex: this.$route.path
    };
  },
  methods: {
    headerSelect(key, keyPath) {
      if (key == null || this.$route.path == key) {
        return;
      }
      this.$router.push({ path: key });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-header {
  padding: 0;
  box-shadow: 0 12px 12px 0 rgba(0, 0, 0, 1);
}
.menu-height {
  height: 80px;
  line-height: 80px;
}
.logo {
  font-size: 28px;
}
</style>