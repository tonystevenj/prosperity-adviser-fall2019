<template>
  <el-container>
    <el-header>
      <el-menu
        :default-active="activeIndex"
        mode="horizontal"
        @select="handleSelect"
        background-color="#f6f6f6"
      >
        <el-menu-item>
          <el-menu-item class="logo">AFRSS</el-menu-item>
        </el-menu-item>
        <el-menu-item index="1">
          <i class="el-icon-house" style="width:65%;">HOME</i>
        </el-menu-item>
        <el-submenu index="2">
          <template slot="title">
            <i class="el-icon-box" style="width:65px;">UTILS</i>
          </template>
          <el-menu-item index="2-1">TOOL 1</el-menu-item>
          <el-menu-item index="2-2">TOOL 3</el-menu-item>
          <el-menu-item index="2-3">TOOL 3</el-menu-item>
          <el-submenu index="2-4">
            <template slot="title">MORE</template>
            <el-menu-item index="2-4-1">TOOL 4</el-menu-item>
            <el-menu-item index="2-4-2">TOOL 5</el-menu-item>
            <el-menu-item index="2-4-3">TOOL 6</el-menu-item>
          </el-submenu>
        </el-submenu>
        <el-menu-item index="3">
          <i class="el-icon-discover" style="width:65%;">GUIDE</i>
        </el-menu-item>
        <el-menu-item index="4">
          <i class="el-icon-postcard" style="width:65%;">ABOUT</i>
        </el-menu-item>
        <!-- <el-menu-item index="4">
          <a href="https://www.ele.me" target="_blank">订单管理</a>
        </el-menu-item>-->
      </el-menu>
    </el-header>
    <div class="banner">
      <div class="banner_content">
        <el-card class="box-card">
          <div slot="header" class="clearfix test">
            <span style="font-weight: bold;">Assistant for Restaurant Site Selection</span>
          </div>
          <div>Content</div>
        </el-card>
      </div>
    </div>
    <el-main>
      <el-card class="box-card gmap-box">
        <div slot="header" class="clearfix">
          <span>Describe</span>
        </div>
        <div>Content Content Content Content Content Content Content Content Content Content Content Content</div>
      </el-card>
      <el-card class="box-card gmap-box">
        <div slot="header" class="clearfix">
          <span>Dashboard</span>
        </div>
        <div class="text item">
          <div class="clearfix">
            <div style="display: none">
              <el-input id="searchbox" v-model="mapform.searchbox" placeholder="Enter a location"></el-input>
              <el-button id="calculate" type="danger" icon="el-icon-s-data">Calculate</el-button>
              <el-slider
                label="Scope"
                id="scope"
                v-model="mapform.scope"
                vertical
                :min="1"
                :max="30"
                :step="1"
                :marks="milemarks"
                height="500px"
              ></el-slider>
            </div>
            <div id="gmap"></div>
          </div>
        </div>
      </el-card>
      <el-card class="box-card gmap-box">
        <div slot="header" class="clearfix">
          <span>Describe</span>
        </div>
        <div>Content Content Content Content Content Content Content Content Content Content Content Content</div>
      </el-card>
    </el-main>
    <el-footer height="100px">
      <div class="footer_link">
        <span>
          <el-link type="info" style="margin-left:10px;">Privacy Policy</el-link>
          <el-link type="info" style="margin-left:10px;">Terms of Use</el-link>
          <el-link type="info" style="margin-left:10px;">About</el-link>
          <p style="color: #a6a9ad; font-weight: bold; font-size: 13px;">@2019</p>
        </span>
      </div>
    </el-footer>

    <el-dialog title="Report" :visible.sync="showReport" width="30%" :before-close="handleClose">
      <span>This is a Report</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="showReport = false">Cancel</el-button>
        <el-button type="primary" @click="showReport = false">Confirm</el-button>
      </span>
    </el-dialog>
  </el-container>
</template>


<script>
import mapstyle from "@/utils/mapstyles/mapstyle_mb.js";
const config = require('../../../config')

