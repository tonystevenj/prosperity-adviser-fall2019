<template>
  <el-header>
    <el-menu :default-active="activeIndex" mode="horizontal" background-color="#f6f6f6">
      <el-menu-item>
        <el-menu-item class="logo">ARSS</el-menu-item>
      </el-menu-item>
      <el-menu-item index="/">
        <router-link :to="{name: 'Index'}">
          <i class="el-icon-house" style="width:65%;">HOME</i>
        </router-link>
      </el-menu-item>
      <el-menu-item index="/guide">
        <i class="el-icon-discover" style="width:65%;">GUIDE</i>
      </el-menu-item>

      <el-menu-item index="/about">
        <router-link to="/about">
          <i class="el-icon-postcard" style="width:65%;">ABOUT</i>
        </router-link>
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
  methods: {}
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