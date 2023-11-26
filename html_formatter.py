import pyperclip


def capital_trend_spy():
    ticker = ""

    input = pyperclip.paste().split('\n')

    a_string = ''
    b_string = ''

    for i in input:
        if "{" not in i:
            ticker = i.strip()
        else:
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
      <title>@replace_with_ticker Capital Trend</title>
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
         <img id="site-logo" src="regentquant-logo-two-colors.svg">
         <h1 class="chart-title">Regentquant @replace_with_ticker Capital Trend</h1>
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
""".replace("@REPLACE_A",a_string).replace("@REPLACE_B",b_string).replace("@replace_with_ticker", ticker.upper())
    file_path = f'capital-trend-{ticker}.html'

    # Writing the HTML content to the file
    with open(file_path, 'w') as file:
        file.write(html_content)

    file.close()
    print(ticker)

def magazine_formatter():
    magazine_name, magazine_date, magazine_name_text, copied_url, copied_url_b = "", "", "", "", ""

    input = "2" # 1 for barrons. 2 for the economist
    magazine_date = "20231125"
    copied_url = "https://drive.google.com/open?id=19SqlM8nvx1ziZBRZaHjy6Y4UAnQk8sUe&usp=drive_copy"

    copied_url_b = copied_url.replace("open?", "uc?export=download&")

    if input == "1":

        magazine_name = "Barrons"
        magazine_name_text = "Barron's"

    elif input == "2":

        magazine_name = "The_Economist"
        magazine_name_text = "The Economist"


    string = f"""                                  <!-- File Start -->
                  <div class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
                     <div class="card">
                        <img src="{magazine_name}_Covers/{magazine_name}_{magazine_date}.jpeg" alt="{magazine_name}_{magazine_date}.jpeg" class="card-img-top">
                        <div class="card-body text-center">
                           <h5 class="card-title">
                              {magazine_name_text}<br></br>
                              <p>{magazine_date[:4]}-{magazine_date[4:6]}-{magazine_date[6:9]}</p>
                           </h5>
                           <a href="{copied_url}" class="btn btn-dark" style="margin-top: 10px; margin-bottom: -1px; background: black; border-width: 0px; background: white; color: #333333; border-width: 1px; border-color: #333333">
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-google" viewBox="0 0 16 16">
  <path d="M15.545 6.558a9.42 9.42 0 0 1 .139 1.626c0 2.434-.87 4.492-2.384 5.885h.002C11.978 15.292 10.158 16 8 16A8 8 0 1 1 8 0a7.689 7.689 0 0 1 5.352 2.082l-2.284 2.284A4.347 4.347 0 0 0 8 3.166c-2.087 0-3.86 1.408-4.492 3.304a4.792 4.792 0 0 0 0 3.063h.003c.635 1.893 2.405 3.301 4.492 3.301 1.078 0 2.004-.276 2.722-.764h-.003a3.702 3.702 0 0 0 1.599-2.431H8v-3.08h7.545z"/>
</svg>                              Preview
                           </a>
                           <br>
                           <a href="{copied_url_b}" class="btn btn-dark" style="margin-top: 10px; margin-bottom: -1px; background: black; border-width: 0px">
                              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-download" viewBox="0 0 16 16">
                                 <path d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5z"/>
                                 <path d="M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3z"/>
                              </svg>
                              Download
                           </a>
                        </div>
                     </div>
                  </div>
                  <!-- File End -->"""

    pyperclip.copy(string)
    print(string)



input = pyperclip.paste().split('\n')


a_string = ''
b_string = ''

for i in input:
    if "{" not in i:
        ticker = i.strip()
    else:
        list = i.split('\t')
        a_string = f"{a_string}{list[0]}\n"
        b_string = f"{b_string}{list[1]}\n"


capital_trend_spy()