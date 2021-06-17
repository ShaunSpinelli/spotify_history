<template>
<div id="sapp">
    <fusioncharts
    :type="type"
    :width="width"
    :height="height"
    :dataFormat="dataFormat"
    :dataSource="dataSource"
    ></fusioncharts>
</div>
</template>

<script>

import Vue from 'vue';
import VueFusionCharts from 'vue-fusioncharts';
import FusionCharts from 'fusioncharts';
import Charts from 'fusioncharts/fusioncharts.charts';
import FusionTheme from 'fusioncharts/themes/fusioncharts.theme.fusion'



function buildDatasource(title, data){
  const chart = {
  caption: title,
  // subCaption: "The number of songs you've listend to broken down by weekday",
  // xAxisName: "Weeek Day",
  yAxisName: "Songs",
  theme: "fusion",
}
  return { chart , data}
}

Vue.use(VueFusionCharts, FusionCharts, Charts, FusionTheme)

export default {
  name: 'weekdaybar',
  props: {title: String, chartData: Array, elwidth: Number},
  data() {
    return {
      width: `${this.elwidth}%`,
      height: '400',
      type: 'column2d',
      dataFormat: 'json',
      dataSource: buildDatasource(this.title, this.chartData),
    }
  }
};

</script>
