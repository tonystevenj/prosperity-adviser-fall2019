<template>
  <div ref="rate" class="wbg" style="width: 100%; height: 400px;"></div>
</template>

<script>
import echarts from "echarts";

export default {
  name: "Rate",
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
    },
    category: {
      type: String,
      required: true
    }
  },
  components: {},
  data() {
    return {
      chart: null
    };
  },
  mounted() {
    this.chart = echarts.init(this.$refs.rate, "light");
    this.draw([]);
    this.request();
  },
  methods: {
    request() {
      // api获取真实数据进行替换
      console.log({
        latitude: this.latitude,
        longitude: this.longitude,
        radius: this.radius,
        category: this.category
      });
      this.axios
        .get("/api/report/feature", {
          params: {
            latitude: this.latitude,
            longitude: this.longitude,
            radius: this.radius,
            category: this.category
          }
        })
        .then(response => {
          this.draw(response.data);
        })
        .catch(response => {
          console.log(response);
        });
    },
    draw(data) {
      let subTitle = [];
      let series = [];
      let line = data.length;
      if (line > 4) {
        line = 4;
      }
      let column = 0;
      for (var i in data) {
        let tmpLen = 0;
        let dataTmp = [];
        if (i < 4) {
          subTitle.push(data[i]["name"]);
        }
        for (var j in data[i]["data"]) {
          dataTmp.push(data[i]["data"][j]);
          tmpLen++;
        }
        data[i]["dataTmp"] = dataTmp;
        if (tmpLen > column) {
          column = tmpLen;
        }
      }
      for (var j = 0; j < column; j++) {
        if (series.indexOf(j) == -1) {
          series.push([]);
        }
        let seriesTmp = [];
        for (var i = 0; i < line; i++) {
          if (data[i]["dataTmp"].hasOwnProperty(j)) {
            seriesTmp.push(data[i]["dataTmp"][j]);
          } else {
            seriesTmp.push(0);
          }
        }
        series[j] = {
          type: "bar",
          data: seriesTmp,
          coordinateSystem: "polar",
          stack: "a"
        };
      }
      console.log(series);
      console.log(subTitle);

      //series[n][i] = data[i]["data"][n]

      this.chart.setOption({
        angleAxis: {},
        radiusAxis: {
          type: "category",
          data: subTitle,
          z: 10
        },
        polar: {},
        series: series
      });
    }
  }
};
</script>