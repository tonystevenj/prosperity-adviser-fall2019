<template>
  <el-container direction="vertical">
    <Header />
    <Banner />
    <el-main>
      <el-card
        class="box-card gmap-box"
        v-loading="loading"
        element-loading-background="rgba(255, 255, 255, 0.5)"
      >
        <div slot="header" class="clearfix">
          <span>Brief Inroduction</span>
        </div>
        <div class="text item">
          <div class="clearfix">
            This is a project which can help you decide where to open a restaurant and how to do well if you have one.(Temporarily, our data is limited in Phoenix city)
            Just click where you potentially want a restaurant, there will be a report to give you surrounding information and analysis of this area based on Yelp dataset.
            See more details about algorithms, please go to <router-link to="/introduction"><b>INTRODUCTION</b></router-link>.
          </div>
        </div>
      </el-card>

      <el-card
        class="box-card gmap-box"
        v-loading="loading"
        element-loading-background="rgba(255, 255, 255, 0.5)"
      >
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
                v-model="mapform.radius_tmp"
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

    </el-main>

    <Footer />

    <el-dialog
      class="report"
      title="Report"
      radius="10"
      :visible.sync="showReport"
      width="80%"
      v-if="showReport"
      :close-on-click-modal="false"
      :close-on-press-escape="false"
    >
      <!-- :before-close="handleClose" -->
      <Layer
        :longitude="mapform.longitude"
        :latitude="mapform.latitude"
        :radius="mapform.radius"
        :zipcode="mapform.zipcode"
      />
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="showReport = false">Close</el-button>
      </span>
    </el-dialog>
  </el-container>
</template>

<script>
import Header from "../components/Header";
import Banner from "../components/Banner";
import Footer from "../components/Footer";
import mapstyle from "@/utils/mapstyles/mapstyle_mb.js";
import Layer from "./components/layer";

const config = require("../../../config");

var mymarkers = [];

var shapes = [];

