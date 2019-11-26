<template>
  <div ref="test" class="wbg" style="width: 100%; height: 400px;"></div>
</template>

<script>
import echarts from "echarts";

export default {
  name: "Test",
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
      chart: null,
    };
  },
  mounted() {
    // 测试传值是否收到，确认没问后题删掉
    console.log(this.latitude, this.longitude, this.radius)
    // 初始化chart
    this.chart = echarts.init(this.$refs.test);
    this.draw();
  },
  methods: {
    draw() {
      // 所有实例：https://echarts.apache.org/examples/zh/
      // 异步更新数据：https://echarts.apache.org/zh/tutorial.html#%E5%BC%82%E6%AD%A5%E6%95%B0%E6%8D%AE%E5%8A%A0%E8%BD%BD%E5%92%8C%E6%9B%B4%E6%96%B0
      // 属性设置：https://echarts.apache.org/zh/option.html
      this.chart.setOption({
        title: {
          text: "Rate",
          textAlign: "auto"
        },
        xAxis: {
          type: "category",
          data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        },
        yAxis: {
          type: "value"
        },
        series: [
          {
            data: [120, 200, 150, 80, 70, 110, 130],
            type: "bar"
          }
        ]
      });
    }
  }
};
</script>