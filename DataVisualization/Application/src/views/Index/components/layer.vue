<template>
  <div>
    <!-- 顶部4个栏 -->
    <el-row :gutter="32" class="row">
      <el-col :span="6">
        <div class="topdesc wbg">
          <div class="icon">
            <i class="el-icon-s-shop" style="color: #6ac6c5;"></i>
          </div>
          <div class="detail">
            <div class="key">Total</div>
            <div class="value">{{ topdata['open_count'] }}</div>
          </div>
        </div>
      </el-col>
      <el-col :span="6">
        <div class="topdesc wbg">
          <div class="icon">
            <i class="el-icon-s-shop" style="color: #f4516c;"></i>
          </div>
          <div class="detail">
            <div class="key">Closed</div>
            <div class="value">{{ topdata['close_count'] }}</div>
          </div>
        </div>
      </el-col>
      <el-col :span="6">
        <div class="topdesc wbg">
          <div class="icon">
            <i class="el-icon-bank-card" style="color: #E6A23C;"></i>
          </div>
          <div class="detail">
            <div class="key">Median earnings</div>
            <div class="value">${{ topdata['median_earnings'] }}</div>
          </div>
        </div>
      </el-col>
      <el-col :span="6">
        <div class="topdesc wbg">
          <div class="icon">
            <i class="el-icon-user" style="color: #36a3f7;"></i>
          </div>
          <div class="detail">
            <div class="key">Population</div>
            <div class="value">{{ topdata['population'] }}</div>
          </div>
        </div>
      </el-col>
    </el-row>
    <!-- table & 控制面板 -->
    <el-row :gutter="32" class="row">
      <el-col :span="12">
        <Panel :latitude="latitude" :longitude="longitude" :radius="radius" :zipcode="zipcode" />
      </el-col>
      <el-col :span="12">
        <Table :latitude="latitude" :longitude="longitude" :radius="radius" />
      </el-col>
    </el-row>
    <!-- 标题 -->
    <el-row :gutter="32" class="row">
      <el-col :span="8">
        <span class="star_type">4 - 5 stars</span>
      </el-col>
      <el-col :span="8">
        <span class="star_type">0 - 3 stars</span>
      </el-col>
      <el-col :span="8">
        <span class="star_type">Closed</span>
      </el-col>
    </el-row>
    <!-- 评分相关性 -->
    <el-row :gutter="32" class="row">
      <el-col :span="8">
        <Rate :latitude="latitude" :longitude="longitude" :radius="radius" :category="category[0]" />
      </el-col>
      <el-col :span="8">
        <Rate :latitude="latitude" :longitude="longitude" :radius="radius" :category="category[1]" />
      </el-col>
      <el-col :span="8">
        <Rate :latitude="latitude" :longitude="longitude" :radius="radius" :category="category[2]" />
      </el-col>
    </el-row>
    <!-- 大字报 -->
    <el-row :gutter="32" class="row">
      <el-col :span="8">
        <WordCloud
          :latitude="latitude"
          :longitude="longitude"
          :radius="radius"
          :category="category[0]"
        />
      </el-col>
      <el-col :span="8">
        <WordCloud
          :latitude="latitude"
          :longitude="longitude"
          :radius="radius"
          :category="category[1]"
        />
      </el-col>
      <el-col :span="8">
        <WordCloud
          :latitude="latitude"
          :longitude="longitude"
          :radius="radius"
          :category="category[2]"
        />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Rate from "./drawRate";
import Comment from "./drawComment";
import WordCloud from "./drawWordCloud";
import Table from "./drawTable";
import Panel from "./drawPanel";

export default {
  name: "Layer",
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
    zipcode: {
      type: Number,
      required: true
    }
  },
  components: {
    Rate,
    Comment,
    WordCloud,
    Table,
    Panel,
  },
  data() {
    return {
      topdata: {
        open_count: 0,
        close_count: 0,
        median_earnings: 0,
        population: 0
      },
      category: ["star45", "star13", "closed"]
    };
  },
  created() {},
  mounted() {
    this.request();
  },
  methods: {
    request() {
      // api获取真实数据进行替换
      this.axios
        .get("/api/report/business", {
          params: {
            latitude: this.latitude,
            longitude: this.longitude,
            radius: this.radius,
            zipcode: this.zipcode
          }
        })
        .then(response => {
          this.topdata["open_count"] = response.data["open_count"];
          this.topdata["close_count"] = response.data["close_count"];
          this.topdata["median_earnings"] = response.data["median_earnings"];
          this.topdata["population"] = response.data["population"];
        })
        .catch(response => {
          console.log(response);
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
.star_type {
  text-align: center;
  font-size: 18px;
}
.diagram_type {
  writing-mode: vertical-lr;
}
</style>