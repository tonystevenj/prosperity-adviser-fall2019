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
          this.draw(
            this.chartGender,
            "Gender distribution",
            response.data["gender"]
          );
          this.draw(this.chartAge, "Age distribution", response.data["age"]);
        })
        .catch(response => {
          console.log(response);
        });
    },
    draw(chartObj, title, data) {
      let legendData = [];
      for (let i in data) {
        let newName =
          data[i]["name"].charAt(0).toUpperCase() + data[i]["name"].slice(1);
        data[i]["name"] = newName;
        legendData.push(newName);
      }
      let option = {
        title: {
          text: title,
          x: "center",
          padding: [10, 0, 0, 0]
        },
        legend: {
          x: "center",
          y: "bottom",
          padding: [0, 0, 10, 0],
          data: legendData
        },
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {d}%"
        },
        series: [
          {
            name: title,
            type: "pie",
            radius: "55%",
            center: ["50%", "45%"],
            data: data,
            label: {
              normal: {
                show: true,
                position: "inside",
                formatter: "{d}%"
              }
            },
            itemStyle: {
              emphasis: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)"
              }
            }
          },
          {
            name: title,
            type: "pie",
            radius: "55%",
            center: ["50%", "45%"],
            data: data,
            label: {
              normal: {
                show: true,
                position: "outside",
                formatter: "{b}"
              }
            },
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