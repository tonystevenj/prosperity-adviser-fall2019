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
        <rate />
      </el-col>
    </el-row>
    <el-row :gutter="32" class="row">
      <el-col :span="8">
        <Test />
      </el-col>
      <el-col :span="8">
        <comment />
      </el-col>
      <el-col :span="8">
        <WordCloud :latitude="latitude" :longitude="longitude" :radius="radius" />
      </el-col>
    </el-row>
    <el-row :gutter="32" class="row">
      <el-col :span="24">
        <WordCloud :latitude="latitude" :longitude="longitude" :radius="radius" />
      </el-col>
    </el-row>
    <el-row :gutter="32" class="row">
      <el-col :span="16">
        <Table />
      </el-col>
      <el-col :span="8">
        <Test />
      </el-col>
    </el-row>
    <el-row :gutter="32" class="row">
      <el-col :span="16">
        <WordCloud :latitude="latitude" :longitude="longitude" :radius="radius" />
      </el-col>
      <el-col :span="8"></el-col>
    </el-row>
  </div>
</template>

<script>
import echarts from "echarts";

import Rate from "./drawRate";
import Comment from "./drawComment";
import WordCloud from "./drawWordCloud";
import Test from "./drawTest";
import Table from "./drawTable";

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
    }
  },
  components: {
    Rate,
    Comment,
    WordCloud,
    Test,
    Table
  },
  data() {
    return {};
  },
  created() {},
  mounted() {},
  methods: {}
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