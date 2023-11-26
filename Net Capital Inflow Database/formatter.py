import pyperclip
import requests
import pyperclip
import os


def main():

    api_key = "ezBrk47F0tOiUtSZU7KevlNnxEEwPgIs"
    data = ''
    # Split the data by lines and then by tabs
    lines = data.split('\n')
    headers = lines[0].split('\t')
    columns = {header: [] for header in headers}

    # Populate the dictionary with data
    for line in lines[1:]:
        values = line.split('\t')
        for header, value in zip(headers, values):
            columns[header].append(value)

    keys = [i for i in columns.keys()]

    for i in keys:

        if i != "Date":

            total_null = 0
            date_list = []
            nci_list = []
            for a in columns[i]:
                if a == "null":
                    total_null = total_null + 1

            if total_null > 0:
                date_list = (columns['Date'][total_null:])
                nci_list = (columns[i][total_null:])
            else:
                date_list = columns['Date']
                nci_list = columns[i]
            # Start Date & End Date
            start_date = date_list[0]
            end_date = date_list[-1]
            print(f"{start_date}\t{end_date}")

            print(i)
            # Grabbing OHLC Data from Polygon
            ticker = i.split(':')[1]
            data = requests.get(
                f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{start_date}/{end_date}?adjusted=true&sort=asc&limit=50000&apiKey={api_key}")
            data = data.json()['results']

            fs = ''
            ohlc_html_list = []
            final_ohlc_html_list = []
            final_nci_html_list = []
            for a in data:

                html = "{time:'@replace_with_date',open:,high:,low:,close:},"
                html = html.replace('open:',f'open:{a["o"]}').replace('high:',f'high:{a["h"]}')
                html = html.replace('low:',f'low:{a["l"]}').replace('close:',f'close:{a["c"]}')
                ohlc_html_list.append(html)
            for date, ohlc_html in zip(date_list, ohlc_html_list):

                ohlc_html = ohlc_html.replace("@replace_with_date", date)
                final_ohlc_html_list.append(ohlc_html)

            for date, nci in zip(date_list, nci_list):

                nci_html = "{time:'@replace_with_date',value:@replace_with_nci},".replace("@replace_with_date", date).replace("@replace_with_nci", nci)
                final_nci_html_list.append(nci_html)

            final_ohlc_html_str = ""
            final_nci_html_str = ""

            for ohlc, nci in zip(final_ohlc_html_list, final_nci_html_list):

                final_ohlc_html_str = f"{final_ohlc_html_str}{ohlc}\n"
                final_nci_html_str = f"{final_nci_html_str}{nci}\n"

            html_template = """
    <!doctype html>
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
          <title>@replace_ticker Capital Trend</title>
          <link rel="icon" type="image/x-icon" href="../../favicon_1.png">
          <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
          <link rel="preconnect" href="https://fonts.googleapis.com">
          <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
          <link href="https://fonts.googleapis.com/css2?family=Saira+Condensed:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">
          <script src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"></script>
          <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
          <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/0.5.0-beta4/html2canvas.min.js"></script>
          <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.4.0/jspdf.umd.min.js"></script>
          <link rel="stylesheet" href="../../chart-styles.css">
       </head>
       <body>
          <section>
             <img id="site-logo" src="../../regentquant-logo-two-colors.svg">
             <h1 class="chart-title">Regentquant @replace_ticker Capital Trend (Capital Trend Shown as 5D Average Value)</h1>
             <h2 class="go-back-to-home-screen"><a href="https://www.regentquant.com">Go Back To Home Screen</a></h2>
             <h2>How to use: Investors may try to predict future price trend by looking at capital trend. Candlestick chart shows underlying stock's historical adjusted OHLC price. Line chart shows net capital inflow (Unit$). The data is estimated by algorithm and for reference only. Data used in calculation is bought from ICE. Users may not reproduce or republish Regentquant's Net Capital Inflow data without permission.</h2>
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
    const baselineSeries = chart.addBaselineSeries({ baseValue: { type: 'price', price: 0 }, topLineColor: 'rgba( 38, 166, 154, 1)', topFillColor1: 'rgba(38, 166, 154, 0.28)', topFillColor2: 'rgba( 38, 166, 154, 0.05)', bottomLineColor: 'rgba( 207, 87, 119, 1)', bottomFillColor1: 'rgba(207, 87, 119, 0.05)', bottomFillColor2: 'rgba( 207, 87, 119, 0.28)' });
    const data = [
    @replace_nci
    ];
    baselineSeries.setData(data);
    
    
    const candlestickSeries = chart.addCandlestickSeries({
        priceScaleId: 'left',
        upColor: '#26a69a', downColor: '#e04d76', borderVisible: false,
        wickUpColor: '#26a69a', wickDownColor: '#e04d76',
    });
    
    candlestickSeries.setData([
    @replace_ohlc
    ]);
    
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
    """

            formatted_html = html_template.replace("@replace_ticker", ticker).replace("@replace_nci", final_nci_html_str).replace("@replace_ohlc", final_ohlc_html_str)


            # Check if html exists
            asset_type = i.split(':')[0]
            file_name = f"capital-trend-{ticker.lower()}.html"

            if asset_type == "ETF":
                # Check if the file exists
                if not os.path.exists(f"ETFS/{file_name}"):
                    # Create the file if it doesn't exist
                    with open(f"ETFS/{file_name}", 'w') as file:
                        file.write('')  # Creating an empty file
                    file.close()

                with open(f"ETFS/{file_name}", "w") as file:
                    file.write(formatted_html)
                file.close()

            elif asset_type == "STOCK":
                # Check if the file exists
                if not os.path.exists(f"STOCKS/{file_name}"):
                    # Create the file if it doesn't exist
                    with open(f"STOCKS/{file_name}", 'w') as file:
                        file.write('')  # Creating an empty file
                    file.close()
                with open(f"STOCKS/{file_name}", "w") as file:
                    file.write(formatted_html)
                file.close()
            print(file_name)

def dashboard():
    type = "STOCKS"

    data = '''capital-trend-abbv.html
capital-trend-aapl.html
capital-trend-adbe.html
capital-trend-amd.html
capital-trend-amzn.html
capital-trend-avgo.html
capital-trend-bac.html
capital-trend-cost.html
capital-trend-cvx.html
capital-trend-googl.html
capital-trend-hd.html
capital-trend-jpm.html
capital-trend-ko.html
capital-trend-lly.html
capital-trend-meta.html
capital-trend-mrk.html
capital-trend-nflx.html
capital-trend-nvda.html
capital-trend-orcl.html
capital-trend-pep.html
capital-trend-pg.html
capital-trend-snow.html
capital-trend-tsla.html
capital-trend-unh.html
capital-trend-v.html
capital-trend-wmt.html
capital-trend-xom.html'''.split('\n')

    for i in data:
        ticker = i.split('.html')[0].split('-')[-1]
        stock = f'<div class="nci-container"><img src="LOGO/{type.upper()}/{ticker.upper()}.svg"><a href="Net%20Capital%20Inflow%20Database/{type.upper()}/capital-trend-{ticker}.html">{ticker.upper()}</a><br></div>'
        print(stock)



dashboard()