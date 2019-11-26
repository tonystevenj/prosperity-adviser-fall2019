<template>
  <div>
    <el-row :gutter="32" class="row">
      <el-col :span="6">
        <div class="topdesc wbg">
          <div class="icon">
            <i class="el-icon-food" style="color: #6ac6c5;"></i>
          </div>
          <div class="detail">
            <div class="key">The number of restaurants</div>
            <div class="value">200</div>
          </div>
        </div>
      </el-col>
      <el-col :span="6">
        <div class="topdesc wbg">
          <div class="icon">
            <i class="el-icon-map-location" style="color: #36a3f7;"></i>
          </div>
          <div class="detail">
            <div class="key">The number of restaurants</div>
            <div class="value">200</div>
          </div>
        </div>
      </el-col>
      <el-col :span="6">
        <div class="topdesc wbg">
          <div class="icon">
            <i class="el-icon-user" style="color: #f4516c;"></i>
          </div>
          <div class="detail">
            <div class="key">The number of restaurants</div>
            <div class="value">200</div>
          </div>
        </div>
      </el-col>
      <el-col :span="6">
        <div class="topdesc wbg">
          <div class="icon">
            <i class="el-icon-bank-card" style="color: #E6A23C;"></i>
          </div>
          <div class="detail">
            <div class="key">The number of restaurants</div>
            <div class="value">200</div>
          </div>
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="32" class="row">
      <el-col :span="24">
        <div id="rate" class="wbg" style="width: 100%; height: 400px;"></div>
      </el-col>
    </el-row>
    <el-row :gutter="32" class="row">
      <el-col :span="8">
        <wordcloud
          class="wbg"
          :data="defaultWords"
          nameKey="name"
          valueKey="value"
          :color="myColors"
          :showTooltip="true"
        ></wordcloud>
        <!-- :wordClick="wordClickHandler" -->
      </el-col>
      <el-col :span="8">
        <div id="test" class="wbg" style="width: 100%; height: 400px; backround-color: #ffffff;"></div>
      </el-col>
      <el-col :span="8">
        <div id="comment" class="wbg" style="width: 100%; height: 400px; backround-color: #ffffff;"></div>
      </el-col>
    </el-row>
    <el-row :gutter="32" class="row">
      <el-col :span="16">
        <el-table :data="tableData" style="width: 100%" height="400">
          <el-table-column fixed prop="date" label="日期" width="150"></el-table-column>
          <el-table-column prop="name" label="姓名" width="120"></el-table-column>
          <el-table-column prop="province" label="省份" width="120"></el-table-column>
          <el-table-column prop="city" label="市区" width="120"></el-table-column>
          <el-table-column prop="address" label="地址" width="300"></el-table-column>
        </el-table>
      </el-col>
      <el-col :span="8">
        <div id="test1" class="wbg" style="width: 100%; height: 400px; backround-color: #ffffff;"></div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import wordcloud from "vue-wordcloud";
import echarts from "echarts";

