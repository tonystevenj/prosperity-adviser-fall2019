<template>
  <div style="margin-top: 0px;">
    <el-card class="box-card score_frame clearfix">
      <el-form :inline="true" class="score_txt">
        <el-form-item label="Summary score:">{{ score }}</el-form-item>
      </el-form>
    </el-card>
    <div class="block" style="margin-top: 20px;">
      <span class="demonstration">Population density</span>
      <el-slider class="slider" v-model="percent.population" @input="calculate"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Median earnings</span>
      <el-slider class="slider" v-model="percent.earnings" @input="calculate"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Park density</span>
      <el-slider class="slider" v-model="percent.park" @input="calculate"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">School density</span>
      <el-slider class="slider" v-model="percent.school" @input="calculate"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Hospital density</span>
      <el-slider class="slider" v-model="percent.hospital" @input="calculate"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Light rail density</span>
      <el-slider class="slider" v-model="percent.rail" @input="calculate"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Aourist attraction density</span>
      <el-slider class="slider" v-model="percent.pride" @input="calculate"></el-slider>
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
      data: {},
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
        .get("/api/report/score_data", {
          params: {
            latitude: this.latitude,
            longitude: this.longitude,
            radius: this.radius,
            zipcode: this.zipcode
          }
        })
        .then(response => {
          this.data = response.data;
          this.calculate();
          this.loading = false;
        })
        .catch(response => {
          console.log(response);
        });
    },
    calculate() {
      let result = 0;
      let area_size = Math.PI * this.radius * this.radius;
      // convert 7 percentage into 100% in total:
      let sum =
        this.percent.population +
        this.percent.earnings +
        this.percent.park +
        this.percent.school +
        this.percent.pride +
        this.percent.hospital +
        this.percent.rail;

      let population_percentage = this.percent.population / sum;
      let earnings_percentage = this.percent.earnings / sum;
      let park_percentage = this.percent.park / sum;
      let school_percentage = this.percent.school / sum;
      let pride_percentage = this.percent.pride / sum;
      let hospital_percentage = this.percent.hospital / sum;
      let rail_percentage = this.percent.rail / sum;

      result +=
        population_percentage *
        this.calculateScore(
          this.data["population"]["sum"] / area_size,
          this.data["population"]["max"]
        );

      result +=
        earnings_percentage *
        this.calculateScore(
          this.data["salary"]["sum"] / area_size,
          this.data["salary"]["max"]
        );

      result +=
        park_percentage *
        this.calculateScore(
          this.data["park"]["sum"] / area_size,
          this.data["park"]["max"]
        );

      result +=
        park_percentage *
        this.calculateScore(
          this.data["park"]["sum"] / area_size,
          this.data["park"]["max"]
        );

      result +=
        school_percentage *
        this.calculateScore(
          this.data["school"]["sum"] / area_size,
          this.data["school"]["max"]
        );

      result +=
        pride_percentage *
        this.calculateScore(
          this.data["pride"]["sum"] / area_size,
          this.data["pride"]["max"]
        );

      result +=
        hospital_percentage *
        this.calculateScore(
          this.data["hospital"]["sum"] / area_size,
          this.data["hospital"]["max"]
        );

      result +=
        rail_percentage *
        this.calculateScore(
          this.data["rail"]["sum"] / area_size,
          this.data["rail"]["max"]
        );

      this.score = (result * 100).toFixed(2);
    },
    calculateScore(current, max) {
      if (current > max) {
        return 1;
      }
      return current / max;
    },
    request_old() {
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
