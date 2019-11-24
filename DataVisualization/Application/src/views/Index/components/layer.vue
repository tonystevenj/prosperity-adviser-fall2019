<template>
  <wordcloud
    :data="defaultWords"
    nameKey="name"
    valueKey="value"
    :color="myColors"
    :showTooltip="true"
    :wordClick="wordClickHandler"
  ></wordcloud>
</template>

<script>
import wordcloud from "vue-wordcloud";

export default {
  name: "Layer",
  components: {
    wordcloud
  },
  data() {
    return {
      myColors: ["#1f77b4", "#629fc9", "#94bedb", "#c9e0ef"],

      defaultWords: [
        {
          name: "Cat",
          value: 26
        },
        {
          name: "fish",
          value: 19
        },
        {
          name: "things",
          value: 18
        },
        {
          name: "look",
          value: 16
        },
        {
          name: "two",
          value: 15
        },
        {
          name: "fun",
          value: 9
        },
        {
          name: "know",
          value: 9
        },
        {
          name: "good",
          value: 9
        },
        {
          name: "play",
          value: 6
        }
      ]
    };
  },
  created() {
    this.word();
    console.log("test1");
  },
  methods: {
    word() {
      this.axios
        .get("/api/report/reviews", {
          params: {
            latitude: "-112.073843",
            longitude: "33.447999",
            radius: "0.1"
          }
        })
        .then(response => {
          var words = []
          console.log(response.data)
          for (var i in response.data) {
            words.push({
                'name': response.data[i][0],
                'value': response.data[i][1],
            })
          }
          this.defaultWords = words
          console.log(words)
        })
        .catch(response => {
          console.log(response);
        });
    }
  }
};
</script>
