import pyperclip
import requests
import pyperclip
import os
from datetime import datetime
import pytz
from concurrent.futures import ThreadPoolExecutor




def main():
    """
    # Directory where the text files are located
    directory = "/Users/curryyao/Library/Mobile Documents/com~apple~CloudDocs/Regent Quant/Database"

    # Initialize a list to store the file names
    file_names = []
    for i in os.listdir(directory):
        if i.endswith(".txt"):
            file_names.append(f"{directory}/{i}")

    # Initialize a dictionary to store data for each stock
    stock_data = {}

    # Iterate through the file names and store data in the dictionary
    for file_name in file_names:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            # Extract the stock name from the header
            header = lines[0].strip().split('\t')
            stock_name = header[1]
            # Initialize a list for the stock's data if it's not in the dictionary
            if stock_name not in stock_data:
                stock_data[stock_name] = []
            # Append the data to the stock's list
            for line in lines[1:]:
                data = line.strip().split('\t')
                stock_data[stock_name].append(data[1])

    # Combine data for all stocks into a single list
    combined_data = []

    # Create the header line with stock names
    header = ['Date'] + list(stock_data.keys())
    combined_data.append('\t'.join(header))

    # Iterate through the data and combine it into a single line
    for i in range(len(stock_data[list(stock_data.keys())[0]])):
        date = lines[i + 1].strip().split('\t')[0]
        values = [date] + [stock_data[stock][i] for stock in stock_data]
        combined_data.append('\t'.join(values))

    fs = f""
    # Print the combined data
    for line in combined_data:
        fs = f"{fs}{line}\n"

    api_key = "ezBrk47F0tOiUtSZU7KevlNnxEEwPgIs"
    data = fs[:-1]
    """
    api_key = "ezBrk47F0tOiUtSZU7KevlNnxEEwPgIs"

    data = pyperclip.paste()
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
                if a.replace("\r", "") == "null":
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
            # Grabbing OHLC Data from Polygon
            ticker = i.split(':')[1].replace("\r", "")

            data = requests.get(
                f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{start_date}/{end_date}?adjusted=true&sort=asc&limit=50000&apiKey={api_key}")
            data = data.json()['results']

            fs = ''
            ohlc_html_list = []
            final_ohlc_html_list = []
            final_nci_html_list = []
            for a in data:
                html = "{time:'@replace_with_date',open:,high:,low:,close:},"
                html = html.replace('open:', f'open:{a["o"]}').replace('high:', f'high:{a["h"]}')
                html = html.replace('low:', f'low:{a["l"]}').replace('close:', f'close:{a["c"]}')
                ohlc_html_list.append(html)
            for date, ohlc_html in zip(date_list, ohlc_html_list):
                ohlc_html = ohlc_html.replace("@replace_with_date", date)
                final_ohlc_html_list.append(ohlc_html)

            for date, nci in zip(date_list, nci_list):
                nci_html = "{time:'@replace_with_date',value:@replace_with_nci},".replace("@replace_with_date",
                                                                                          date).replace(
                    "@replace_with_nci", nci)
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
     <meta charset="UTF-8">
     <meta name="description" content="In-depth analysis of @replace_ticker stock capital trends.">
     <meta name="keywords" content="@replace_ticker, capital trend, stock capital analysis, stock market, investment insights, market predictions, stock performance">
     <meta name="author" content="Regentquant">
     <meta name="robots" content="index, follow">
     <meta name="canonical" href="https://www.regentquant.com/">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
        <style>
            img {
border-radius: 3px;
     height: 32px; /* Example height, adjust as needed */
  width: auto; /* Maintain aspect ratio */
  margin-right: 10px; /* Optional: Adds space between the image and text */
                margin-bottom: 3px;
            }
        </style>
           <section>
              <img id="site-logo" src="../../regentquant-logo-two-colors.svg">
              <h1 class="chart-title">@replace_logoRegentquant @replace_ticker Capital Trend (Daily Amount)</h1>
              <h2 class="go-back-to-home-screen"><a href="https://www.regentquant.com">Go Back To Home Screen</a></h2>
              <h2>How to use: Investors may try to predict future price trend by looking at capital trend. Candlestick chart shows underlying stock's historical adjusted OHLC price. Line chart shows net capital inflow (Unit$). The data is estimated by algorithm and for reference only. Data used in calculation is bought from ICE. Users may not reproduce or republish Regentquant's Net Capital Inflow data without permission.</h2>
             <button id="download-chart">Save Chart</button> <button><a href="https://docs.google.com/spreadsheets/d/e/2PACX-1vSKtccuxjMvuMaBrgBQMfPXHs6W3LKdAcZ0MzmEv1RNl0sAEkYaN4MYQyPTIrPIjSXwXoBzKOlg_2kt/pubhtml" style="color: white">Download Data</a></button>
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
function customPriceFormatter(price) {
    return  price.toFixed(2) + ' M'; // Replace 'CustomText' with your desired text
}

// Update your baselineSeries creation
const baselineSeries = chart.addBaselineSeries({
    baseValue: { type: 'price', price: 0 },
    topLineColor: 'rgba(38, 166, 154, 1)',
    topFillColor1: 'rgba(38, 166, 154, 0.28)',
    topFillColor2: 'rgba(38, 166, 154, 0.05)',
    bottomLineColor: 'rgba(239, 83, 80, 1)',
    bottomFillColor1: 'rgba(239, 83, 80, 0.05)',
    bottomFillColor2: 'rgba(239, 83, 80, 0.28)',
    priceFormat: {
        type: 'custom',
        formatter: customPriceFormatter
    }
});   
     const data = [
     @replace_nci
     ];
     baselineSeries.setData(data);


     const candlestickSeries = chart.addCandlestickSeries({
         priceScaleId: 'left',
         upColor: '#26a69a', downColor: '#ef5350', borderVisible: false,
         wickUpColor: '#26a69a', wickDownColor: '#ef5350',
     });

     candlestickSeries.setData([
     @replace_ohlc
     ]);

        const totalDataPoints = data.length;
       const visibleRange = Math.min(30, totalDataPoints);
       chart.timeScale().setVisibleLogicalRange({
         from: totalDataPoints - visibleRange,
         to: totalDataPoints - 1,
       });

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

            replace_logo = ""
            if "STOCK:" in i:
                replace_logo = f'<img src="../../LOGO/STOCKS/{ticker}.svg">'
            elif "ETF:" in i:
                replace_logo = f'<img src="../../LOGO/ETFS/{ticker}.svg">'

            formatted_html = html_template.replace("@replace_ticker", ticker).replace("@replace_nci",
                                                                                      final_nci_html_str).replace(
                "@replace_ohlc", final_ohlc_html_str).replace("@replace_logo",replace_logo)

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

    fs = '''<!doctype html>
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
      <title>Regentquant Capital Trend Dashboard</title>
          <meta charset="UTF-8">
    <meta name="description" content="Track capital trend of popular ETFs and stocks.">
    <meta name="keywords" content="capital trend, regentquant capital trend, etf capital trend, stock capital trend, quantitative trading, stock indicator">
    <meta name="author" content="Regentquant">
    <meta name="robots" content="index, follow">
    <meta name="canonical" href="https://www.regentquant.com/">
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
   <style>

h3, h4 {
font-family: "Saira Condensed", sans-serif;
font-weight: 500;
font-size: 1.5rem;
color: #333333;
    margin-top: 50px;
    margin-bottom: 17px;
}
h4 {
   font-size: 1rem;
}
a {
    font-family: "Saira Condensed", sans-serif;
font-weight: 500;
font-size: 1rem;
color: #3374f6;
display: flex; /* Use flexbox for the link */
  align-items: center; /* Align the text with the image */
  text-decoration: none; /* Optional: Removes underline from the link */
}
.warning {
    color: red;
    font-size: 1.5rem;
    font-weight: 600;
}
.asset-type {
   font-weight: 600;
}
img {
border-radius: 3px;
     height: 37px; /* Example height, adjust as needed */
  width: auto; /* Maintain aspect ratio */
  margin-right: 10px; /* Optional: Adds space between the image and text */
}
.bi {
    width: 23px;
    height: auto;
    position: relative;
    margin-bottom: 5px;
    color: red;
    margin-right: 5px;
}
.rectangle-fill {
    flex-grow: 1; /* This makes the rectangle-fill take up the full width */
    display: flex;
    align-items: center;
    justify-content: left; /* Center content inside rectangle-fill */
    text-decoration: none; /* Optional: removes underline from links */
}
.capital-trend-container {
      display: flex; /* Use flexbox to align children */
  align-items: center; /* Align children vertically in the center */
  justify-content: left; /* Align children horizontally in the center */
  height: 37px; /* Make the container full height of the viewport */
   margin-bottom: 17px;
   background: #FBFBFD;
   border-radius: 3px;
}
.subtitle {
    margin-top: -15px;
    margin-bottom: 15px;
}
   </style>
   <body>
<section>
<img id="site-logo" src="regentquant-logo-two-colors.svg">
<h1 class="chart-title">Regentquant Capital Trend Dashboard (Alphabetical Order)</h1>
<h2 style="color: #333333">Last updated: @replace_time (New York Time)</h2>
    <h3 class='asset-type'>Today's Capital Trend Visualization</h3>
    <h2 class="subtitle">Overwhelmed by Data? Let the Expertise of the Regentquant Team Guide You Through Key Insights!</h2>
    <div class="capital-trend-container"><a href="Capital%20Trend/Capital%20Trend%20Visualization%20(Top%205%20Net%20Inflow%20&%20Top%205%20Net%20Outflow).pdf" class="rectangle-fill"><img src="LOGO/pdf-icon.svg" alt="PDF logo">Top 5 Net Inflow & Top 5 Net Outflow</a><br></div>
<h3 class="asset-type"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-fire" viewBox="0 0 16 16">
  <path d="M8 16c3.314 0 6-2 6-5.5 0-1.5-.5-4-2.5-6 .25 1.5-1.25 2-1.25 2C11 4 9 .5 6 0c.357 2 .5 4-2 6-1.25 1-2 2.729-2 4.5C2 14 4.686 16 8 16m0-1c-1.657 0-3-1-3-2.75 0-.75.25-2 1.25-3C6.125 10 7 10.5 7 10.5c-.375-1.25.5-3.25 2-3.5-.179 1-.25 2 1 3 .625.5 1 1.364 1 2.25C11 14 9.657 15 8 15"/>
</svg>Trending Tickers</h3>
<div class="capital-trend-container"><a href="Capital%20Trend/ETFS/capital-trend-qqq.html" class="rectangle-fill"><img src="LOGO/ETFS/QQQ.svg" alt="QQQ logo">QQQ</a><br></div>
<div class="capital-trend-container"><a href="Capital%20Trend/ETFS/capital-trend-spy.html" class="rectangle-fill"><img src="LOGO/ETFS/SPY.svg" alt="SPY logo">SPY</a><br></div>
<div class="capital-trend-container"><a href="Capital%20Trend/STOCKS/capital-trend-tsla.html" class="rectangle-fill"><img src="LOGO/STOCKS/TSLA.svg" alt="TSLA logo">TSLA</a><br></div>
<div class="capital-trend-container"><a href="Capital%20Trend/STOCKS/capital-trend-nvda.html" class="rectangle-fill"><img src="LOGO/STOCKS/NVDA.svg" alt="NVDA logo">NVDA</a><br></div>
<div class="capital-trend-container"><a href="Capital%20Trend/STOCKS/capital-trend-aapl.html" class="rectangle-fill"><img src="LOGO/STOCKS/AAPL.svg" alt="AAPL logo">AAPL</a><br></div>
    <h3 class='asset-type'>ETFs</h3>\n'''.replace("@replace_time",datetime.now(pytz.timezone('America/New_York')).strftime('%Y-%m-%d %H:%M:%S'))
    for i in sorted(os.listdir("ETFS")):

        if "html" in i:
            ticker = i.split('.html')[0].split('-')[-1]
            s = '<div class="capital-trend-container"><a href="Capital%20Trend/ETFS/capital-trend-@replace_ticker_lower.html" class="rectangle-fill"><img src="LOGO/ETFS/@replace_ticker_upper.svg" alt="@replace_ticker_upper logo">@replace_ticker_upper</a><br></div>'.replace("@replace_ticker_upper", ticker.upper()).replace("@replace_ticker_lower", ticker.lower())
            fs = f"{fs}{s}\n"

    fs = f"{fs}<h3 class='asset-type'>STOCKs</h3>\n"

    for i in sorted(os.listdir("STOCKS")):

        if "html" in i:
            ticker = i.split('.html')[0].split('-')[-1]
            s = '<div class="capital-trend-container"><a href="Capital%20Trend/STOCKS/capital-trend-@replace_ticker_lower.html" class="rectangle-fill"><img src="LOGO/STOCKS/@replace_ticker_upper.svg" alt="@replace_ticker_upper logo">@replace_ticker_upper</a><br></div>'.replace(
                "@replace_ticker_upper", ticker.upper()).replace("@replace_ticker_lower", ticker.lower())
            fs = f"{fs}{s}\n"

    fs = f"""{fs}\n
      <div class="nci-footer" style="width: 100%; height: 300px; background: white; margin-top: 50px; color: white; text-align: center; display: flex; justify-content: center; align-items: center;">
         <p style="margin: 0;"></p>
      </div>
   </body>
</html>"""

    with open("../capital-trend-dashboard.html", "w") as file:
        file.write(fs)
    file.close()


import time
s = time.time()
main()
dashboard()
e = time.time()
print(e-s)