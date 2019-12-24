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
      let data = {
        "star45": [{"name": "food_type", "value": 0.089, "data": {"Mexican": 18.29, "American (New)": 15.85, "American (Traditional)": 9.76, "Italian": 6.1, "American (New),American (Traditional)": 3.66, "other": 46.34}}, {"name": "WheelchairAccessible", "value": 0.079, "data": {"true": 42.68, "false": 4.88, "other": 52.44}}, {"name": "Caters", "value": 0.056, "data": {"true": 47.56, "false": 28.05, "other": 24.39}}, {"name": "OutdoorSeating", "value": 0.053, "data": {"true": 63.41, "false": 21.95, "other": 14.64}}, {"name": "Alcohol", "value": 0.051, "data": {"full_bar": 41.46, "none": 25.61, "beer_and_wine": 9.76, "other": 23.17}}, {"name": "lot", "value": 0.049, "data": {"0": 54.88, "1": 23.17, "other": 21.95}}, {"name": "NoiseLevel", "value": 0.048, "data": {"average": 54.88, "quiet": 7.32, "loud": 2.44, "other": 35.36}}, {"name": "WiFi", "value": 0.044, "data": {"free": 54.88, "no": 24.39, "paid": 1.22, "other": 19.51}}, {"name": "BikeParking", "value": 0.042, "data": {"true": 74.39, "false": 4.88, "other": 20.73}}, {"name": "RestaurantsPriceRange2", "value": 0.039, "data": {"2": 51.22, "1": 26.83, "3": 3.66, "4": 1.22, "other": 17.07}}],
        "star13": [{"name": "food_type", "value": 0.089, "data": {"American (Traditional)": 13.24, "Mexican": 10.29, "American (New)": 7.35, "American (New),American (Traditional)": 4.41, "Greek,Mediterranea": 2.94, "other": 61.77}}, {"name": "WheelchairAccessible", "value": 0.079, "data": {"true": 11.76, "other": 88.24}}, {"name": "Caters", "value": 0.056, "data": {"false": 42.65, "true": 30.88, "other": 26.47}}, {"name": "OutdoorSeating", "value": 0.053, "data": {"true": 58.82, "false": 22.06, "other": 19.12}}, {"name": "Alcohol", "value": 0.051, "data": {"full_bar": 39.71, "none": 29.41, "beer_and_wine": 10.29, "other": 20.59}}, {"name": "lot", "value": 0.049, "data": {"0": 73.53, "1": 8.82, "other": 17.65}}, {"name": "NoiseLevel", "value": 0.048, "data": {"average": 57.35, "loud": 8.82, "quiet": 5.88, "very_loud": 2.94, "other": 25.01}}, {"name": "WiFi", "value": 0.044, "data": {"free": 39.71, "no": 32.35, "paid": 1.47, "other": 26.47}}, {"name": "BikeParking", "value": 0.042, "data": {"true": 69.12, "false": 11.76, "other": 19.12}}, {"name": "RestaurantsPriceRange2", "value": 0.039, "data": {"2": 57.35, "1": 33.82, "3": 1.47, "other": 7.36}}],
        "closed": [{"name": "food_type", "value": 0.089, "data": {"American (New)": 13.68, "Mexican": 12.63, "Italian": 9.47, "American (Traditional)": 8.42, "Greek,Mediterranea": 3.16, "other": 52.64}}, {"name": "WheelchairAccessible", "value": 0.079, "data": {"true": 10.53, "other": 89.47}}, {"name": "Caters", "value": 0.056, "data": {"true": 35.79, "false": 22.11, "other": 42.1}}, {"name": "OutdoorSeating", "value": 0.053, "data": {"true": 67.37, "false": 24.21, "other": 8.42}}, {"name": "Alcohol", "value": 0.051, "data": {"full_bar": 42.11, "none": 32.63, "beer_and_wine": 12.63, "other": 12.63}}, {"name": "lot", "value": 0.049, "data": {"0": 68.42, "1": 22.11, "other": 9.47}}, {"name": "NoiseLevel", "value": 0.048, "data": {"average": 54.74, "quiet": 6.32, "loud": 5.26, "very_loud": 2.11, "other": 31.57}}, {"name": "WiFi", "value": 0.044, "data": {"free": 32.63, "no": 20.0, "other": 47.37}}, {"name": "BikeParking", "value": 0.042, "data": {"true": 36.84, "false": 6.32, "other": 56.84}}, {"name": "RestaurantsPriceRange2", "value": 0.039, "data": {"2": 53.68, "1": 38.95, "3": 2.11, "4": 1.05, "other": 4.21}}]
      };
      this.draw(data[this.category]);
      // this.axios
      //   .get("/api/report/feature", {
      //     params: {
      //       latitude: this.latitude,
      //       longitude: this.longitude,
      //       radius: this.radius,
      //       category: this.category
      //     }
      //   })
      //   .then(response => {
      //     this.draw(response.data);
      //   })
      //   .catch(response => {
      //     console.log(response);
      //   });
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
        title: {
          text: "Feature",
          textAlign: "auto"
        },
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