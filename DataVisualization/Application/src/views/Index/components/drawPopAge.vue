<template>
  <el-row :gutter="32" class="row">
    <el-col :span="12">
      <div ref="gender" class="wbg" style="width: 100%; height: 400px;"></div>
    </el-col>
    <el-col :span="12">
      <div ref="age" class="wbg" style="width: 100%; height: 400px;"></div>
    </el-col>
  </el-row>
</template>

<script>
import echarts from "echarts";

export default {
  name: "PopAge",
  props: {
    zipcode: {
      type: Number,
      required: true
    }
  },
  components: {},
  data() {
    return {
      chartGender: null,
      chartAge: null
    };
  },
  mounted() {
    this.chartGender = echarts.init(this.$refs.gender, "light");
    this.chartAge = echarts.init(this.$refs.age, "light");
    this.draw(this.chartGender, []);
    this.draw(this.chartAge, []);
    this.request();
  },
  methods: {
    request() {
      this.axios
        .get("/api/report/pop_age", {
          params: {
            zipcode: this.zipcode
          }
        })
        .then(response => {
          this.draw(this.chartGender, "Gender", response.data["gender"])
          this.draw(this.chartAge, "Age", response.data["age"])
        })
        .catch(response => {
          console.log(response);
        });
    },
    draw(chartObj, title, data) {
      let option = {
        title: {
          text: title,
          x: "center"
        },
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        series: [
          {
            name: title,
            type: "pie",
            radius: "55%",
            center: ["50%", "50%"],
            data: data,
            itemStyle: {
              emphasis: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)"
              }
            }
          }
        ]
      };
      chartObj.setOption(option);
    }
  }
};
</script>