export default {
  name: "Index",
  components: {
    Header,
    Banner,
    Footer,
    Layer
  },
  data() {
    return {
      milemarks: {
        1: "1",
        15: "15",
        30: "30"
      },
      mapform: {
        longitude: -112.05709983455688,
        latitude: 33.451329291863644,
        radius: 1,
        radius_tmp: 1,
        zipcode: 85006,
        place: "",
        searchbox: ""
      },
      gmap: {},
      activeIndex: "1",
      activeIndex2: "1",
      loading: false,
      showReport: false,
      usBounds: {
        north: 49.773477,
        south: 23.386988,
        west: -125.770392,
        east: -62.366074
      },
      searchbox: null,
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
        // styles: mapstyle,
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
      process.env.NODE_ENV === "production";
      script.src = "./static/geo_jsonp.js";
      document.getElementsByTagName("head")[0].appendChild(script);
    },
    initSearchBox() {
      // https://developers-dot-devsite-v2-prod.appspot.com/maps/documentation/javascript/examples/places-searchbox?hl=zh-CN
      var input = document.getElementById("searchbox");
      var button = document.getElementById("calculate");
      var scope = document.getElementById("scope");
      this.searchBox = new google.maps.places.SearchBox(input);
      this.gmap.controls[google.maps.ControlPosition.TOP_CENTER].push(input);
      this.gmap.controls[google.maps.ControlPosition.TOP_CENTER].push(button);
      this.gmap.controls[google.maps.ControlPosition.LEFT_CENTER].push(scope);

      this.gmap.addListener("bounds_changed", () => {
        this.searchBox.setBounds(this.gmap.getBounds());
      });

      // Listen for the event fired when the user selects a prediction and retrieve
      // more details for that place.
      this.searchBox.addListener("places_changed", this.searchMap);
    },
    searchMap() {
      {
        this.loading = true;
        // this.mapform.latitude = e.latLng.lat();
        // this.mapform.longitude = e.latLng.lng();

        // let e = new google.maps.LatLng({lat: this.mapform.latitude, lng: this.mapform.longitude});
        // this.sitePin(e);

        // setTimeout(() => {
        //   this.loading = false;
        //   this.showReport = true;
        // }, 1000);
        var markers = [];
        var places = this.searchBox.getPlaces();

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
          this.sitePin(place.geometry.location);
          setTimeout(() => {
            this.loading = false;
            this.showReport = true;
          }, 1000);
          return;
          // var icon = {
          //   url: place.icon,
          //   size: new google.maps.Size(71, 71),
          //   origin: new google.maps.Point(0, 0),
          //   anchor: new google.maps.Point(17, 34),
          //   scaledSize: new google.maps.Size(25, 25)
          // };

          // Create a marker for each place.
          // markers.push(
          //   new google.maps.Marker({
          //     map: this.gmap,
          //     icon: icon,
          //     title: place.name,
          //     position: place.geometry.location
          //   })
          // );

          // if (place.geometry.viewport) {
          //   // Only geocodes have viewport.
          //   bounds.union(place.geometry.viewport);
          // } else {
          //   bounds.extend(place.geometry.location);
          // }
        });
        // this.gmap.fitBounds(bounds);
      }
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
          this.gmap.setZoom(10);
          this.gmap.setCenter(marker.getPosition());
        });

        // add add pin event
        // https://developers-dot-devsite-v2-prod.appspot.com/maps/documentation/javascript/examples/event-arguments?hl=zh-CN
        this.gmap.addListener("click", this.onclickmap);

        // todo: heat map
        // https://developers-dot-devsite-v2-prod.appspot.com/maps/documentation/javascript/examples/layer-heatmap?hl=zh-CN

        return marker;
      });

      // https://developers.google.com/maps/documentation/javascript/marker-clustering?hl=zh-CN
      var markerCluster = new MarkerClusterer(this.gmap, markers);
    },
    onclickmap(e) {
      this.loading = true;
      // this.mapform.latitude = e.latLng.lat();
      // this.mapform.longitude = e.latLng.lng();

      this.sitePin(e.latLng);

      setTimeout(() => {
        this.loading = false;
        this.showReport = true;
      }, 1000);

      // get zipcode
      // https://stackoverflow.com/questions/6764917/latitude-and-longitude-can-find-zip-code
      // var geocoder = new google.maps.Geocoder();
      // geocoder.geocode({ latLng: e.latLng }, (results, status) => {
      //   if (status != "OK") {
      //     this.$message.error("Network error, please try again!");
      //     return;
      //   }
      //   for (var i in results[0]["address_components"]) {
      //     if (
      //       results[0]["address_components"][i]["types"].indexOf(
      //         "postal_code"
      //       ) > -1
      //     ) {
      //       this.mapform.zipcode = Number(
      //         results[0]["address_components"][i]["long_name"]
      //       );
      //       setTimeout(() => {
      //         this.loading = false;
      //         this.showReport = true;
      //       }, 1000);

      //     }
      //   }
      // });
    },
    sitePin(latLng) {
      //clear others
      for (var i = 0; i < mymarkers.length; i++) {
        mymarkers[i].setMap(null);
      }

      for (var i = 0; i < shapes.length; i++) {
        shapes[i].setMap(null);
      }

      var marker = new google.maps.Marker({
        map: this.gmap,
        position: latLng,
        icon: this.centerMarker
      });

      mymarkers.push(marker);

      // Shapes
      // https://developers-dot-devsite-v2-prod.appspot.com/maps/documentation/javascript/shapes?hl=zh-CN
      var cityCircle = new google.maps.Circle({
        map: this.gmap,
        strokeColor: "#FF0000",
        strokeOpacity: 0.6,
        strokeWeight: 2,
        fillColor: "#FF0000",
        fillOpacity: 0.2,
        center: latLng,
        radius: this.mapform.radius_tmp * 1609.344
      });

      cityCircle.addListener("click", this.onclickmap);
      shapes.push(cityCircle);
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
.el-dialog {
  border-radius: 20;
  background-color: #f0f1f4 !important;
}
.el-dialog__header,
.el-dialog__footer {
  background-color: #ffffff;
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
