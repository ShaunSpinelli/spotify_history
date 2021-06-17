<template>
<div id="heatpap">
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

import FusionCharts from "fusioncharts";
import Charts from "fusioncharts/fusioncharts.charts";
import { FCComponent } from "vue-fusioncharts";
// Resolves charts dependency
Charts(FusionCharts);



const dataSource = {
  chart: {
    caption: "Body Mass Index Chart",
    xaxisname: "Height (cm)",
    yaxisname: "Weight (kg)",
    theme: "fusion",
    showvalues: "1",
    plottooltext: "<b>BMI Value : $dataValue</b>{br}$trLabel"
  },
  dataset: [
    {
      data: [
        {
          rowid: "40",
          columnid: "152",
          value: 17,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 5 kg to be in Normal zone"
        },
        {
          rowid: "40",
          columnid: "155",
          value: 17,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 5 kg to be in Normal zone"
        },
        {
          rowid: "40",
          columnid: "158",
          value: 16,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 8 kg to be in Normal zone"
        },
        {
          rowid: "40",
          columnid: "161",
          value: 15,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 11 kg to be in Normal zone"
        },
        {
          rowid: "40",
          columnid: "164",
          value: 15,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 11 kg to be in Normal zone"
        },
        {
          rowid: "40",
          columnid: "167",
          value: 14,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 14 kg to be in Normal zone"
        },
        {
          rowid: "40",
          columnid: "170",
          value: 14,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 14 kg to be in Normal zone"
        },
        {
          rowid: "40",
          columnid: "173",
          value: 13,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 18 kg to be in Normal zone"
        },
        {
          rowid: "40",
          columnid: "176",
          value: 13,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 18 kg to be in Normal zone"
        },
        {
          rowid: "40",
          columnid: "179",
          value: 12,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 23 kg to be in Normal zone"
        },
        {
          rowid: "40",
          columnid: "182",
          value: 12,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 23 kg to be in Normal zone"
        },
        {
          rowid: "40",
          columnid: "185",
          value: 12,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 23 kg to be in Normal zone"
        },
        {
          rowid: "40",
          columnid: "188",
          value: 11,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 29 kg to be in Normal zone"
        },
        {
          rowid: "40",
          columnid: "191",
          value: 11,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 29 kg to be in Normal zone"
        },
        {
          rowid: "40",
          columnid: "194",
          value: 11,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 29 kg to be in Normal zone"
        },
        {
          rowid: "40",
          columnid: "197",
          value: 10,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 36 kg to be in Normal zone"
        },
        {
          rowid: "40",
          columnid: "200",
          value: 10,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 36 kg to be in Normal zone"
        },
        {
          rowid: "40",
          columnid: "203",
          value: 10,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 36 kg to be in Normal zone"
        },
        {
          rowid: "40",
          columnid: "206",
          value: 9,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 44 kg to be in Normal zone"
        },
        {
          rowid: "40",
          columnid: "209",
          value: 9,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 44 kg to be in Normal zone"
        },
        {
          rowid: "45",
          columnid: "152",
          value: 19,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "45",
          columnid: "155",
          value: 19,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "45",
          columnid: "158",
          value: 18,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 3 kg to be in Normal zone"
        },
        {
          rowid: "45",
          columnid: "161",
          value: 17,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 5 kg to be in Normal zone"
        },
        {
          rowid: "45",
          columnid: "164",
          value: 17,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 5 kg to be in Normal zone"
        },
        {
          rowid: "45",
          columnid: "167",
          value: 16,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 8 kg to be in Normal zone"
        },
        {
          rowid: "45",
          columnid: "170",
          value: 16,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 8 kg to be in Normal zone"
        },
        {
          rowid: "45",
          columnid: "173",
          value: 15,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 12 kg to be in Normal zone"
        },
        {
          rowid: "45",
          columnid: "176",
          value: 15,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 12 kg to be in Normal zone"
        },
        {
          rowid: "45",
          columnid: "179",
          value: 14,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 16 kg to be in Normal zone"
        },
        {
          rowid: "45",
          columnid: "182",
          value: 14,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 16 kg to be in Normal zone"
        },
        {
          rowid: "45",
          columnid: "185",
          value: 13,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 21 kg to be in Normal zone"
        },
        {
          rowid: "45",
          columnid: "188",
          value: 13,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 21 kg to be in Normal zone"
        },
        {
          rowid: "45",
          columnid: "191",
          value: 12,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 26 kg to be in Normal zone"
        },
        {
          rowid: "45",
          columnid: "194",
          value: 12,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 26 kg to be in Normal zone"
        },
        {
          rowid: "45",
          columnid: "197",
          value: 12,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 26 kg to be in Normal zone"
        },
        {
          rowid: "45",
          columnid: "200",
          value: 11,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 33 kg to be in Normal zone"
        },
        {
          rowid: "45",
          columnid: "203",
          value: 11,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 33 kg to be in Normal zone"
        },
        {
          rowid: "45",
          columnid: "206",
          value: 11,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 33 kg to be in Normal zone"
        },
        {
          rowid: "45",
          columnid: "209",
          value: 10,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 41 kg to be in Normal zone"
        },
        {
          rowid: "50",
          columnid: "152",
          value: 22,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "50",
          columnid: "155",
          value: 21,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "50",
          columnid: "158",
          value: 20,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "50",
          columnid: "161",
          value: 19,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "50",
          columnid: "164",
          value: 19,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "50",
          columnid: "167",
          value: 18,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 3 kg to be in Normal zone"
        },
        {
          rowid: "50",
          columnid: "170",
          value: 17,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 6 kg to be in Normal zone"
        },
        {
          rowid: "50",
          columnid: "173",
          value: 17,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 6 kg to be in Normal zone"
        },
        {
          rowid: "50",
          columnid: "176",
          value: 16,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 9 kg to be in Normal zone"
        },
        {
          rowid: "50",
          columnid: "179",
          value: 16,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 9 kg to be in Normal zone"
        },
        {
          rowid: "50",
          columnid: "182",
          value: 15,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 13 kg to be in Normal zone"
        },
        {
          rowid: "50",
          columnid: "185",
          value: 15,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 13 kg to be in Normal zone"
        },
        {
          rowid: "50",
          columnid: "188",
          value: 14,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 18 kg to be in Normal zone"
        },
        {
          rowid: "50",
          columnid: "191",
          value: 14,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 18 kg to be in Normal zone"
        },
        {
          rowid: "50",
          columnid: "194",
          value: 13,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 23 kg to be in Normal zone"
        },
        {
          rowid: "50",
          columnid: "197",
          value: 13,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 23 kg to be in Normal zone"
        },
        {
          rowid: "50",
          columnid: "200",
          value: 13,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 23 kg to be in Normal zone"
        },
        {
          rowid: "50",
          columnid: "203",
          value: 12,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 29 kg to be in Normal zone"
        },
        {
          rowid: "50",
          columnid: "206",
          value: 12,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 29 kg to be in Normal zone"
        },
        {
          rowid: "50",
          columnid: "209",
          value: 11,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 36 kg to be in Normal zone"
        },
        {
          rowid: "55",
          columnid: "152",
          value: 24,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "55",
          columnid: "155",
          value: 23,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "55",
          columnid: "158",
          value: 22,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "55",
          columnid: "161",
          value: 21,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "55",
          columnid: "164",
          value: 20,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "55",
          columnid: "167",
          value: 20,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "55",
          columnid: "170",
          value: 19,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "55",
          columnid: "173",
          value: 18,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 3 kg to be in Normal zone"
        },
        {
          rowid: "55",
          columnid: "176",
          value: 18,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 3 kg to be in Normal zone"
        },
        {
          rowid: "55",
          columnid: "179",
          value: 17,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 6 kg to be in Normal zone"
        },
        {
          rowid: "55",
          columnid: "182",
          value: 17,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 6 kg to be in Normal zone"
        },
        {
          rowid: "55",
          columnid: "185",
          value: 16,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 10 kg to be in Normal zone"
        },
        {
          rowid: "55",
          columnid: "188",
          value: 16,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 10 kg to be in Normal zone"
        },
        {
          rowid: "55",
          columnid: "191",
          value: 15,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 15 kg to be in Normal zone"
        },
        {
          rowid: "55",
          columnid: "194",
          value: 15,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 15 kg to be in Normal zone"
        },
        {
          rowid: "55",
          columnid: "197",
          value: 14,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 20 kg to be in Normal zone"
        },
        {
          rowid: "55",
          columnid: "200",
          value: 14,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 20 kg to be in Normal zone"
        },
        {
          rowid: "55",
          columnid: "203",
          value: 13,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 25 kg to be in Normal zone"
        },
        {
          rowid: "55",
          columnid: "206",
          value: 13,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 25 kg to be in Normal zone"
        },
        {
          rowid: "55",
          columnid: "209",
          value: 13,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 25 kg to be in Normal zone"
        },
        {
          rowid: "60",
          columnid: "152",
          value: 26,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 3 kg to be in Normal zone"
        },
        {
          rowid: "60",
          columnid: "155",
          value: 25,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "60",
          columnid: "158",
          value: 24,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "60",
          columnid: "161",
          value: 23,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "60",
          columnid: "164",
          value: 22,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "60",
          columnid: "167",
          value: 22,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "60",
          columnid: "170",
          value: 21,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "60",
          columnid: "173",
          value: 20,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "60",
          columnid: "176",
          value: 19,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "60",
          columnid: "179",
          value: 19,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "60",
          columnid: "182",
          value: 18,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 3 kg to be in Normal zone"
        },
        {
          rowid: "60",
          columnid: "185",
          value: 18,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 3 kg to be in Normal zone"
        },
        {
          rowid: "60",
          columnid: "188",
          value: 17,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 7 kg to be in Normal zone"
        },
        {
          rowid: "60",
          columnid: "191",
          value: 16,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 11 kg to be in Normal zone"
        },
        {
          rowid: "60",
          columnid: "194",
          value: 16,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 11 kg to be in Normal zone"
        },
        {
          rowid: "60",
          columnid: "197",
          value: 15,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 16 kg to be in Normal zone"
        },
        {
          rowid: "60",
          columnid: "200",
          value: 15,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 16 kg to be in Normal zone"
        },
        {
          rowid: "60",
          columnid: "203",
          value: 15,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 16 kg to be in Normal zone"
        },
        {
          rowid: "60",
          columnid: "206",
          value: 14,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 21 kg to be in Normal zone"
        },
        {
          rowid: "60",
          columnid: "209",
          value: 14,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 21 kg to be in Normal zone"
        },
        {
          rowid: "65",
          columnid: "152",
          value: 28,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 8 kg to be in Normal zone"
        },
        {
          rowid: "65",
          columnid: "155",
          value: 27,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 6 kg to be in Normal zone"
        },
        {
          rowid: "65",
          columnid: "158",
          value: 26,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 4 kg to be in Normal zone"
        },
        {
          rowid: "65",
          columnid: "161",
          value: 25,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "65",
          columnid: "164",
          value: 24,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "65",
          columnid: "167",
          value: 23,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "65",
          columnid: "170",
          value: 22,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "65",
          columnid: "173",
          value: 22,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "65",
          columnid: "176",
          value: 21,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "65",
          columnid: "179",
          value: 20,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "65",
          columnid: "182",
          value: 20,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "65",
          columnid: "185",
          value: 19,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "65",
          columnid: "188",
          value: 18,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 4 kg to be in Normal zone"
        },
        {
          rowid: "65",
          columnid: "191",
          value: 18,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 4 kg to be in Normal zone"
        },
        {
          rowid: "65",
          columnid: "194",
          value: 17,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 8 kg to be in Normal zone"
        },
        {
          rowid: "65",
          columnid: "197",
          value: 17,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 8 kg to be in Normal zone"
        },
        {
          rowid: "65",
          columnid: "200",
          value: 16,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 12 kg to be in Normal zone"
        },
        {
          rowid: "65",
          columnid: "203",
          value: 16,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 12 kg to be in Normal zone"
        },
        {
          rowid: "65",
          columnid: "206",
          value: 15,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 17 kg to be in Normal zone"
        },
        {
          rowid: "65",
          columnid: "209",
          value: 15,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 17 kg to be in Normal zone"
        },
        {
          rowid: "70",
          columnid: "152",
          value: 30,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 13 kg to be in Normal zone"
        },
        {
          rowid: "70",
          columnid: "155",
          value: 29,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 11 kg to be in Normal zone"
        },
        {
          rowid: "70",
          columnid: "158",
          value: 28,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 9 kg to be in Normal zone"
        },
        {
          rowid: "70",
          columnid: "161",
          value: 27,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 6 kg to be in Normal zone"
        },
        {
          rowid: "70",
          columnid: "164",
          value: 26,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 4 kg to be in Normal zone"
        },
        {
          rowid: "70",
          columnid: "167",
          value: 25,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "70",
          columnid: "170",
          value: 24,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "70",
          columnid: "173",
          value: 23,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "70",
          columnid: "176",
          value: 23,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "70",
          columnid: "179",
          value: 22,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "70",
          columnid: "182",
          value: 21,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "70",
          columnid: "185",
          value: 20,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "70",
          columnid: "188",
          value: 20,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "70",
          columnid: "191",
          value: 19,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "70",
          columnid: "194",
          value: 19,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "70",
          columnid: "197",
          value: 18,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 4 kg to be in Normal zone"
        },
        {
          rowid: "70",
          columnid: "200",
          value: 18,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 4 kg to be in Normal zone"
        },
        {
          rowid: "70",
          columnid: "203",
          value: 17,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 8 kg to be in Normal zone"
        },
        {
          rowid: "70",
          columnid: "206",
          value: 16,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 13 kg to be in Normal zone"
        },
        {
          rowid: "70",
          columnid: "209",
          value: 16,
          trlabel:
            "You are in Severe Thinness zone.{br} You need to increase 13 kg to be in Normal zone"
        },
        {
          rowid: "75",
          columnid: "152",
          value: 32,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 18 kg to be in Normal zone"
        },
        {
          rowid: "75",
          columnid: "155",
          value: 31,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 16 kg to be in Normal zone"
        },
        {
          rowid: "75",
          columnid: "158",
          value: 30,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 14 kg to be in Normal zone"
        },
        {
          rowid: "75",
          columnid: "161",
          value: 29,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 12 kg to be in Normal zone"
        },
        {
          rowid: "75",
          columnid: "164",
          value: 28,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 9 kg to be in Normal zone"
        },
        {
          rowid: "75",
          columnid: "167",
          value: 27,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 7 kg to be in Normal zone"
        },
        {
          rowid: "75",
          columnid: "170",
          value: 26,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 4 kg to be in Normal zone"
        },
        {
          rowid: "75",
          columnid: "173",
          value: 25,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "75",
          columnid: "176",
          value: 24,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "75",
          columnid: "179",
          value: 23,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "75",
          columnid: "182",
          value: 23,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "75",
          columnid: "185",
          value: 22,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "75",
          columnid: "188",
          value: 21,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "75",
          columnid: "191",
          value: 21,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "75",
          columnid: "194",
          value: 20,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "75",
          columnid: "197",
          value: 19,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "75",
          columnid: "200",
          value: 19,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "75",
          columnid: "203",
          value: 18,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 4 kg to be in Normal zone"
        },
        {
          rowid: "75",
          columnid: "206",
          value: 18,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 4 kg to be in Normal zone"
        },
        {
          rowid: "75",
          columnid: "209",
          value: 17,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 9 kg to be in Normal zone"
        },
        {
          rowid: "80",
          columnid: "152",
          value: 35,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 24 kg to be in Normal zone"
        },
        {
          rowid: "80",
          columnid: "155",
          value: 33,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 21 kg to be in Normal zone"
        },
        {
          rowid: "80",
          columnid: "158",
          value: 32,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 19 kg to be in Normal zone"
        },
        {
          rowid: "80",
          columnid: "161",
          value: 31,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 17 kg to be in Normal zone"
        },
        {
          rowid: "80",
          columnid: "164",
          value: 30,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 15 kg to be in Normal zone"
        },
        {
          rowid: "80",
          columnid: "167",
          value: 29,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 12 kg to be in Normal zone"
        },
        {
          rowid: "80",
          columnid: "170",
          value: 28,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 10 kg to be in Normal zone"
        },
        {
          rowid: "80",
          columnid: "173",
          value: 27,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 7 kg to be in Normal zone"
        },
        {
          rowid: "80",
          columnid: "176",
          value: 26,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 5 kg to be in Normal zone"
        },
        {
          rowid: "80",
          columnid: "179",
          value: 25,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "80",
          columnid: "182",
          value: 24,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "80",
          columnid: "185",
          value: 23,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "80",
          columnid: "188",
          value: 23,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "80",
          columnid: "191",
          value: 22,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "80",
          columnid: "194",
          value: 21,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "80",
          columnid: "197",
          value: 21,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "80",
          columnid: "200",
          value: 20,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "80",
          columnid: "203",
          value: 19,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "80",
          columnid: "206",
          value: 19,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "80",
          columnid: "209",
          value: 18,
          trlabel:
            "You are in Moderate Thinness zone.{br} You need to increase 4 kg to be in Normal zone"
        },
        {
          rowid: "85",
          columnid: "152",
          value: 37,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 29 kg to be in Normal zone"
        },
        {
          rowid: "85",
          columnid: "155",
          value: 35,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 25 kg to be in Normal zone"
        },
        {
          rowid: "85",
          columnid: "158",
          value: 34,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 24 kg to be in Normal zone"
        },
        {
          rowid: "85",
          columnid: "161",
          value: 33,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 22 kg to be in Normal zone"
        },
        {
          rowid: "85",
          columnid: "164",
          value: 32,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 20 kg to be in Normal zone"
        },
        {
          rowid: "85",
          columnid: "167",
          value: 30,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 16 kg to be in Normal zone"
        },
        {
          rowid: "85",
          columnid: "170",
          value: 29,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 13 kg to be in Normal zone"
        },
        {
          rowid: "85",
          columnid: "173",
          value: 28,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 11 kg to be in Normal zone"
        },
        {
          rowid: "85",
          columnid: "176",
          value: 27,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 8 kg to be in Normal zone"
        },
        {
          rowid: "85",
          columnid: "179",
          value: 27,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 8 kg to be in Normal zone"
        },
        {
          rowid: "85",
          columnid: "182",
          value: 26,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 5 kg to be in Normal zone"
        },
        {
          rowid: "85",
          columnid: "185",
          value: 25,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "85",
          columnid: "188",
          value: 24,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "85",
          columnid: "191",
          value: 23,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "85",
          columnid: "194",
          value: 23,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "85",
          columnid: "197",
          value: 22,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "85",
          columnid: "200",
          value: 21,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "85",
          columnid: "203",
          value: 21,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "85",
          columnid: "206",
          value: 20,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "85",
          columnid: "209",
          value: 19,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "90",
          columnid: "152",
          value: 39,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 33 kg to be in Normal zone"
        },
        {
          rowid: "90",
          columnid: "155",
          value: 37,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 30 kg to be in Normal zone"
        },
        {
          rowid: "90",
          columnid: "158",
          value: 36,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 29 kg to be in Normal zone"
        },
        {
          rowid: "90",
          columnid: "161",
          value: 35,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 27 kg to be in Normal zone"
        },
        {
          rowid: "90",
          columnid: "164",
          value: 33,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 23 kg to be in Normal zone"
        },
        {
          rowid: "90",
          columnid: "167",
          value: 32,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 21 kg to be in Normal zone"
        },
        {
          rowid: "90",
          columnid: "170",
          value: 31,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 19 kg to be in Normal zone"
        },
        {
          rowid: "90",
          columnid: "173",
          value: 30,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 16 kg to be in Normal zone"
        },
        {
          rowid: "90",
          columnid: "176",
          value: 29,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 14 kg to be in Normal zone"
        },
        {
          rowid: "90",
          columnid: "179",
          value: 28,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 11 kg to be in Normal zone"
        },
        {
          rowid: "90",
          columnid: "182",
          value: 27,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 8 kg to be in Normal zone"
        },
        {
          rowid: "90",
          columnid: "185",
          value: 26,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 5 kg to be in Normal zone"
        },
        {
          rowid: "90",
          columnid: "188",
          value: 25,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "90",
          columnid: "191",
          value: 25,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "90",
          columnid: "194",
          value: 24,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "90",
          columnid: "197",
          value: 23,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "90",
          columnid: "200",
          value: 23,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "90",
          columnid: "203",
          value: 22,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "90",
          columnid: "206",
          value: 21,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "90",
          columnid: "209",
          value: 21,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "95",
          columnid: "152",
          value: 41,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 38 kg to be in Normal zone"
        },
        {
          rowid: "95",
          columnid: "155",
          value: 40,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 37 kg to be in Normal zone"
        },
        {
          rowid: "95",
          columnid: "158",
          value: 38,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 34 kg to be in Normal zone"
        },
        {
          rowid: "95",
          columnid: "161",
          value: 37,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 32 kg to be in Normal zone"
        },
        {
          rowid: "95",
          columnid: "164",
          value: 35,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 28 kg to be in Normal zone"
        },
        {
          rowid: "95",
          columnid: "167",
          value: 34,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 27 kg to be in Normal zone"
        },
        {
          rowid: "95",
          columnid: "170",
          value: 33,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 24 kg to be in Normal zone"
        },
        {
          rowid: "95",
          columnid: "173",
          value: 32,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 22 kg to be in Normal zone"
        },
        {
          rowid: "95",
          columnid: "176",
          value: 31,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 20 kg to be in Normal zone"
        },
        {
          rowid: "95",
          columnid: "179",
          value: 30,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 17 kg to be in Normal zone"
        },
        {
          rowid: "95",
          columnid: "182",
          value: 29,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 15 kg to be in Normal zone"
        },
        {
          rowid: "95",
          columnid: "185",
          value: 28,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 12 kg to be in Normal zone"
        },
        {
          rowid: "95",
          columnid: "188",
          value: 27,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 9 kg to be in Normal zone"
        },
        {
          rowid: "95",
          columnid: "191",
          value: 26,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 5 kg to be in Normal zone"
        },
        {
          rowid: "95",
          columnid: "194",
          value: 25,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "95",
          columnid: "197",
          value: 24,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "95",
          columnid: "200",
          value: 24,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "95",
          columnid: "203",
          value: 23,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "95",
          columnid: "206",
          value: 22,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "95",
          columnid: "209",
          value: 22,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "100",
          columnid: "152",
          value: 43,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 43 kg to be in Normal zone"
        },
        {
          rowid: "100",
          columnid: "155",
          value: 42,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 42 kg to be in Normal zone"
        },
        {
          rowid: "100",
          columnid: "158",
          value: 40,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 39 kg to be in Normal zone"
        },
        {
          rowid: "100",
          columnid: "161",
          value: 39,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 37 kg to be in Normal zone"
        },
        {
          rowid: "100",
          columnid: "164",
          value: 37,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 34 kg to be in Normal zone"
        },
        {
          rowid: "100",
          columnid: "167",
          value: 36,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 32 kg to be in Normal zone"
        },
        {
          rowid: "100",
          columnid: "170",
          value: 35,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 30 kg to be in Normal zone"
        },
        {
          rowid: "100",
          columnid: "173",
          value: 33,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 26 kg to be in Normal zone"
        },
        {
          rowid: "100",
          columnid: "176",
          value: 32,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 23 kg to be in Normal zone"
        },
        {
          rowid: "100",
          columnid: "179",
          value: 31,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 21 kg to be in Normal zone"
        },
        {
          rowid: "100",
          columnid: "182",
          value: 30,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 18 kg to be in Normal zone"
        },
        {
          rowid: "100",
          columnid: "185",
          value: 29,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 16 kg to be in Normal zone"
        },
        {
          rowid: "100",
          columnid: "188",
          value: 28,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 12 kg to be in Normal zone"
        },
        {
          rowid: "100",
          columnid: "191",
          value: 27,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 9 kg to be in Normal zone"
        },
        {
          rowid: "100",
          columnid: "194",
          value: 27,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 9 kg to be in Normal zone"
        },
        {
          rowid: "100",
          columnid: "197",
          value: 26,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 6 kg to be in Normal zone"
        },
        {
          rowid: "100",
          columnid: "200",
          value: 25,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "100",
          columnid: "203",
          value: 24,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "100",
          columnid: "206",
          value: 24,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "100",
          columnid: "209",
          value: 23,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "105",
          columnid: "152",
          value: 45,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 48 kg to be in Normal zone"
        },
        {
          rowid: "105",
          columnid: "155",
          value: 44,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 47 kg to be in Normal zone"
        },
        {
          rowid: "105",
          columnid: "158",
          value: 42,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 44 kg to be in Normal zone"
        },
        {
          rowid: "105",
          columnid: "161",
          value: 41,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 42 kg to be in Normal zone"
        },
        {
          rowid: "105",
          columnid: "164",
          value: 39,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 39 kg to be in Normal zone"
        },
        {
          rowid: "105",
          columnid: "167",
          value: 38,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 37 kg to be in Normal zone"
        },
        {
          rowid: "105",
          columnid: "170",
          value: 36,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 34 kg to be in Normal zone"
        },
        {
          rowid: "105",
          columnid: "173",
          value: 35,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 31 kg to be in Normal zone"
        },
        {
          rowid: "105",
          columnid: "176",
          value: 34,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 29 kg to be in Normal zone"
        },
        {
          rowid: "105",
          columnid: "179",
          value: 33,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 27 kg to be in Normal zone"
        },
        {
          rowid: "105",
          columnid: "182",
          value: 32,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 25 kg to be in Normal zone"
        },
        {
          rowid: "105",
          columnid: "185",
          value: 31,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 22 kg to be in Normal zone"
        },
        {
          rowid: "105",
          columnid: "188",
          value: 30,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 19 kg to be in Normal zone"
        },
        {
          rowid: "105",
          columnid: "191",
          value: 29,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 16 kg to be in Normal zone"
        },
        {
          rowid: "105",
          columnid: "194",
          value: 28,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 13 kg to be in Normal zone"
        },
        {
          rowid: "105",
          columnid: "197",
          value: 27,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 10 kg to be in Normal zone"
        },
        {
          rowid: "105",
          columnid: "200",
          value: 26,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 6 kg to be in Normal zone"
        },
        {
          rowid: "105",
          columnid: "203",
          value: 25,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "105",
          columnid: "206",
          value: 25,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "105",
          columnid: "209",
          value: 24,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "110",
          columnid: "152",
          value: 48,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 54 kg to be in Normal zone"
        },
        {
          rowid: "110",
          columnid: "155",
          value: 46,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 51 kg to be in Normal zone"
        },
        {
          rowid: "110",
          columnid: "158",
          value: 44,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 49 kg to be in Normal zone"
        },
        {
          rowid: "110",
          columnid: "161",
          value: 42,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 46 kg to be in Normal zone"
        },
        {
          rowid: "110",
          columnid: "164",
          value: 41,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 44 kg to be in Normal zone"
        },
        {
          rowid: "110",
          columnid: "167",
          value: 39,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 41 kg to be in Normal zone"
        },
        {
          rowid: "110",
          columnid: "170",
          value: 38,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 39 kg to be in Normal zone"
        },
        {
          rowid: "110",
          columnid: "173",
          value: 37,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 37 kg to be in Normal zone"
        },
        {
          rowid: "110",
          columnid: "176",
          value: 36,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 35 kg to be in Normal zone"
        },
        {
          rowid: "110",
          columnid: "179",
          value: 34,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 31 kg to be in Normal zone"
        },
        {
          rowid: "110",
          columnid: "182",
          value: 33,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 28 kg to be in Normal zone"
        },
        {
          rowid: "110",
          columnid: "185",
          value: 32,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 26 kg to be in Normal zone"
        },
        {
          rowid: "110",
          columnid: "188",
          value: 31,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 23 kg to be in Normal zone"
        },
        {
          rowid: "110",
          columnid: "191",
          value: 30,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 20 kg to be in Normal zone"
        },
        {
          rowid: "110",
          columnid: "194",
          value: 29,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 17 kg to be in Normal zone"
        },
        {
          rowid: "110",
          columnid: "197",
          value: 28,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 14 kg to be in Normal zone"
        },
        {
          rowid: "110",
          columnid: "200",
          value: 28,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 14 kg to be in Normal zone"
        },
        {
          rowid: "110",
          columnid: "203",
          value: 27,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 10 kg to be in Normal zone"
        },
        {
          rowid: "110",
          columnid: "206",
          value: 26,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 6 kg to be in Normal zone"
        },
        {
          rowid: "110",
          columnid: "209",
          value: 25,
          trlabel: "You are in Normal zone"
        },
        {
          rowid: "115",
          columnid: "152",
          value: 50,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 59 kg to be in Normal zone"
        },
        {
          rowid: "115",
          columnid: "155",
          value: 48,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 56 kg to be in Normal zone"
        },
        {
          rowid: "115",
          columnid: "158",
          value: 46,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 54 kg to be in Normal zone"
        },
        {
          rowid: "115",
          columnid: "161",
          value: 44,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 51 kg to be in Normal zone"
        },
        {
          rowid: "115",
          columnid: "164",
          value: 43,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 49 kg to be in Normal zone"
        },
        {
          rowid: "115",
          columnid: "167",
          value: 41,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 46 kg to be in Normal zone"
        },
        {
          rowid: "115",
          columnid: "170",
          value: 40,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 45 kg to be in Normal zone"
        },
        {
          rowid: "115",
          columnid: "173",
          value: 38,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 41 kg to be in Normal zone"
        },
        {
          rowid: "115",
          columnid: "176",
          value: 37,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 39 kg to be in Normal zone"
        },
        {
          rowid: "115",
          columnid: "179",
          value: 36,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 37 kg to be in Normal zone"
        },
        {
          rowid: "115",
          columnid: "182",
          value: 35,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 34 kg to be in Normal zone"
        },
        {
          rowid: "115",
          columnid: "185",
          value: 34,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 32 kg to be in Normal zone"
        },
        {
          rowid: "115",
          columnid: "188",
          value: 33,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 30 kg to be in Normal zone"
        },
        {
          rowid: "115",
          columnid: "191",
          value: 32,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 27 kg to be in Normal zone"
        },
        {
          rowid: "115",
          columnid: "194",
          value: 31,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 24 kg to be in Normal zone"
        },
        {
          rowid: "115",
          columnid: "197",
          value: 30,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 21 kg to be in Normal zone"
        },
        {
          rowid: "115",
          columnid: "200",
          value: 29,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 18 kg to be in Normal zone"
        },
        {
          rowid: "115",
          columnid: "203",
          value: 28,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 14 kg to be in Normal zone"
        },
        {
          rowid: "115",
          columnid: "206",
          value: 27,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 11 kg to be in Normal zone"
        },
        {
          rowid: "115",
          columnid: "209",
          value: 26,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 7 kg to be in Normal zone"
        },
        {
          rowid: "120",
          columnid: "152",
          value: 52,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 63 kg to be in Normal zone"
        },
        {
          rowid: "120",
          columnid: "155",
          value: 50,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 61 kg to be in Normal zone"
        },
        {
          rowid: "120",
          columnid: "158",
          value: 48,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 59 kg to be in Normal zone"
        },
        {
          rowid: "120",
          columnid: "161",
          value: 46,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 56 kg to be in Normal zone"
        },
        {
          rowid: "120",
          columnid: "164",
          value: 45,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 55 kg to be in Normal zone"
        },
        {
          rowid: "120",
          columnid: "167",
          value: 43,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 52 kg to be in Normal zone"
        },
        {
          rowid: "120",
          columnid: "170",
          value: 42,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 50 kg to be in Normal zone"
        },
        {
          rowid: "120",
          columnid: "173",
          value: 40,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 46 kg to be in Normal zone"
        },
        {
          rowid: "120",
          columnid: "176",
          value: 39,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 45 kg to be in Normal zone"
        },
        {
          rowid: "120",
          columnid: "179",
          value: 37,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 41 kg to be in Normal zone"
        },
        {
          rowid: "120",
          columnid: "182",
          value: 36,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 38 kg to be in Normal zone"
        },
        {
          rowid: "120",
          columnid: "185",
          value: 35,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 36 kg to be in Normal zone"
        },
        {
          rowid: "120",
          columnid: "188",
          value: 34,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 34 kg to be in Normal zone"
        },
        {
          rowid: "120",
          columnid: "191",
          value: 33,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 31 kg to be in Normal zone"
        },
        {
          rowid: "120",
          columnid: "194",
          value: 32,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 28 kg to be in Normal zone"
        },
        {
          rowid: "120",
          columnid: "197",
          value: 31,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 25 kg to be in Normal zone"
        },
        {
          rowid: "120",
          columnid: "200",
          value: 30,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 22 kg to be in Normal zone"
        },
        {
          rowid: "120",
          columnid: "203",
          value: 29,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 19 kg to be in Normal zone"
        },
        {
          rowid: "120",
          columnid: "206",
          value: 28,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 15 kg to be in Normal zone"
        },
        {
          rowid: "120",
          columnid: "209",
          value: 27,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 11 kg to be in Normal zone"
        },
        {
          rowid: "125",
          columnid: "152",
          value: 54,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 68 kg to be in Normal zone"
        },
        {
          rowid: "125",
          columnid: "155",
          value: 52,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 66 kg to be in Normal zone"
        },
        {
          rowid: "125",
          columnid: "158",
          value: 50,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 64 kg to be in Normal zone"
        },
        {
          rowid: "125",
          columnid: "161",
          value: 48,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 61 kg to be in Normal zone"
        },
        {
          rowid: "125",
          columnid: "164",
          value: 46,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 58 kg to be in Normal zone"
        },
        {
          rowid: "125",
          columnid: "167",
          value: 45,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 57 kg to be in Normal zone"
        },
        {
          rowid: "125",
          columnid: "170",
          value: 43,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 54 kg to be in Normal zone"
        },
        {
          rowid: "125",
          columnid: "173",
          value: 42,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 52 kg to be in Normal zone"
        },
        {
          rowid: "125",
          columnid: "176",
          value: 40,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 48 kg to be in Normal zone"
        },
        {
          rowid: "125",
          columnid: "179",
          value: 39,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 46 kg to be in Normal zone"
        },
        {
          rowid: "125",
          columnid: "182",
          value: 38,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 44 kg to be in Normal zone"
        },
        {
          rowid: "125",
          columnid: "185",
          value: 37,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 42 kg to be in Normal zone"
        },
        {
          rowid: "125",
          columnid: "188",
          value: 35,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 37 kg to be in Normal zone"
        },
        {
          rowid: "125",
          columnid: "191",
          value: 34,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 35 kg to be in Normal zone"
        },
        {
          rowid: "125",
          columnid: "194",
          value: 33,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 32 kg to be in Normal zone"
        },
        {
          rowid: "125",
          columnid: "197",
          value: 32,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 29 kg to be in Normal zone"
        },
        {
          rowid: "125",
          columnid: "200",
          value: 31,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 26 kg to be in Normal zone"
        },
        {
          rowid: "125",
          columnid: "203",
          value: 30,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 23 kg to be in Normal zone"
        },
        {
          rowid: "125",
          columnid: "206",
          value: 29,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 19 kg to be in Normal zone"
        },
        {
          rowid: "125",
          columnid: "209",
          value: 29,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 19 kg to be in Normal zone"
        },
        {
          rowid: "130",
          columnid: "152",
          value: 56,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 73 kg to be in Normal zone"
        },
        {
          rowid: "130",
          columnid: "155",
          value: 54,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 71 kg to be in Normal zone"
        },
        {
          rowid: "130",
          columnid: "158",
          value: 52,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 69 kg to be in Normal zone"
        },
        {
          rowid: "130",
          columnid: "161",
          value: 50,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 66 kg to be in Normal zone"
        },
        {
          rowid: "130",
          columnid: "164",
          value: 48,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 64 kg to be in Normal zone"
        },
        {
          rowid: "130",
          columnid: "167",
          value: 47,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 62 kg to be in Normal zone"
        },
        {
          rowid: "130",
          columnid: "170",
          value: 45,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 59 kg to be in Normal zone"
        },
        {
          rowid: "130",
          columnid: "173",
          value: 43,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 56 kg to be in Normal zone"
        },
        {
          rowid: "130",
          columnid: "176",
          value: 42,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 54 kg to be in Normal zone"
        },
        {
          rowid: "130",
          columnid: "179",
          value: 41,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 52 kg to be in Normal zone"
        },
        {
          rowid: "130",
          columnid: "182",
          value: 39,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 48 kg to be in Normal zone"
        },
        {
          rowid: "130",
          columnid: "185",
          value: 38,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 46 kg to be in Normal zone"
        },
        {
          rowid: "130",
          columnid: "188",
          value: 37,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 44 kg to be in Normal zone"
        },
        {
          rowid: "130",
          columnid: "191",
          value: 36,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 42 kg to be in Normal zone"
        },
        {
          rowid: "130",
          columnid: "194",
          value: 35,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 39 kg to be in Normal zone"
        },
        {
          rowid: "130",
          columnid: "197",
          value: 33,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 33 kg to be in Normal zone"
        },
        {
          rowid: "130",
          columnid: "200",
          value: 33,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 33 kg to be in Normal zone"
        },
        {
          rowid: "130",
          columnid: "203",
          value: 32,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 30 kg to be in Normal zone"
        },
        {
          rowid: "130",
          columnid: "206",
          value: 31,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 27 kg to be in Normal zone"
        },
        {
          rowid: "130",
          columnid: "209",
          value: 30,
          trlabel:
            "You are in Overweight zone.{br} You need to reduce 24 kg to be in Normal zone"
        },
        {
          rowid: "135",
          columnid: "152",
          value: 58,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 78 kg to be in Normal zone"
        },
        {
          rowid: "135",
          columnid: "155",
          value: 56,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 76 kg to be in Normal zone"
        },
        {
          rowid: "135",
          columnid: "158",
          value: 54,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 74 kg to be in Normal zone"
        },
        {
          rowid: "135",
          columnid: "161",
          value: 52,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 71 kg to be in Normal zone"
        },
        {
          rowid: "135",
          columnid: "164",
          value: 50,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 69 kg to be in Normal zone"
        },
        {
          rowid: "135",
          columnid: "167",
          value: 48,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 66 kg to be in Normal zone"
        },
        {
          rowid: "135",
          columnid: "170",
          value: 47,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 65 kg to be in Normal zone"
        },
        {
          rowid: "135",
          columnid: "173",
          value: 45,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 61 kg to be in Normal zone"
        },
        {
          rowid: "135",
          columnid: "176",
          value: 44,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 60 kg to be in Normal zone"
        },
        {
          rowid: "135",
          columnid: "179",
          value: 42,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 56 kg to be in Normal zone"
        },
        {
          rowid: "135",
          columnid: "182",
          value: 41,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 54 kg to be in Normal zone"
        },
        {
          rowid: "135",
          columnid: "185",
          value: 39,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 50 kg to be in Normal zone"
        },
        {
          rowid: "135",
          columnid: "188",
          value: 38,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 48 kg to be in Normal zone"
        },
        {
          rowid: "135",
          columnid: "191",
          value: 37,
          trlabel:
            "You are in Obese Class II.{br} You need to reduce 46 kg to be in Normal zone"
        },
        {
          rowid: "135",
          columnid: "194",
          value: 36,
          trlabel:
            "You are in Obese Class III.{br} You need to reduce 43 kg to be in Normal zone"
        },
        {
          rowid: "135",
          columnid: "197",
          value: 35,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 40 kg to be in Normal zone"
        },
        {
          rowid: "135",
          columnid: "200",
          value: 34,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 38 kg to be in Normal zone"
        },
        {
          rowid: "135",
          columnid: "203",
          value: 33,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 35 kg to be in Normal zone"
        },
        {
          rowid: "135",
          columnid: "206",
          value: 32,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 32 kg to be in Normal zone"
        },
        {
          rowid: "135",
          columnid: "209",
          value: 31,
          trlabel:
            "You are in Obese Class I.{br} You need to reduce 28 kg to be in Normal zone"
        }
      ]
    }
  ],
  colorrange: {
    gradient: "0",
    minvalue: "0",
    code: "E24B1A",
    startlabel: "Severe Thinness",
    endlabel: "Obese Class III",
    color: [
      {
        code: "0155E8",
        minvalue: "0",
        maxvalue: "16",
        label: "Severe Thinness"
      },
      {
        code: "2BA8E8",
        minvalue: "17",
        maxvalue: "18",
        label: "Moderate Thinness"
      },
      {
        code: "21C451",
        minvalue: "18.5",
        maxvalue: "25",
        label: "Normal"
      },
      {
        code: "FFD315",
        minvalue: "25.5",
        maxvalue: "30",
        label: "Overweight"
      },
      {
        code: "E8990C",
        minvalue: "30.5",
        maxvalue: "35",
        label: "Obese Class I"
      },
      {
        code: "C24314",
        minvalue: "35.5",
        maxvalue: "40",
        label: "Obese Class II"
      },
      {
        code: "FF0000",
        minvalue: "40.5",
        maxvalue: "100",
        label: "Obese Class III"
      }
    ]
  }
};

export default {
  name: 'heatmap',
  components: {
    fusioncharts: FCComponent
  },
  data: () => ({
    type: "heatmap",
    width: "100%",
    height: "100%",
    dataFormat: "json",
    dataSource
  })
};


</script>

