<template>
  <div ref="crime" class="wbg" style="width: 100%; height: 400px;"></div>
</template>

<script>
import echarts from "echarts";

export default {
  name: "Crime",
  props: {
    zipcode: {
      type: Number,
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
    this.chart = echarts.init(this.$refs.crime, "light");
    this.draw([]);
    this.request();
  },
  methods: {
    request() {
      this.axios
        .get("/api/report/crime", {
          params: {
            zipcode: this.zipcode
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
      let legendData = [];
      let xAxisData = [];
      let seriesData = [];
      let maxValue = 0;
      if (data.length == 0) {
        xAxisData = {
          data: [],
          type: "time",
          splitLine: {
            show: false
          }
        };
      }
      for (let i in data) {
        legendData.push(i);
        let xAxisTmp = [];
        let seriesTmp = [];
        for (let j in data[i]) {
          if (data[i][j] > maxValue) {
            maxValue = data[i][j];
          }
          var itemDate = new Date(j - 1);
          xAxisTmp.push(itemDate.getMonth() + 1 + "/" + itemDate.getFullYear());
          seriesTmp.push({
            name: itemDate.toString(),
            value: [
              [
                itemDate.getFullYear(),
                itemDate.getMonth() + 1,
                itemDate.getDate()
              ].join("/"),
              data[i][j]
            ]
          });
        }
        xAxisData.push({
          data: xAxisTmp,
          type: "time",
          splitLine: {
            show: false
          }
        });
        seriesData.push({
          name: i,
          type: "line",
          data: seriesTmp,
          areaStyle: { normal: {} }
        });
      }
      let option = {
        title: {
          text: "Crime"
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "cross",
            label: {
              backgroundColor: "#6a7985"
            }
          }
        },
        legend: {
          type: "scroll",
          data: legendData,
          bottom: 0
        },
        xAxis: xAxisData,
        yAxis: {
          type: "value",
          boundaryGap: [0, "100%"],
          splitLine: {
            show: false
          },
          max: maxValue + 10
        },
        series: seriesData
      };
      this.chart.setOption(option);
    }
  }
};
</script>