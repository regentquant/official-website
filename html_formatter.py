import pyperclip


def fear_and_greed_index():
    input = pyperclip.paste().split('\n')

    a_string = ''
    b_string = ''

    for i in input:
        list = i.split('\t')
        a_string = f"{a_string}{list[0]}\n"
        b_string = f"{b_string}{list[1]}\n"

    html_content = """<!doctype html>
<html lang="en">
   <head>
           <!-- Google tag (gtag.js) -->
      <script async src="https://www.googletagmanager.com/gtag/js?id=G-LYVSDS633M"></script>
      <script>
         window.dataLayer = window.dataLayer || [];
         function gtag(){dataLayer.push(arguments);}
         gtag('js', new Date());
         gtag('config', 'G-LYVSDS633M');
      </script>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>SPY Capital Trend</title>
      <link rel="icon" type="image/x-icon" href="favicon_1.png">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Saira+Condensed:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">
      <script src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/0.5.0-beta4/html2canvas.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.4.0/jspdf.umd.min.js"></script>
      <link rel="stylesheet" href="chart-styles.css">
   </head>
   <body>
      <section>
         <img id="site-logo" src="REGENTQUANT.svg">
         <h1 class="chart-title">Regent Quant SPY Capital Trend</h1>
         <h2 class="go-back-to-home-screen"><a href="https://www.regentquant.com">Go Back To Home Screen</a></h2>
         <h2>How to use: Investors can predict future price trend by looking at capital trend. Candlestick chart shows underlying stock's historical adjusted OHLC price. Line chart shows daily block order amount (Unit$). Here block order stands for the largest 30% of orders in terms of turnover over the past 200 days. The data is estimated by algorithm and for reference only.</h2>
        <button id="download-chart">Save Chart</button>
      </section>
      <!-- Fund NAV Chart -->
      <div id="container"></div>
      <section id="footer"></section>
      <script type="text/javascript">
        // Lightweight Charts™ Example: Two Price Scales
// https://tradingview.github.io/lightweight-charts/tutorials/how_to/two-price-scales

const chartOptions = {
	rightPriceScale: {
		visible: true,
	},
	leftPriceScale: {
		visible: true,
	},
	layout: {
		textColor: 'black',
		background: { type: 'solid', color: 'white' },
	},
	crosshair: {
		mode: 0, // CrosshairMode.Normal
	},
};
/** @type {import('lightweight-charts').IChartApi} */
const chart = LightweightCharts.createChart(document.getElementById('container'), chartOptions);
const baselineSeries = chart.addBaselineSeries({ baseValue: { type: 'price', price: 0 }, topLineColor: 'rgba( 38, 166, 154, 1)', topFillColor1: 'rgba( 38, 166, 154, 0.28)', topFillColor2: 'rgba( 38, 166, 154, 0.05)', bottomLineColor: 'rgba( 239, 83, 80, 1)', bottomFillColor1: 'rgba( 239, 83, 80, 0.05)', bottomFillColor2: 'rgba( 239, 83, 80, 0.28)' });
const data = [@REPLACE_A];
baselineSeries.setData(data);


const candlestickSeries = chart.addCandlestickSeries({
	priceScaleId: 'left',
	upColor: '#26a69a', downColor: '#ef5350', borderVisible: false,
	wickUpColor: '#26a69a', wickDownColor: '#ef5350',
});

candlestickSeries.setData([@REPLACE_B]);

chart.timeScale().fitContent();

         chart.applyOptions({
                         layout: {
                             fontFamily: "'Saira Condensed', sans-serif",
                         },
                     });

         window.addEventListener('resize', resizeChart);

         function resizeChart() {
         const container = document.getElementById('container');
         chart.resize(
         container.offsetWidth,
         container.offsetHeight
         );
         }
         resizeChart();
         document.getElementById('download-chart').addEventListener('click', function() {
         const chartContainer = document.getElementById('container');

         html2canvas(chartContainer, {
         scale: 5  // Increase this value for higher resolution
         }).then(canvas => {
         const link = document.createElement('a');
         link.href = canvas.toDataURL('image/png');
         link.download = 'chart_high_res.png';
         link.click();
         });
         });

      </script>
   </body>
</html>
""".replace("@REPLACE_A",a_string).replace("@REPLACE_B",b_string)
    file_path = 'capital-trend-spy.html'

    # Writing the HTML content to the file
    with open(file_path, 'w') as file:
        file.write(html_content)

    file.close()


fear_and_greed_index()