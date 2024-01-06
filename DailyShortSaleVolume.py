import requests
import os
from datetime import datetime
import pyperclip
import pytz
underlying_list = ['ETF:SPY', 'ETF:QQQ', 'STOCK:TSLA', 'STOCK:NVDA', 'STOCK:AAPL', 'STOCK:MSFT', 'STOCK:GOOG', 'STOCK:AMZN', 'STOCK:NVDA', 'STOCK:META', 'STOCK:TSLA', 'ETF:AAPB', 'ETF:ARKK', 'ETF:DIA', 'ETF:FNGU', 'ETF:HYG', 'ETF:IWM', 'ETF:QQQM', 'ETF:SOXL', 'ETF:SOXS', 'ETF:SQQQ', 'ETF:TECL', 'ETF:TLT', 'ETF:TQQQ', 'ETF:TSLL', 'ETF:UPRO', 'ETF:UVXY', 'ETF:VOO', 'ETF:SVXY', 'STOCK:LULU', 'STOCK:GS', 'STOCK:NFLX', 'STOCK:GOOGL', 'STOCK:JPM', 'STOCK:NVO', 'STOCK:SVXY', 'STOCK:BABA', 'STOCK:UNH', 'STOCK:AVGO', 'STOCK:JNJ', 'STOCK:CRM', 'STOCK:LMT', 'STOCK:BAC', 'STOCK:CSCO', 'STOCK:V', 'STOCK:TSM', 'STOCK:COIN', 'STOCK:COST', 'STOCK:LLY', 'STOCK:KO', 'STOCK:INTC', 'STOCK:UBER', 'STOCK:AMD']

dir = "/Users/curryyao/Downloads/Daily Short Sale Volume"

def download_data_from_finra():

    date_list = '''2023-12-19
    2023-12-20
    2023-12-21'''.split('\n')

    for date in date_list:
        date_identifier = f"{date[:4]}{date[5:7]}{date[8:10]}"

        # URL of the file to be downloaded
        url = f"https://cdn.finra.org/equity/regsho/daily/CNMSshvol{date_identifier}.txt"

        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Save the content to a file
            with open(f"{dir}/CNMSshvol{date_identifier}.txt", "w") as file:
                list = (response.text.split('\n')[1:-2])
                fs = ""
                for i in list:
                    fs = f"{fs}{i}\n"
                fs = (fs.strip())
                file.write(fs)
            file_path = f"{dir}/CNMSshvol{date_identifier}.txt"
        else:
            file_path = "Download failed with status code: " + str(response.status_code)

def draft():
    dir = "/Users/curryyao/Downloads/waitforcombine/DSSV"

    for file in os.listdir(dir):
        if file.endswith(".txt"):
            type = "STOCK" if "STOCK:" in file else "ETF"
            with open(f"{dir}/{file}", "r") as f:
                c = f.readlines()
                start_date = (c[0].split('|')[0])
                end_date = (c[-1].split('|')[0])
                start_date = f"{start_date[:4]}-{start_date[4:6]}-{start_date[6:8]}"
                end_date = f"{end_date[:4]}-{end_date[4:6]}-{end_date[6:8]}"
            api = f"https://api.polygon.io/v2/aggs/ticker/{file.replace('.txt','').replace(f'{type}:','')}/range/1/day/{start_date}/{end_date}?adjusted=true&sort=asc&limit=50000&apiKey=ezBrk47F0tOiUtSZU7KevlNnxEEwPgIs"
            data = requests.get(api).json()['results']
            fs = ''
            for i in data:
                date = datetime.utcfromtimestamp(int(i['t']) / 1000).strftime('%Y-%m-%d')
                string = f"{date}|{i['o']}|{i['h']}|{i['l']}|{i['c']}"
                fs = f"{fs}{string}\n"

            fs = fs.strip()
            with open(f"/Users/curryyao/Downloads/waitforcombine/OHLC/{file}", "w") as file:
                file.write(fs)


