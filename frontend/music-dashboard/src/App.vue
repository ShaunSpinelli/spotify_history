<template>
  <div id="app">
    <h1>Your Spotify</h1>

      <h2>The number of songs you've listend to broken down by weekday</h2>
      <div id="weekdays">
      <weekdaybar title="Last Week" :chartData="chartDataWeek" :elwidth="width"/>
      <weekdaybar title="Last Month" :chartData="chartDataMonth" :elwidth="width"/>
      <weekdaybar title="All Time" :chartData="chartDataWeek" :elwidth="width"/>
    </div>
      <heatmap/>

  </div>
</template>

<script>
import weekdaybar from './components/weekDays.vue'
import heatmap from './components/heatMap.vue'


const chartDataWeek = [
    {
      label: "Mon",
      value: "2900"
    },
    {
      "label": "Tues",
      value: "260"
    },
    {
      "label": "Wed",
      value: "180"
    },
    {
      "label": "Thurs",
      value: "140"
    },
    {
      "label": "Fri",
      value: "115"
    },
    {
      "label": "Sat",
      value: "100"
    },
    {
      "label": "Sun",
      value: "30"
    },
  ]
  
  const chartDataMonth = [
    {
      label: "Mon",
      value: "12"
    },
    {
      "label": "Tues",
      value: "20"
    },
    {
      "label": "Wed",
      value: "18"
    },
    {
      "label": "Thurs",
      value: "14"
    },
    {
      "label": "Fri",
      value: "15"
    },
    {
      "label": "Sat",
      value: "10"
    },
    {
      "label": "Sun",
      value: "12"
    },
  ]

  const width = 30;


export default {
  name: 'App',
  components: {
    weekdaybar,
    heatmap,
  },
  data: function() {
    return {
      chartDataWeek,
      chartDataMonth,
      width
    }
  }
}
</script>

<style>

#weekdays {
  margin: auto;
  max-width: 95%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  flex-wrap: wrap;
  border-style: solid;
  border-width: thin;


}


#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
