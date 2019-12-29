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
            <div class="key">Open</div>
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
    <!-- 犯罪率 -->
    <el-row :gutter="32" class="row">
      <el-col :span="24">
        <Crime :zipcode="zipcode" />
      </el-col>
    </el-row>

    <!-- 标题 -->
    <br />
    <br />
    <br />
    <el-row :gutter="32" class="row">
      <div class="star_type" style="font-size:30px">Features summary of surrounding restaurants</div>
    </el-row>
    <el-row :gutter="32" class="row">
      <div
        class="star_type"
      >There are {{topdata.stars45+topdata.stars03+topdata.close_count}} restaurants in total, and they are divided into three group: star 4-5,star 0-3 and closed for ever</div>
    </el-row>
    <!-- 相关性标题 -->
    <br />
    <el-row :gutter="32" class="row">
      <el-col :span="32">
        <div
          class="star_type"
          style="font-size:20px"
        >Analysis 1: Most important factors to improve prosperity</div>
      </el-col>
    </el-row>
    <el-row :gutter="32" class="row">
      <el-col :span="8">
        <div class="star_type">Restaurants with 4 - 5 stars ({{topdata.stars45}})</div>
      </el-col>
      <el-col :span="8">
        <div class="star_type">Restaurants with 0 - 3 stars ({{topdata.stars03}})</div>
      </el-col>
      <el-col :span="8">
        <div class="star_type">Closed restaurants ({{topdata.close_count}})</div>
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

    <!-- 大字报标题 -->
    <br />
    <br />
    <br />
    <el-row :gutter="32" class="row">
      <el-col :span="24">
        <div
          class="star_type"
          style="font-size:20px"
        >Analysis 2: Most frequency words in users review</div>
      </el-col>
    </el-row>
    <el-row :gutter="32" class="row">
      <el-col :span="8">
        <div class="star_type">Restaurants with 4 - 5 stars ({{topdata.stars45}})</div>
      </el-col>
      <el-col :span="8">
        <div class="star_type">Restaurants with 0 - 3 stars ({{topdata.stars03}})</div>
      </el-col>
      <el-col :span="8">
        <div class="star_type">Closed restaurants ({{topdata.close_count}})</div>
      </el-col>
    </el-row>

    <!-- 聚合大字报 -->
    <el-row :gutter="32" class="row">
      <el-col :span="24">
        <WordCloud
          :latitude="latitude"
          :longitude="longitude"
          :radius="radius"
          :category="category[3]"
        />
      </el-col>
    </el-row>

    <!-- Gender and age -->
    <el-row :gutter="32" class="row">
      <el-col :span="16">
        <PopAge :zipcode="zipcode" />
      </el-col>
    </el-row>

    <!-- 大字报 -->
    <!-- <el-row :gutter="32" class="row">
      <el-col :span="8">
        <WordCloud
          :latitude="latitude"
          :longitude="longitude"
          :radius="radius"
          :category="category[0]+'info'"
        />
      </el-col>
      <el-col :span="8">
        <WordCloud
          :latitude="latitude"
          :longitude="longitude"
          :radius="radius"
          :category="category[1]+'info'"
        />
      </el-col>
      <el-col :span="8">
        <WordCloud
          :latitude="latitude"
          :longitude="longitude"
          :radius="radius"
          :category="category[2]+'info'"
        />
      </el-col>
    </el-row>-->
  </div>
</template>

<script>
import Rate from "./drawRate";
import Comment from "./drawComment";
import WordCloud from "./drawWordCloud";
import Table from "./drawTable";
import Panel from "./drawPanel";
import Crime from "./drawCrime";
import PopAge from "./drawPopAge";

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
    Crime,
    PopAge
  },
  data() {
    return {
      topdata: {
        open_count: 0,
        stars45: 0,
        stars03: 0,
        close_count: 0,
        median_earnings: 0,
        population: 0
      },
      category: ["star45", "star13", "closed", "reviewsfeature"]
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
          this.topdata["stars45"] = response.data["stars45"];
          this.topdata["stars03"] = response.data["stars03"];
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
  font-weight: bold;
  font-size: 18px;
}
.diagram_type {
  writing-mode: vertical-lr;
}
</style>