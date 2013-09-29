function load_search_num_chart() {
  $('#search_num_chart').highcharts({
         credits: {
          enabled: false
          },
          title: {
              text: '搜索次数--时间',
              x: -20 //center
          },
          xAxis: {
              categories: date_list
          },
          yAxis: {
              title: {
                  text: '搜索次数'
              },
          },
          legend: {
              layout: 'vertical',
              align: 'right',
              verticalAlign: 'middle',
              borderWidth: 0
          },
          series: [{
              name: '搜索次数',
              data: search_num_list
          }]
      });
}

function load_click_rate_chart() {
  $('#click_rate_chart').highcharts({
         credits: {
          enabled: false
          },
          title: {
              text: '点击率--时间',
              x: -20 //center
          },
          xAxis: {
              categories: date_list
          },
          yAxis: {
              title: {
                  text: '点击率'
              },
          },
          legend: {
              layout: 'vertical',
              align: 'right',
              verticalAlign: 'middle',
              borderWidth: 0
          },
          series: [{
              name: '点击率',
              data: click_rate_list
          }]
      });
}


