<template>



      <!-- swiper -->
      <swiper :options="swiperOption">

       <swiper-slide>
       <el-card :body-style="{ padding: '0px' }">
        <img src="../../../../static/databases.png" class="img-xys">
        <div style="padding: 10px;">
          <strong>Comprehensive Databases</strong>
          <div class="bottom">Based on Yelp, census org and other credible datasets.</div>
        </div>
        </el-card>
        </swiper-slide>


       <swiper-slide>
       <el-card :body-style="{ padding: '0px' }">
        <img src="../../../../static/review.png" class="img-xys">
        <div style="padding: 10px;">
          <strong>Review’s Key Words</strong>
          <div class="bottom">Visualized high-frequency key words of targeted business circle.</div>
        </div>
        </el-card>
        </swiper-slide>


        <swiper-slide>
       <el-card :body-style="{ padding: '0px' }">
        <img src="../../../../static/facilities.png" class="img-xys">
        <div style="padding: 10px;">
          <strong>Communal facilities</strong>
          <div class="bottom">Popular communal facilities in the targeted area.</div>
        </div>
        </el-card>
        </swiper-slide>

       <swiper-slide>
       <el-card :body-style="{ padding: '0px' }">
        <img src="../../../../static/competitors.png" class="img-xys">
        <div style="padding: 10px;">
          <strong>Nearby Competitors</strong>
          <div class="bottom">Specific information of selected nearby restaurants.</div>
        </div>
        </el-card>
        </swiper-slide>

        <swiper-slide>
       <el-card :body-style="{ padding: '0px' }">
        <img src="../../../../static/people.png" class="img-xys">
        <div style="padding: 10px;">
          <strong>Potential Customers</strong>
          <div class="bottom">Authoritative population data of selected area.</div>
        </div>
        </el-card>
        </swiper-slide>

        <swiper-slide>
       <el-card :body-style="{ padding: '0px' }">
        <img src="../../../../static/income.png" class="img-xys">
        <div style="padding: 10px;">
          <strong>Consumption Ability</strong>
          <div class="bottom">Reliable income data of selected area.</div>
        </div>
        </el-card>
        </swiper-slide>

        <swiper-slide>
       <el-card :body-style="{ padding: '0px' }">
        <img src="../../../../static/store.png" class="img-xys">
        <div style="padding: 10px;">
          <strong>Possible Risks</strong>
          <div class="bottom">Nearby closed restaurants’ yelp review key word.</div>
        </div>
        </el-card>
        </swiper-slide>


        <div class="swiper-pagination" slot="pagination"></div>
      </swiper>

</template>

<script>
  import { swiper, swiperSlide } from 'vue-awesome-swiper'
   import './css/swiper.css'

  import 'semantic-ui-css/semantic.min.css';


  export default {
    name: "coverflow",
    components: {
    swiper,
    swiperSlide
    },

    data() {
      return {
        swiperOption: {
          effect: 'coverflow',
          grabCursor: true,
          centeredSlides: true,
          slidesPerView: 'auto',
          coverflowEffect: {
            rotate: 50,
            stretch: 0,
            depth: 100,
            modifier: 1,
            slideShadows : true
          },
          pagination: {
            el: '.swiper-pagination'
          }
        }
      }
    }
  }
</script>


<style scoped>


.img-xys {
  display: inline-block;
  height: auto;
  max-width: 100%;

}


 .bottom {
    margin-top: 10px;
    line-height: 12px;
    margin-bottom: 10px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }

  .clearfix:after {
      clear: both
  }


  .swiper-inner {
    width: 100%;
    height: 400px;
    padding-top: 50px;
    padding-bottom: 50px;
  }
  .swiper-slide {
    background-position: center;
    background-size: cover;

    width: 235px;
    height: 323px;

  }
</style>
