<template>
  <el-container direction="vertical">
    <Header />
    <Banner />
    <el-main>
      <el-card class="box-card" element-loading-background="rgba(255, 255, 255, 0.5)">
        <div slot="header" class="title clearfix" style="color:#2486b9">
          <span>Introduction</span>
        </div>
        <div class="text item">
          <div class="markdown clearfix">
            <!-- 块开始 -->

            <p>Our project is called assistant for restaurant site selection (ARSS),a web-based service.</p>
            <p>The goal of ARSS is to give restaurant owner a report about their businesses’ or their potential business’s local surrounding information and provide a suggestion score based on their customized weight factors.</p>
            <p>Furthermore, it can give a report that if I want to or already have a restaurant here, what features I should care most to make my restaurant be more popular. Currently, this product is only work in Phoenix, Arizona.</p>

            <!-- 块结束 -->
          </div>
        </div>
      </el-card>
      <el-card class="box-card" element-loading-background="rgba(255, 255, 255, 0.5)">
        <div slot="header" class="title clearfix" style="color:#2486b9">
          <span>Motivation</span>
        </div>
        <div class="text item">
          <div class="markdown clearfix">
            <!-- 块开始 -->

            <p>The idea was inspired by yelp dataset challenge’s winning projects. After reviewing these brilliant projects, our team member noticed yelp’s dataset is very versatile. It contains a variety of very important data about restaurants.</p>
            <p>There are total number of 59387 restaurants’ core information that distributed in 10 different metropolitan areas. After we found some other related supporting datasets, we believed we could use yelp’s dataset to create a very useful project.</p>

            <!-- 块结束 -->
          </div>
        </div>
      </el-card>
      <el-card class="box-card" element-loading-background="rgba(255, 255, 255, 0.5)">
        <div slot="header" class="title clearfix" style="color:#2486b9">
          <span>Aims</span>
        </div>
        <div class="text item">
          <div class="markdown clearfix">
            <!-- 块开始 -->

            <p>​ As restaurant owner, it is important to know the surrounding information such as population and costumer’s interests. Although, the restaurant&#39;s objective condition is the decisive factor of success, knowing the surrounding competitor’s information and local landscape are also very important.</p>
            <p>​ Our aims are:</p>
            <p>​ 1.Help our user to know more about their target locations’ surroundings, to see if that is a great place to open a restaurant.</p>
            <p>​ 2.If the user already owns a place, we want to help them to know their potentials and what they can improve.</p>

            <!-- 块结束 -->
          </div>
        </div>
      </el-card>
      <el-card class="box-card" element-loading-background="rgba(255, 255, 255, 0.5)">
        <div slot="header" class="title clearfix" style="color:#2486b9">
          <span>Datasets</span>
        </div>
        <div class="text item">
          <div class="markdown clearfix">
            <!-- 块开始 -->

            <p>​ Our main datasets are yelp datasets, The Yelp dataset is a subset of yelp’s registered businesses, reviews, and other data for use in personal, educational, and academic purposes. Available as JSON files.</p>
            <p>​ Other datasets we use are:</p>
            <p>​ 1.Earnings and population datasets from census.gov</p>
            <p>​ 2.Communal facilities and crime datasets from the City of Phoenix Mapping Open Data.</p>
            <p>​ 3.School dataset from National Center for Education Statistics</p>
            <table>
              <tr>
                <th>Data Source</th>
                <th>Dataset</th>
                <th>Size</th>
                <th>Description</th>
                <th>Web Link</th>
              </tr>
              <tr>
                <td rowspan="6">Yelp Challenge Data</td>
                <td>Business</td>
                <td>135 MB</td>
                <td>Business characteristics</td>
                <td>
                  <a
                    href="https://www.yelp.com/dataset"
                    target="_blank"
                  >https://www.yelp.com/dataset</a>
                </td>
              </tr>
              <tr>
                <td>User</td>
                <td>2.4 GB</td>
                <td>User characteristics</td>
                <td>
                  <a
                    href="https://www.yelp.com/dataset"
                    target="_blank"
                  >https://www.yelp.com/dataset</a>
                </td>
              </tr>
              <tr>
                <td>Checkin</td>
                <td>399 MB</td>
                <td>Checkin timestamp</td>
                <td>
                  <a
                    href="https://www.yelp.com/dataset"
                    target="_blank"
                  >https://www.yelp.com/dataset</a>
                </td>
              </tr>
              <tr>
                <td>Photos</td>
                <td>25 MB</td>
                <td>Photo caption and classification</td>
                <td>
                  <a
                    href="https://www.yelp.com/dataset"
                    target="_blank"
                  >https://www.yelp.com/dataset</a>
                </td>
              </tr>
              <tr>
                <td>Review</td>
                <td>5.2 GB</td>
                <td>User review</td>
                <td>
                  <a
                    href="https://www.yelp.com/dataset"
                    target="_blank"
                  >https://www.yelp.com/dataset</a>
                </td>
              </tr>
              <tr>
                <td>Tip</td>
                <td>238 MB</td>
                <td>User suggestions</td>
                <td>
                  <a
                    href="https://www.yelp.com/dataset"
                    target="_blank"
                  >https://www.yelp.com/dataset</a>
                </td>
              </tr>
              <tr>
                <td>Census Data</td>
                <td>Population</td>
                <td>975 MB</td>
                <td>Population and earning information</td>
                <td>
                  <a
                    href="https://factfinder.census.gov"
                    target="_blank"
                  >https://factfinder.census.gov</a>
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
                    target="_blank"
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
                    target="_blank"
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
                    target="_blank"
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
                    target="_blank"
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
                    target="_blank"
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
                    target="_blank"
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
                    target="_blank"
                  >https://nces.ed.gov/ccd/elsi/expressTables.aspx</a>
                </td>
              </tr>
            </table>

            <!-- 块结束 -->
          </div>
        </div>
      </el-card>
      <el-card class="box-card" element-loading-background="rgba(255, 255, 255, 0.5)">
        <div slot="header" class="title clearfix" style="color:#2486b9">
          <span>Methodology</span>
        </div>
        <div class="text item">
          <div class="markdown clearfix">
            <!-- 块开始 -->

            <h2 id="1-location-score-calculation-" style="color:#158bb8">1. Location Score Calculation</h2>
            <hr />
            <p>In our project, the first question to solve is: Is the place a good one to open a restaurant? To answer this question, we considered several factors that may affect the population flow in common sense: earnings, popultion, nearby schools, parks, train stations, hospital, tourist attraction (the dataset of those factors are given in forms of longitude and latitude).</p>
            <p>The final score ouput is in 100 scale, like this:</p>
            <div class="center">
              <img class="image" src="../../../static/figure11.png" />
            </div>
            <div class="center" style="font-size:15px;font-weight:bold">
              <p>Fifure: Result of Site Score</p>
            </div>
            <p>As shown, there are 7 terms in the form, every term has 100 scaled score, and the seekbar is used for setting the weight among 7 terms. It works just like your final grade in your college class, for example, the &quot;park&quot; as your &quot;midterm exam&quot;, &quot;school&quot; is &quot;homework&quot;, &quot;earning&quot; is &quot;final exam&quot;, your final grade is based on every grade of single term multiply it&#39;s weight, and in our project, the weight is adjustable by yourself! So, the question is, how to give out score for single term.</p>
            <h3 id="calculate-score-for-single-term">Calculate score for single term</h3>
            <p>Here we use park data as sample, the pipe line for other data is almostly same. So, tell a location is good or not among the whole city, user need choose a small area which he wants to be reported. We temporarily call this location A. We give the density of park in this area, compare with the max density of the whole city, give out the score. For density of location A, it&#39;s easy to calculate, because we can easily get the amount of park from our data set, and the area size also easily calculate because the location A is a circle, and the radius can be set by user. i.e. the area size of A is set by user. So, the key question is how to calculate the max density of the whole city.</p>
            <h3
              id="calculate-the-max-density-of-the-whole-city"
            >Calculate the max density of the whole city</h3>
            <p>The parks are presented by points with longitude and latitude. Shown as below, you can think the whole plane is the map of Phoenix City, points are parks.</p>
            <div class="center">
              <img class="image" src="../../../static/figure12.png" />
            </div>
            <div class="center" style="font-size:15px;font-weight:bold">
              <p>Fifure: Parks Location in Phoenix</p>
            </div>
            <p>It&#39;s easy to see the most dense part in the graph is approximately at (-112,08,33.45). So we need to calculate the density around this point, the result can be think as the max density of this city.</p>
            <p>So we dicide do a K-mean cluster to get those compact point together, like below graph:</p>
            <div class="center">
              <img class="image" src="../../../static/figure13.png" />
            </div>
            <div class="center" style="font-size:15px;font-weight:bold">
              <p>Fifure: Cluster Result</p>
            </div>
            <p>
              *It&#39;s obviously in this graph that the most density part is successfully clustered together as blue. (you need to do many times of k-mean to see if the result is what you want, because k-mean result is different with different cluster amount and initial points)
              <br />To calculate the density of blue cluster, we need the amount and area size, the amount is easy to count but for area size, we used an approximate algorithm to do it: First, we find the convex hull (using Jarvis March algorithm) of those points, it&#39;s likely a ellipse. we set the longest distance of a pair among those hull points as the longer radius and divide other points into two groups using the line formed by longer radius, calculate the shortest distance between two groups, set the value as the shorter radius of our ellipse. Then we can calculate the max density of the area.
            </p>
            <div class="center">
              <img class="image" src="../../../static/figure14.png" />
            </div>
            <div class="center" style="font-size:15px;font-weight:bold">
              <p>Fifure: Result of Convex Hull</p>
            </div>
            <p>
              So the red points in above figure is the convex hull points of cluster-blue. And pink circled pair is points with longest distance among these shell points. And other shell point are divided into two parts, in this case, every part has four points, and blue-circled pair is the shortest pair between two parts. So, now we can calculate the area size according to ellipse formula: Pi
              <em>a</em>b(a=distance of pink-circled pair, b=istance of blue-circled pair). Then the density of cluster-blue can be easily calculated, which is the max park density of Phoenix city.
            </p>
            <h2 id="data-preprocessing" style="color:#158bb8">2. Data Preprocessing</h2>
            <hr />
            <p>A number of data preprocessing steps were applied to the Yelp business data, including flattening business Json data file attributes, removing restaurants afficiated with other business types, identifying restaurant cuisine type, and converting the coordinate systems of supplemental data to latitude and longitude-based geographical coordinate system. The raw Yelp json file uses double quote mark for the first and two levels of attributes and single quote mark for the third level attribute. The python json package can only identify the attributes within double quote mark, and the attributes within a single quote mark have to be expanded by writing codes. A hospital or a shopping mall listed in the yelp data can also have the category of restaurant because there is a restaurant within it. The corresponding star scores may be for the hospital or shopping mall, not just for restaurants. Such types of restaurants have to be excluded from the analysis. In this study, these types of restaurants as well as restaurant cuisine types were extracted based on comparisons with the complete list of yelp categories for businesses. The web application developed in this project requires the use of latitude and longitude-based geographical coordinate system in order to calculate the distances between selected restaurant site and its neighboring facilities. However, the supplemental data such as parks, hospitals, schools, and so on use different coordinate systems, which have to be converted to latitude and longitude either by python Geopandas library or Google Earth.</p>

            <!-- <table>
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Categories</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Phoenix Children's Hospital</td>
                  <td>Doctors, Cardiologists, Health & Medical, Emergency Medicine, Restaurants, Pediatricians, Hospitals, Mediterranean</td>
                </tr>
                <tr>
                  <td>Mendy's Place</td>
                  <td>Hospitals, Restaurants, Health & Medical</td>
                </tr>
              </tbody>
            </table> -->
            <div class="center">
              <img class="image" src="../../../static/table3.png" />
            </div>


            <h3 id="feature-selection">Feature Selection</h3>
            <p>As a new restaurant owner, it is interesting to see what types of restaurants having been open or closed at the intended restaurant site, and what types of services these restaurants have provided. To help with that, the most important features that affect a restaurant star score were extracted using random forest regression analysis in this project. The attributes that are related to restaurant characteristics were used as independent varables and the scores of restaurants were treated as a dependent variable. Before conducting regression analysis, the attributes with large missing data that is greater than 90% were removed from analysis. The remaining text attributes were then converted to categorical variables. The restaurant data was divided into training and testing data sets and fit to the random forest regressor of python sklearn package. The mean absolute percentage error (MAPE) between the predicted restaurant scores and the actual scores was calculated and the prediction accuracy of this analysis, defined as 100% minus mean percentage absolute error, is 80.25%. The table below lists the top 10 features identified by random forest regression analysis and their corresponding importance scores. As shown in this table, attributes of cuisine type, wheelchair accessibility, catering capability, provision of outdoor seating, alcohol provision, parking lot, noise level, provision of WiFi, parking for bikes, and restaurant prices are important features that affect the star scores of restaurants.</p>
            <table>
              <thead>
                <tr>
                  <th>Features</th>
                  <th>Importance</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Cuisine Type</td>
                  <td>0.089</td>
                </tr>
                <tr>
                  <td>WheelchairAccessible</td>
                  <td>0.079</td>
                </tr>
                <tr>
                  <td>Caters</td>
                  <td>0.056</td>
                </tr>
                <tr>
                  <td>OutdoorSeating</td>
                  <td>0.053</td>
                </tr>
                <tr>
                  <td>Alcohol</td>
                  <td>0.051</td>
                </tr>
                <tr>
                  <td>Lot</td>
                  <td>0.049</td>
                </tr>
                <tr>
                  <td>NoiseLevel</td>
                  <td>0.048</td>
                </tr>
                <tr>
                  <td>WiFi</td>
                  <td>0.044</td>
                </tr>
                <tr>
                  <td>BikeParking</td>
                  <td>0.042</td>
                </tr>
                <tr>
                  <td>RestaurantsPriceRange</td>
                  <td>0.039</td>
                </tr>
              </tbody>
            </table>
            <p>The percentage distributions of possible values for these features are displayed in the user interface in the format of stacked bar charts. Three charts for three categories of restaurants, that is, one category for open restaurants with a score greater than or equal to 4, one category for open restaurants with score less than 4, and the third category of closed restaurants. As shown in the charts below, the y-axis lists the top 10 features from the most important feature at the top to the least important feature at the bottom. The x-axis shows the percentage of each possible value for each feature. By looking at the distribution of each feature value and comparing them among three restaurant groups, user can identify which type of food is dominant in study area and can get good star scores, and also determine if they want to provide the services such as WiFi, wheel chair services, and so on. For example, the charts below indicate that american food is popular in the selected area and can get a score of greater than four.</p>
            <div class="center">
              <img class="image" src="../../../static/figure9.png" />
            </div>
            <div class="center">
              <img class="image" src="../../../static/figure10.png" />
            </div>
            <!-- <table>
              <thead>
                <tr>
                  <th>X</th>
                  <th>Y</th>
                  <th>NAME</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>643615.8091</td>
                  <td>918636.1</td>
                  <td>ABRAZO CENTRAL CAMPUS</td>
                </tr>
                <tr>
                  <td>770177.5594</td>
                  <td>877237.3</td>
                  <td>BANNER BAYWOOD MEDICAL CENTER</td>
                </tr>
                <tr>
                  <td>666574.665</td>
                  <td>893895.6</td>
                  <td>MARICOPA INTEGRATED HEALTH SYSTEM</td>
                </tr>
                <tr>
                  <td>687667.1043</td>
                  <td>967273</td>
                  <td>MAYO CLINIC HOSPITAL</td>
                </tr>
                <tr>
                  <td>692673.2638</td>
                  <td>877741.4</td>
                  <td>TEMPE ST. LUKE'S HOSPITAL</td>
                </tr>
              </tbody>
            </table>

            <div class="center">
              <i class="el-icon-bottom" style>Geopandas: to_crs()</i>
            </div>

            <table>
              <thead>
                <tr>
                  <th>NAME</th>
                  <th>Longitude</th>
                  <th>Latitude</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>ABRAZO CENTRAL CAMPUS</td>
                  <td>-112.102</td>
                  <td>33.52511</td>
                </tr>
                <tr>
                  <td>BANNER BAYWOOD MEDICAL CENTER</td>
                  <td>-111.687</td>
                  <td>33.41125</td>
                </tr>
                <tr>
                  <td>MARICOPA INTEGRATED HEALTH SYSTEM</td>
                  <td>-112.026</td>
                  <td>33.4572</td>
                </tr>
                <tr>
                  <td>MAYO CLINIC HOSPITAL</td>
                  <td>-111.957</td>
                  <td>33.65891</td>
                </tr>
                <tr>
                  <td>TEMPE ST. LUKE'S HOSPITAL</td>
                  <td>-111.941</td>
                  <td>33.41285</td>
                </tr>
              </tbody>
            </table>

            <table>
              <thead>
                <tr>
                  <th>School ID</th>
                  <th>Location Address</th>
                  <th>City</th>
                  <th>State</th>
                  <th>ZIP</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>40010601892</td>
                  <td>17811 North 32nd Street</td>
                  <td>Phoenix</td>
                  <td>AZ</td>
                  <td>85032</td>
                </tr>
                <tr>
                  <td>40041701588</td>
                  <td>7050 S. 24th Street</td>
                  <td>Phoenix</td>
                  <td>AZ</td>
                  <td>85042</td>
                </tr>
                <tr>
                  <td>40906000652</td>
                  <td>10444 N 39th Avenue</td>
                  <td>Phoenix</td>
                  <td>AZ</td>
                  <td>85051</td>
                </tr>
                <tr>
                  <td>40906000915</td>
                  <td>3021 W. Evans Dr.</td>
                  <td>Phoenix</td>
                  <td>AZ</td>
                  <td>85053</td>
                </tr>
                <tr>
                  <td>40012801715</td>
                  <td>425 North 36th Street</td>
                  <td>Phoenix</td>
                  <td>AZ</td>
                  <td>85008</td>
                </tr>
              </tbody>
            </table>

            <div class="center">
              <i class="el-icon-bottom" style>Google Earth</i>
            </div>

            <table>
              <thead>
                <tr>
                  <th>School ID</th>
                  <th>Longitude</th>
                  <th>Latitude</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>40010601892</td>
                  <td>-112.01187</td>
                  <td>33.6482973</td>
                </tr>
                <tr>
                  <td>40041701588</td>
                  <td>-112.03218</td>
                  <td>33.382485</td>
                </tr>
                <tr>
                  <td>40906000652</td>
                  <td>-112.14436</td>
                  <td>33.581094</td>
                </tr>
                <tr>
                  <td>40906000915</td>
                  <td>-112.12465</td>
                  <td>33.6161736</td>
                </tr>
                <tr>
                  <td>40012801715</td>
                  <td>-112.00365</td>
                  <td>33.4534726</td>
                </tr>
              </tbody>
            </table> -->

            <h2 id="3-key-factors-in-users-opinion-" style="color:#158bb8">3. Key Factors in Users&#39; Opinion</h2>
            <hr />
            <p>We divide all restaurants in area A into three groups: star 0-3, star 4-5 and closed. In this part, we try to give different features of three groups in users&#39; eyes. Then we add all reviews of one single restaurant together, as terms of this restaurant given by users. And do the TF-IDF, output the term-weight list for every restaurant and get top 10 terms. Collect all keywords in same group, sum the weight of same words, as the keywords of the whole group.</p>
            <div class="center">
              <img class="image" src="../../../static/figure15.png" />
            </div>
            <div class="center" style="font-size:15px;font-weight:bold">
              <p>Fifure: Pipeline of TF-IDF</p>
            </div>
            <p>Significance: By given this data, we can figure out what factors customer cares most.</p>
            <p>Result sample:</p>
            <div class="center">
              <img
                class="image"
                style="max-width: 800px; width: 800px;"
                src="../../../static/figure16.png"
              />
            </div>
            <div class="center" style="font-size:15px;font-weight:bold">
              <p>Fifure: Result of TF-IDF</p>
            </div>
            
            <p>
              This is a real result of a certain point in the map. As we can see, in this case, for the first figure, we can figure out that maybe it&#39;s better to sell tacos, users in this area seems like tacos. And for the last figure, we can see people in this area seems don&#39;t like coffee. So on and so for. There are many interesting results you can conclude from these graph.
              <br />​
            </p>

            <h2 style="color:#158bb8">4. How this project run</h2>

            <p>We use Python to develop the project Including data processing, data analysis, and a web server, this webserver bases on Flask. And also, we use NumPy, Pandas, and Scikit-learn to analyze datasets. We have many datasets with geographic information, so we create a geo index with Redis. So, you can see, we input the longitude and latitude, Redis will create a geo index of this dataset. When we query this index use longitude, latitude, and radius, it will return a list of points nearby that point we input and sorted by distance.</p>
            <p>On the frontend, we use NodeJS to develop, bases on Vue and Element UI. These libraries help us fast to develop the frontend. Next, we use the Google Maps API to develop the map function. And the last, we have many diagrams bases on Apache Echarts. It's very professional at data visualization and easy to use.</p>

            <div class="icon_list">
              <el-row :gutter="20">
                <el-col :span="12">
                  <img class="icon" src="../../../static/python_icon.png" />
                  <span>Python 3</span>
                </el-col>
                <el-col :span="12">
                  <img class="icon" src="../../../static/nodejs_icon.png" />
                  <span>Node.js</span>
                </el-col>
              </el-row>
              <el-row :gutter="20">
                <el-col :span="12">
                  <img class="icon" src="../../../static/flask_icon.png" />
                  <span>Flask</span>
                </el-col>
                <el-col :span="12">
                  <img class="icon" src="../../../static/vue_icon.png" />
                  <span>Vue.js</span>
                </el-col>
              </el-row>
              <el-row :gutter="20">
                <el-col :span="12">
                  <img class="icon" src="../../../static/numpy_icon.png" />
                  <span>NumPy</span>
                </el-col>
                <el-col :span="12">
                  <img class="icon" src="../../../static/element_icon.png" />
                  <span>Element UI</span>
                </el-col>
              </el-row>
              <el-row :gutter="20">
                <el-col :span="12">
                  <img class="icon" src="../../../static/pandas_icon.png" />
                  <span>Pandas</span>
                </el-col>
                <el-col :span="12">
                  <img class="icon" src="../../../static/googlemap_icon.png" />
                  <span>Google Maps API</span>
                </el-col>
              </el-row>
              <el-row :gutter="20">
                <el-col :span="12">
                  <img class="icon" src="../../../static/scikitlearn_icon.png" />
                  <span>scikit-learn</span>
                </el-col>
                <el-col :span="12">
                  <img class="icon" src="../../../static/echarts_icon.png" />
                  <span>Apache Echarts</span>
                </el-col>
              </el-row>
              <el-row :gutter="20">
                <el-col :span="12">
                  <img class="icon" src="../../../static/redis_icon.png" />
                  <span>Redis</span>
                </el-col>
                <el-col :span="12"></el-col>
              </el-row>
            </div>

            <p>The server process initiate will load and process all of the datasets. It will divide each dataset into two parts. One part has longitude and latitude and used to create the geo index. The other part is stored in memory, and it used to do some data analysis.</p>
            <p>Then, the server starts, it will provide some APIs, when receiving a request, it will get some data from geo index and memory, then do some analysis, and return the result to the browser.</p>

            <div class="center">
              <img class="image" src="../../../static/figure17.png" />
            </div>
            <p>When you select a point on the map of the website, it can get the longitude, latitude, and zip code, and then, it will send some requests to the server. After that, it will draw some diagrams use the result from the server.</p>

            <!-- 块结束 -->
          </div>
        </div>
      </el-card>
      <el-card class="box-card" element-loading-background="rgba(255, 255, 255, 0.5)">
        <div slot="header" class="title clearfix" style="color:#2486b9">
          <span>​Summary</span>
        </div>
        <div class="text item">
          <div class="markdown clearfix">
            <!-- 块开始 -->

            <p>We collected data from multiple authoritative source.​We used different method to analyze our datas.</p>
            <p>The most important achievement about this project, is the universally applicability and the potential.</p>
            <p>We can apply on more cities by adding more cities&#39; supporting data.</p>
            <p>​We can make our report more comprehensive by using more factors.</p>
            <p>​We can get more accurate analysis result by using more advanced method.</p>

            <!-- 块结束 -->
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
  border-radius: 10px;
  margin: 0 auto;
  margin-top: 20px;
  font-size: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
}
.box-card .title {
  font-size: 24px;
  font-weight: bold;
  color: #333333;
}
.markdown {
  font-size: 16px;
  color: #333333;
}
.markdown p {
  color: #555555;
  /* font-family: "" */
}
.markdown .center {
  text-align: center;
  margin: 20px auto;
}
.markdown .image {
  max-width: 600px;
}
.markdown table {
  margin: 20px auto;
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
.markdown .icon_list {
  width: 600px;
  margin: 20px auto;
}
.markdown .icon {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.markdown .icon_list span {
  font-size: 30px;
  padding-left: 10px;
}
</style>
