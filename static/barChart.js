let chartOptions = {
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

  export function buildWeekdayChart(data, title, elemId){
    const mySongs = Object.entries(data).reduce((acc, [k,v]) => {
        acc[k] =v
        return acc
     }, [0,0,0,0,0,0,0])
     
     options =  Object.assign({}, chartOptions)
     
     options.series[0].data = mySongs
     options.title.text = title
 
     const chart = new ApexCharts(document.querySelector(elemId), options);
     chart.render();
  }
