// import { buildWeekdayChart }  from './barChart.js';

var options = {
    series: [{
    name: 'Songs',
    data: [],//[2.3, 3.1, 4.0, 10.1, 4.0, 3.6, 3.2]
  }],
    chart: {
    height: 350,
    type: 'bar',
  },
  plotOptions: {
    bar: {
      dataLabels: {
        position: 'top', // top, center, bottom
      },
    }
  },
//   dataLabels: {
//     enabled: true,
//     formatter: function (val) {
//       return val + " songs"
//     },
//     offsetY: -20,
//     style: {
//       fontSize: '12px',
//       colors: ["#304758"]
//     }
//   },

  xaxis: {
    categories: ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"],
    position: 'top',
    axisBorder: {
      show: false
    },
    axisTicks: {
      show: false
    },
    crosshairs: {
      fill: {
        type: 'gradient',
        gradient: {
          colorFrom: '#D8E3F0',
          colorTo: '#BED1E6',
          stops: [0, 100],
          opacityFrom: 0.4,
          opacityTo: 0.5,
        }
      }
    },
    tooltip: {
      enabled: true,
    }
  },
  yaxis: {
    axisBorder: {
      show: false
    },
    axisTicks: {
      show: false,
    },
    labels: {
      show: false,
      formatter: function (val) {
        return val + " songs";
      }
    }

  },
  title: {
    text: 'Songs listened to by Weekday',
    floating: true,
    offsetY: 330,
    align: 'center',
    style: {
      color: '#444'
    }
  }
  };

const href = window.location.href.split("/")
const user = href[href.length - 1]

fetch(`/api/mysongs/${user}`)
  .then(res => res.json())
  .then(json => {

    // buildWeekdayChart(json["month_songs"], "Songs list to over last month", '#wd-month')

    // console.log(json)
    // const mySongs = Object.entries(json["month_songs"]).reduce((acc, [k,v]) => {
    //    acc[k] =v
    //    return acc
    // }, [0,0,0,0,0,0,0])
    // options.series[0].data = mySongs

    // const chart = new ApexCharts(document.querySelector("#wd-month"), options);
    // chart.render();

  })