export default {
  name: "Layer",
  components: {
    wordcloud: wordcloud
    // "v-chart": ECharts
  },
  data() {
    let data = [];

    for (let i = 0; i <= 360; i++) {
      let t = (i / 180) * Math.PI;
      let r = Math.sin(2 * t) * Math.cos(2 * t);
      data.push([r, i]);
    }

    return {
      myColors: ["#1f77b4", "#629fc9", "#94bedb", "#c9e0ef"],

      defaultWords: [
        {
          name: "landing...",
          value: 100
        }
      ],
      tableData: [
        {
          date: "2016-05-03",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          date: "2016-05-02",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          date: "2016-05-04",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          date: "2016-05-01",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          date: "2016-05-08",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          date: "2016-05-06",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          date: "2016-05-07",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          date: "2016-05-07",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          date: "2016-05-07",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          date: "2016-05-07",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          date: "2016-05-07",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        },
        {
          date: "2016-05-07",
          name: "王小虎",
          province: "上海",
          city: "普陀区",
          address: "上海市普陀区金沙江路 1518 弄",
          zip: 200333
        }
      ]
    };
  },
  created() {
    this.word();
  },
  mounted() {
    // 评分
    this.drawRate();
    this.drawTest();
    this.drawTest1();
    this.drawComment();
  },
  methods: {
    word() {
      this.axios
        .get("/api/report/reviews", {
          params: {
            latitude: "-112.073843",
            longitude: "33.447999",
            radius: "0.1"
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
          this.defaultWords = words;
        })
        .catch(response => {
          console.log(response);
        });
    },
    drawRate() {
      // 异步更新数据：https://www.echartsjs.com/zh/tutorial.html#%E5%BC%82%E6%AD%A5%E6%95%B0%E6%8D%AE%E5%8A%A0%E8%BD%BD%E5%92%8C%E6%9B%B4%E6%96%B0
      // 属性设置：https://www.echartsjs.com/zh/option.html#title
      const charts = echarts.init(document.getElementById("rate"), "light");
      charts.setOption({
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
    },
    /**
     * test
     */
    drawTest() {
      // 异步更新数据：https://www.echartsjs.com/zh/tutorial.html#%E5%BC%82%E6%AD%A5%E6%95%B0%E6%8D%AE%E5%8A%A0%E8%BD%BD%E5%92%8C%E6%9B%B4%E6%96%B0
      // 属性设置：https://www.echartsjs.com/zh/option.html#title
      const charts = echarts.init(document.getElementById("test"), "light");
      charts.setOption({
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
    },
    /**
     * test1
     */
    drawTest1() {
      // 异步更新数据：https://www.echartsjs.com/zh/tutorial.html#%E5%BC%82%E6%AD%A5%E6%95%B0%E6%8D%AE%E5%8A%A0%E8%BD%BD%E5%92%8C%E6%9B%B4%E6%96%B0
      // 属性设置：https://www.echartsjs.com/zh/option.html#title
      const charts = echarts.init(document.getElementById("test1"), "light");
      charts.setOption({
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
    },
    /**
     * 绘制评分
     */
    drawComment() {
      // https://www.echartsjs.com/zh/tutorial.html#%E5%BC%82%E6%AD%A5%E6%95%B0%E6%8D%AE%E5%8A%A0%E8%BD%BD%E5%92%8C%E6%9B%B4%E6%96%B0
      // 属性设置：https://www.echartsjs.com/zh/option.html#title
      const charts = echarts.init(document.getElementById("comment"), "light");
      var base = +new Date(1968, 9, 3);
      var oneDay = 24 * 3600 * 1000;
      var date = [];

      var data = [Math.random() * 300];

      for (var i = 1; i < 20000; i++) {
        var now = new Date((base += oneDay));
        date.push(
          [now.getFullYear(), now.getMonth() + 1, now.getDate()].join("/")
        );
        data.push(Math.round((Math.random() - 0.5) * 20 + data[i - 1]));
      }

      charts.setOption({
        tooltip: {
          trigger: "axis",
          position: function(pt) {
            return [pt[0], "10%"];
          }
        },
        title: {
          left: "center",
          text: "Area"
        },
        toolbox: {
          feature: {
            dataZoom: {
              yAxisIndex: "none"
            },
            restore: {},
            saveAsImage: {}
          }
        },
        xAxis: {
          type: "category",
          boundaryGap: false,
          data: date
        },
        yAxis: {
          type: "value",
          boundaryGap: [0, "100%"]
        },
        dataZoom: [
          {
            type: "inside",
            start: 0,
            end: 10
          },
          {
            start: 0,
            end: 10,
            handleIcon:
              "M10.7,11.9v-1.3H9.3v1.3c-4.9,0.3-8.8,4.4-8.8,9.4c0,5,3.9,9.1,8.8,9.4v1.3h1.3v-1.3c4.9-0.3,8.8-4.4,8.8-9.4C19.5,16.3,15.6,12.2,10.7,11.9z M13.3,24.4H6.7V23h6.6V24.4z M13.3,19.6H6.7v-1.4h6.6V19.6z",
            handleSize: "80%",
            handleStyle: {
              color: "#fff",
              shadowBlur: 3,
              shadowColor: "rgba(0, 0, 0, 0.6)",
              shadowOffsetX: 2,
              shadowOffsetY: 2
            }
          }
        ],
        series: [
          {
            name: "模拟数据",
            type: "line",
            smooth: true,
            symbol: "none",
            sampling: "average",
            itemStyle: {
              color: "rgb(255, 70, 131)"
            },
            areaStyle: {
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  offset: 0,
                  color: "rgb(255, 158, 68)"
                },
                {
                  offset: 1,
                  color: "rgb(255, 70, 131)"
                }
              ])
            },
            data: data
          }
        ]
      });
    }
  }
};
</script>

<style>
.row {
  margin-bottom: 32px;
}
.wbg {
  background-color: #ffffff;
}
.topdesc {
  height: 108px;
}
.icon {
  float: left;
  font-size: 82px;
  line-height: 115px;
  padding-left: 10px;
}
.detail {
  float: right;
  padding: 10px;
}
.detail .key {
  font-size: 14px;
  font-weight: bold;
}
.detail .value {
  font-size: 32px;
  line-height: 76px;
  font-weight: bolder;
  text-align: center;
}
</style>