export default {
  name: "Index",
  data() {
    return {
      milemarks: {
        1: "1",
        15: "15",
        30: "30"
      },
      mapform: {
        scope: 5,
        place: "",
        searchbox: ""
      },
      gmap: {},
      activeIndex: "1",
      activeIndex2: "1",
      showReport: false,
      usBounds: {
        north: 49.773477,
        south: 23.386988,
        west: -125.770392,
        east: -62.366074
      },
      centerMarker:
        "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png"
    };
  },
  mounted() {
    this.initMap();
    this.initSearchBox();
    window.gmap_callback = this.dataHandle;
  },
  methods: {
    initMap() {
      /**
       * More map styles
       * https://snazzymaps.com/style/8097/wy
       */
      this.gmap = new google.maps.Map(document.getElementById("gmap"), {
        zoom: 10,
        mapTypeControl: true,
        zoomControl: true,
        scaleControl: true,
        streetViewControl: true,
        fullscreenControl: true,
        gestureHandling: "auto",
        center: new google.maps.LatLng(33.450164, -112.074615),
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        // mapTypeIds: [
        //   google.maps.MapTypeId.ROADMAP,
        //   google.maps.MapTypeId.SATELLITE,
        //   google.maps.MapTypeId.HYBRID,
        //   google.maps.MapTypeId.TERRAIN,
        //   google.maps.MapTypeId.STYLED_MAP
        // ],
        styles: mapstyle,
        // Restricting Map Bounds
        // https://developers-dot-devsite-v2-prod.appspot.com/maps/documentation/javascript/examples/control-bounds-restriction?hl=zh-CN
        restriction: {
          latLngBounds: this.usBounds,
          strictBounds: false
        }
      });

      // Create a <script> tag and set the USGS URL as the source.
      var script = document.createElement("script");
      // This example uses a local copy of the GeoJSON stored at
      // script.src = "https://afrsscdn.hopeness.net/static/all_geo_jsonp.js";
      process.env.NODE_ENV === 'production'
      script.src = "/static/geo_jsonp.js";
      document.getElementsByTagName("head")[0].appendChild(script);
    },
    initSearchBox() {
      // https://developers-dot-devsite-v2-prod.appspot.com/maps/documentation/javascript/examples/places-searchbox?hl=zh-CN
      var input = document.getElementById("searchbox");
      var button = document.getElementById("calculate");
      var scope = document.getElementById("scope");
      var searchBox = new google.maps.places.SearchBox(input);
      this.gmap.controls[google.maps.ControlPosition.TOP_CENTER].push(input);
      this.gmap.controls[google.maps.ControlPosition.TOP_CENTER].push(button);
      this.gmap.controls[google.maps.ControlPosition.LEFT_CENTER].push(scope);

      this.gmap.addListener("bounds_changed", () => {
        searchBox.setBounds(this.gmap.getBounds());
      });

      var markers = [];
      // Listen for the event fired when the user selects a prediction and retrieve
      // more details for that place.
      searchBox.addListener("places_changed", () => {
        var places = searchBox.getPlaces();

        if (places.length == 0) {
          return;
        }

        // Clear out the old markers.
        markers.forEach(function(marker) {
          marker.setMap(null);
        });
        markers = [];

        // For each place, get the icon, name and location.
        var bounds = new google.maps.LatLngBounds();
        places.forEach(place => {
          if (!place.geometry) {
            console.log("Returned place contains no geometry");
            return;
          }
          var icon = {
            url: place.icon,
            size: new google.maps.Size(71, 71),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(17, 34),
            scaledSize: new google.maps.Size(25, 25)
          };

          // Create a marker for each place.
          markers.push(
            new google.maps.Marker({
              map: this.gmap,
              icon: icon,
              title: place.name,
              position: place.geometry.location
            })
          );

          if (place.geometry.viewport) {
            // Only geocodes have viewport.
            bounds.union(place.geometry.viewport);
          } else {
            bounds.extend(place.geometry.location);
          }
        });
        this.gmap.fitBounds(bounds);
      });
    },
    dataHandle(results) {
      var markers = [];
      results.map((location, i) => {
        // latitude and longitude
        var latLng = new google.maps.LatLng(
          location["latitude"],
          location["longitude"]
        );

        // marker
        // https://developers.google.com/maps/documentation/javascript/markers?hl=zh-CN
        var marker = new google.maps.Marker({
          map: this.gmap,
          title: "testtest",
          position: latLng
        });

        // Marker Animations
        // https://developers-dot-devsite-v2-prod.appspot.com/maps/documentation/javascript/examples/marker-animations?hl=zh-CN
        marker.addListener("click", () => {
          if (marker.getAnimation() !== null) {
            marker.setAnimation(null);
          } else {
            marker.setAnimation(google.maps.Animation.BOUNCE);
          }
        });

        // add click event
        // https://developers.google.com/maps/documentation/javascript/events?hl=zh-CN
        marker.addListener("click", () => {
          this.showReport = true;
          this.gmap.setZoom(10);
          this.gmap.setCenter(marker.getPosition());
        });

        // add add pin event
        // https://developers-dot-devsite-v2-prod.appspot.com/maps/documentation/javascript/examples/event-arguments?hl=zh-CN
        this.gmap.addListener("click", e => {
          this.sitePin(e.latLng);
        });

        // todo: heat map
        // https://developers-dot-devsite-v2-prod.appspot.com/maps/documentation/javascript/examples/layer-heatmap?hl=zh-CN

        return marker;
      });

      // https://developers.google.com/maps/documentation/javascript/marker-clustering?hl=zh-CN
      var markerCluster = new MarkerClusterer(this.gmap, markers);
    },
    sitePin(latLng) {
      var marker = new google.maps.Marker({
        map: this.gmap,
        position: latLng,
        icon: this.centerMarker
      });

      // Shapes
      // https://developers-dot-devsite-v2-prod.appspot.com/maps/documentation/javascript/shapes?hl=zh-CN
      var cityCircle = new google.maps.Circle({
        map: this.gmap,
        strokeColor: "#FF0000",
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: "#FF0000",
        fillOpacity: 0.35,
        center: latLng,
        radius: this.mapform.scope * 1609.344
      });
    },
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    onSubmit() {
      console.log("submit!");
    },
    handleClose(done) {
      this.$confirm("Confirm closed？")
        .then(_ => {
          done();
        })
        .catch(_ => {});
    }
  }
};
</script>


