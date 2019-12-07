<template>
  <div style="margin-top: 0px;">
    <div class="block">
      <span class="demonstration">Population density</span>
      <el-slider v-model="percent.population"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Median earnings</span>
      <el-slider v-model="percent.earnings"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Park density</span>
      <el-slider v-model="percent.park" :show-tooltip="false"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">School density</span>
      <el-slider v-model="percent.school" :format-tooltip="formatTooltip"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Hospital density</span>
      <el-slider v-model="percent.hospital" :format-tooltip="formatTooltip"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Aourist attraction density</span>
      <el-slider v-model="percent.pride" :format-tooltip="formatTooltip"></el-slider>
    </div>
  </div>
</template>

<script>
export default {
  name: "Panel",
  // 接收宿主传过来的值
  props: {
    latitude: {
      type: Number,
      required: true
    },
    longitude: {
      type: Number,
      required: true
    },
    radius: {
      type: Number,
      required: true
    }
  },
  components: {},
  data() {
    return {
      percent: {
        population: 50,
        earnings: 50,
        park: 50,
        school: 50,
        hospital: 50,
        pride: 50,
      }
    };
  },
  mounted() {
  },
  methods: {
    
  }
};
</script>