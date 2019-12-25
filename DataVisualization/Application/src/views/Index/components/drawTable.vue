<template>
  <el-tabs v-model="activeName">
    <el-tab-pane label="Business" name="business">
      <el-table
        :data="businessData"
        style="width: 100%"
        height="400"
        v-loading="loading"
        empty-text="No data."
      >
        <el-table-column type="index" width="50"></el-table-column>
        <el-table-column prop="name" label="Name" width="200"></el-table-column>
        <el-table-column prop="distance" label="Distance" width="120"></el-table-column>
        <el-table-column prop="food_type" label="Food Type" width="260"></el-table-column>
      </el-table>
    </el-tab-pane>
    <el-tab-pane label="Park" name="park">
      <el-table
        :data="parkData"
        style="width: 100%"
        height="400"
        v-loading="loading"
        empty-text="No data."
      >
        <el-table-column type="index" width="50"></el-table-column>
        <el-table-column prop="name" label="Name" width="200"></el-table-column>
        <el-table-column prop="distance" label="Distance" width="120"></el-table-column>
        <el-table-column prop="adress" label="Address" width="260"></el-table-column>
      </el-table>
    </el-tab-pane>
    <el-tab-pane label="School" name="school">
      <el-table
        :data="schoolData"
        style="width: 100%"
        height="400"
        v-loading="loading"
        empty-text="No data."
      >
        <el-table-column type="index" width="50"></el-table-column>
        <el-table-column prop="school name" label="Name" width="200"></el-table-column>
        <el-table-column prop="distance" label="Distance" width="120"></el-table-column>
        <el-table-column prop="address" label="Address" width="260"></el-table-column>
      </el-table>
    </el-tab-pane>
    <el-tab-pane label="Tourist Attraction" name="pride">
      <el-table
        :data="prideData"
        style="width: 100%"
        height="400"
        v-loading="loading"
        empty-text="No data."
      >
        <el-table-column type="index" width="50"></el-table-column>
        <el-table-column prop="place_name" label="Name" width="200"></el-table-column>
        <el-table-column prop="distance" label="Distance" width="120"></el-table-column>
        <el-table-column prop="address_" label="Address" width="260"></el-table-column>
      </el-table>
    </el-tab-pane>
    <el-tab-pane label="Light rail" name="rail">
      <el-table
        :data="railData"
        style="width: 100%"
        height="400"
        v-loading="loading"
        empty-text="No data."
      >
        <el-table-column type="index" width="50"></el-table-column>
        <el-table-column prop="location" label="Name" width="420"></el-table-column>
        <el-table-column prop="distance" label="Distance" width="120"></el-table-column>
      </el-table>
    </el-tab-pane>
  </el-tabs>
</template>

<script>
export default {
  name: "Table",
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
  components: {},
  data() {
    return {
      activeName: "business",
      businessData: [],
      parkData: [],
      schoolData: [],
      prideData: [],
      railData: [],
      loading: true
    };
  },
  mounted() {
    this.request();
  },
  methods: {
    request() {
      this.loading = true;
      this.axios
        .get("/api/report/table", {
          params: {
            latitude: this.latitude,
            longitude: this.longitude,
            radius: this.radius
          }
        })
        .then(response => {
          this.businessData = response.data["business"];
          this.parkData = response.data["park"];
          this.schoolData = response.data["school"];
          this.prideData = response.data["pride"];
          this.railData = response.data["rail"];
          this.loading = false;
        })
        .catch(response => {
          this.loading = false;
          console.log(response);
        });
    }
  }
};
</script>