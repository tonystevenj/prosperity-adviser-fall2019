<template>
  <div style="margin-top: 0px;">
    <el-card class="box-card score_frame clearfix">
      <el-form :inline="true" class="score_txt">
        <el-form-item label="Summary score:">{{ score }}</el-form-item>
        <el-form-item class="button">
          <el-button type="primary" @click="calculate" :disabled="loading">Calculate</el-button>
        </el-form-item>
      </el-form>
    </el-card>
    <div class="block" style="margin-top: 20px;">
      <span class="demonstration">Population density</span>
      <el-slider class="slider" v-model="percent.population"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Median earnings</span>
      <el-slider class="slider" v-model="percent.earnings"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Park density</span>
      <el-slider class="slider" v-model="percent.park"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">School density</span>
      <el-slider class="slider" v-model="percent.school"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Hospital density</span>
      <el-slider class="slider" v-model="percent.hospital"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Light rail density</span>
      <el-slider class="slider" v-model="percent.rail"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Aourist attraction density</span>
      <el-slider class="slider" v-model="percent.pride"></el-slider>
    </div>
  </div>
</template>

<script>
export default {
  name: "Panel",
  // 接收宿主传过来的值
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
  components: {},
  data() {
    return {
      percent: {
        population: 50,
        earnings: 50,
        park: 50,
        school: 50,
        hospital: 50,
        pride: 50,
        rail: 50
      },
      score: 0,
      loading: false
    };
  },
  mounted() {
    this.request();
  },
  methods: {
    request() {
      this.loading = true;
      this.axios
        .get("/api/report/score", {
          params: {
            latitude: this.latitude,
            longitude: this.longitude,
            radius: this.radius,
            zipcode: this.zipcode,
            population_percentage: this.percent.population / 100,
            salary_percentage: this.percent.earnings / 100,
            park_percentage: this.percent.park / 100,
            school_percentage: this.percent.school / 100,
            pride_percentage: this.percent.pride / 100,
            hospital_percentage: this.percent.hospital / 100,
            rail_percentage: this.percent.rail / 100
          }
        })
        .then(response => {
          this.score = (response.data * 100).toFixed(2);
          this.loading = false;
        })
        .catch(response => {
          console.log(response);
        });
    },
    calculate() {
      this.request();
    }
  }
};
</script>

<style>
.score_txt .el-form-item__label {
  font-size: 30px;
  line-height: 40px;
}
.score_txt .el-form-item__content {
  font-size: 30px;
  font-weight: bold;
  line-height: 40px;
}
.score_txt .button {
  float: right;
}
</style>

<style scoped>
.score_txt {
}
.slider {
}
</style>
