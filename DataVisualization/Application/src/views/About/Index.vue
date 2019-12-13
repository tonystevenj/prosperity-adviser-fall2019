<template>
  <el-container direction="vertical">
    <Header />
    <Banner />
    <el-main>
      <el-card class="box-card" element-loading-background="rgba(255, 255, 255, 0.5)">
        <div slot="header" class="title clearfix">
          <span>Introduction</span>
        </div>
        <div class="text item">
          <div class="markdown clearfix">
            <!-- 块开始 -->

            <p>
              <img src="/Users/zhoulinlin/Desktop/daimages/title.jpeg" alt="avatar" />
            </p>
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

            <!-- 块结束 -->
          </div>
        </div>
      </el-card>
      <el-card class="box-card" element-loading-background="rgba(255, 255, 255, 0.5)">
        <div slot="header" class="title clearfix">
          <span>Motivation</span>
        </div>
        <div class="text item">
          <div class="markdown clearfix">
            <!-- 块开始 -->

            <p>
              ​
              <em>The idea was inspired by yelp dataset challenge’s winning projects. After reviewing these brilliant projects, our team member noticed yelp’s dataset is very versatile. It contains a variety of very important data about restaurants.</em>
              ​
              <br />​
              <br />​
              <em>There are total number of 59387 restaurants’ core information that distributed in 10 different metropolitan areas. After we found some other related supporting datasets, we believed we could use yelp’s dataset to create a very useful project.</em>
            </p>

            <!-- 块结束 -->
          </div>
        </div>
      </el-card>
      <el-card class="box-card" element-loading-background="rgba(255, 255, 255, 0.5)">
        <div slot="header" class="title clearfix">
          <span>Aims</span>
        </div>
        <div class="text item">
          <div class="markdown clearfix">
            <!-- 块开始 -->

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

            <!-- 块结束 -->
          </div>
        </div>
      </el-card>
      <el-card class="box-card" element-loading-background="rgba(255, 255, 255, 0.5)">
        <div slot="header" class="title clearfix">
          <span>Datasets</span>
        </div>
        <div class="text item">
          <div class="markdown clearfix">
            <!-- 块开始 -->

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
            <table>
              <tr>
                <th>Data Source</th>
                <th>Dataset</th>
                <th>Size</th>
                <br />
                <th>Description</th>
                <th>Web Link</th>
              </tr>
              <tr>
                <td rowspan="6">Yelp Challenge Data</td>
                <td>Business</td>
                <td>135 MB</td>
                <td>Business characteristics</td>
                <td>
                  <a href="https://www.yelp.com/dataset">https://www.yelp.com/dataset</a>
                </td>
              </tr>
              <tr>
                <td>User</td>
                <td>2.4 GB</td>
                <td>User characteristics</td>
                <td>
                  <a href="https://www.yelp.com/dataset">https://www.yelp.com/dataset</a>
                </td>
              </tr>
              <tr>
                <td>Checkin</td>
                <td>399 MB</td>
                <td>Checkin timestamp</td>
                <td>
                  <a href="https://www.yelp.com/dataset">https://www.yelp.com/dataset</a>
                </td>
              </tr>
              <tr>
                <td>Photos</td>
                <td>25 MB</td>
                <td>Photo caption and classification</td>
                <td>
                  <a href="https://www.yelp.com/dataset">https://www.yelp.com/dataset</a>
                </td>
              </tr>
              <tr>
                <td>Review</td>
                <td>5.2 GB</td>
                <td>User review</td>
                <td>
                  <a href="https://www.yelp.com/dataset">https://www.yelp.com/dataset</a>
                </td>
              </tr>
              <tr>
                <td>Tip</td>
                <td>238 MB</td>
                <td>User suggestions</td>
                <td>
                  <a href="https://www.yelp.com/dataset">https://www.yelp.com/dataset</a>
                </td>
              </tr>
              <tr>
                <td>Census Data</td>
                <td>Population</td>
                <td>975 MB</td>
                <td>Population and earning information</td>
                <td>
                  <a href="https://factfinder.census">https://factfinder.census</a>
                </td>
              </tr>
              <tr>
                <td rowspan="6">City of Phoenix Mapping Open Data</td>
                <td>Park</td>
                <td>30KB</td>
                <td>Location of parks and links to websites</td>
                <td>
                  <a
                    href="https://mapping-phoenix.opendata.arcgis.com/"
                  >https://mapping-phoenix.opendata.arcgis.com/</a>
                </td>
              </tr>
              <tr>
                <td>Hospital</td>
                <td>15KB</td>
                <td>Hospital locations</td>
                <td>
                  <a
                    href="https://mapping-phoenix.opendata.arcgis.com/"
                  >https://mapping-phoenix.opendata.arcgis.com/</a>
                </td>
              </tr>
              <tr>
                <td>Points of Pride</td>
                <td>25KB</td>
                <td>Points of pride locations and images</td>
                <td>
                  <a
                    href="https://mapping-phoenix.opendata.arcgis.com/"
                  >https://mapping-phoenix.opendata.arcgis.com/</a>
                </td>
              </tr>
              <tr>
                <td>Light Rail Station</td>
                <td>12KB</td>
                <td>Light rail station locations</td>
                <td>
                  <a
                    href="https://mapping-phoenix.opendata.arcgis.com/"
                  >https://mapping-phoenix.opendata.arcgis.com/</a>
                </td>
              </tr>
              <tr>
                <td>Traffic Volume</td>
                <td>14.4MB</td>
                <td>Traffic volume measurement location and recorded volume counts from year 2009 to 2018</td>
                <td>
                  <a
                    href="https://mapping-phoenix.opendata.arcgis.com/"
                  >https://mapping-phoenix.opendata.arcgis.com/</a>
                </td>
              </tr>
              <tr>
                <td>Crime</td>
                <td>24MB</td>
                <td>Crime data between 2015 and 2019</td>
                <td>
                  <a
                    href="https://mapping-phoenix.opendata.arcgis.com/"
                  >https://mapping-phoenix.opendata.arcgis.com/</a>
                </td>
              </tr>
              <tr>
                <td>National Center for Education Statistics</td>
                <td>School</td>
                <td>535KB</td>
                <td>School location and enrollment data from the academic year 2008 to 2018</td>
                <td>
                  <a
                    href="https://nces.ed.gov/ccd/elsi/expressTables.aspx"
                  >https://nces.ed.gov/ccd/elsi/expressTables.aspx</a>
                </td>
              </tr>
            </table>

            <!-- 块结束 -->
          </div>
        </div>
      </el-card>
      <el-card class="box-card" element-loading-background="rgba(255, 255, 255, 0.5)">
        <div slot="header" class="title clearfix">
          <span>Methology</span>
        </div>
        <div class="text item">
          <div class="markdown clearfix">
            <!-- 块开始 -->

            <p>
              ​
              <em>method</em>
              ​
              <br />​
              <img src="/Users/zhoulinlin/Desktop/daimages/Picture1.png" alt="avatar" />
            </p>
            <h2 id="1-location-score-calculation-">1. Location Score Calculation(分数计算)</h2>
            <p>In our project, the first question to solve is: Is the place a good one to open a restaurant? To answer this question, we considered several factors that may affect the population flow in common sense: earnings, popultion, nearby schools, parks, train stations, hospital, tourist attraction (the dataset of those factors are given in forms of longitude and latitude).</p>
            <p>
              The final score ouput is in 100 scale, like this:
              <br />&quot;Fgure 11 output of &quot;Site Score&quot;
            </p>
            <p>As shown, there are 7 terms in the form, every term has 100 scaled score, and the seekbar is used for setting the weight among 7 terms. It works just like your final grade in your college class, for example, the &quot;park&quot; as your &quot;midterm exam&quot;, &quot;school&quot; is &quot;homework&quot;, &quot;earning&quot; is &quot;final exam&quot;, your final grade is based on every grade of single term multiply it&#39;s weight, and in our project, the weight is adjustable by yourself! So, the question is, how to give out score for single term.</p>
            <h3 id="calculate-score-for-single-term">Calculate score for single term</h3>
            <p>Here we use park data as sample, the pipe line for other data is almostly same. So, tell a location is good or not among the whole city, user need choose a small area which he wants to be reported. We temporarily call this location A. We give the density of park in this area, compare with the max density of the whole city, give out the score. For density of location A, it&#39;s easy to calculate, because we can easily get the amount of park from our data set, and the area size also easily calculate because the location A is a circle, and the radius can be set by user. i.e. the area size of A is set by user. So, the key question is how to calculate the max density of the whole city.</p>
            <h3
              id="calculate-the-max-density-of-the-whole-city"
            >Calculate the max density of the whole city</h3>
            <p>The parks are presented by points with longitude and latitude. Shown as below, you can think the whole plane is the map of Phoenix City, points are parks.</p>
            <p>&quot;figure: Park locations in Phoenix&quot;</p>
            <p>It&#39;s easy to see the most dense part in the graph is approximately at (-112,08,33.45). So we need to calculate the density around this point, the result can be think as the max density of this city.</p>
            <p>So we dicide do a K-mean cluster to get those compact point together, like below graph:</p>
            <p>&quot;figure: K-mean cluster result&quot;</p>
            <p>
              It&#39;s obviously in this graph that the most density part is successfully clustered together as blue. (you need to do many times of k-mean to see if the result is what you want, because k-mean result is different with different cluster amount and initial points)
              <br />To calculate the density of blue cluster, we need the amount and area size, the amount is easy to count but for area size, we used an approximate algorithm to do it: First, we find the convex hull (using Jarvis March algorithm) of those points, it&#39;s likely a ellipse. we set the longest distance of a pair among those hull points as the longer radius and divide other points into two groups using the line formed by longer radius, calculate the shortest distance between two groups, set the value as the shorter radius of our ellipse. Then we can calculate the max density of the area.
            </p>
            <p>&quot;figure: Convex hull result&quot;</p>
            <p>
              So the red points in above figure is the convex hull points of cluster-blue. And pink circled pair is points with longest distance among these shell points. And other shell point are divided into two parts, in this case, every part has four points, and blue-circled pair is the shortest pair between two parts. So, now we can calculate the area size according to ellipse formula: Pi
              <em>a</em>b(a=distance of pink-circled pair, b=istance of blue-circled pair). Then the density of cluster-blue can be easily calculated, which is the max park density of Phoenix city.
            </p>
            <h2 id="2-">2. 艳姐的部分</h2>
            <h2 id="3-key-factors-in-users-opinion-">3. Key Factors in Users&#39; Opinion(大字报)</h2>
            <p>We divide all restaurants in area A into three groups: star 0-3, star 4-5 and closed. In this part, we try to give different features of three groups in users&#39; eyes. Then we add all reviews of one single restaurant together, as terms of this restaurant given by users. And do the TF-IDF, output the term-weight list for every restaurant and get top 10 terms. Collect all keywords in same group, sum the weight of same words, as the keywords of the whole group.</p>
            <p>&quot;figure: Pipe line of TF-IDF&quot;</p>
            <p>Significance: By given this data, we can figure out what factors customer cares most.</p>
            <p>Result sample:</p>
            <p>&quot;figure Sample Result of TF-IDF&quot;</p>
            <p>
              This is a real result of a certain point in the map. As we can see, in this case, for the first figure, we can figure out that maybe it&#39;s better to sell tacos, users in this area seems like tacos. And for the last figure, we can see people in this area seems don&#39;t like coffee. So on and so for. There are many interesting results you can conclude from these graph.
              ​
              <br />​
            </p>

            <!-- 块结束 -->
          </div>
        </div>
      </el-card>
      <el-card class="box-card" element-loading-background="rgba(255, 255, 255, 0.5)">
        <div slot="header" class="title clearfix">
          <span>​Summary</span>
        </div>
        <div class="text item">
          <div class="markdown clearfix">
            <!-- 块开始 -->

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
.box-card {
  max-width: 1200px;
  margin: 0 auto;
  margin-top: 20px;
  font-size: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
}
.box-card .title {
  font-size: 24px;
  font-weight: bold;
}
.markdown {
  font-size: 16px;
  color: #333333;
}
.markdown p {
  color: #000000;
  /* font-family: "" */
}
.markdown table {
  font-family: verdana, arial, sans-serif;
  font-size: 11px;
  color: #333333;
  border-width: 1px;
  border-color: #666666;
  border-collapse: collapse;
}
.markdown table th {
  border-width: 1px;
  padding: 8px;
  border-style: solid;
  border-color: #666666;
  background-color: #dedede;
}
.markdown table td {
  border-width: 1px;
  padding: 8px;
  border-style: solid;
  border-color: #666666;
  background-color: #ffffff;
}
</style>
