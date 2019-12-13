<template>
  <el-container direction="vertical">
    <Header />
    <Banner />
    <el-main>
      <el-card class="box-card" element-loading-background="rgba(255, 255, 255, 0.5)">
        <div slot="header" class="clearfix">
          <span>Dashboard</span>
        </div>
        <div class="text item">
          <div class="clearfix">
            <p>
              <img alt="avatar" src="/Users/zhoulinlin/Desktop/daimages/title.jpeg" />
            </p>

            <h1>Introduction</h1>

            <hr />

            <p>
              <em>Our project is called assistant for restaurant site selection (ARSS),a web-based service.</em>
            </p>

            <p>
              <em>The goal of ARSS is to give restaurant owner a report about their businesses’ or their potential business’s local surrounding information and provide a suggestion score based on their customized weight factors.</em>
            </p>

            <p>
              <em>Furthermore, it can give a report that if I want to or already have a restaurant here, what features I should care most to make my restaurant be more popular. Currently, this product is only work in Phoenix, Arizona.</em>
            </p>

            <h1>Motivation</h1>

            <hr />

            <p>
              ​
              <em>The idea was inspired by yelp dataset challenge’s winning projects. After reviewing these brilliant projects, our team member noticed yelp’s dataset is very versatile. It contains a variety of very important data about restaurants.</em>
              ​
              ​
              ​
              <em>There are total number of 59387 restaurants’ core information that distributed in 10 different metropolitan areas. After we found some other related supporting datasets, we believed we could use yelp’s dataset to create a very useful project.</em>
            </p>

            <h1>Aims</h1>

            <hr />

            <p>
              ​
              <em>As restaurant owner, it is important to know the surrounding information such as population and costumer’s interests. Although, the restaurant&#39;s objective condition is the decisive factor of success, knowing the surrounding competitor’s information and local landscape are also very important.</em>
            </p>

            <p>
              ​
              <em>Our aims are:</em>
            </p>

            <p>
              ​
              <em>1.Help our user to know more about their target locations’ surroundings, to see if that is a great place to open a restaurant.</em>
            </p>

            <p>
              ​
              <em>2.If the user already owns a place, we want to help them to know their potentials and what they can improve.</em>
            </p>

            <h1>Datasets</h1>

            <hr />

            <p>
              ​
              <em>Our main datasets are yelp datasets, The Yelp dataset is a subset of yelp’s registered businesses, reviews, and other data for use in personal, educational, and academic purposes. Available as JSON files.</em>
            </p>

            <p>
              ​
              <em>Other datasets we use are:</em>
            </p>

            <p>
              ​
              <em>1.Earnings and population datasets from census.gov</em>
            </p>

            <p>
              ​
              <em>2.Communal facilities and crime datasets from the City of Phoenix Mapping Open Data.</em>
            </p>

            <p>
              ​
              <em>3.School dataset from National Center for Education Statistics</em>
            </p>

            <p>
              &lt;table&gt;
              &lt;tr&gt;
              &lt;th&gt;Data Source&lt;/th&gt;
              &lt;th&gt;Dataset&lt;/th&gt;
              &lt;th&gt;Size&lt;/th&gt;
              <br />&lt;th&gt;Description&lt;/th&gt;
              &lt;th&gt;Web Link&lt;/th&gt;
              &lt;/tr &gt;
              &lt;tr &gt;
              &lt;td rowspan=&quot;6&quot;&gt;Yelp Challenge Data&lt;/td&gt;
              &lt;td&gt;Business&lt;/td&gt;
              &lt;td&gt;135 MB&lt;/td&gt;
              &lt;td&gt;Business characteristics&lt;/td&gt;
              &lt;td&gt;https://www.yelp.com/dataset&lt;/td&gt;
              &lt;/tr&gt;
              &lt;tr&gt;
              &lt;td&gt;User&lt;/td&gt;
              &lt;td&gt;2.4 GB&lt;/td&gt;
              &lt;td&gt;User characteristics&lt;/td&gt;
              &lt;td&gt;https://www.yelp.com/dataset&lt;/td&gt;
              &lt;/tr&gt;
              &lt;tr&gt;
              &lt;td&gt;Checkin&lt;/td&gt;
              &lt;td&gt;399 MB&lt;/td&gt;
              &lt;td&gt;Checkin timestamp&lt;/td&gt;
              &lt;td&gt;https://www.yelp.com/dataset&lt;/td&gt;
              &lt;/tr&gt;
              &lt;tr&gt;
              &lt;td&gt;Photos&lt;/td&gt;
              &lt;td&gt;25 MB&lt;/td&gt;
              &lt;td&gt;Photo caption and classification&lt;/td&gt;
              &lt;td&gt;https://www.yelp.com/dataset&lt;/td&gt;
              &lt;/tr&gt;
              &lt;tr&gt;
              &lt;td&gt;Review&lt;/td&gt;
              &lt;td&gt;5.2 GB&lt;/td&gt;
              &lt;td&gt;User review&lt;/td&gt;
              &lt;td&gt;https://www.yelp.com/dataset&lt;/td&gt;
              &lt;/tr&gt;
              &lt;tr&gt;
              &lt;td&gt;Tip&lt;/td&gt;
              &lt;td&gt;238 MB&lt;/td&gt;
              &lt;td&gt;User suggestions&lt;/td&gt;
              &lt;td&gt;https://www.yelp.com/dataset&lt;/td&gt;
              &lt;/tr&gt;
              &lt;tr &gt;
              &lt;td&gt;Census Data&lt;/td&gt;
              &lt;td&gt;Population&lt;/td&gt;
              &lt;td&gt;975 MB&lt;/td&gt;
              &lt;td&gt;Population and earning information&lt;/td&gt;
              &lt;td&gt;https://factfinder.census&lt;/td&gt;
              &lt;/tr&gt;
              &lt;tr &gt;
              &lt;td rowspan=&quot;6&quot;&gt;City of Phoenix Mapping Open Data&lt;/td&gt;
              &lt;td&gt;Park&lt;/td&gt;
              &lt;td&gt;30KB&lt;/td&gt;
              &lt;td&gt;Location of parks and links to websites&lt;/td&gt;
              &lt;td&gt;https://mapping-phoenix.opendata.arcgis.com/&lt;/td&gt;
              &lt;/tr&gt;
              &lt;tr &gt;
              &lt;td&gt;Hospital&lt;/td&gt;
              &lt;td&gt;15KB&lt;/td&gt;
              &lt;td&gt;Hospital locations&lt;/td&gt;
              &lt;td&gt;https://mapping-phoenix.opendata.arcgis.com/&lt;/td&gt;
              &lt;/tr&gt;
              &lt;tr &gt;
              &lt;td&gt;Points of Pride&lt;/td&gt;
              &lt;td&gt;25KB&lt;/td&gt;
              &lt;td&gt;Points of pride locations and images&lt;/td&gt;
              &lt;td&gt;https://mapping-phoenix.opendata.arcgis.com/&lt;/td&gt;
              &lt;/tr&gt;
              &lt;tr &gt;
              &lt;td&gt;Light Rail Station&lt;/td&gt;
              &lt;td&gt;12KB&lt;/td&gt;
              &lt;td&gt;Light rail station locations&lt;/td&gt;
              &lt;td&gt;https://mapping-phoenix.opendata.arcgis.com/&lt;/td&gt;
              &lt;/tr&gt;
              &lt;tr &gt;
              &lt;td&gt;Traffic Volume&lt;/td&gt;
              &lt;td&gt;14.4MB&lt;/td&gt;
              &lt;td&gt;Traffic volume measurement location and recorded volume counts from year 2009 to 2018&lt;/td&gt;
              &lt;td&gt;https://mapping-phoenix.opendata.arcgis.com/&lt;/td&gt;
              &lt;/tr&gt;
              &lt;tr &gt;
              &lt;td&gt;Crime&lt;/td&gt;
              &lt;td&gt;24MB&lt;/td&gt;
              &lt;td&gt;Crime data between 2015 and 2019&lt;/td&gt;
              &lt;td&gt;https://mapping-phoenix.opendata.arcgis.com/&lt;/td&gt;
              &lt;/tr&gt;
              &lt;tr&gt;
              &lt;td &gt;National Center for Education Statistics&lt;/td&gt;
              &lt;td &gt;School&lt;/td&gt;
              &lt;td &gt;535KB&lt;/td&gt;
              &lt;td &gt;School location and enrollment data from the academic year 2008 to 2018&lt;/td&gt;
              &lt;td &gt;https://nces.ed.gov/ccd/elsi/expressTables.aspx&lt;/td&gt;
              &lt;/tr&gt;
              &lt;/table&gt;
            </p>

            <h1>Methology</h1>

            <hr />

            <p>
              ​
              <em>method</em>
              ​
              ​
              <img alt="avatar" src="/Users/zhoulinlin/Desktop/daimages/Picture1.png" />
              ​
              ​
            </p>

            <h1>​Summary</h1>

            <hr />

            <p>
              ​
              <em>We collected data from multiple authoritative source.</em>
              ​
              ​
              <br />​
              <br />​ ​
              <em>We used different method to analyze our datas.</em>
              ​ ​
              <br />​ ​
              <br />​ ​
              <em>The most important achievement about this project, is the universally applicability and the potential.</em>
              ​ ​
              <br />​
              ​
              <em>We can apply on more cities by adding more cities&#39; supporting data.</em>
              ​ ​
              <br />​
              <em>We can make our report more comprehensive by using more factors.</em>
              ​ ​
              <br />​
              <em>We can get more accurate analysis result by using more advanced method.</em>
              ​
              ​
              ​
            </p>
          </div>
        </div>
      </el-card>
    </el-main>

    <Footer />
  </el-container>
</template>

<script>
import Header from "../components/Header";
import Banner from "../components/Banner";
import Footer from "../components/Footer";

export default {
  name: "Index",
  components: {
    Header,
    Banner,
    Footer
  },
  data() {
    return {};
  },
  mounted() {},
  methods: {}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
