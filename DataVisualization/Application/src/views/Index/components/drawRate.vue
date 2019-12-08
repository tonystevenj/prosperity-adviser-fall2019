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
      let maxLine = 8;
      if (line > maxLine) {
        line = maxLine;
      }
      let column = 0;
      for (var i in data) {
        let tmpLen = 0;
        let dataTmp = [];
        if (i < maxLine) {
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
      let titleTmp = [];
      let valueTmp = [];
      let titleStatus = false;
      for (var j = 0; j < column; j++) {
        if (series.indexOf(j) == -1) {
          series.push([]);
        }
        let seriesTmp = [];
        for (let i = line - 1; i >= 0; i--) {
          if (data[i]["dataTmp"].hasOwnProperty(j)) {
            seriesTmp.push(data[i]["dataTmp"][j]);
            if (!titleStatus) {
              titleTmp.push(Object.keys(data[i]["data"]));
              valueTmp.push(data[i]["dataTmp"])
            }
          } else {
            seriesTmp.push(0);
          }
        }
        titleStatus = true;
        series[j] = {
          type: "bar",
          data: seriesTmp,
          stack: "a",
          label: {
            normal: {
              show: true,
              position: "insideRight",
              formatter: params => {
                if (
                  titleTmp[params["dataIndex"]][params["seriesIndex"]] !=
                  undefined
                ) {
                  let newTitle =
                    titleTmp[params["dataIndex"]][params["seriesIndex"]];
                  if (params["value"] < 5) {
                    return "";
                  } else if (params["value"] > 10 && newTitle.length < 20) {
                    return titleTmp[params["dataIndex"]][params["seriesIndex"]];
                  } else {
                    return "";
                  }
                }
              }
            }
          }
        };
      }
      this.chart.setOption({
        tooltip: {
          trigger: "axis",
          axisPointer: {
            // 坐标轴指示器，坐标轴触发有效
            type: "shadow" // 默认为直线，可选为：'line' | 'shadow'
          },
          formatter: (params, ticket, callback) => {
            let list = ""
            for (let i in params) {
              if (params[i]["value"] == 0) {
                continue;
              }
              let subTitle = titleTmp[params[0]["dataIndex"]][i]
              let subValue = valueTmp[params[0]["dataIndex"]][i]
              list += '<div style="color:'+params[i]["color"]+'"><b>'+(++i)+')</b>.'+subTitle+': <b>'+subValue+'%</b></div>'
            }
            let html = `
                <div>
                    <div><b>`+params[0]["axisValueLabel"]+`:</b></div>
                    <div>`+list+`</div>
                </div>
                `;
            return html;
          }
        },
        grid: {
          top: "3%",
          left: "2%",
          right: "3%",
          bottom: "2%",
          containLabel: true
        },
        xAxis: {
          type: "value"
        },
        yAxis: {
          type: "category",
          data: subTitle.reverse(),
          axisLabel: {
            interval: 0,
            rotate: 40
          }
        },
        series: series
      });
    }
  }
};
</script>