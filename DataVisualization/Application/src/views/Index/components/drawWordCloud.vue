<template>
  <div ref="wordcloud" class="wbg" style="width: 100%; height: 400px;"></div>
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
    category:{
      type:String,
      required:true
    }
  },
  components: {},
  data() {
    return {
      defaultWords: [
        {
          name: "Landing...",
          value: 1000
        }
      ],
      chart: null
    };
  },
  mounted() {
    // console.log(this.latitude, this.longitude, this.radius)
    this.chart = echarts.init(this.$refs.wordcloud);
    this.draw(this.defaultWords);
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
          })
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
          for (var i in response.data) {
            words.push({
              name: response.data[i][0],
              value: response.data[i][1]
            });
          }
          this.draw(words);
        })
        .catch(response => {
          console.log(response);
        });
    },
    draw(words) {
      // https://github.com/ecomfe/echarts-wordcloud
      this.chart.setOption({
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
      });
    }
  }
};
</script>