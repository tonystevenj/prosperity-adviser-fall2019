<template>
  <div style="margin-top: 0px;">
    <el-card class="box-card score_frame clearfix">
      <el-form :inline="true" class="score_txt">
        <el-form-item label="Summary score:">{{ score }}</el-form-item>
      </el-form>
    </el-card>
    <div class="block" style="margin-top: 20px;">
      <span class="demonstration">Population density weighting factor</span>
      <el-slider class="slider" v-model="percent.population" @input="calculate"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Median earnings weighting factor</span>
      <el-slider class="slider" v-model="percent.earnings" @input="calculate"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Park density weighting factor</span>
      <el-slider class="slider" v-model="percent.park" @input="calculate"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">School density weighting factor</span>
      <el-slider class="slider" v-model="percent.school" @input="calculate"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Hospital density weighting factor</span>
      <el-slider class="slider" v-model="percent.hospital" @input="calculate"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Light rail density weighting factor</span>
      <el-slider class="slider" v-model="percent.rail" @input="calculate"></el-slider>
    </div>
    <div class="block">
      <span class="demonstration">Aourist attraction density weighting factor</span>
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
      data: {
        park: {
          sum: 0,
          max: 1.201385924
        },
        school: {
          sum: 0,
          max: 5.815748132
        },
        pride: {
          sum: 0,
          max: 2.31007695
        },
        hospital: {
          sum: 0,
          max: 0.340240332
        },
        rail: {
          sum: 0,
          max: 0.373340781
        },
        salary: {
          sum: 0,
          max: 61968
        },
        population: {
          sum: 0,
          max: 70008
        }
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
      this.data = {"park": {"sum": 13, "max": 1.201385924}, "school": {"sum": 10, "max": 5.815748132}, "pride": {"sum": 6, "max": 2.31007695}, "hospital": {"sum": 2, "max": 0.340240332}, "rail": {"sum": 3, "max": 0.373340781}, "salary": {"sum": 21183.0, "max": 61968}, "population": {"sum": 25097.0, "max": 70008}};
      this.calculate();
      this.loading = false;
      // this.axios
      //   .get("/api/report/score_data", {
      //     params: {
      //       latitude: this.latitude,
      //       longitude: this.longitude,
      //       radius: this.radius,
      //       zipcode: this.zipcode
      //     }
      //   })
      //   .then(response => {
      //     this.data = response.data;
      //     this.calculate();
      //     this.loading = false;
      //   })
      //   .catch(response => {
      //     console.log(response);
      //   });
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
        (this.data["population"]["sum"] / this.data["population"]["max"]);

      result +=
        earnings_percentage *
        (this.data["salary"]["sum"] / this.data["salary"]["max"]);

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
</style>
