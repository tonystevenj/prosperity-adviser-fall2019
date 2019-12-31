<template>
  <el-row :gutter="32" class="row">
    <el-col :span="8">
      <div ref="star45" class="wbg" style="width: 100%; height: 400px;"></div>
    </el-col>
    <el-col :span="8">
      <div ref="star13" class="wbg" style="width: 100%; height: 400px;"></div>
    </el-col>
    <el-col :span="8">
      <div ref="closed" class="wbg" style="width: 100%; height: 400px;"></div>
    </el-col>
  </el-row>
</template>

<script>
import echarts from "echarts";
require("echarts-wordcloud");

export default {
  name: "WordCloud",
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
      defaultWords: [
        {
          name: "Loading...",
          value: 1000
        }
      ],
      chartStar45: null,
      chartStar13: null,
      chartStarClosed: null
    };
  },
  mounted() {
    this.chartStar45 = echarts.init(this.$refs.star45);
    this.chartStar13 = echarts.init(this.$refs.star13);
    this.chartStarClosed = echarts.init(this.$refs.closed);
    this.draw(this.chartStar45, this.defaultWords);
    this.draw(this.chartStar13, this.defaultWords);
    this.draw(this.chartStarClosed, this.defaultWords);
    this.request();
  },

  methods: {
    request() {
      this.axios
        .get("/api/report/reviews", {
          params: {
            latitude: this.latitude,
            longitude: this.longitude,
            radius: this.radius,
            category: this.category
          }
        })
        .then(response => {
          var words = [];
          for (let i in response.data) {
            let words = [];
            if (response.data[i]["reviews"] == null) {
              words = [
                {
                  name: "No data",
                  value: 1000
                }
              ];
            } else {
              for (let j in response.data[i]["reviews"]) {
                words.push({
                  name: response.data[i]["reviews"][j],
                  value: response.data[i]["weights"][j]
                });
              }
            }
            switch (response.data[i]["category"]) {
              case "star45":
                this.draw(this.chartStar45, words);
                break;
              case "star13":
                this.draw(this.chartStar13, words);
                break;
              case "closed":
                this.draw(this.chartStarClosed, words);
                break;
            }
          }
        })
        .catch(response => {
          console.log(response);
          let words = [
            {
              name: "No data",
              value: 1000
            }
          ];
          this.draw(this.chartStar45, words);
          this.draw(this.chartStar13, words);
          this.draw(this.chartStarClosed, words);
        });
    },
    draw(chartObj, words) {
      // https://github.com/ecomfe/echarts-wordcloud
      let options = {
        title: {
          text: "Reviews",
          textAlign: "auto"
        },
        series: [
          {
            type: "wordCloud",
            shape: "circle",
            left: "center",
            top: "center",
            width: "90%",
            height: "90%",
            right: null,
            bottom: null,
            sizeRange: [9, 80],
            rotationRange: [-90, 90],
            rotationStep: 45,
            gridSize: 8,
            drawOutOfBound: false,
            // Global text style
            textStyle: {
              normal: {
                fontFamily: "sans-serif",
                fontWeight: "bold",
                // Color can be a callback function or a color string
                color: function() {
                  // Random color
                  return (
                    "rgb(" +
                    [
                      Math.round(Math.random() * 160),
                      Math.round(Math.random() * 160),
                      Math.round(Math.random() * 160)
                    ].join(",") +
                    ")"
                  );
                }
              },
              emphasis: {
                shadowBlur: 10,
                shadowColor: "#333"
              }
            },
            // Data is an array. Each array item must have name and value property.
            data: words
          }
        ]
      };
      chartObj.setOption(options);
    }
  }
};
</script>