def writing_to_html():

    with open(f"DSSV_database/template.txt", "r") as f:
        template = f.read()

    for file in os.listdir("DSSV_database/DSSV"):
        if file.endswith(".txt"):
            ticker = file.split(':')[1].replace('.txt','')

            short_sale_html = ""
            price_data_html = ""
            # Formatting short sale data
            with open(f"DSSV_database/DSSV/{file}", "r") as f:
                c = f.readlines()
                index = 0
                for i in c:
                    if index == 0:
                        date = i.split('|')[0]
                        short_sale_html = f"@@{short_sale_html}time:'{date[:4]}-{date[4:6]}-{date[6:8]}',value:{i.split('|')[2].strip()},color:'#3761F6'@,".replace('@@',"{").replace('@',"}")
                        index += 1
                    else:
                        date = i.split('|')[0]
                        last_value = c[index-1].split('|')[2].strip()
                        current_value = i.split('|')[2].strip()
                        if int(current_value) > int(last_value):
                            short_sale_html = f"{short_sale_html}@@time:'{date[:4]}-{date[4:6]}-{date[6:8]}',value:{i.split('|')[2].strip()},color:'#3761F6'@,".replace('@@',"{").replace('@',"}")
                        else:
                            short_sale_html = f"{short_sale_html}@@time:'{date[:4]}-{date[4:6]}-{date[6:8]}',value:{i.split('|')[2].strip()},color:'#90BFF9'@,".replace('@@',"{").replace('@',"}")
                        index += 1

            with open(f"DSSV_database/OHLC/{file}", "r") as f:
                c = f.readlines()
                for i in c:
                    string = f"@@time:'{i.split('|')[0]}',open:{i.split('|')[1]},high:{i.split('|')[2]},low:{i.split('|')[3]},close:{i.split('|')[4].strip()}@,".replace('@@','{').replace('@','}')
                    price_data_html = f"{price_data_html}{string}"

            with open(f"DSSV_database/dssv-{file.replace('.txt','').split(':')[1]}.html", "w") as file:
                file.write(template.replace("price_data = [];",f"price_data = [{price_data_html}];").replace('Ticker',ticker).replace("volumeSeries.setData([]);",f"volumeSeries.setData([{short_sale_html}]);"))

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
      <title>Regentquant Daily Short Sale Volume Dashboard</title>
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
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
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
<h1 class="chart-title">Regentquant Daily Short Sale Volume Dashboard (Alphabetical Order)</h1>
<h2 style="color: #333333">Last updated: @replace_time (New York Time)</h2>
<h3 class="asset-type"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-fire" viewBox="0 0 16 16">
  <path d="M8 16c3.314 0 6-2 6-5.5 0-1.5-.5-4-2.5-6 .25 1.5-1.25 2-1.25 2C11 4 9 .5 6 0c.357 2 .5 4-2 6-1.25 1-2 2.729-2 4.5C2 14 4.686 16 8 16m0-1c-1.657 0-3-1-3-2.75 0-.75.25-2 1.25-3C6.125 10 7 10.5 7 10.5c-.375-1.25.5-3.25 2-3.5-.179 1-.25 2 1 3 .625.5 1 1.364 1 2.25C11 14 9.657 15 8 15"/>
</svg>Trending Tickers</h3>
<div class="capital-trend-container"><a href="DSSV_database/dssv-QQQ.html" target="_blank" class="rectangle-fill"><img src="LOGO/ETFS/QQQ.svg" alt="QQQ logo">QQQ</a><br></div>
<div class="capital-trend-container"><a href="DSSV_database/dssv-SPY.html" target="_blank" class="rectangle-fill"><img src="LOGO/ETFS/SPY.svg" alt="SPY logo">SPY</a><br></div>
<div class="capital-trend-container"><a href="DSSV_database/dssv-TSLA.html" target="_blank" class="rectangle-fill"><img src="LOGO/ETFS/TSLA.svg" alt="TSLA logo">TSLA</a><br></div>
<div class="capital-trend-container"><a href="DSSV_database/dssv-NVDA.html" target="_blank" class="rectangle-fill"><img src="LOGO/ETFS/NVDA.svg" alt="NVDA logo">NVDA</a><br></div>
<div class="capital-trend-container"><a href="DSSV_database/dssv-AAPL.html" target="_blank" class="rectangle-fill"><img src="LOGO/ETFS/AAPL.svg" alt="AAPL logo">AAPL</a><br></div>
    <h3 class='asset-type'>ETFs</h3>\n'''.replace("@replace_time",
                                                  datetime.now(pytz.timezone('America/New_York')).strftime(
                                                      '%Y-%m-%d %H:%M:%S'))


    etfs = [i for i in underlying_list if "ETF" in i]
    stocks = [i for i in underlying_list if "STOCK" in i]

    for i in etfs:
        s = f"""<div class="capital-trend-container"><a href="DSSV_database/dssv-{i.replace('ETF:','')}.html" target="_blank" class="rectangle-fill"><img src="LOGO/ETFS/{i.replace('ETF:','')}.svg" alt="{i.replace('ETF:','')} logo">{i.replace('ETF:','')}</a><br></div>"""
        fs = f"{fs}{s}\n"
    for i in stocks:
        s = f"""<div class="capital-trend-container"><a href="DSSV_database/dssv-{i.replace('STOCK:','')}.html" target="_blank" class="rectangle-fill"><img src="LOGO/ETFS/{i.replace('STOCK:','')}.svg" alt="{i.replace('STOCK:','')} logo">{i.replace('STOCK:','')}</a><br></div>"""
        fs = f"{fs}{s}\n"


    fs = f"""{fs}\n
      <div class="nci-footer" style="width: 100%; height: 300px; background: white; margin-top: 50px; color: white; text-align: center; display: flex; justify-content: center; align-items: center;">
         <p style="margin: 0;"></p>
      </div>
   </body>
</html>"""

    with open("daily-short-sale-volume-dashboard.html", "w") as file:
        file.write(fs)
    file.close()


writing_to_html()