<style>
.banner_content .el-card__header {
  border-bottom-color: rgba(0, 0, 0, 0.6);
}
#searchbox {
  width: 50%;
  min-width: 400px;
  margin-top: 10px;
  margin-right: 0;
  border-right: none;
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
}
#calculate {
  margin-top: 10px;
  margin-left: 0;
  border-left: none;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}
#scope {
  margin-left: 5px;
}
#scope .el-slider__runway {
  background-color: rgba(0, 0, 0, 0.5);
}
#scope .el-slider__button {
  border: 2px solid rgba(255, 0, 0, 0.8);
}
#scope .el-slider__bar {
  background-color: rgba(255, 0, 0, 0.6);
}
#scope .el-slider__marks-text {
  font-weight: bold;
  color: #ffffff;
  text-shadow: 1px 1px 3px #000000;
}
#scope .el-slider__stop {
  background-color: #333333;
}
</style>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-header {
  padding: 0;
  box-shadow: 0 12px 12px 0 rgba(0, 0, 0, 1);
}
.el-footer {
  background-color: rgb(240, 240, 240);
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  border-top: 1px solid rgb(228, 228, 228);
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
.el-footer .footer_link {
  margin-top: 20px;
  text-align: center;
}
.menu-height {
  height: 80px;
  line-height: 80px;
}
.logo {
  font-size: 28px;
}
.banner {
  width: 100%;
  height: 400px;
  background: url("/static/banner_1.jpg") no-repeat center top;
  background-size: cover;
  -moz-background-size: 100% 100%;
}
.banner_content {
  float: right;
  width: 400px;
  height: 360px;
  background-color: rgba(0, 0, 0, 0.5);
  border-color: black;
  margin-top: 20px;
  margin-right: 30px;
  border-radius: 8px;
}
.banner_content .box-card {
  background: none;
  border: none;
  margin: 20px;
  color: #dddddd;
  box-shadow: none;
}
.el-card {
  padding: 0px;
}
#gmap {
  min-height: 800px;
  width: 100%;
  border-radius: 8px;
  border: 1px solid #eeeeee;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1) inset;
}
.gmap-box {
  border-radius: 10px;
  padding: 0px;
  margin-bottom: 15px;
}
.el-carousel__item h3 {
  color: #475669;
  font-size: 18px;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>
