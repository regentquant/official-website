import pyperclip
import requests
import pyperclip
import os
def capital_trend():

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

    html_content = """
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

api_key = "ezBrk47F0tOiUtSZU7KevlNnxEEwPgIs"
data = '''Date	ETF:SPY	ETF:QQQ	ETF:SQQQ	ETF:TQQQ	ETF:XLF	ETF:SOXL	STOCK:NVDA	STOCK:TSLA	STOCK:AAPL	STOCK:AMZN	STOCK:META	STOCK:NFLX	STOCK:GOOGL	STOCK:AVGO	STOCK:AMD	STOCK:SNOW
2013-12-02	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
2013-12-03	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
2013-12-04	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
2013-12-05	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
2013-12-06	-617017597	-162820535	3225873	-14429153	-18436983	null	null	null	null	null	null	null	null	null	null	null
2013-12-09	-12074820	191033102	-264410	13622450	5832690	null	null	null	null	null	null	null	null	null	null	null
2013-12-10	-71650247	170125240	-1750689	21532168	23510887	null	null	null	null	null	null	null	null	null	null	null
2013-12-11	-675046800	-82468100	3471237	-547431	-97418829	null	null	null	null	null	null	null	null	null	null	null
2013-12-12	-737458690	80727643	661019	5747906	20164149	null	null	null	null	null	null	null	null	null	null	null
2013-12-13	-1348431607	-126979467	9261398	-27136852	82888204	null	null	null	null	null	null	null	null	null	null	null
2013-12-16	-1288299703	-126560924	7595283	-33873282	125352926	null	null	null	null	null	null	null	null	null	null	null
2013-12-17	-1363022744	-122728125	8903739	-37059840	89887014	null	null	null	null	null	null	null	null	null	null	null
2013-12-18	-617913882	103349576	2168722	-10480698	266158342	null	null	null	null	null	null	null	null	null	null	null
2013-12-19	-709131484	-244093229	5345066	-24076717	177015517	null	null	null	null	null	null	null	null	null	null	null
2013-12-20	-28358122	-68625904	-3669067	11550440	74099974	null	null	null	null	null	null	null	null	null	null	null
2013-12-23	-160399385	-66655252	-4126881	21092345	32465988	null	null	null	null	null	null	null	null	null	null	null
2013-12-24	689388461	-2833918	-5971807	25545809	110747989	null	null	null	null	null	null	null	null	null	null	null
2013-12-26	1171063374	183701468	-7965713	35361180	70607061	null	null	null	null	null	null	null	null	null	null	null
2013-12-27	1745158739	432116353	-9780497	44393757	95469305	null	null	null	null	null	null	null	null	null	null	null
2013-12-30	576516243	-13713480	-1606136	10830835	54191642	null	null	null	null	null	null	null	null	null	null	null
2013-12-31	493840318	-19227249	95710	1703418	41014159	null	null	null	null	null	null	null	null	null	null	null
2014-01-02	-473445479	-158739933	5114183	-13994166	-34560883	null	null	null	null	null	null	null	null	null	null	null
2014-01-03	-725457409	-514443465	10531806	-42162583	-12529022	null	null	null	null	null	null	null	null	null	null	null
2014-01-06	-976839012	-671153399	11471535	-52810413	58585794	null	null	null	null	null	null	null	null	null	null	null
2014-01-07	165542420	-252794871	3330495	-23523507	109744146	null	null	null	null	null	null	null	null	null	null	null
2014-01-08	66619448	-298004791	2596262	-24588254	130396428	null	null	null	null	null	null	null	null	null	null	null
2014-01-09	438825880	-238192306	1853094	-20094560	215277341	null	null	null	null	null	null	null	null	null	null	null
2014-01-10	-53506179	-302823248	-1378305	-5569079	83507093	null	null	null	null	null	null	null	null	null	null	null
2014-01-13	-3716789	-176708005	-891239	-5052170	-42260247	null	null	null	null	null	null	null	null	null	null	null
2014-01-14	41133605	-110479003	-4353526	1281927	-3273606	null	null	null	null	null	null	null	null	null	null	null
2014-01-15	262374585	-40239401	-7011671	13155387	70943063	null	null	null	null	null	null	null	null	null	null	null
2014-01-16	389095347	76159870	-11050729	32307972	-41227741	null	null	null	null	null	null	null	null	null	null	null
2014-01-17	116812055	117531999	-6303731	17795947	40929217	null	null	null	null	null	null	null	null	null	null	null
2014-01-21	38435702	305757677	-14798734	52631112	136632845	null	null	null	null	null	null	null	null	null	null	null
2014-01-22	-570140713	244557318	-10175503	44852067	84658641	null	null	null	null	null	null	null	null	null	null	null
2014-01-23	-1870104498	-215655079	3153262	-3119690	-177024403	null	null	null	null	null	null	null	null	null	null	null
2014-01-24	-2197199189	-586529474	24616226	-33039327	-192733481	null	null	null	null	null	null	null	null	null	null	null
2014-01-27	-1746124803	-674905756	40482229	-38872623	-285424654	null	null	null	null	null	null	null	null	null	null	null
2014-01-28	-1050192465	-1011886528	58015445	-65603802	-221067050	null	null	null	null	null	null	null	null	null	null	null
2014-01-29	-1766349644	-1454126453	80885385	-102488929	-372470544	null	null	null	null	null	null	null	null	null	null	null
2014-01-30	-435103097	-913241002	61220513	-59975527	-177493753	null	null	null	null	null	null	null	null	null	null	null
2014-01-31	-442888289	-708302107	52305906	-46371770	-152882321	null	null	null	null	null	null	null	null	null	null	null
2014-02-03	-759632698	-737026500	62675659	-50949492	-195762148	null	null	null	null	null	null	null	null	null	null	null
2014-02-04	-845715424	-281208269	35168601	-26448216	-161781984	null	null	null	null	null	null	null	null	null	null	null
2014-02-05	-641382977	-250874377	37080498	-21304231	-99827671	null	null	null	null	null	null	null	null	null	null	null
2014-02-06	-550788702	-288298352	36713972	-26829799	-85081511	null	null	null	null	null	null	null	null	null	null	null
2014-02-07	520182761	156030467	-3261316	3313412	95748008	null	null	null	null	null	null	null	null	null	null	null
2014-02-10	813846257	717977293	-48607907	45101217	205233154	null	null	null	null	null	null	null	null	null	null	null
2014-02-11	959557456	726714055	-57276573	54030977	156071613	null	null	null	null	null	null	null	null	null	null	null
2014-02-12	1532715602	1114506882	-102475910	86793424	204143746	null	null	null	null	null	null	null	null	null	null	null
2014-02-13	1455755428	1060410890	-114511627	88743579	102637326	null	null	null	null	null	null	null	null	null	null	null
2014-02-14	1592461419	814534028	-94095388	70096366	-1316063	null	null	null	null	null	null	null	null	null	null	null
2014-02-18	2186916025	816060325	-104767338	68414397	-28253978	null	null	null	null	null	null	null	null	null	null	null
2014-02-19	1441104171	319513850	-45479563	20694497	-197747957	null	null	null	null	null	null	null	null	null	null	null
2014-02-20	1828680565	288993390	-48417800	16831009	-127995025	null	null	null	null	null	null	null	null	null	null	null
2014-02-21	2025886468	208836386	-36874510	2172208	-34563683	null	null	null	null	null	null	null	null	null	null	null
2014-02-24	2043613604	420591026	-66947253	23472352	68421985	null	null	null	null	null	null	null	null	null	null	null
2014-02-25	1931255331	122839255	-15272487	1450758	16617237	null	null	null	null	null	null	null	null	null	null	null
2014-02-26	2470249540	488620340	-51652420	28701666	57401403	null	null	null	null	null	null	null	null	null	null	null
2014-02-27	2461252058	379792120	-53288475	31926536	49161630	null	null	null	null	null	null	null	null	null	null	null
2014-02-28	2167545388	353885464	-51569706	38611488	58940434	null	null	null	null	null	null	null	null	null	null	null
2014-03-03	1238424003	-103853139	33288674	-11092208	-112238122	null	null	null	null	null	null	null	null	null	null	null
2014-03-04	1587387377	210244146	-30234485	19523896	66647362	null	null	null	null	null	null	null	null	null	null	null
2014-03-05	1781704967	331880373	-58214644	34350496	221529100	null	null	null	null	null	null	null	null	null	null	null
2014-03-06	1757882168	299225094	-24585964	18310383	273473575	null	null	null	null	null	null	null	null	null	null	null
2014-03-07	956086755	-33878976	22081896	-11322931	324454701	null	null	null	null	null	null	null	null	null	null	null
2014-03-10	937481685	94247022	-6741762	5147152	353100954	null	null	null	null	null	null	null	null	null	null	null
2014-03-11	-29493775	-165276447	34916156	-21433912	173500600	null	null	null	null	null	null	null	null	null	null	null
2014-03-12	-902425954	-267147022	52749595	-33227882	-8282051	null	null	null	null	null	null	null	null	null	null	null
2014-03-13	-1942210081	-490543535	80453229	-59370116	-201685033	null	null	null	null	null	null	null	null	null	null	null
2014-03-14	-1226064608	-476133398	75716504	-54416919	-412394164	null	null	null	null	null	null	null	null	null	null	null
2014-03-17	-196463444	-158524429	33622455	-19702617	-286807792	null	null	null	null	null	null	null	null	null	null	null
2014-03-18	829932364	136893673	-4302560	8534253	-96853192	null	null	null	null	null	null	null	null	null	null	null
2014-03-19	1811508825	-207437175	31570620	-17092538	11363406	null	null	null	null	null	null	null	null	null	null	null
2014-03-20	2900838699	171165201	-18229511	19785785	285752674	null	null	null	null	null	null	null	null	null	null	null
2014-03-21	2730440540	70309084	-16990633	4913082	401291188	null	null	null	null	null	null	null	null	null	null	null
2014-03-24	1434773374	-523689670	33397639	-63307495	240977297	null	null	null	null	null	null	null	null	null	null	null
2014-03-25	1286830671	-585511921	43056626	-68074490	107466319	null	null	null	null	null	null	null	null	null	null	null
2014-03-26	850113263	-437873064	35799112	-59537135	28919582	null	null	null	null	null	null	null	null	null	null	null
2014-03-27	-91505696	-823798489	88952803	-100195882	-278115528	null	null	null	null	null	null	null	null	null	null	null
2014-03-28	-44447552	-251232660	11073909	-40641677	-222385941	null	null	null	null	null	null	null	null	null	null	null
2014-03-31	1128372644	344675571	-59377687	33677628	-65896685	null	null	null	null	null	null	null	null	null	null	null
2014-04-01	1037684943	391023013	-83432639	47860422	52742133	null	null	null	null	null	null	null	null	null	null	null
2014-04-02	1639600470	625322035	-117861508	64261422	184458236	null	null	null	null	null	null	null	null	null	null	null
2014-04-03	1451164986	639543460	-132121651	68433738	260134781	null	null	null	null	null	null	null	null	null	null	null
2014-04-04	1018405901	-14155124	-36879541	-9369235	156282402	null	null	null	null	null	null	null	null	null	null	null
2014-04-07	162955713	-325333133	45715791	-45488487	-47172397	null	null	null	null	null	null	null	null	null	null	null
2014-04-08	165746057	-303156916	58891926	-44543011	-105309484	null	null	null	null	null	null	null	null	null	null	null
2014-04-09	51458829	-181652662	33830622	-13915168	-117784252	null	null	null	null	null	null	null	null	null	null	null
2014-04-10	58994637	-314677819	67545545	-37803600	-213158460	null	null	null	null	null	null	null	null	null	null	null
2014-04-11	-51219786	-121721980	62775670	-5822521	-357871082	null	null	null	null	null	null	null	null	null	null	null
2014-04-14	802810550	178245445	-26824824	36717094	-123785043	null	null	null	null	null	null	null	null	null	null	null
2014-04-15	268184820	-218801751	39115025	-19644558	-40726770	null	null	null	null	null	null	null	null	null	null	null
2014-04-16	14305900	-270629165	48482569	-62983540	-41233943	null	null	null	null	null	null	null	null	null	null	null
2014-04-17	784539230	98202162	-18892634	-4047114	167046239	null	null	null	null	null	null	null	null	null	null	null
2014-04-21	1508854694	452411339	-89005073	36927871	271360998	null	null	null	null	null	null	null	null	null	null	null
2014-04-22	1635632000	465790739	-69682768	28631940	197687279	null	null	null	null	null	null	null	null	null	null	null
2014-04-23	1172654187	351577117	-63241451	28937893	107659520	null	null	null	null	null	null	null	null	null	null	null
2014-04-24	1363718387	-38651646	-66628550	71189932	47050847	null	null	null	null	null	null	null	null	null	null	null
2014-04-25	628535921	-325549747	-9659638	23182355	-66910702	null	null	null	null	null	null	null	null	null	null	null
2014-04-28	-5772390	-558062511	30018524	2097984	-126461468	null	null	null	null	null	null	null	null	null	null	null
2014-04-29	-292152411	-630150809	21610532	8080006	-88842261	null	null	null	null	null	null	null	null	null	null	null
2014-04-30	567661926	-384913884	-12653185	32687353	-103758625	null	null	null	null	null	null	null	null	null	null	null
2014-05-01	92657377	37748230	-16385574	19263180	-103724494	null	null	null	null	null	null	null	null	null	null	null
2014-05-02	188070217	186079384	-55144510	52625979	-11246082	null	null	null	null	null	null	null	null	null	null	null
2014-05-05	595803062	353040921	-84337411	59938849	53548367	null	null	null	null	null	null	null	null	null	null	null
2014-05-06	-311600492	1794355	-8608759	-1359933	-161962443	null	null	null	null	null	null	null	null	null	null	null
2014-05-07	-410051296	-259088839	32043084	-42338090	-74706757	null	null	null	null	null	null	null	null	null	null	null
2014-05-08	-54628507	-399194782	52767121	-47740181	-8252568	null	null	null	null	null	null	null	null	null	null	null
2014-05-09	344176763	-296712258	52371555	-49377693	-99028042	null	null	null	null	null	null	null	null	null	null	null
2014-05-12	780313777	-151703661	33517001	-33454994	-18200640	null	null	null	null	null	null	null	null	null	null	null
2014-05-13	1193742804	163832904	-20633465	12102605	108694243	null	null	null	null	null	null	null	null	null	null	null
2014-05-14	431389538	229487700	-42489912	34127955	-26800922	null	null	null	null	null	null	null	null	null	null	null
2014-05-15	-399027152	-157523619	10657164	-11174426	-159444333	null	null	null	null	null	null	null	null	null	null	null
2014-05-16	-566313905	-273477185	14365606	-6668526	-172025892	null	null	null	null	null	null	null	null	null	null	null
2014-05-19	-841055929	-317598445	30607657	-11545789	-173239394	null	null	null	null	null	null	null	null	null	null	null
2014-05-20	-1300903800	-561438160	64751847	-49004284	-201244892	null	null	null	null	null	null	null	null	null	null	null
2014-05-21	-231658461	-88021544	14937988	-8396061	-94652806	null	null	null	null	null	null	null	null	null	null	null
2014-05-22	837636439	459889572	-38655156	46197140	13413147	null	null	null	null	null	null	null	null	null	null	null
2014-05-23	1507298298	739819331	-65352342	66407887	121803278	null	null	null	null	null	null	null	null	null	null	null
2014-05-27	1515587717	764356240	-67675327	69277238	135496300	null	null	null	null	null	null	null	null	null	null	null
2014-05-28	2159974946	728022968	-67420159	77288661	122073177	null	null	null	null	null	null	null	null	null	null	null
2014-05-29	2128639336	629860371	-58946503	72469729	84629160	null	null	null	null	null	null	null	null	null	null	null
2014-05-30	2035744658	289372513	-33824246	37667718	74970835	null	null	null	null	null	null	null	null	null	null	null
2014-06-02	1639972228	-72610373	-3654215	-724247	40484061	null	null	null	null	null	null	null	null	null	null	null
2014-06-03	649104632	-427737772	27582665	-39486221	-32538057	null	null	null	null	null	null	null	null	null	null	null
2014-06-04	843272071	-142119870	-3725028	-15700069	50779190	null	null	null	null	null	null	null	null	null	null	null
2014-06-05	878168726	-85370278	-9946087	-3513678	87175837	null	null	null	null	null	null	null	null	null	null	null
2014-06-06	965932114	211092222	-34013865	24227629	151536739	null	null	null	null	null	null	null	null	null	null	null
2014-06-09	1111833906	311167959	-42104768	33946257	207183168	null	null	null	null	null	null	null	null	null	null	null
2014-06-10	2084097597	615177574	-59801377	60963608	174781386	null	null	null	null	null	null	null	null	null	null	null
2014-06-11	1163328688	394188820	-36104624	32701728	96709325	null	null	null	null	null	null	null	null	null	null	null
2014-06-12	-101135450	-64643843	16621511	-23832173	-33169135	null	null	null	null	null	null	null	null	null	null	null
2014-06-13	-202496343	-140092630	15342295	-27609941	-113748499	null	null	null	null	null	null	null	null	null	null	null
2014-06-16	-121386527	-24168085	7313569	-11100866	-239519185	null	null	null	null	null	null	null	null	null	null	null
2014-06-17	-186039268	-96219740	1680344	-10549649	-132564348	null	null	null	null	null	null	null	null	null	null	null
2014-06-18	647358595	-21978429	-11170003	9341026	-91834334	null	null	null	null	null	null	null	null	null	null	null
2014-06-19	900533343	206150709	-25065943	15383790	-70371735	null	null	null	null	null	null	null	null	null	null	null
2014-06-20	1212400518	-161049230	-5237568	9452446	-51000012	null	null	null	null	null	null	null	null	null	null	null
2014-06-23	298384797	-320197746	6584605	-7164391	28245570	null	null	null	null	null	null	null	null	null	null	null
2014-06-24	-35849826	-253343506	-2359256	585783	-34512230	null	null	null	null	null	null	null	null	null	null	null
2014-06-25	341721523	-12567866	-26083656	12991571	-8623385	null	null	null	null	null	null	null	null	null	null	null
2014-06-26	244478151	-204550274	-18401788	14011140	-11083482	null	null	null	null	null	null	null	null	null	null	null
2014-06-27	-821934176	176822438	-29515410	18289037	-41208128	null	null	null	null	null	null	null	null	null	null	null
2014-06-30	-84812541	480184723	-50315226	41976478	-130762464	null	null	null	null	null	null	null	null	null	null	null
2014-07-01	674560106	627433218	-48308609	38840529	-61739986	null	null	null	null	null	null	null	null	null	null	null
2014-07-02	563490783	590019010	-33718081	42689022	-52766083	null	null	null	null	null	null	null	null	null	null	null
2014-07-03	1368617500	906372786	-64282491	75173397	46957127	null	null	null	null	null	null	null	null	null	null	null
2014-07-07	1062881867	562278838	-41091368	43090613	-15986649	null	null	null	null	null	null	null	null	null	null	null
2014-07-08	67961052	119265218	-804248	-6022580	-51415089	null	null	null	null	null	null	null	null	null	null	null
2014-07-09	-47342599	14899812	-3904329	8960843	-66264396	null	null	null	null	null	null	null	null	null	null	null
2014-07-10	-1046569151	-413149108	27744100	-35901568	-141486302	null	null	null	null	null	null	null	null	null	null	null
2014-07-11	-1370501633	-422231086	18985943	-23541135	-196000703	null	null	null	null	null	null	null	null	null	null	null
2014-07-14	-186567577	-44493717	-12578694	24148892	-99213379	null	null	null	null	null	null	null	null	null	null	null
2014-07-15	65617807	16494890	-24877301	33427675	85369415	null	null	null	null	null	null	null	null	null	null	null
2014-07-16	93189819	2795369	-16670505	28362426	-34917163	null	null	null	null	null	null	null	null	null	null	null
2014-07-17	-38971913	-12623504	-16781463	20605999	-69157546	null	null	null	null	null	null	null	null	null	null	null
2014-07-18	776758146	145983734	-29678688	23581879	1690129	null	null	null	null	null	null	null	null	null	null	null
2014-07-21	-144098507	-203069311	7817567	-23280514	-81885300	null	null	null	null	null	null	null	null	null	null	null
2014-07-22	920049731	221114222	-29249788	29637224	-121570986	null	null	null	null	null	null	null	null	null	null	null
2014-07-23	660836345	240956293	-37672190	31473746	-18069210	null	null	null	null	null	null	null	null	null	null	null
2014-07-24	1618363371	479355624	-55900927	60327150	133202063	null	null	null	null	null	null	null	null	null	null	null
2014-07-25	247963699	-11523363	-8964675	6514272	33101474	null	null	null	null	null	null	null	null	null	null	null
2014-07-28	396090293	141107875	-24142967	22178090	36864448	null	null	null	null	null	null	null	null	null	null	null
2014-07-29	-217573979	63652965	-8641877	3390614	-14618009	null	null	null	null	null	null	null	null	null	null	null
2014-07-30	-700886428	129032698	-3878824	-245214	40083185	null	null	null	null	null	null	null	null	null	null	null
2014-07-31	-1656556799	-138390492	21658502	-30056923	-120437472	null	null	null	null	null	null	null	null	null	null	null
2014-08-01	-1421602709	-252398159	29003477	-35376063	-178236769	null	null	null	null	null	null	null	null	null	null	null
2014-08-04	-1317583258	-49164190	-3620697	-4922803	-72637071	null	null	null	null	null	null	null	null	null	null	null
2014-08-05	-1962029063	-498889919	31811891	-44075478	-157350639	null	null	null	null	null	null	null	null	null	null	null
2014-08-06	-1638923379	-652178654	42739755	-60207010	-157650300	null	null	null	null	null	null	null	null	null	null	null
2014-08-07	-1536459079	-325540654	17437228	-30967058	-85426084	null	null	null	null	null	null	null	null	null	null	null
2014-08-08	-797654153	296485725	-23679851	22783489	89060256	null	null	null	null	null	null	null	null	null	null	null
2014-08-11	-168588239	343051015	-13596430	15699241	82949846	null	null	null	null	null	null	null	null	null	null	null
2014-08-12	38009275	470777409	-27922830	30409374	222976827	null	null	null	null	null	null	null	null	null	null	null
2014-08-13	190779553	585270230	-49856033	43999791	201425877	null	null	null	null	null	null	null	null	null	null	null
2014-08-14	1241989649	746594206	-72490167	76711680	282574787	null	null	null	null	null	null	null	null	null	null	null
2014-08-15	421874709	615058447	-67777683	69138512	164133595	null	null	null	null	null	null	null	null	null	null	null
2014-08-18	272298429	734571358	-62614870	69425374	159364251	null	null	null	null	null	null	null	null	null	null	null
2014-08-19	1366716749	1143386565	-95394481	108050603	170056342	null	null	null	null	null	null	null	null	null	null	null
2014-08-20	1515967824	951559144	-65545147	91044109	138010806	null	null	null	null	null	null	null	null	null	null	null
2014-08-21	1525160691	925262971	-53187291	78609953	151106071	null	null	null	null	null	null	null	null	null	null	null
2014-08-22	1496673200	924690010	-55878776	77173000	159615711	null	null	null	null	null	null	null	null	null	null	null
2014-08-25	1480277756	757129568	-53704448	75800969	173473161	null	null	null	null	null	null	null	null	null	null	null
2014-08-26	1418251414	728852712	-42946500	61302017	159838305	null	null	null	null	null	null	null	null	null	null	null
2014-08-27	837286501	714477809	-41502795	53899351	106912122	null	null	null	null	null	null	null	null	null	null	null
2014-08-28	-43180420	385274354	-22556967	20480555	-26392611	null	null	null	null	null	null	null	null	null	null	null
2014-08-29	68711441	282644033	-14973918	-10365597	55746250	null	null	null	null	null	null	null	null	null	null	null
2014-09-02	-853546250	97690563	-13497800	-16045174	17461174	null	null	null	null	null	null	null	null	null	null	null
2014-09-03	-1535846781	-273834078	4185326	-38868815	-27769407	null	null	null	null	null	null	null	null	null	null	null
2014-09-04	-1152315745	-160970691	-9973417	-24646963	31475031	null	null	null	null	null	null	null	null	null	null	null
2014-09-05	-667783267	61499979	-24291793	-964254	42366859	null	null	null	null	null	null	null	null	null	null	null
2014-09-08	-800003168	126727422	-25236583	24778702	21463038	null	null	null	null	null	null	null	null	null	null	null
2014-09-09	-844436960	-82541536	132557	-12737964	-83654351	null	null	null	null	null	null	null	null	null	null	null
2014-09-10	-367090047	329245861	-25014068	16735199	-20935595	null	null	null	null	null	null	null	null	null	null	null
2014-09-11	-955998911	-38023044	4731962	-26546034	-13043126	null	null	null	null	null	null	null	null	null	null	null
2014-09-12	-1652572912	-375496615	25994342	-64691908	24339884	null	null	null	null	null	null	null	null	null	null	null
2014-09-15	-1616402750	-725241702	57338480	-108111707	-24056033	null	null	null	null	null	null	null	null	null	null	null
2014-09-16	-404596383	-291245175	26855160	-63100261	110131841	null	null	null	null	null	null	null	null	null	null	null
2014-09-17	-412167952	-412665949	31524930	-65404524	169449025	null	null	null	null	null	null	null	null	null	null	null
2014-09-18	507505974	93207374	854556	-9393946	216159854	null	null	null	null	null	null	null	null	null	null	null
2014-09-19	279800261	86684619	-18404193	23529902	134802576	null	null	null	null	null	null	null	null	null	null	null
2014-09-22	289920579	35833519	-19713164	27315265	71458146	null	null	null	null	null	null	null	null	null	null	null
2014-09-23	-1059209220	-270038292	4168389	27898597	-17246917	null	null	null	null	null	null	null	null	null	null	null
2014-09-24	-902685979	-125150965	-10440838	40217063	-81969164	null	null	null	null	null	null	null	null	null	null	null
2014-09-25	-2111468233	-848215031	39949865	-34024448	-276214954	null	null	null	null	null	null	null	null	null	null	null
2014-09-26	-752677645	-171193281	19541412	561311	-95904777	null	null	null	null	null	null	null	null	null	null	null
2014-09-29	-353933479	-75188973	16758817	7251191	-107748420	null	null	null	null	null	null	null	null	null	null	null
2014-09-30	-31692818	213810777	-2225251	685956	-88684801	null	null	null	null	null	null	null	null	null	null	null
2014-10-01	-595734279	-373647126	57263893	-75187800	-260188748	null	null	null	null	null	null	null	null	null	null	null
2014-10-02	-12492039	-24057352	34041640	-37484353	-84652814	null	null	null	null	null	null	null	null	null	null	null
2014-10-03	89595239	-96649865	28502595	-35165351	-60191932	null	null	null	null	null	null	null	null	null	null	null
2014-10-06	-324477942	13966544	17510898	-32834544	44589572	null	null	null	null	null	null	null	null	null	null	null
2014-10-07	-331555690	-465111600	56060756	-83558899	-51199339	null	null	null	null	null	null	null	null	null	null	null
2014-10-08	266403277	150710862	2465932	-9923176	166025322	null	null	null	null	null	null	null	null	null	null	null
2014-10-09	-185120504	-98747464	21700520	-41411712	-123023261	null	null	null	null	null	null	null	null	null	null	null
2014-10-10	-1030139225	-655517488	90869090	-134596417	-176359208	null	null	null	null	null	null	null	null	null	null	null
2014-10-13	-490949402	-449257154	102492888	-95255238	-88107815	null	null	null	null	null	null	null	null	null	null	null
2014-10-14	493654989	47001924	43774395	-14608031	156156394	null	null	null	null	null	null	null	null	null	null	null
2014-10-15	-220533809	-432730136	106073204	-95782483	-156421935	null	null	null	null	null	null	null	null	null	null	null
2014-10-16	381736076	-283996513	106822533	-95336866	41146789	null	null	null	null	null	null	null	null	null	null	null
2014-10-17	622137264	279116320	14419238	7499352	119825457	null	null	null	null	null	null	null	null	null	null	null
2014-10-20	913839252	366616828	-33754613	15651791	133178350	null	null	null	null	null	null	null	null	null	null	null
2014-10-21	490296749	461832816	-43797636	14830240	121032807	null	null	null	null	null	null	null	null	null	null	null
2014-10-22	744453806	606712304	-82576241	66050663	328110264	null	null	null	null	null	null	null	null	null	null	null
2014-10-23	935644757	1039117760	-147539296	149229432	439037085	null	null	null	null	null	null	null	null	null	null	null
2014-10-24	1485413496	970479724	-117348427	139585040	367884127	null	null	null	null	null	null	null	null	null	null	null
2014-10-27	796850042	549153241	-84876121	108132992	234814789	null	null	null	null	null	null	null	null	null	null	null
2014-10-28	1128556749	480288821	-66215634	103461699	213325413	null	null	null	null	null	null	null	null	null	null	null
2014-10-29	922232746	331658231	-49481103	70200976	238895119	null	null	null	null	null	null	null	null	null	null	null
2014-10-30	950045752	22670013	-11376627	19667440	195139182	null	null	null	null	null	null	null	null	null	null	null
2014-10-31	972258305	-479511554	-11026671	20336801	200848559	null	null	null	null	null	null	null	null	null	null	null
2014-11-03	1659013146	-21009581	-32797551	60796355	306093502	null	null	null	null	null	null	null	null	null	null	null
2014-11-04	815426246	-486848423	8519760	-13482294	127805346	null	null	null	null	null	null	null	null	null	null	null
2014-11-05	1405059988	-287158673	-12720903	-5079129	174606254	null	null	null	null	null	null	null	null	null	null	null
2014-11-06	1390289817	-219421276	-15585865	5962084	134871358	null	null	null	null	null	null	null	null	null	null	null
2014-11-07	566917414	-131989647	17675822	-56940063	96200187	null	null	null	null	null	null	null	null	null	null	null
2014-11-10	496376295	-269294323	21143172	-71892050	56066781	null	null	null	null	null	null	null	null	null	null	null
2014-11-11	701703203	57409867	-6429987	-16765496	52050368	null	null	null	null	null	null	null	null	null	null	null
2014-11-12	350864455	188873434	-11625885	19672752	-63753466	null	null	null	null	null	null	null	null	null	null	null
2014-11-13	6905558	330057044	-44888694	65610794	-83701074	null	null	null	null	null	null	null	null	null	null	null
2014-11-14	-87947811	568329222	-69244694	108400738	-133248487	null	null	null	null	null	null	null	null	null	null	null
2014-11-17	141897645	250212073	-50872323	50455845	-190724625	null	null	null	null	null	null	null	null	null	null	null
2014-11-18	904057474	373864916	-61768229	63463457	-79689391	null	null	null	null	null	null	null	null	null	null	null
2014-11-19	867759929	52758696	-37356623	19315991	-87018848	null	null	null	null	null	null	null	null	null	null	null
2014-11-20	1165942659	98235398	-19243669	-7969811	-117548543	null	null	null	null	null	null	null	null	null	null	null
2014-11-21	1840756058	11130131	-9598986	8309466	-40515710	null	null	null	null	null	null	null	null	null	null	null
2014-11-24	1684608488	351964887	-33364515	81621208	26911834	null	null	null	null	null	null	null	null	null	null	null
2014-11-25	1013816211	282695003	-28782518	91638403	-39723214	null	null	null	null	null	null	null	null	null	null	null
2014-11-26	511175790	640925243	-69761251	166634532	21338555	null	null	null	null	null	null	null	null	null	null	null
2014-11-28	200413317	622150846	-69172017	171235789	84253916	null	null	null	null	null	null	null	null	null	null	null
2014-12-01	-402391101	412695748	-50165262	97917490	-34604521	null	null	null	null	null	null	null	null	null	null	null
2014-12-02	-474675441	474856364	-43621652	96190083	-17760146	null	null	null	null	null	null	null	null	null	null	null
2014-12-03	156929488	318912871	-29022728	68581199	47340760	null	null	null	null	null	null	null	null	null	null	null
2014-12-04	409918050	210238434	-10599855	33716630	39420500	null	null	null	null	null	null	null	null	null	null	null
2014-12-05	1170999832	208078659	-8987605	-14791382	95709670	null	null	null	null	null	null	null	null	null	null	null
2014-12-08	1406934372	331054418	-16196774	644551	259069008	null	null	null	null	null	null	null	null	null	null	null
2014-12-09	1032958597	26866118	3940467	-51709445	111883083	null	null	null	null	null	null	null	null	null	null	null
2014-12-10	-76232033	-218831608	22744880	-103160813	-28460101	null	null	null	null	null	null	null	null	null	null	null
2014-12-11	732778658	-27439735	-881350	-67157794	80350897	null	null	null	null	null	null	null	null	null	null	null
2014-12-12	-374281023	-398392761	26648943	-78687651	-92034270	null	null	null	null	null	null	null	null	null	null	null
2014-12-15	-641631123	-446143491	36733596	-90574243	-246939839	null	null	null	null	null	null	null	null	null	null	null
2014-12-16	-596879192	-508242285	48717059	-97004955	-152887889	null	null	null	null	null	null	null	null	null	null	null
2014-12-17	698961751	84292242	2031012	-21506394	63315536	null	null	null	null	null	null	null	null	null	null	null
2014-12-18	1279165985	138404885	-3144916	-13943661	51823807	null	null	null	null	null	null	null	null	null	null	null
2014-12-19	1284403667	271635091	-37840285	57814406	82008664	null	null	null	null	null	null	null	null	null	null	null
2014-12-22	874084159	655582623	-69437622	119988858	181003048	null	null	null	null	null	null	null	null	null	null	null
2014-12-23	1650622987	658300545	-79755421	117046188	212880246	null	null	null	null	null	null	null	null	null	null	null
2014-12-24	975449973	407539394	-56252850	91682151	112494113	null	null	null	null	null	null	null	null	null	null	null
2014-12-26	447225342	260163025	-31360406	75657192	63473388	null	null	null	null	null	null	null	null	null	null	null
2014-12-29	1359752181	408569452	-20485331	47387002	185566223	null	null	null	null	null	null	null	null	null	null	null
2014-12-30	1480747785	-2316734	1941213	-13538497	110773597	null	null	null	null	null	null	null	null	null	null	null
2014-12-31	309973599	119802916	-4429110	2453879	37295854	null	null	null	null	null	null	null	null	null	null	null
2015-01-02	-108620136	-134846252	8991615	-23884665	851004	null	null	null	null	null	null	null	null	null	null	null
2015-01-05	-959145102	-533309629	32898204	-85231120	-130770168	null	null	null	null	null	null	null	null	null	null	null
2015-01-06	-2002884994	-846867634	53294833	-122416329	-288605488	null	null	null	null	null	null	null	null	null	null	null
2015-01-07	-1116565375	-457039676	29832971	-55421510	-193218673	null	null	null	null	null	null	null	null	null	null	null
2015-01-08	-51457692	-132871574	7631374	-5393549	-79834466	null	null	null	null	null	null	null	null	null	null	null
2015-01-09	-318137660	-208784103	15513681	-30205171	-109241390	null	null	null	null	null	null	null	null	null	null	null
2015-01-12	-592564536	-190070706	15238091	-32869579	-81366941	null	null	null	null	null	null	null	null	null	null	null
2015-01-13	207666090	111730171	-14340168	8055510	34487662	null	null	null	null	null	null	null	null	null	null	null
2015-01-14	-291205748	-354857471	22468358	-70333987	-149029707	null	null	null	null	null	null	null	null	null	null	null
2015-01-15	-1528851716	-931720662	63413385	-154413144	-335567858	null	null	null	null	null	null	null	null	null	null	null
2015-01-16	-632958727	-502448159	31642198	-92631206	-162992975	null	null	null	null	null	null	null	null	null	null	null
2015-01-20	-425292859	-213562161	9584914	-49520921	-137279930	null	null	null	null	null	null	null	null	null	null	null
2015-01-21	-277026435	-111723804	5555212	-33085384	-101316401	null	null	null	null	null	null	null	null	null	null	null
2015-01-22	427303001	369039029	-40815964	45256784	115477670	null	null	null	null	null	null	null	null	null	null	null
2015-01-23	476496116	801016826	-74991088	112264235	153018649	null	null	null	null	null	null	null	null	null	null	null
2015-01-26	448119364	444463037	-47215521	59996566	62491103	null	null	null	null	null	null	null	null	null	null	null
2015-01-27	330364848	156816881	-21398545	278802	40723713	null	null	null	null	null	null	null	null	null	null	null
2015-01-28	-175884624	87872538	-17246762	3225779	-111448166	null	null	null	null	null	null	null	null	null	null	null
2015-01-29	-707247398	-278094296	13328340	-43198966	-155366985	null	null	null	null	null	null	null	null	null	null	null
2015-01-30	-804909163	-404083139	24155049	-68273608	-185787963	null	null	null	null	null	null	null	null	null	null	null
2015-02-02	-934027745	-311908614	14575251	-52435666	-137540536	null	null	null	null	null	null	null	null	null	null	null
2015-02-03	-371028040	-64805220	-24101679	35052621	36166750	null	null	null	null	null	null	null	null	null	null	null
2015-02-04	-738066729	-121596001	-7345732	10061230	167182854	null	null	null	null	null	null	null	null	null	null	null
2015-02-05	-227812424	190615914	-28546579	54459111	170938316	null	null	null	null	null	null	null	null	null	null	null
2015-02-06	507765904	124445881	-20729390	45545644	416917667	null	null	null	null	null	null	null	null	null	null	null
2015-02-09	592565621	341610404	-13761139	71418548	280379937	null	null	null	null	null	null	null	null	null	null	null
2015-02-10	977818139	526796356	-12194807	72592747	231325798	null	null	null	null	null	null	null	null	null	null	null
2015-02-11	1200507109	648526101	-33218062	101896908	141140350	null	null	null	null	null	null	null	null	null	null	null
2015-02-12	1228659199	665432327	-40625026	115373824	161789555	null	null	null	null	null	null	null	null	null	null	null
2015-02-13	1779496745	935002841	-65114543	164446657	-5436306	null	null	null	null	null	null	null	null	null	null	null
2015-02-17	2034421711	844247493	-71047203	142769622	77325140	null	null	null	null	null	null	null	null	null	null	null
2015-02-18	969245572	566764726	-50628768	97331562	-54279938	null	null	null	null	null	null	null	null	null	null	null
2015-02-19	688325996	587481621	-46362209	85950936	-34681865	null	null	null	null	null	null	null	null	null	null	null
2015-02-20	185436617	541162849	-30125078	54192472	-104476224	null	null	null	null	null	null	null	null	null	null	null
2015-02-23	-807581950	202236099	-6676627	1708573	-135053490	null	null	null	null	null	null	null	null	null	null	null
2015-02-24	-786724785	104397766	-11260062	5918673	-78902296	null	null	null	null	null	null	null	null	null	null	null
2015-02-25	-407312261	146213390	-12673147	8061667	15825136	null	null	null	null	null	null	null	null	null	null	null
2015-02-26	-561372246	130861392	-8300887	15397430	-3246079	null	null	null	null	null	null	null	null	null	null	null
2015-02-27	-927838031	-242611393	5618056	-26613144	-62843501	null	null	null	null	null	null	null	null	null	null	null
2015-03-02	-39348021	46420037	-9596418	20062358	50119004	null	null	null	null	null	null	null	null	null	null	null
2015-03-03	-1279299979	-125548086	1730343	-15261901	-102943278	null	null	null	null	null	null	null	null	null	null	null
2015-03-04	-1800067504	-246049797	10309118	-45625675	-215118266	null	null	null	null	null	null	null	null	null	null	null
2015-03-05	-858393857	-290947469	12439670	-52674536	-110964485	null	null	null	null	null	null	null	null	null	null	null
2015-03-06	-1423017768	-328164619	15835592	-63675164	-51285294	null	null	null	null	null	null	null	null	null	null	null
2015-03-09	-1370723153	-379978270	18905621	-72484920	-58039844	null	null	null	null	null	null	null	null	null	null	null
2015-03-10	-1789887993	-480234564	29397749	-87004706	-50370351	null	null	null	null	null	null	null	null	null	null	null
2015-03-11	-1905293066	-441578032	25390645	-79086037	118041163	null	null	null	null	null	null	null	null	null	null	null
2015-03-12	-1724570247	-390367275	15495939	-70673924	169345897	null	null	null	null	null	null	null	null	null	null	null
2015-03-13	-1514930010	-402005944	18560285	-73835540	85201921	null	null	null	null	null	null	null	null	null	null	null
2015-03-16	-797163438	-281753449	12605935	-60957692	100177291	null	null	null	null	null	null	null	null	null	null	null
2015-03-17	-174790742	-20067465	-5481531	-9737393	117801526	null	null	null	null	null	null	null	null	null	null	null
2015-03-18	392166882	96735575	-13429528	25041078	83179174	null	null	null	null	null	null	null	null	null	null	null
2015-03-19	-777768977	186376043	-8225515	27738139	-117801359	null	null	null	null	null	null	null	null	null	null	null
2015-03-20	1380429948	657159300	-43648329	106675559	13719721	null	null	null	null	null	null	null	null	null	null	null
2015-03-23	592987741	439476493	-23147954	62257759	-83971831	null	null	null	null	null	null	null	null	null	null	null
2015-03-24	823908850	508111750	-28215222	66938286	-87154818	null	null	null	null	null	null	null	null	null	null	null
2015-03-25	228388013	200374885	-9345079	11945216	-193828638	null	null	null	null	null	null	null	null	null	null	null
2015-03-26	1151941116	29747719	22581109	-60252760	-76774989	null	null	null	null	null	null	null	null	null	null	null
2015-03-27	212800935	30281645	31365936	-70562809	-173123432	null	null	null	null	null	null	null	null	null	null	null
2015-03-30	535689175	67641491	13105400	-16257474	-76769513	null	null	null	null	null	null	null	null	null	null	null
2015-03-31	175792031	-183154698	26512662	-56327644	-74740208	null	null	null	null	null	null	null	null	null	null	null
2015-04-01	381884067	-125395477	25647507	-51581155	-64572698	null	null	null	null	null	null	null	null	null	null	null
2015-04-02	700032658	-88285169	-238940	6337114	-18210291	null	null	null	null	null	null	null	null	null	null	null
2015-04-06	1035124504	-37203245	-2100815	19424231	40867157	null	null	null	null	null	null	null	null	null	null	null
2015-04-07	772656774	22838444	-984616	597601	-50168117	null	null	null	null	null	null	null	null	null	null	null
2015-04-08	2026298888	485946468	-30822471	85063816	54066620	null	null	null	null	null	null	null	null	null	null	null
2015-04-09	2993835502	828447188	-54242219	149796824	68308277	null	null	null	null	null	null	null	null	null	null	null
2015-04-10	3047393181	845570654	-55443733	156758201	17543657	null	null	null	null	null	null	null	null	null	null	null
2015-04-13	2508935710	650266881	-49464967	130202456	53245085	null	null	null	null	null	null	null	null	null	null	null
2015-04-14	1453290062	354480314	-24477464	62264189	42205691	null	null	null	null	null	null	null	null	null	null	null
2015-04-15	1548708296	303155138	-22293424	47232102	77393321	null	null	null	null	null	null	null	null	null	null	null
2015-04-16	966109647	42186694	-4400854	5603167	140950716	null	null	null	null	null	null	null	null	null	null	null
2015-04-17	-689670832	-435202968	23801786	-66861294	39951055	null	null	null	null	null	null	null	null	null	null	null
2015-04-20	-502265607	-251355897	15490266	-39338805	31822422	null	null	null	null	null	null	null	null	null	null	null
2015-04-21	-673190657	-212850186	-16498324	-30353522	14804089	null	null	null	null	null	null	null	null	null	null	null
2015-04-22	-824546663	-305690329	-12915637	-36785602	-16655184	null	null	null	null	null	null	null	null	null	null	null
2015-04-23	258900097	-10374046	-41463238	27776804	-55390068	null	null	null	null	null	null	null	null	null	null	null
2015-04-24	1886724872	591685033	-88343137	120219725	14514939	null	null	null	null	null	null	null	null	null	null	null
2015-04-27	1217744649	315127769	-74233062	82941914	-19727056	null	null	null	null	null	null	null	null	null	null	null
2015-04-28	2240548267	315053723	-46036285	91317087	63512081	null	null	null	null	null	null	null	null	null	null	null
2015-04-29	823201578	-44463911	-8248699	12679816	-24872715	null	null	null	null	null	null	null	null	null	null	null
2015-04-30	-844011186	-427168797	34222734	-101840823	-92774901	null	null	null	null	null	null	null	null	null	null	null
2015-05-01	-573277795	-419398238	36069112	-91035592	-15886489	null	null	null	null	null	null	null	null	null	null	null
2015-05-04	174103212	-191805945	16514583	-50159207	30778728	null	null	null	null	null	null	null	null	null	null	null
2015-05-05	-836401609	-317197818	33080354	-97640531	-51346917	null	null	null	null	null	null	null	null	null	null	null
2015-05-06	-843111096	-245834579	31294665	-94076820	-68791240	null	null	null	null	null	null	null	null	null	null	null
2015-05-07	517513034	197840434	-11450788	24614557	72658811	null	null	null	null	null	null	null	null	null	null	null
2015-05-08	1068641130	221261592	-7261708	21062440	116259430	null	null	null	null	null	null	null	null	null	null	null
2015-05-11	283072331	-59668806	20029724	-45190198	46034933	null	null	null	null	null	null	null	null	null	null	null
2015-05-12	1368171471	241657822	14379580	-20612474	-13223682	null	null	null	null	null	null	null	null	null	null	null
2015-05-13	1626820783	618770564	-27243926	67545585	92981347	null	null	null	null	null	null	null	null	null	null	null
2015-05-14	2077219422	618783417	-36190249	73808671	93806571	null	null	null	null	null	null	null	null	null	null	null
2015-05-15	78054190	111770003	-14816114	-21576319	-67195444	null	null	null	null	null	null	null	null	null	null	null
2015-05-18	892136265	364903111	-25746345	21221468	-8610181	null	null	null	null	null	null	null	null	null	null	null
2015-05-19	-171539361	307628678	-46694695	37161000	180082071	null	null	null	null	null	null	null	null	null	null	null
2015-05-20	293779130	151887153	-31369517	8173313	64877247	null	null	null	null	null	null	null	null	null	null	null
2015-05-21	-81828569	121001352	-14136046	-17032054	-50954499	null	null	null	null	null	null	null	null	null	null	null
2015-05-22	-140502754	421575601	-21478297	45287031	42342188	null	null	null	null	null	null	null	null	null	null	null
2015-05-26	-1616476852	56322793	10713709	-18368766	-83251555	null	null	null	null	null	null	null	null	null	null	null
2015-05-27	-256886699	281531091	-21475447	56220163	-97040742	null	null	null	null	null	null	null	null	null	null	null
2015-05-28	-502007164	97964159	-3753059	26716792	-81407805	null	null	null	null	null	null	null	null	null	null	null
2015-05-29	-1906077066	-241815640	33397066	-26679159	-91562133	null	null	null	null	null	null	null	null	null	null	null
2015-06-01	-1005865321	-189782257	31127873	-25444116	-78440621	null	null	null	null	null	null	null	null	null	null	null
2015-06-02	-221159215	-83777849	15530029	-12832138	24002777	null	null	null	null	null	null	null	null	null	null	null
2015-06-03	-385568057	-97617761	26902836	-18946544	27331060	null	null	null	null	null	null	null	null	null	null	null
2015-06-04	-798038937	-16895447	20751582	-16235349	-9300491	null	null	null	null	null	null	null	null	null	null	null
2015-06-05	-703500833	9273638	6491459	-29358771	168753046	null	null	null	null	null	null	null	null	null	null	null
2015-06-08	-1856864521	-368764631	31151273	-98642261	83202665	null	null	null	null	null	null	null	null	null	null	null
2015-06-09	-1378608134	-358500310	30446689	-95457513	93692926	null	null	null	null	null	null	null	null	null	null	null
2015-06-10	-702985589	-301150401	37273845	-83235710	114546165	null	null	null	null	null	null	null	null	null	null	null
2015-06-11	640083079	-80408707	14870991	-31660630	287340101	null	null	null	null	null	null	null	null	null	null	null
2015-06-12	279617684	-208756793	15548875	-30666859	93329934	null	null	null	null	null	null	null	null	null	null	null
2015-06-15	1298669787	-264069575	34069160	-37914188	59010916	null	null	null	null	null	null	null	null	null	null	null
2015-06-16	1551414362	-27280709	8167198	19459451	80133281	null	null	null	null	null	null	null	null	null	null	null
2015-06-17	548468138	-206255131	17068348	1020921	-80672643	null	null	null	null	null	null	null	null	null	null	null
2015-06-18	1064205867	-98432663	-234118	19702813	-24126820	null	null	null	null	null	null	null	null	null	null	null
2015-06-19	1112506620	-41426929	-550446	29879717	-26405959	null	null	null	null	null	null	null	null	null	null	null
2015-06-22	1524677674	427945181	-49998783	122402893	118396101	null	null	null	null	null	null	null	null	null	null	null
2015-06-23	861662690	231643410	-32123235	79768128	154873015	null	null	null	null	null	null	null	null	null	null	null
2015-06-24	-310238218	61064544	-17802056	36699500	145651456	null	null	null	null	null	null	null	null	null	null	null
2015-06-25	-2152433007	-145920034	8473206	-38879139	-54633132	null	null	null	null	null	null	null	null	null	null	null
2015-06-26	-1114558781	-112572053	23119306	-51838726	86442970	null	null	null	null	null	null	null	null	null	null	null
2015-06-29	-2305356461	-605288267	49784313	-146909110	-52534963	null	null	null	null	null	null	null	null	null	null	null
2015-06-30	-2548445849	-287979879	20586702	-86395249	-70803843	null	null	null	null	null	null	null	null	null	null	null
2015-07-01	-914560648	-23409292	-10438308	-31834258	110748586	null	null	null	null	null	null	null	null	null	null	null
2015-07-02	-267801004	-136604312	-7599936	-6201950	138058425	null	null	null	null	null	null	null	null	null	null	null
2015-07-06	-286113357	-113355397	-18525592	54003056	25566235	null	null	null	null	null	null	null	null	null	null	null
2015-07-07	132295338	56610619	-7612588	43262878	7526865	null	null	null	null	null	null	null	null	null	null	null
2015-07-08	-172865359	-436915455	47143710	-48589539	-154834965	null	null	null	null	null	null	null	null	null	null	null
2015-07-09	-658352305	-582650701	42963474	-56469268	-188093021	null	null	null	null	null	null	null	null	null	null	null
2015-07-10	203283782	-298557419	20275399	-24406537	-103545790	null	null	null	null	null	null	null	null	null	null	null
2015-07-13	1003375484	49888352	-22487744	-8422917	35857833	null	null	null	null	null	null	null	null	null	null	null
2015-07-14	1851837037	412451936	-61645017	96545263	159108329	null	null	null	null	null	null	null	null	null	null	null
2015-07-15	2802887675	783454888	-101763720	170848609	371938619	null	null	null	null	null	null	null	null	null	null	null
2015-07-16	3435019678	1018574707	-103099263	185125025	366353844	null	null	null	null	null	null	null	null	null	null	null
2015-07-17	2294217080	1034168410	-102092668	205672158	265304238	null	null	null	null	null	null	null	null	null	null	null
2015-07-20	1849888312	1084282020	-103067959	206112894	222976794	null	null	null	null	null	null	null	null	null	null	null
2015-07-21	516815595	694469525	-77504311	147566555	175495074	null	null	null	null	null	null	null	null	null	null	null
2015-07-22	-609738155	315496844	-49255472	86688767	147953460	null	null	null	null	null	null	null	null	null	null	null
2015-07-23	-2414931646	-14031329	-10313661	30857568	11301047	null	null	null	null	null	null	null	null	null	null	null
2015-07-24	-2685817658	-499653646	27779872	-38610881	-10996916	null	null	null	null	null	null	null	null	null	null	null
2015-07-27	-4003318813	-930091534	71087200	-111731738	-115432155	null	null	null	null	null	null	null	null	null	null	null
2015-07-28	-2762358395	-715560952	43607881	-76002343	-45210161	null	null	null	null	null	null	null	null	null	null	null
2015-07-29	-1378653080	-303338246	10946569	-6984528	-63671781	null	null	null	null	null	null	null	null	null	null	null
2015-07-30	-825648476	-157584210	-7151151	24186086	-34889857	null	null	null	null	null	null	null	null	null	null	null
2015-07-31	-147138934	69804375	-19983008	41794032	-8227840	null	null	null	null	null	null	null	null	null	null	null
2015-08-03	313362915	164515830	-29472295	54922211	-38304247	null	null	null	null	null	null	null	null	null	null	null
2015-08-04	-441478380	-48986410	6907621	-2261675	-99930054	null	null	null	null	null	null	null	null	null	null	null
2015-08-05	-478416306	3089428	-8898044	9617043	-129278564	null	null	null	null	null	null	null	null	null	null	null
2015-08-06	-848266632	-380933268	22783876	-71174015	-125122709	null	null	null	null	null	null	null	null	null	null	null
2015-08-07	-1254302496	-533385360	43776229	-128705258	-123489560	null	null	null	null	null	null	null	null	null	null	null
2015-08-10	-141703077	-223031860	21748411	-58751839	24391942	null	null	null	null	null	null	null	null	null	null	null
2015-08-11	-385990465	-318509196	21644909	-77579888	-67582201	null	null	null	null	null	null	null	null	null	null	null
2015-08-12	-927103333	-552872202	53765550	-136736518	-254630396	null	null	null	null	null	null	null	null	null	null	null
2015-08-13	-734271284	-357227133	23701980	-114907128	-188215201	null	null	null	null	null	null	null	null	null	null	null
2015-08-14	-258926406	-221601911	-3645424	-79823741	-96254407	null	null	null	null	null	null	null	null	null	null	null
2015-08-17	-484982309	-276338507	4561696	-96916666	-169917774	null	null	null	null	null	null	null	null	null	null	null
2015-08-18	-324176116	-118513732	866929	-75124084	-113133443	null	null	null	null	null	null	null	null	null	null	null
2015-08-19	-951385999	-364551930	20736180	-119785796	-107346575	null	null	null	null	null	null	null	null	null	null	null
2015-08-20	-1030308829	-609225646	54742480	-172949118	-260393673	null	null	null	null	null	null	null	null	null	null	null
2015-08-21	-1577821455	-841053676	103212934	-238086118	-484816964	null	null	null	null	null	null	null	null	null	null	null
2015-08-24	-1930278363	-964437267	98118504	-330865658	-606817232	null	null	null	null	null	null	null	null	null	null	null
2015-08-25	-2042029453	-682556461	42705140	-243525597	-493327080	null	null	null	null	null	null	null	null	null	null	null
2015-08-26	-1394786308	-242717718	-18830537	-129078481	-159645935	null	null	null	null	null	null	null	null	null	null	null
2015-08-27	-364657515	233839156	-80216033	48269661	119443331	null	null	null	null	null	null	null	null	null	null	null
2015-08-28	294630293	537122803	-101204424	150871543	212108102	null	null	null	null	null	null	null	null	null	null	null
2015-08-31	459840295	267868596	-90484942	162266597	266838907	null	null	null	null	null	null	null	null	null	null	null
2015-09-01	788225254	219679420	-17202990	51990831	90873142	null	null	null	null	null	null	null	null	null	null	null
2015-09-02	718648376	218947523	-10409763	5072001	-7310119	null	null	null	null	null	null	null	null	null	null	null
2015-09-03	340297748	-16266605	17463048	-77804733	-59956035	null	null	null	null	null	null	null	null	null	null	null
2015-09-04	-521172171	-307776951	26410867	-153232017	-85052907	null	null	null	null	null	null	null	null	null	null	null
2015-09-08	-531493908	100190454	-8275760	-44717472	80662392	null	null	null	null	null	null	null	null	null	null	null
2015-09-09	-939210496	-284409785	-8082603	-56240636	134662936	null	null	null	null	null	null	null	null	null	null	null
2015-09-10	-1010128268	-263461259	-12794923	-8489656	84092938	null	null	null	null	null	null	null	null	null	null	null
2015-09-11	-973367206	-168293053	-7603431	-20233911	-51177222	null	null	null	null	null	null	null	null	null	null	null
2015-09-14	-813913310	-78083302	-23111429	-13218315	-7602675	null	null	null	null	null	null	null	null	null	null	null
2015-09-15	-340154303	-5410632	-16677950	-25159869	-16699657	null	null	null	null	null	null	null	null	null	null	null
2015-09-16	726933839	391876479	-59512856	72917939	67869132	null	null	null	null	null	null	null	null	null	null	null
2015-09-17	1686724638	324270854	-39225481	50597493	-9682520	null	null	null	null	null	null	null	null	null	null	null
2015-09-18	915947635	79779923	-12820802	-13439979	-91314827	null	null	null	null	null	null	null	null	null	null	null
2015-09-21	1964224544	339094793	-39811046	58104487	-103095546	null	null	null	null	null	null	null	null	null	null	null
2015-09-22	784965069	-114179600	13369567	-52146501	-266088751	null	null	null	null	null	null	null	null	null	null	null
2015-09-23	406254902	-247092508	7627112	-72982118	-303225288	null	null	null	null	null	null	null	null	null	null	null
2015-09-24	-948300961	-553393323	55443337	-181197279	-372921677	null	null	null	null	null	null	null	null	null	null	null
2015-09-25	116245040	-291670240	19503131	-137674604	-187987272	null	null	null	null	null	null	null	null	null	null	null
2015-09-28	-693477739	-605691239	65860340	-236258197	-222962271	null	null	null	null	null	null	null	null	null	null	null
2015-09-29	-219634936	-428925746	31879232	-157042081	-159377317	null	null	null	null	null	null	null	null	null	null	null
2015-09-30	26374568	-228314478	10553731	-87888550	-92681380	null	null	null	null	null	null	null	null	null	null	null
2015-10-01	234590866	-241213063	9664711	-64563181	-88078661	null	null	null	null	null	null	null	null	null	null	null
2015-10-02	418410552	-135557202	15019223	-35774769	-303811687	null	null	null	null	null	null	null	null	null	null	null
2015-10-05	1242566619	302539096	-54018132	96142163	-113360851	null	null	null	null	null	null	null	null	null	null	null
2015-10-06	1657823799	440229526	-16811083	81443105	-170959361	null	null	null	null	null	null	null	null	null	null	null
2015-10-07	1198472646	286919839	17820922	18401561	-140526623	null	null	null	null	null	null	null	null	null	null	null
2015-10-08	2154461591	357486887	2890014	27382552	-60280402	null	null	null	null	null	null	null	null	null	null	null
2015-10-09	1998659608	382881684	-13563710	66037291	1372634	null	null	null	null	null	null	null	null	null	null	null
2015-10-12	1146728408	281335393	2848031	49025025	-70144776	null	null	null	null	null	null	null	null	null	null	null
2015-10-13	793455400	315899114	-12559878	21500351	-56269569	null	null	null	null	null	null	null	null	null	null	null
2015-10-14	540565991	304017671	-5893252	38899631	-220325592	null	null	null	null	null	null	null	null	null	null	null
2015-10-15	287078537	646365126	-57003414	131924770	-92558045	null	null	null	null	null	null	null	null	null	null	null
2015-10-16	-128847503	510010504	-48124106	96779467	42101994	null	null	null	null	null	null	null	null	null	null	null
2015-10-19	-280154001	556561556	-41398671	89523788	-10730842	null	null	null	null	null	null	null	null	null	null	null
2015-10-20	-637193971	239859315	-38591108	72847096	104258994	null	null	null	null	null	null	null	null	null	null	null
2015-10-21	-361450667	208934571	-41269358	49741507	176929809	null	null	null	null	null	null	null	null	null	null	null
2015-10-22	381222324	277241943	-31932897	62239492	168349663	null	null	null	null	null	null	null	null	null	null	null
2015-10-23	1037334050	523238136	-49666926	114214899	208011214	null	null	null	null	null	null	null	null	null	null	null
2015-10-26	1986768219	397726140	-39141536	87399343	204255146	null	null	null	null	null	null	null	null	null	null	null
2015-10-27	1731236008	624018017	-56961711	139024060	95632634	null	null	null	null	null	null	null	null	null	null	null
2015-10-28	2366200628	691624305	-59871342	143110715	255399237	null	null	null	null	null	null	null	null	null	null	null
2015-10-29	1634113024	189753881	-19537541	39565391	87789759	null	null	null	null	null	null	null	null	null	null	null
2015-10-30	274556389	-250839933	9982030	-61955427	-90720625	null	null	null	null	null	null	null	null	null	null	null
2015-11-02	356182860	-65971343	-6695375	-25028855	77144350	null	null	null	null	null	null	null	null	null	null	null
2015-11-03	1236099212	54307915	-14448157	-8041677	188938792	null	null	null	null	null	null	null	null	null	null	null
2015-11-04	-101434558	-125378462	-7482099	-24563887	-27428918	null	null	null	null	null	null	null	null	null	null	null
2015-11-05	-1016824492	-82856158	-9948053	-22466589	117974933	null	null	null	null	null	null	null	null	null	null	null
2015-11-06	-707605934	-53897405	-2340600	-819901	324872302	null	null	null	null	null	null	null	null	null	null	null
2015-11-09	-1749866744	-532339859	31306303	-96089232	85640685	null	null	null	null	null	null	null	null	null	null	null
2015-11-10	-2094415105	-879348189	54487050	-151578316	58495700	null	null	null	null	null	null	null	null	null	null	null
2015-11-11	-1960980325	-835946025	45578244	-155498247	81000903	null	null	null	null	null	null	null	null	null	null	null
2015-11-12	-2395560676	-880339743	54670602	-167194596	-129165704	null	null	null	null	null	null	null	null	null	null	null
2015-11-13	-2735296698	-1006604938	72135078	-205582772	-359717451	null	null	null	null	null	null	null	null	null	null	null
2015-11-16	-1744610757	-609893055	37464364	-106312591	-226445966	null	null	null	null	null	null	null	null	null	null	null
2015-11-17	-1578654017	-179282969	11446035	-17973459	-220977551	null	null	null	null	null	null	null	null	null	null	null
2015-11-18	-329642749	177313053	-3521612	58341429	-25958287	null	null	null	null	null	null	null	null	null	null	null
2015-11-19	-127683324	455148384	-36042141	136872824	130492576	null	null	null	null	null	null	null	null	null	null	null
2015-11-20	1296651550	973137603	-74906040	233260837	304020315	null	null	null	null	null	null	null	null	null	null	null
2015-11-23	979071026	852636399	-59235428	190445950	287035903	null	null	null	null	null	null	null	null	null	null	null
2015-11-24	1422413457	775926775	-52946581	114346212	180203580	null	null	null	null	null	null	null	null	null	null	null
2015-11-25	1234488057	624324010	-40020874	71451055	22375004	null	null	null	null	null	null	null	null	null	null	null
2015-11-27	2077893023	601939420	-30419270	46824255	25083463	null	null	null	null	null	null	null	null	null	null	null
2015-11-30	908493267	233584915	-9726641	-5080667	-49001393	null	null	null	null	null	null	null	null	null	null	null
2015-12-01	1590595399	471954515	-21663610	33616844	29479616	null	null	null	null	null	null	null	null	null	null	null
2015-12-02	475084654	312657257	-15658260	59674180	45650834	null	null	null	null	null	null	null	null	null	null	null
2015-12-03	-563812891	-112510336	14726274	-21146809	-25470979	null	null	null	null	null	null	null	null	null	null	null
2015-12-04	-6341727	87364262	-9867525	28140209	35822597	null	null	null	null	null	null	null	null	null	null	null
2015-12-07	-147782556	61567978	-2985587	-2521644	-18941044	null	null	null	null	null	null	null	null	null	null	null
2015-12-08	-1396919229	-230123123	16975562	-66292407	-173735921	null	null	null	null	null	null	null	null	null	null	null
2015-12-09	-1078690506	-517905296	41086466	-151532958	-202799501	null	null	null	null	null	null	null	null	null	null	null
2015-12-10	-20058061	-48359521	4376977	-35846176	-71531886	null	null	null	null	null	null	null	null	null	null	null
2015-12-11	-1449650848	-543289848	55227583	-178601394	-318657629	null	null	null	null	null	null	null	null	null	null	null
2015-12-14	-810378890	-508950508	50988334	-146606981	-311751035	null	null	null	null	null	null	null	null	null	null	null
2015-12-15	278500675	-210671691	26623126	-64453124	-99873352	null	null	null	null	null	null	null	null	null	null	null
2015-12-16	1252454820	70364679	-14758806	67961401	144903935	null	null	null	null	null	null	null	null	null	null	null
2015-12-17	-88732443	-418906151	9209715	-37228002	-21600102	null	null	null	null	null	null	null	null	null	null	null
2015-12-18	215573524	-338294319	5941514	-9329977	-40722921	null	null	null	null	null	null	null	null	null	null	null
2015-12-21	-6035254	-257443152	-17553002	-28899840	115380053	null	null	null	null	null	null	null	null	null	null	null
2015-12-22	-350092112	-323075184	-9961626	-41799495	53271737	null	null	null	null	null	null	null	null	null	null	null
2015-12-23	-477666357	-112405464	-3381710	-54535692	-41791874	null	null	null	null	null	null	null	null	null	null	null
2015-12-24	722073107	279916120	-19226643	8158259	72523536	null	null	null	null	null	null	null	null	null	null	null
2015-12-28	668393371	319498139	-29139761	28192136	202175378	null	null	null	null	null	null	null	null	null	null	null
2015-12-29	1728736084	634449472	-31281836	115901417	198425593	null	null	null	null	null	null	null	null	null	null	null
2015-12-30	712079766	251939495	-9552582	34705923	80294610	null	null	null	null	null	null	null	null	null	null	null
2015-12-31	-340064806	-178928701	18906424	-63183916	-27399264	null	null	null	null	null	null	null	null	null	null	null
2016-01-04	-1029906216	-518254330	46585717	-141829557	-191657041	null	null	null	null	null	null	null	null	null	null	null
2016-01-05	-706262935	-477289953	45229227	-121629566	-115990851	null	null	null	null	null	null	null	null	null	null	null
2016-01-06	-1663852332	-784972264	77250587	-206456615	-319019756	null	null	null	null	null	null	null	null	null	null	null
2016-01-07	-830001331	-543497525	66558582	-180151236	-434556460	null	null	null	null	null	null	null	null	null	null	null
2016-01-08	-515645324	-563504889	38776653	-190017940	-417395261	null	null	null	null	null	null	null	null	null	null	null
2016-01-11	-546388156	-472315046	19399574	-137706673	-284928915	null	null	null	null	null	null	null	null	null	null	null
2016-01-12	-262538142	-171564780	-15137860	-60088383	-301981620	null	null	null	null	null	null	null	null	null	null	null
2016-01-13	-378918772	-299229689	-6375530	-104598192	-265574759	null	null	null	null	null	null	null	null	null	null	null
2016-01-14	-187738540	-187374251	-32239672	-42186705	-31696543	null	null	null	null	null	null	null	null	null	null	null
2016-01-15	-443148365	-22964864	12917739	-50750674	-141429806	null	null	null	null	null	null	null	null	null	null	null
2016-01-19	-377381085	-7746694	-10129209	-87355696	-81220479	null	null	null	null	null	null	null	null	null	null	null
2016-01-20	-652508788	-235681371	50619557	-154313069	-212590775	null	null	null	null	null	null	null	null	null	null	null
2016-01-21	-277317266	163377534	-1664787	-28263601	-91415532	null	null	null	null	null	null	null	null	null	null	null
2016-01-22	-419400978	195025541	-9439261	-25533942	-83918838	null	null	null	null	null	null	null	null	null	null	null
2016-01-25	-383907902	95213415	-20295646	2263780	-57435499	null	null	null	null	null	null	null	null	null	null	null
2016-01-26	336256664	433560770	-20018578	101630316	-6760085	null	null	null	null	null	null	null	null	null	null	null
2016-01-27	451507948	292962433	-25333764	38537781	114020427	null	null	null	null	null	null	null	null	null	null	null
2016-01-28	101816491	-35582275	-27916566	44612955	116529455	null	null	null	null	null	null	null	null	null	null	null
2016-01-29	332807276	10921404	-26122396	47041559	146594433	null	null	null	null	null	null	null	null	null	null	null
2016-02-01	546023049	282787473	-42027133	75584899	194326153	null	null	null	null	null	null	null	null	null	null	null
2016-02-02	-484095240	-136200761	3426844	-30774110	-19154719	null	null	null	null	null	null	null	null	null	null	null
2016-02-03	-773155609	-122390741	7951411	-35897182	-158035884	null	null	null	null	null	null	null	null	null	null	null
2016-02-04	-558956711	-97343311	53788709	-124881695	-80997472	null	null	null	null	null	null	null	null	null	null	null
2016-02-05	-1670507303	-534372915	123138111	-263697541	-277002048	null	null	null	null	null	null	null	null	null	null	null
2016-02-08	-1732242370	-761663277	151883303	-318613149	-375253164	null	null	null	null	null	null	null	null	null	null	null
2016-02-09	-1151508776	-655464725	135693181	-273864240	-385787917	null	null	null	null	null	null	null	null	null	null	null
2016-02-10	-713724560	-336178598	65232347	-145740670	-153291695	null	null	null	null	null	null	null	null	null	null	null
2016-02-11	-890250772	-6265959	76443203	-159778953	-450725103	null	null	null	null	null	null	null	null	null	null	null
2016-02-12	205211734	380590450	6063675	-17973899	-238318662	null	null	null	null	null	null	null	null	null	null	null
2016-02-16	315739348	537206794	-57214436	39142736	55102427	null	null	null	null	null	null	null	null	null	null	null
2016-02-17	883837393	899432973	-98553580	131909625	305767937	null	null	null	null	null	null	null	null	null	null	null
2016-02-18	562305092	495958204	-35777429	24073766	66993635	null	null	null	null	null	null	null	null	null	null	null
2016-02-19	361063747	347835313	-71889775	102803573	258722563	null	null	null	null	null	null	null	null	null	null	null
2016-02-22	432631338	321799784	-60237526	100025875	187050665	null	null	null	null	null	null	null	null	null	null	null
2016-02-23	215887513	95235147	-9016824	56538701	-67720256	null	null	null	null	null	null	null	null	null	null	null
2016-02-24	-480113253	-240865396	36439676	-39143880	-306381264	null	null	null	null	null	null	null	null	null	null	null
2016-02-25	243165784	-13035528	11776877	19269872	-69004470	null	null	null	null	null	null	null	null	null	null	null
2016-02-26	-27906855	-330432502	40973533	-71794025	82912784	null	null	null	null	null	null	null	null	null	null	null
2016-02-29	-73844528	-338966919	58142131	-114889007	20183443	null	null	null	null	null	null	null	null	null	null	null
2016-03-01	957074216	158882816	2404477	22272583	307937343	null	null	null	null	null	null	null	null	null	null	null
2016-03-02	865505281	35436593	6189033	-11714274	548971335	null	null	null	null	null	null	null	null	null	null	null
2016-03-03	80653121	-162046954	26252769	-66613900	534252344	null	null	null	null	null	null	null	null	null	null	null
2016-03-04	951780058	192677150	841897	3627453	421104834	null	null	null	null	null	null	null	null	null	null	null
2016-03-07	786505429	-59078023	28909492	-58978661	351647350	null	null	null	null	null	null	null	null	null	null	null
2016-03-08	145902010	-191113431	82349210	-174072014	58392432	null	null	null	null	null	null	null	null	null	null	null
2016-03-09	732165739	201906876	45904087	-74486974	-57381297	null	null	null	null	null	null	null	null	null	null	null
2016-03-10	634245988	268990566	34860554	-53444676	-194727132	null	null	null	null	null	null	null	null	null	null	null
2016-03-11	1192579564	325072132	17367174	-27789744	-175058088	null	null	null	null	null	null	null	null	null	null	null
2016-03-14	712923051	521761127	-17367023	47926185	-172520244	null	null	null	null	null	null	null	null	null	null	null
2016-03-15	562768625	115547247	-20777072	126312138	-158530611	null	null	null	null	null	null	null	null	null	null	null
2016-03-16	127317296	38623065	-22142888	103878336	-220448308	null	null	null	null	null	null	null	null	null	null	null
2016-03-17	896277804	59641151	-21267804	118921228	-130062163	null	null	null	null	null	null	null	null	null	null	null
2016-03-18	822293748	-356554635	-9973902	101124447	-123518737	null	null	null	null	null	null	null	null	null	null	null
2016-03-21	1259674749	-371432192	-8298662	94885348	-108787006	null	null	null	null	null	null	null	null	null	null	null
2016-03-22	1724903791	-19495289	-35228892	87363134	-51644686	null	null	null	null	null	null	null	null	null	null	null
2016-03-23	1388112553	-312176411	2889439	14381654	-66932610	null	null	null	null	null	null	null	null	null	null	null
2016-03-24	869998251	-224120801	-4985727	30165856	-191387845	null	null	null	null	null	null	null	null	null	null	null
2016-03-28	-152229453	-41209083	18211587	-27105620	-240075008	null	null	null	null	null	null	null	null	null	null	null
2016-03-29	-176485406	123220602	9076112	-9281809	-247450691	null	null	null	null	null	null	null	null	null	null	null
2016-03-30	-482443226	135086084	-9078664	22400792	-115636586	null	null	null	null	null	null	null	null	null	null	null
2016-03-31	599661255	512739416	-27954156	67948206	-12683026	null	null	null	null	null	null	null	null	null	null	null
2016-04-01	1245147935	744329290	-44533709	110695000	105768879	null	null	null	null	null	null	null	null	null	null	null
2016-04-04	1092484789	653254965	-41472220	104100199	11193485	null	null	null	null	null	null	null	null	null	null	null
2016-04-05	378783642	318238231	-5521990	22188138	-16901142	null	null	null	null	null	null	null	null	null	null	null
2016-04-06	726919371	403298620	-2886930	20241880	-62602710	null	null	null	null	null	null	null	null	null	null	null
2016-04-07	-595538282	-45526312	21384181	-50979570	-178277889	null	null	null	null	null	null	null	null	null	null	null
2016-04-08	-1552967212	-261054737	36541025	-99541868	-127471332	null	null	null	null	null	null	null	null	null	null	null
2016-04-11	-1366575584	28646012	16278291	-27499226	13644138	null	null	null	null	null	null	null	null	null	null	null
2016-04-12	-73875327	259691028	-20344192	37361894	192567030	null	null	null	null	null	null	null	null	null	null	null
2016-04-13	128612180	225586211	-19002825	25412823	267303992	null	null	null	null	null	null	null	null	null	null	null
2016-04-14	1276685093	547671405	-45249203	108684118	405752243	null	null	null	null	null	null	null	null	null	null	null
2016-04-15	808274883	413364793	-37260807	94768908	264232794	null	null	null	null	null	null	null	null	null	null	null
2016-04-18	1839271351	406781908	-41919429	90930971	251880623	null	null	null	null	null	null	null	null	null	null	null
2016-04-19	428488056	47537174	-7743702	19226581	258379760	null	null	null	null	null	null	null	null	null	null	null
2016-04-20	67652009	-1868032	3654821	-6882094	303006947	null	null	null	null	null	null	null	null	null	null	null
2016-04-21	-839513487	-139990714	16330741	-40008074	165396714	null	null	null	null	null	null	null	null	null	null	null
2016-04-22	224296024	-232163367	30054629	-76475968	304540401	null	null	null	null	null	null	null	null	null	null	null
2016-04-25	-588501955	-257980305	29553949	-129181625	167252927	null	null	null	null	null	null	null	null	null	null	null
2016-04-26	-580280821	-126639882	20845356	-99907938	125943243	null	null	null	null	null	null	null	null	null	null	null
2016-04-27	-953547025	-445094370	58599144	-173185214	-51564334	null	null	null	null	null	null	null	null	null	null	null
2016-04-28	-232532054	-343887487	46310133	-140687561	73912044	null	null	null	null	null	null	null	null	null	null	null
2016-04-29	-855540952	-422871669	54635177	-136768576	-78458164	null	null	null	null	null	null	null	null	null	null	null
2016-05-02	-311899172	-410420726	52738221	-82814152	41794580	null	null	null	null	null	null	null	null	null	null	null
2016-05-03	-340848031	-504209646	68949077	-105960825	-85160317	null	null	null	null	null	null	null	null	null	null	null
2016-05-04	-727366543	-526929672	63392218	-94584094	-117295198	null	null	null	null	null	null	null	null	null	null	null
2016-05-05	-1511065206	-487696438	79887469	-95382811	-153385518	null	null	null	null	null	null	null	null	null	null	null
2016-05-06	-938978608	-199577437	52189495	-54843709	-89301216	null	null	null	null	null	null	null	null	null	null	null
2016-05-09	-1065715198	-204419231	44337203	-48294568	-206649295	null	null	null	null	null	null	null	null	null	null	null
2016-05-10	80715449	151709497	3389749	21472279	-78980593	null	null	null	null	null	null	null	null	null	null	null
2016-05-11	151903137	197836321	-1921775	58422990	-71581502	null	null	null	null	null	null	null	null	null	null	null
2016-05-12	574486379	-71196110	4857165	9804628	-82157063	null	null	null	null	null	null	null	null	null	null	null
2016-05-13	319589107	-51388247	-4884209	47805170	-133035188	null	null	null	null	null	null	null	null	null	null	null
2016-05-16	591204853	-23644045	-3652088	48590716	-3290225	null	null	null	null	null	null	null	null	null	null	null
2016-05-17	-385628991	-418850908	38404472	-23428473	-120566253	null	null	null	null	null	null	null	null	null	null	null
2016-05-18	429896807	-124246483	4329192	19397748	65413603	null	null	null	null	null	null	null	null	null	null	null
2016-05-19	-40789133	-118364266	8967433	-3165246	-26238482	null	null	null	null	null	null	null	null	null	null	null
2016-05-20	664081089	112407813	-10986951	4884526	83660057	null	null	null	null	null	null	null	null	null	null	null
2016-05-23	404813004	61324005	-1077089	-9238653	-6529649	null	null	null	null	null	null	null	null	null	null	null
2016-05-24	1376422992	503202713	-47410323	77578283	137363921	null	null	null	null	null	null	null	null	null	null	null
2016-05-25	1542611886	636467385	-46246024	75533780	97186383	null	null	null	null	null	null	null	null	null	null	null
2016-05-26	2087006930	990654075	-83389936	153172136	148380633	null	null	null	null	null	null	null	null	null	null	null
2016-05-27	1999729836	941634462	-70604340	148101863	166812312	null	null	null	null	null	null	null	null	null	null	null
2016-05-31	1446707770	885904991	-65719304	144335578	168825856	null	null	null	null	null	null	null	null	null	null	null
2016-06-01	1185656486	732738263	-44938493	106587934	59390065	null	null	null	null	null	null	null	null	null	null	null
2016-06-02	533794226	430370886	-22412911	51521142	-52167320	null	null	null	null	null	null	null	null	null	null	null
2016-06-03	-79658974	94645578	6381278	-14473286	-153070267	null	null	null	null	null	null	null	null	null	null	null
2016-06-06	-127093095	64280375	8578247	-17259913	-148571957	null	null	null	null	null	null	null	null	null	null	null
2016-06-07	250266373	12876498	14731335	-30674297	-90149142	null	null	null	null	null	null	null	null	null	null	null
2016-06-08	552208880	46694229	8332879	-17044183	-53155681	null	null	null	null	null	null	null	null	null	null	null
2016-06-09	561733278	172549696	17693412	-36435654	-99548896	null	null	null	null	null	null	null	null	null	null	null
2016-06-10	267883571	50180566	20614761	-36733032	-36543297	null	null	null	null	null	null	null	null	null	null	null
2016-06-13	-461715413	-196697261	49916659	-98072715	-112078403	null	null	null	null	null	null	null	null	null	null	null
2016-06-14	-1037256632	-317588458	44089402	-122063754	-236335381	null	null	null	null	null	null	null	null	null	null	null
2016-06-15	-1171732434	-286490789	38806337	-126823983	-143019006	null	null	null	null	null	null	null	null	null	null	null
2016-06-16	-738268418	-539527314	40596881	-81991504	-140150120	null	null	null	null	null	null	null	null	null	null	null
2016-06-17	-298415152	-469974032	38849689	-77130676	-115059528	null	null	null	null	null	null	null	null	null	null	null
2016-06-20	288158172	-229881704	749265	-29447014	18028002	null	null	null	null	null	null	null	null	null	null	null
2016-06-21	377157223	17603699	-9049358	18476693	178360578	null	null	null	null	null	null	null	null	null	null	null
2016-06-22	279113621	-74355263	-3127746	15238609	136289978	null	null	null	null	null	null	null	null	null	null	null
2016-06-23	555033417	249330946	-37467034	45104564	292619504	null	null	null	null	null	null	null	null	null	null	null
2016-06-24	1260417985	369374092	-15850178	57098532	186858907	null	null	null	null	null	null	null	null	null	null	null
2016-06-27	456501411	5751752	43710727	-10558307	-111176460	null	null	null	null	null	null	null	null	null	null	null
2016-06-28	1022998408	41761667	29013413	11655428	-23517310	null	null	null	null	null	null	null	null	null	null	null
2016-06-29	1114317140	204689918	7112505	55201845	28076115	null	null	null	null	null	null	null	null	null	null	null
2016-06-30	1165539204	261107108	3758485	55731951	7974531	null	null	null	null	null	null	null	null	null	null	null
2016-07-01	1360683563	561902808	-56182484	124814182	92645574	null	null	null	null	null	null	null	null	null	null	null
2016-07-05	1100142677	602780366	-72578568	141245064	164192316	null	null	null	null	null	null	null	null	null	null	null
2016-07-06	1244243292	578114317	-52862133	124203097	1521250	null	null	null	null	null	null	null	null	null	null	null
2016-07-07	446552694	335203675	-29418443	76897812	-65837192	null	null	null	null	null	null	null	null	null	null	null
2016-07-08	493491275	341534513	-31489748	84264391	-45513207	null	null	null	null	null	null	null	null	null	null	null
2016-07-11	653215915	331892221	-28018088	87896572	93379266	null	null	null	null	null	null	null	null	null	null	null
2016-07-12	2189375627	719347111	-67232028	160931436	289046470	null	null	null	null	null	null	null	null	null	null	null
2016-07-13	1729894112	537627303	-56496708	123580136	220648647	null	null	null	null	null	null	null	null	null	null	null
2016-07-14	2726756324	682156230	-51148570	110956037	282350438	null	null	null	null	null	null	null	null	null	null	null
2016-07-15	1569058827	355349132	-23146316	49080350	91764793	null	null	null	null	null	null	null	null	null	null	null
2016-07-18	1336767355	343559661	-22453270	33198744	115253065	null	null	null	null	null	null	null	null	null	null	null
2016-07-19	814558453	-70532670	2933556	-30134354	-25750510	null	null	null	null	null	null	null	null	null	null	null
2016-07-20	1463517219	171543184	-14843116	6806052	61090802	null	null	null	null	null	null	null	null	null	null	null
2016-07-21	198114055	-15446928	-11637654	-1485634	-100072878	null	null	null	null	null	null	null	null	null	null	null
2016-07-22	1257736614	205783222	-22429089	32907824	53728435	null	null	null	null	null	null	null	null	null	null	null
2016-07-25	331613243	-87509603	-524778	-18502899	-80403841	null	null	null	null	null	null	null	null	null	null	null
2016-07-26	105163563	210652265	-12334360	14011392	-43825279	null	null	null	null	null	null	null	null	null	null	null
2016-07-27	-800704957	154368502	-9543628	28203007	-96790392	null	null	null	null	null	null	null	null	null	null	null
2016-07-28	-288865902	361504451	-22271737	71330133	-50293996	null	null	null	null	null	null	null	null	null	null	null
2016-07-29	-512704108	435951504	-27452078	85450096	-104085904	null	null	null	null	null	null	null	null	null	null	null
2016-08-01	-238266540	699804337	-48121245	150200423	-55986613	null	null	null	null	null	null	null	null	null	null	null
2016-08-02	-841477632	383251224	-27870910	87007098	-113594711	null	null	null	null	null	null	null	null	null	null	null
2016-08-03	150883460	402921398	-24063056	67515600	-21680826	null	null	null	null	null	null	null	null	null	null	null
2016-08-04	711163023	367758215	-19187487	57531590	-53787942	null	null	null	null	null	null	null	null	null	null	null
2016-08-05	985963670	392922009	-18013823	67084765	-7646236	null	null	null	null	null	null	null	null	null	null	null
2016-08-08	762347069	103210846	1841030	2262020	36754682	null	null	null	null	null	null	null	null	null	null	null
2016-08-09	1598918873	487579115	-31762746	93613977	117301547	null	null	null	null	null	null	null	null	null	null	null
2016-08-10	412715395	174556107	-15849085	37479144	-5082921	null	null	null	null	null	null	null	null	null	null	null
2016-08-11	595019047	181012286	-18266903	44825077	73579684	null	null	null	null	null	null	null	null	null	null	null
2016-08-12	-627733290	-165530490	-4740449	-16063308	-21642800	null	null	null	null	null	null	null	null	null	null	null
2016-08-15	344990099	123649554	-20771063	34318178	-10787261	null	null	null	null	null	null	null	null	null	null	null
2016-08-16	-663532082	-154122352	2464309	-25694206	-85411281	null	null	null	null	null	null	null	null	null	null	null
2016-08-17	-488022097	-90081689	1398594	6768045	-13403843	null	null	null	null	null	null	null	null	null	null	null
2016-08-18	-544029686	-166196354	6641681	-15816221	-95626113	null	null	null	null	null	null	null	null	null	null	null
2016-08-19	-313255555	8726410	7635350	-11094968	-77148193	null	null	null	null	null	null	null	null	null	null	null
2016-08-22	-1067934090	-122207603	22001170	-38579644	-147526630	null	null	null	null	null	null	null	null	null	null	null
2016-08-23	183301360	134833355	5347739	14083254	-45460311	null	null	null	null	null	null	null	null	null	null	null
2016-08-24	21118786	42703707	9092718	-7817504	-50522961	null	null	null	null	null	null	null	null	null	null	null
2016-08-25	-723083599	-109373723	15977577	-22843721	35403085	null	null	null	null	null	null	null	null	null	null	null
2016-08-26	-463788659	-169483654	13205559	-4594012	98793785	null	null	null	null	null	null	null	null	null	null	null
2016-08-29	456137519	-40739501	-1562460	17908732	182749949	null	null	null	null	null	null	null	null	null	null	null
2016-08-30	-599036117	-389614147	19766367	-29321087	193340647	null	null	null	null	null	null	null	null	null	null	null
2016-08-31	-798001642	-400583290	22310306	-33675701	143750241	null	null	null	null	null	null	null	null	null	null	null
2016-09-01	-1256025865	-499041219	10694155	-56448675	-4258521	null	null	null	null	null	null	null	null	null	null	null
2016-09-02	-646858234	-297477796	-3071784	-28085874	68972508	null	null	null	null	null	null	null	null	null	null	null
2016-09-06	-949111796	-245089345	-6740659	-20255659	-105484521	null	null	null	null	null	null	null	null	null	null	null
2016-09-07	-965770033	-84843901	-18555457	5177945	-209689700	null	null	null	null	null	null	null	null	null	null	null
2016-09-08	-948898894	-119487358	-21504538	3005518	-166333502	null	null	null	null	null	null	null	null	null	null	null
2016-09-09	-934766382	-207910704	10700099	-18599830	-156862707	null	null	null	null	null	null	null	null	null	null	null
2016-09-12	-470613660	-66966081	-3536495	-9002125	-210315920	null	null	null	null	null	null	null	null	null	null	null
2016-09-13	-1205214400	-492376669	41162712	-78877079	-204462731	null	null	null	null	null	null	null	null	null	null	null
2016-09-14	-711212514	-224618913	21101884	-42894001	-113417637	null	null	null	null	null	null	null	null	null	null	null
2016-09-15	971677618	308391500	-9695077	33851042	-43907347	null	null	null	null	null	null	null	null	null	null	null
2016-09-16	996611445	411093349	-24207260	63053414	-30139599	null	null	null	null	null	null	null	null	null	null	null
2016-09-19	-289978946	-32872436	4854162	-8896029	-142660294	null	null	null	null	null	null	null	null	null	null	null
2016-09-20	-309379351	331889032	-35205631	41284596	-80253827	null	null	null	null	null	null	null	null	null	null	null
2016-09-21	339676529	279107302	-17539407	529737	-65298954	null	null	null	null	null	null	null	null	null	null	null
2016-09-22	-150520303	187232828	-9565474	-17781572	-81834495	null	null	null	null	null	null	null	null	null	null	null
2016-09-23	-83944772	142697881	-9449008	-21224475	-66926261	null	null	null	null	null	null	null	null	null	null	null
2016-09-26	-530704626	71917632	2143308	-23644247	-73259880	null	null	null	null	null	null	null	null	null	null	null
2016-09-27	-13104949	115455012	-405319	-8068573	43276827	null	null	null	null	null	null	null	null	null	null	null
2016-09-28	-809563061	-66520726	-670641	-19771859	-19529613	null	null	null	null	null	null	null	null	null	null	null
2016-09-29	-1766951484	-498234709	32149253	-93832437	-95611896	null	null	null	null	null	null	null	null	null	null	null
2016-09-30	-628843153	-3500774	6812433	-31193924	46699116	null	null	null	null	null	null	null	null	null	null	null
2016-10-03	-539861296	-16493213	6255235	-31871193	67363789	null	null	null	null	null	null	null	null	null	null	null
2016-10-04	-1275563534	-204047034	17679312	-50078515	85763608	null	null	null	null	null	null	null	null	null	null	null
2016-10-05	-521972042	-17021870	9218651	-6312820	175693511	null	null	null	null	null	null	null	null	null	null	null
2016-10-06	159872951	158295308	-3338035	22758860	128864078	null	null	null	null	null	null	null	null	null	null	null
2016-10-07	-922815719	-268084303	21944554	-43502085	-16321935	null	null	null	null	null	null	null	null	null	null	null
2016-10-10	237102464	107614579	-1776512	13673431	90989364	null	null	null	null	null	null	null	null	null	null	null
2016-10-11	182688966	-89482870	15322528	-40690193	-116124865	null	null	null	null	null	null	null	null	null	null	null
2016-10-12	-160235422	-286229735	33082628	-51757339	-145387802	null	null	null	null	null	null	null	null	null	null	null
2016-10-13	-11660001	-241049335	44131007	-40504432	-166768484	null	null	null	null	null	null	null	null	null	null	null
2016-10-14	914392816	55605836	18865709	25871533	5514354	null	null	null	null	null	null	null	null	null	null	null
2016-10-17	179735819	-175582977	21779260	1866665	-99428858	null	null	null	null	null	null	null	null	null	null	null
2016-10-18	1511133683	195235402	-7655637	84037432	64963975	null	null	null	null	null	null	null	null	null	null	null
2016-10-19	1880793437	201294741	-13200265	65069531	78784396	null	null	null	null	null	null	null	null	null	null	null
2016-10-20	1034557776	53966516	-24396354	44341051	210053132	null	null	null	null	null	null	null	null	null	null	null
2016-10-21	-115871807	47896879	-16145515	3124267	66698251	null	null	null	null	null	null	null	null	null	null	null
2016-10-24	-356653273	305871498	-23640126	32022593	161407928	null	null	null	null	null	null	null	null	null	null	null
2016-10-25	-1528201631	7372757	-3203259	-19286158	80501307	null	null	null	null	null	null	null	null	null	null	null
2016-10-26	-2511257247	-108523144	6848761	-56515182	48925674	null	null	null	null	null	null	null	null	null	null	null
2016-10-27	-2352385044	-62975877	7364597	-55945466	79312109	null	null	null	null	null	null	null	null	null	null	null
2016-10-28	-1356712673	21097602	371300	-16009193	77744377	null	null	null	null	null	null	null	null	null	null	null
2016-10-31	-589135578	-100023458	11962939	-43822662	84293641	null	null	null	null	null	null	null	null	null	null	null
2016-11-01	-636793029	-165619436	22225786	-58810294	59949389	null	null	null	null	null	null	null	null	null	null	null
2016-11-02	-685661032	-185636913	28458494	-47888896	-80715027	null	null	null	null	null	null	null	null	null	null	null
2016-11-03	-563973548	-332928138	37731233	-51364411	-63475350	null	null	null	null	null	null	null	null	null	null	null
2016-11-04	-324673552	-453275964	49493439	-74910136	23774312	null	null	null	null	null	null	null	null	null	null	null
2016-11-07	75181645	-314734536	30620891	-40052989	46924195	null	null	null	null	null	null	null	null	null	null	null
2016-11-08	826053583	-10763693	4315028	17919276	133637590	null	null	null	null	null	null	null	null	null	null	null
2016-11-09	1602261091	444859888	-13343370	85012931	511904868	null	null	null	null	null	null	null	null	null	null	null
2016-11-10	1206848635	317497526	5808397	37491748	666241854	null	null	null	null	null	null	null	null	null	null	null
2016-11-11	376779522	250823456	21751999	55143282	583445873	null	null	null	null	null	null	null	null	null	null	null
2016-11-14	-793813222	-148113435	62955971	-36509241	710027385	null	null	null	null	null	null	null	null	null	null	null
2016-11-15	-578230590	-39621955	49383873	-23328834	582995124	null	null	null	null	null	null	null	null	null	null	null
2016-11-16	-1496444956	-214306589	39902840	-37194973	161200625	null	null	null	null	null	null	null	null	null	null	null
2016-11-17	-171306868	294372145	-10770315	64208915	72612014	null	null	null	null	null	null	null	null	null	null	null
2016-11-18	367309636	166945761	-20697221	22899685	161030592	null	null	null	null	null	null	null	null	null	null	null
2016-11-21	1351755028	528764102	-53336138	112250483	23960180	null	null	null	null	null	null	null	null	null	null	null
2016-11-22	578099998	275747076	-40852431	74808309	78203759	null	null	null	null	null	null	null	null	null	null	null
2016-11-23	707022501	-50417157	-18167238	15468691	357067741	null	null	null	null	null	null	null	null	null	null	null
2016-11-25	327105986	-116051091	-8588285	2659311	172166453	null	null	null	null	null	null	null	null	null	null	null
2016-11-28	363290526	-1610430	-11199588	46831450	-22524870	null	null	null	null	null	null	null	null	null	null	null
2016-11-29	-15468690	-42189632	-9604433	26152251	1572785	null	null	null	null	null	null	null	null	null	null	null
2016-11-30	-294091262	-192887063	14501181	-31409601	184050915	null	null	null	null	null	null	null	null	null	null	null
2016-12-01	-449314249	-244055305	18626497	-61705259	222426804	null	null	null	null	null	null	null	null	null	null	null
2016-12-02	-425870295	-59164736	9907987	-39020299	135508348	null	null	null	null	null	null	null	null	null	null	null
2016-12-05	-132340747	134469493	-5269580	-38395347	412808840	null	null	null	null	null	null	null	null	null	null	null
2016-12-06	83211016	66673739	5449533	-34693826	409607315	null	null	null	null	null	null	null	null	null	null	null
2016-12-07	1304324507	397717374	-17889287	52325030	378074469	null	null	null	null	null	null	null	null	null	null	null
2016-12-08	2611880823	771605201	-46962506	151390515	307105287	null	null	null	null	null	null	null	null	null	null	null
2016-12-09	2835112022	700788611	-50430463	155594297	326515243	null	null	null	null	null	null	null	null	null	null	null
2016-12-12	1797647141	335945775	-24979136	87369033	96753033	null	null	null	null	null	null	null	null	null	null	null
2016-12-13	2172342685	627202103	-51103147	135787722	62437627	null	null	null	null	null	null	null	null	null	null	null
2016-12-14	1032364251	575416045	-25763148	118517450	-147558619	null	null	null	null	null	null	null	null	null	null	null
2016-12-15	686189342	621366921	-32103123	121899276	-76186622	null	null	null	null	null	null	null	null	null	null	null
2016-12-16	268617844	229509118	-2444374	65272147	-96710342	null	null	null	null	null	null	null	null	null	null	null
2016-12-19	1591442290	622747756	-27486160	139634400	-59190976	null	null	null	null	null	null	null	null	null	null	null
2016-12-20	1660874693	416665443	-8216535	102600908	-43052306	null	null	null	null	null	null	null	null	null	null	null
2016-12-21	1505520226	261305858	-18111117	72158462	-29365793	null	null	null	null	null	null	null	null	null	null	null
2016-12-22	596081332	-96927555	8239665	1200679	-272052222	null	null	null	null	null	null	null	null	null	null	null
2016-12-23	767896418	49797917	-2912850	12281713	-141774790	null	null	null	null	null	null	null	null	null	null	null
2016-12-27	434294810	-21690862	-3796556	8608824	-29414655	null	null	null	null	null	null	null	null	null	null	null
2016-12-28	-1152363249	-350351801	18434856	-56233281	-147626089	null	null	null	null	null	null	null	null	null	null	null
2016-12-29	-480739197	-401989053	19961538	-64487920	-108846870	null	null	null	null	null	null	null	null	null	null	null
2016-12-30	-548062215	-550415934	33592167	-74435762	39661447	null	null	null	null	null	null	null	null	null	null	null
2017-01-03	-954566181	-458940558	36022012	-72470006	155744909	null	null	null	null	null	null	null	null	null	null	null
2017-01-04	-960585812	-399059234	33479311	-74651464	181729751	null	null	null	null	null	null	null	null	null	null	null
2017-01-05	-372823299	-43734973	8496620	-13120445	117311801	null	null	null	null	null	null	null	null	null	null	null
2017-01-06	138490208	277522816	-15827444	52762302	226007582	null	null	null	null	null	null	null	null	null	null	null
2017-01-09	158353360	807240389	-51150267	121590666	80212803	null	null	null	null	null	null	null	null	null	null	null
2017-01-10	609421714	894188155	-65830850	141661499	24422881	null	null	null	null	null	null	null	null	null	null	null
2017-01-11	401646722	735178852	-52419446	121574868	-50378762	null	null	null	null	null	null	null	null	null	null	null
2017-01-12	435008080	339851116	-18245953	62561261	-56617529	null	null	null	null	null	null	null	null	null	null	null
2017-01-13	417925664	287576663	-21743012	45608046	-10667075	null	null	null	null	null	null	null	null	null	null	null
2017-01-17	733128357	-40226358	9726066	-7234191	-82034370	null	null	null	null	null	null	null	null	null	null	null
2017-01-18	174467091	-58840385	9831078	-30294771	-32322488	null	null	null	null	null	null	null	null	null	null	null
2017-01-19	-865470125	-49853587	4949206	-33179774	-122984425	null	null	null	null	null	null	null	null	null	null	null
2017-01-20	-367893555	362975740	-36727802	21261556	45028237	null	null	null	null	null	null	null	null	null	null	null
2017-01-23	-1495434455	272093252	-9833724	-10570233	-140634863	null	null	null	null	null	null	null	null	null	null	null
2017-01-24	-403197038	615495220	-45469940	39090161	57886804	null	null	null	null	null	null	null	null	null	null	null
2017-01-25	435833263	698193262	-53708941	71340697	126796675	null	null	null	null	null	null	null	null	null	null	null
2017-01-26	543607792	495279914	-59672471	87723253	287929125	null	null	null	null	null	null	null	null	null	null	null
2017-01-27	-303078720	403916444	-48475154	76705057	173191527	null	null	null	null	null	null	null	null	null	null	null
2017-01-30	-205000296	174199584	-40543175	53779147	193925901	null	null	null	null	null	null	null	null	null	null	null
2017-01-31	-1503248494	-198960435	-4428829	1450587	54159525	null	null	null	null	null	null	null	null	null	null	null
2017-02-01	-2576840470	-212237605	-575839	6698909	-32068454	null	null	null	null	null	null	null	null	null	null	null
2017-02-02	-1184011194	-168430899	20605609	-30266457	-168482570	null	null	null	null	null	null	null	null	null	null	null
2017-02-03	-84206217	-85148996	13720448	-15609403	5683598	null	null	null	null	null	null	null	null	null	null	null
2017-02-06	-128646780	81338399	1189451	12412090	28219137	null	null	null	null	null	null	null	null	null	null	null
2017-02-07	840284221	401496179	-31782060	61842473	62261447	null	null	null	null	null	null	null	null	null	null	null
2017-02-08	1619296226	316870075	-22488710	37789419	-150041759	null	null	null	null	null	null	null	null	null	null	null
2017-02-09	1333093256	610042495	-48939304	78282822	-6520838	null	null	null	null	null	null	null	null	null	null	null
2017-02-10	1275421604	573889169	-51432052	78373400	-9126636	null	null	null	null	null	null	null	null	null	null	null
2017-02-13	2559432555	789539232	-69657425	106289051	156227079	null	null	null	null	null	null	null	null	null	null	null
2017-02-14	2397052445	675548452	-58550847	88051751	325706666	null	null	null	null	null	null	null	null	null	null	null
2017-02-15	2541680496	789582095	-67994106	114189925	526417501	null	null	null	null	null	null	null	null	null	null	null
2017-02-16	1340567977	487117570	-43576456	75299836	319878011	null	null	null	null	null	null	null	null	null	null	null
2017-02-17	510795997	458699086	-40989141	70537170	107902753	null	null	null	null	null	null	null	null	null	null	null
2017-02-21	610649896	434742440	-39813725	78990967	92497755	null	null	null	null	null	null	null	null	null	null	null
2017-02-22	224946348	354752740	-31670768	66688510	-64894701	null	null	null	null	null	null	null	null	null	null	null
2017-02-23	-165826990	-56794168	-2404471	8239265	-227067797	null	null	null	null	null	null	null	null	null	null	null
2017-02-24	170330582	-68284012	2963968	248627	-217085636	null	null	null	null	null	null	null	null	null	null	null
2017-02-27	711305559	-266307189	22365565	-32923498	-30842888	null	null	null	null	null	null	null	null	null	null	null
2017-02-28	-664968405	-599222832	49360244	-86368301	-225520552	null	null	null	null	null	null	null	null	null	null	null
2017-03-01	573325788	-324771375	19356968	-45343368	-74707656	null	null	null	null	null	null	null	null	null	null	null
2017-03-02	-153311704	-320139893	17218833	-45965210	-119956768	null	null	null	null	null	null	null	null	null	null	null
2017-03-03	773411659	-185385016	8220260	-11270186	101097269	null	null	null	null	null	null	null	null	null	null	null
2017-03-06	530197561	-243552706	13184043	-21122614	-45597047	null	null	null	null	null	null	null	null	null	null	null
2017-03-07	559264618	-174130291	7147197	-5946748	-24460643	null	null	null	null	null	null	null	null	null	null	null
2017-03-08	-377013405	-236212187	18183833	-16843214	-73011006	null	null	null	null	null	null	null	null	null	null	null
2017-03-09	383730541	-68865806	6240553	12634912	151743294	null	null	null	null	null	null	null	null	null	null	null
2017-03-10	-527428399	-19329972	-10072649	22626494	33654857	null	null	null	null	null	null	null	null	null	null	null
2017-03-13	-1060464396	184888615	-26544251	62703857	145571660	null	null	null	null	null	null	null	null	null	null	null
2017-03-14	-1183464520	83229341	-23505213	40835305	96383821	null	null	null	null	null	null	null	null	null	null	null
2017-03-15	-853339355	15919389	-24220273	33833685	104526853	null	null	null	null	null	null	null	null	null	null	null
2017-03-16	-1728439823	-64910978	-17220847	23214039	99572589	null	null	null	null	null	null	null	null	null	null	null
2017-03-17	-980168587	-315217030	-7388666	7493280	12492591	null	null	null	null	null	null	null	null	null	null	null
2017-03-20	-600530200	-325131328	-7296542	252108	-133237139	null	null	null	null	null	null	null	null	null	null	null
2017-03-21	-523703810	-412943747	1848046	-6812720	-210088435	null	null	null	null	null	null	null	null	null	null	null
2017-03-22	-626667233	-293359375	-8884412	11969513	-345098250	null	null	null	null	null	null	null	null	null	null	null
2017-03-23	563387028	-264771460	-6761264	4001847	-310245260	null	null	null	null	null	null	null	null	null	null	null
2017-03-24	501151683	108089076	-15404908	16106815	-167405545	null	null	null	null	null	null	null	null	null	null	null
2017-03-27	1075717686	88076364	-22923220	34767239	-213961732	null	null	null	null	null	null	null	null	null	null	null
2017-03-28	2255167051	509198683	-51022028	105639479	61155704	null	null	null	null	null	null	null	null	null	null	null
2017-03-29	2004490781	385827968	-36857699	100154959	-28484023	null	null	null	null	null	null	null	null	null	null	null
2017-03-30	2039941351	605957482	-53052380	136119894	35345665	null	null	null	null	null	null	null	null	null	null	null
2017-03-31	2178064604	446162224	-49675581	143611709	-134991047	null	null	null	null	null	null	null	null	null	null	null
2017-04-03	1101685793	249374545	-29643175	107374680	-112099992	null	null	null	null	null	null	null	null	null	null	null
2017-04-04	1221826069	62292401	-16891887	68816552	-378877247	null	null	null	null	null	null	null	null	null	null	null
2017-04-05	1464027185	156000139	-15028241	58610659	-106986750	null	null	null	null	null	null	null	null	null	null	null
2017-04-06	1381793607	234689837	-12767671	53551275	-202440198	null	null	null	null	null	null	null	null	null	null	null
2017-04-07	1344764198	224556640	-1900909	27486646	-140699347	null	null	null	null	null	null	null	null	null	null	null
2017-04-10	2375883108	478603020	-18002946	52408745	7920010	null	null	null	null	null	null	null	null	null	null	null
2017-04-11	1071795235	186739361	-3241826	15392265	68924462	null	null	null	null	null	null	null	null	null	null	null
2017-04-12	124089040	-175076781	20676904	-35620961	-191796489	null	null	null	null	null	null	null	null	null	null	null
2017-04-13	-472319171	-373769500	28342031	-50629686	-369055986	null	null	null	null	null	null	null	null	null	null	null
2017-04-17	-80375387	-259827346	15935770	-35685950	-133813520	null	null	null	null	null	null	null	null	null	null	null
2017-04-18	-944754895	-511578742	36792058	-76092848	-288085205	null	null	null	null	null	null	null	null	null	null	null
2017-04-19	-56383320	31385087	2808359	-8179883	-98747779	null	null	null	null	null	null	null	null	null	null	null
2017-04-20	1038604203	406070592	-31261963	67513154	183982211	null	null	null	null	null	null	null	null	null	null	null
2017-04-21	379077979	293371986	-28587093	55937123	129687757	null	null	null	null	null	null	null	null	null	null	null
2017-04-24	-331055718	401275710	-32815469	68847467	83506706	null	null	null	null	null	null	null	null	null	null	null
2017-04-25	953418236	772363609	-61208726	131108812	303606144	null	null	null	null	null	null	null	null	null	null	null
2017-04-26	1302926060	576317498	-48684377	104933720	340215526	null	null	null	null	null	null	null	null	null	null	null
2017-04-27	839745283	581374445	-39943062	93670295	78631062	null	null	null	null	null	null	null	null	null	null	null
2017-04-28	961289928	857303307	-37403365	139092650	114045885	null	null	null	null	null	null	null	null	null	null	null
2017-05-01	1302802656	847442450	-35614239	151139010	118455659	null	null	null	null	null	null	null	null	null	null	null
2017-05-02	241262955	781289477	-24780278	138316596	-125036256	null	null	null	null	null	null	null	null	null	null	null
2017-05-03	-762789985	485010590	-8126466	92758839	-132125931	null	null	null	null	null	null	null	null	null	null	null
2017-05-04	-1083594504	257378516	4105278	48741516	71434069	null	null	null	null	null	null	null	null	null	null	null
2017-05-05	435138243	212973068	-8050157	33888024	86737330	null	null	null	null	null	null	null	null	null	null	null
2017-05-08	88153272	53614321	2632040	2418768	-74029474	null	null	null	null	null	null	null	null	null	null	null
2017-05-09	410270243	141578153	-7305885	19993916	118396634	null	null	null	null	null	null	null	null	null	null	null
2017-05-10	1165006968	288654404	-17977839	44658031	60768141	null	null	null	null	null	null	null	null	null	null	null
2017-05-11	722223150	-113311180	-7797823	24652291	-166716099	null	null	null	null	null	null	null	null	null	null	null
2017-05-12	127640992	-55050851	-12168225	34806458	-196698718	null	null	null	null	null	null	null	null	null	null	null
2017-05-15	828247356	141003719	-17659907	65947957	-44983720	null	null	null	null	null	null	null	null	null	null	null
2017-05-16	229766542	133854975	-11022975	65524624	-17277178	null	null	null	null	null	null	null	null	null	null	null
2017-05-17	-1185971489	-160532414	16887777	14123268	-240689532	null	null	null	null	null	null	null	null	null	null	null
2017-05-18	-1195436	560857966	-17035807	97837108	-499278	null	null	null	null	null	null	null	null	null	null	null
2017-05-19	592605169	733571760	-23017792	105916299	223315824	null	null	null	null	null	null	null	null	null	null	null
2017-05-22	346043463	710043119	-26421554	99895519	191871130	null	null	null	null	null	null	null	null	null	null	null
2017-05-23	938334077	520398647	-17520964	33521760	216065980	null	null	null	null	null	null	null	null	null	null	null
2017-05-24	2448627161	1140674489	-56967329	144774157	309365834	null	null	null	null	null	null	null	null	null	null	null
2017-05-25	2528943731	1099619002	-50888056	148396374	276239388	null	null	null	null	null	null	null	null	null	null	null
2017-05-26	1319669992	900881527	-42555163	131134768	200573708	null	null	null	null	null	null	null	null	null	null	null
2017-05-30	413194571	866140267	-38195458	130389978	40215124	null	null	null	null	null	null	null	null	null	null	null
2017-05-31	-57863242	665603949	-27589809	114454685	-203152831	null	null	null	null	null	null	null	null	null	null	null
2017-06-01	200056234	641230478	-22753319	101414586	624961	null	null	null	null	null	null	null	null	null	null	null
2017-06-02	23789283	725495530	-25743469	96574699	-196696323	null	null	null	null	null	null	null	null	null	null	null
2017-06-05	741390709	654985676	-17575894	72838292	-152820537	null	null	null	null	null	null	null	null	null	null	null
2017-06-06	741031693	498519264	-12310347	43298468	-204471277	null	null	null	null	null	null	null	null	null	null	null
2017-06-07	1166353483	841657959	-32289084	128812188	97643862	null	null	null	null	null	null	null	null	null	null	null
2017-06-08	636321439	454371135	-23379511	63961395	156153781	null	null	null	null	null	null	null	null	null	null	null
2017-06-09	278693343	-318104297	19694003	-50289437	492708827	null	null	null	null	null	null	null	null	null	null	null
2017-06-12	-810619299	-903739892	49361325	-112387310	443790207	null	null	null	null	null	null	null	null	null	null	null
2017-06-13	291579784	-707301550	25462442	-59276974	753242776	null	null	null	null	null	null	null	null	null	null	null
2017-06-14	-383734682	-943560621	33105714	-90402612	442297891	null	null	null	null	null	null	null	null	null	null	null
2017-06-15	-579612837	-572005589	34277827	-57308580	164787967	null	null	null	null	null	null	null	null	null	null	null
2017-06-16	-1138411128	-568600591	30463998	-41952359	-126737637	null	null	null	null	null	null	null	null	null	null	null
2017-06-19	464193768	221505647	-23731538	75577618	-67075507	null	null	null	null	null	null	null	null	null	null	null
2017-06-20	-849523682	-421763195	21687409	-29139008	-334637667	null	null	null	null	null	null	null	null	null	null	null
2017-06-21	129366323	-41954212	2815381	-343540	-261099143	null	null	null	null	null	null	null	null	null	null	null
2017-06-22	653518355	-88688300	-10151621	12695367	-291046716	null	null	null	null	null	null	null	null	null	null	null
2017-06-23	1569598824	482779694	-36495084	69356154	-221113109	null	null	null	null	null	null	null	null	null	null	null
2017-06-26	966923300	-4841282	-4538586	-12076282	-249069528	null	null	null	null	null	null	null	null	null	null	null
2017-06-27	1078100835	-55510046	2016885	-38068307	-11785904	null	null	null	null	null	null	null	null	null	null	null
2017-06-28	1477703192	48285816	-2197890	-26415226	248275509	null	null	null	null	null	null	null	null	null	null	null
2017-06-29	264108235	-421554910	44187921	-124516819	444913761	null	null	null	null	null	null	null	null	null	null	null
2017-06-30	262165951	-207810246	32035465	-99504736	416378164	null	null	null	null	null	null	null	null	null	null	null
2017-07-03	369739569	-133397011	30507650	-85346739	476437107	null	null	null	null	null	null	null	null	null	null	null
2017-07-05	1141213929	637686261	-20766548	40932391	402400106	null	null	null	null	null	null	null	null	null	null	null
2017-07-06	-194912481	-130571032	37596983	-65696938	200203356	null	null	null	null	null	null	null	null	null	null	null
2017-07-07	1176921057	545914945	-28733361	67143712	234806971	null	null	null	null	null	null	null	null	null	null	null
2017-07-10	940437975	406824057	-25914612	53963232	218726582	null	null	null	null	null	null	null	null	null	null	null
2017-07-11	58860813	578002084	-35140589	66689146	-1314006	null	null	null	null	null	null	null	null	null	null	null
2017-07-12	395671531	575264137	-33444390	66510265	-38346260	null	null	null	null	null	null	null	null	null	null	null
2017-07-13	1325165291	776117102	-89646058	83598548	57046774	null	null	null	null	null	null	null	null	null	null	null
2017-07-14	1361432928	743733162	-86639798	92395002	-139858204	null	null	null	null	null	null	null	null	null	null	null
2017-07-17	1269155276	644506720	-81012598	97637835	-191982565	null	null	null	null	null	null	null	null	null	null	null
2017-07-18	1461039488	844647118	-91738363	128636827	-251105617	null	null	null	null	null	null	null	null	null	null	null
2017-07-19	1398080702	817379374	-84873575	132219655	-269506970	null	null	null	null	null	null	null	null	null	null	null
2017-07-20	1234396119	1166277132	-70649456	197428009	-309693499	null	null	null	null	null	null	null	null	null	null	null
2017-07-21	-450514757	580636885	-31411748	94329423	-191917332	null	null	null	null	null	null	null	null	null	null	null
2017-07-24	-80146365	668909003	-28426055	106687597	-24225845	null	null	null	null	null	null	null	null	null	null	null
2017-07-25	944723790	132976544	-2915342	108554751	277065455	null	null	null	null	null	null	null	null	null	null	null
2017-07-26	-182884858	41457410	-1036827	88359929	170421099	null	null	null	null	null	null	null	null	null	null	null
2017-07-27	-529324806	-387502003	20287088	44459494	-9590039	null	null	null	null	null	null	null	null	null	null	null
2017-07-28	-58136512	128724056	31345403	57348451	-25851795	null	null	null	null	null	null	null	null	null	null	null
2017-07-31	-1012739870	-346328920	53509366	-14976318	5636590	null	null	null	null	null	null	null	null	null	null	null
2017-08-01	-2274936493	-245985053	26463016	-84029911	-783505	null	null	null	null	null	null	null	null	null	null	null
2017-08-02	-2147240915	-465721045	70643774	-117799820	82993175	null	null	null	null	null	null	null	null	null	null	null
2017-08-03	-2551471796	-511172292	72614594	-143870201	164524406	null	null	null	null	null	null	null	null	null	null	null
2017-08-04	-1587529077	-564736902	28792100	-90859467	252465320	null	null	null	null	null	null	null	null	null	null	null
2017-08-07	-753969522	-145623996	-2838405	-21516054	89848214	null	null	null	null	null	null	null	null	null	null	null
2017-08-08	20407890	155000214	7203383	34483378	9162469	null	null	null	null	null	null	null	null	null	null	null
2017-08-09	-5881951	131358590	-757571	18737265	-100178969	null	null	null	null	null	null	null	null	null	null	null
2017-08-10	-294060876	115045510	24546727	-23762139	-157260680	null	null	null	null	null	null	null	null	null	null	null
2017-08-11	-203269399	292851509	8758101	13570045	-332725034	null	null	null	null	null	null	null	null	null	null	null
2017-08-14	110401328	391035883	2306406	34867514	-176478413	null	null	null	null	null	null	null	null	null	null	null
2017-08-15	-85923201	441242633	-4533964	29450178	-157323918	null	null	null	null	null	null	null	null	null	null	null
2017-08-16	392947985	451560333	-43157173	89970306	-26570821	null	null	null	null	null	null	null	null	null	null	null
2017-08-17	312111360	329659724	-47651118	91754344	-52708766	null	null	null	null	null	null	null	null	null	null	null
2017-08-18	77583332	300855771	-33555077	70804557	90306725	null	null	null	null	null	null	null	null	null	null	null
2017-08-21	-580065382	-84939121	10541188	-15920235	-84009575	null	null	null	null	null	null	null	null	null	null	null
2017-08-22	168476881	23546195	-2596776	23764781	-92697711	null	null	null	null	null	null	null	null	null	null	null
2017-08-23	-411731335	-181705107	32142205	-73354937	-160714242	null	null	null	null	null	null	null	null	null	null	null
2017-08-24	123800322	-58344602	22882366	-40028699	43833338	null	null	null	null	null	null	null	null	null	null	null
2017-08-25	294089120	-470636911	46478827	-79026954	59166249	null	null	null	null	null	null	null	null	null	null	null
2017-08-28	55738799	-144818613	8770115	-11571451	88873172	null	null	null	null	null	null	null	null	null	null	null
2017-08-29	-72927697	-319446312	24020962	-52961205	-64661456	null	null	null	null	null	null	null	null	null	null	null
2017-08-30	1062252936	265741944	-22465708	60506994	55816600	null	null	null	null	null	null	null	null	null	null	null
2017-08-31	2056070586	899869845	-75597307	173048502	40042297	null	null	null	null	null	null	null	null	null	null	null
2017-09-01	2017515017	873516832	-88618727	192884072	41601281	null	null	null	null	null	null	null	null	null	null	null
2017-09-05	1698200617	346597728	-35414466	79477536	-20027715	null	null	null	null	null	null	null	null	null	null	null
2017-09-06	1710938291	140034745	-11939669	39418846	196066274	null	null	null	null	null	null	null	null	null	null	null
2017-09-07	1488404330	21604045	-3020820	14262408	-67069	null	null	null	null	null	null	null	null	null	null	null
2017-09-08	317859996	-658445006	45115336	-106250982	89237845	null	null	null	null	null	null	null	null	null	null	null
2017-09-11	600822860	-233896100	30045254	-70226296	121953979	null	null	null	null	null	null	null	null	null	null	null
2017-09-12	1946677184	130840351	-17744431	36983767	385467578	null	null	null	null	null	null	null	null	null	null	null
2017-09-13	1944926804	334746592	-24758729	48884796	222071435	null	null	null	null	null	null	null	null	null	null	null
2017-09-14	762067504	-193541474	11288625	-38296213	293569581	null	null	null	null	null	null	null	null	null	null	null
2017-09-15	1519592960	287152518	-26057794	51590691	87086305	null	null	null	null	null	null	null	null	null	null	null
2017-09-18	1070074202	-6061967	-5871232	22966024	63680287	null	null	null	null	null	null	null	null	null	null	null
2017-09-19	822378939	126713415	-2568178	14358821	-4369180	null	null	null	null	null	null	null	null	null	null	null
2017-09-20	283219522	-196344215	14694665	-31935294	120613391	null	null	null	null	null	null	null	null	null	null	null
2017-09-21	636102263	-183513086	22549858	-35556165	235302296	null	null	null	null	null	null	null	null	null	null	null
2017-09-22	-6592811	-552716464	56456572	-109768832	227395090	null	null	null	null	null	null	null	null	null	null	null
2017-09-25	-759388135	-916780699	94695771	-200547596	80828658	null	null	null	null	null	null	null	null	null	null	null
2017-09-26	-1147794012	-794642825	78305717	-174378897	14520636	null	null	null	null	null	null	null	null	null	null	null
2017-09-27	-383981527	-320599632	24021416	-50527573	66236439	null	null	null	null	null	null	null	null	null	null	null
2017-09-28	331697012	-290090327	17018309	-38317715	18435319	null	null	null	null	null	null	null	null	null	null	null
2017-09-29	1305104522	308561601	-23866010	51081755	161258133	null	null	null	null	null	null	null	null	null	null	null
2017-10-02	2326382528	781602357	-67188770	142500328	291360896	null	null	null	null	null	null	null	null	null	null	null
2017-10-03	2306266593	746134564	-58855663	133000552	299666698	null	null	null	null	null	null	null	null	null	null	null
2017-10-04	1686930685	487041783	-28296999	64112276	79699518	null	null	null	null	null	null	null	null	null	null	null
2017-10-05	2216923569	1111819176	-70804862	164854914	205479380	null	null	null	null	null	null	null	null	null	null	null
2017-10-06	789228564	606627622	-40528969	95343293	179268805	null	null	null	null	null	null	null	null	null	null	null
2017-10-09	-198570528	580188977	-39384321	97676809	40568699	null	null	null	null	null	null	null	null	null	null	null
2017-10-10	211446619	256039261	-22226483	49287447	93092194	null	null	null	null	null	null	null	null	null	null	null
2017-10-11	462610806	399922086	-38483490	90293140	108555219	null	null	null	null	null	null	null	null	null	null	null
2017-10-12	-888954188	68559108	-10522473	20289148	-151185111	null	null	null	null	null	null	null	null	null	null	null
2017-10-13	531595473	403551766	-31141268	72655661	-126407138	null	null	null	null	null	null	null	null	null	null	null
2017-10-16	1264440684	533382683	-37735722	76427817	4471247	null	null	null	null	null	null	null	null	null	null	null
2017-10-17	450940589	553845751	-39509638	63930479	-139837249	null	null	null	null	null	null	null	null	null	null	null
2017-10-18	559570623	328420013	-20797643	13579382	42317799	null	null	null	null	null	null	null	null	null	null	null
2017-10-19	1837501700	410203865	-5095154	20979979	219966421	null	null	null	null	null	null	null	null	null	null	null
2017-10-20	2150636437	327919093	-4291115	488294	274995261	null	null	null	null	null	null	null	null	null	null	null
2017-10-23	1470595664	-119040979	26513262	-63854176	217346184	null	null	null	null	null	null	null	null	null	null	null
2017-10-24	2477571596	93930786	13826793	-11052824	397805419	null	null	null	null	null	null	null	null	null	null	null
2017-10-25	1027359483	-165333389	35784119	-49625750	89778884	null	null	null	null	null	null	null	null	null	null	null
2017-10-26	1120734752	-406391376	27236313	-71041368	122445292	null	null	null	null	null	null	null	null	null	null	null
2017-10-27	1062386144	-82897846	453743	-401290	-76910603	null	null	null	null	null	null	null	null	null	null	null
2017-10-30	685365219	324475596	-39625579	98448791	-181035043	null	null	null	null	null	null	null	null	null	null	null
2017-10-31	359575326	480217867	-45003816	107927532	-297277612	null	null	null	null	null	null	null	null	null	null	null
2017-11-01	1529355624	547647257	-70181749	168994974	-26407049	null	null	null	null	null	null	null	null	null	null	null
2017-11-02	965743865	311662653	-59988388	128731948	-34512656	null	null	null	null	null	null	null	null	null	null	null
2017-11-03	618219240	92607954	-41180723	105962935	-12991539	null	null	null	null	null	null	null	null	null	null	null
2017-11-06	2097267119	175284264	-31488568	102664799	1377449	null	null	null	null	null	null	null	null	null	null	null
2017-11-07	1260953010	-281592770	-5599597	48338730	-72557964	null	null	null	null	null	null	null	null	null	null	null
2017-11-08	1402047636	128932970	-17875269	89338898	-280721696	null	null	null	null	null	null	null	null	null	null	null
2017-11-09	515891056	167769263	-3599854	52310653	-605477421	null	null	null	null	null	null	null	null	null	null	null
2017-11-10	333479581	-217416302	24621116	-43262549	-572323376	null	null	null	null	null	null	null	null	null	null	null
2017-11-13	-9876831	-372829281	33627322	-142553156	-452923348	null	null	null	null	null	null	null	null	null	null	null
2017-11-14	-297838153	-523464211	48889732	-187967644	-490946331	null	null	null	null	null	null	null	null	null	null	null
2017-11-15	-671754485	-531129850	81450073	-231952724	-274431410	null	null	null	null	null	null	null	null	null	null	null
2017-11-16	698110694	96507630	22449742	-72474922	78241281	null	null	null	null	null	null	null	null	null	null	null
2017-11-17	-371511645	-67900992	30235318	-85270772	73411732	null	null	null	null	null	null	null	null	null	null	null
2017-11-20	-57091031	85568952	36778823	-6641643	98038257	null	null	null	null	null	null	null	null	null	null	null
2017-11-21	1467155146	646960070	-4981638	106063202	308104976	null	null	null	null	null	null	null	null	null	null	null
2017-11-22	889564674	697112646	-31144063	141708617	162299919	null	null	null	null	null	null	null	null	null	null	null
2017-11-24	524703316	500778347	-12857335	114473995	76857985	null	null	null	null	null	null	null	null	null	null	null
2017-11-27	983160641	761387012	-22961747	154774488	199784005	null	null	null	null	null	null	null	null	null	null	null
2017-11-28	1511887805	737268579	-36987606	166004414	309489545	null	null	null	null	null	null	null	null	null	null	null
2017-11-29	4445759	-1864653	11755210	-2212285	455248495	null	null	null	null	null	null	null	null	null	null	null
2017-11-30	989198680	197676845	-8594543	34925266	737596114	null	null	null	null	null	null	null	null	null	null	null
2017-12-01	216110009	-215436292	24644675	-86656225	628813557	null	null	null	null	null	null	null	null	null	null	null
2017-12-04	125484428	-448411458	40548226	-150184094	684911159	null	null	null	null	null	null	null	null	null	null	null
2017-12-05	-803696052	-397695684	28912813	-133306282	509570708	null	null	null	null	null	null	null	null	null	null	null
2017-12-06	7393920	345007025	-16054615	41791725	242427752	null	null	null	null	null	null	null	null	null	null	null
2017-12-07	194063176	196772079	-9820374	17968614	73464608	null	null	null	null	null	null	null	null	null	null	null
2017-12-08	1715263322	564991011	-53468969	164947078	208657520	null	null	null	null	null	null	null	null	null	null	null
2017-12-11	3081518288	1134596293	-90303261	292664792	-10769270	null	null	null	null	null	null	null	null	null	null	null
2017-12-12	3655869114	721078037	-58562106	199449861	154644726	null	null	null	null	null	null	null	null	null	null	null
2017-12-13	4012985988	689470781	-57177054	200539750	51538117	null	null	null	null	null	null	null	null	null	null	null
2017-12-14	2342111695	611498950	-44922757	182812539	-51891008	null	null	null	null	null	null	null	null	null	null	null
2017-12-15	2125838855	963794192	-48826594	210356531	45468339	null	null	null	null	null	null	null	null	null	null	null
2017-12-18	2066811052	938828320	-42446786	195646718	212805636	null	null	null	null	null	null	null	null	null	null	null
2017-12-19	239787110	749158869	-30770046	161328134	64510566	null	null	null	null	null	null	null	null	null	null	null
2017-12-20	-986801197	286501121	-3194079	55139234	262844339	null	null	null	null	null	null	null	null	null	null	null
2017-12-21	794816481	311327484	-5570341	63459969	383876555	null	null	null	null	null	null	null	null	null	null	null
2017-12-22	-601739293	-331865517	26529290	-60190096	180096930	null	null	null	null	null	null	null	null	null	null	null
2017-12-26	-1849673935	-767228719	45781185	-142233409	45528096	null	null	null	null	null	null	null	null	null	null	null
2017-12-27	-498652584	-261010627	20785545	-57036564	-612843	null	null	null	null	null	null	null	null	null	null	null
2017-12-28	81390569	307015096	-776609	-45472328	5183473	null	null	null	null	null	null	null	null	null	null	null
2017-12-29	-1449751949	-244821006	21898743	-140798550	-147677022	null	null	null	null	null	null	null	null	null	null	null
2018-01-02	-6012992	314903286	-9864838	-35808994	-79828135	null	null	null	null	null	null	null	null	null	null	null
2018-01-03	1396220547	803531458	-39304776	75006042	86708962	null	null	null	null	null	null	null	null	null	null	null
2018-01-04	1978392566	913173601	-48138589	110232989	226387019	null	null	null	null	null	null	null	null	null	null	null
2018-01-05	2936644878	906756932	-60464873	218695901	145849013	null	null	null	null	null	null	null	null	null	null	null
2018-01-08	4007642888	1572705328	-83692735	332618303	119180140	null	null	null	null	null	null	null	null	null	null	null
2018-01-09	3675729785	1365492952	-68915594	301853333	232246462	null	null	null	null	null	null	null	null	null	null	null
2018-01-10	2730333627	744254450	-31303860	155175194	259325230	null	null	null	null	null	null	null	null	null	null	null
2018-01-11	2715856178	781433733	-32232810	164457640	238330838	null	null	null	null	null	null	null	null	null	null	null
2018-01-12	2707782689	874899834	-26594708	162993755	360853881	null	null	null	null	null	null	null	null	null	null	null
2018-01-16	1885849869	588154034	-21801030	93924477	503890659	null	null	null	null	null	null	null	null	null	null	null
2018-01-17	2544792835	648582533	-38590158	128367652	447681731	null	null	null	null	null	null	null	null	null	null	null
2018-01-18	2696144334	963142311	-56268196	206818833	241295463	null	null	null	null	null	null	null	null	null	null	null
2018-01-19	3326209260	835773589	-51208742	193756061	275313166	null	null	null	null	null	null	null	null	null	null	null
2018-01-22	3388229295	754299931	-50254238	216260150	226668212	null	null	null	null	null	null	null	null	null	null	null
2018-01-23	4688868029	1172615404	-60866269	341104222	191628419	null	null	null	null	null	null	null	null	null	null	null
2018-01-24	3225618412	743765181	-21600740	195389732	269958419	null	null	null	null	null	null	null	null	null	null	null
2018-01-25	3171169458	793242624	-29444563	235094858	254257178	null	null	null	null	null	null	null	null	null	null	null
2018-01-26	2577886237	961348112	-41337793	291611010	234629387	null	null	null	null	null	null	null	null	null	null	null
2018-01-29	737486044	312390269	-10587654	80680978	156571801	null	null	null	null	null	null	null	null	null	null	null
2018-01-30	-1011678902	-544144289	30002423	-153572604	33541665	null	null	null	null	null	null	null	null	null	null	null
2018-01-31	-1412246818	-248517364	-1653581	-55441422	-8408288	null	null	null	null	null	null	null	null	null	null	null
2018-02-01	-1501831789	-481707906	16215258	-167016419	181831709	null	null	null	null	null	null	null	null	null	null	null
2018-02-02	-2919630431	-1297757026	72164224	-411923792	-74100106	null	null	null	null	null	null	null	null	null	null	null
2018-02-05	-2632722726	-1221662209	79990821	-376022576	-208821459	null	null	null	null	null	null	null	null	null	null	null
2018-02-06	-1483384817	-815278690	37872774	-213663812	20964174	null	null	null	null	null	null	null	null	null	null	null
2018-02-07	-995208762	-626638856	66431500	-281154716	86965308	null	null	null	null	null	null	null	null	null	null	null
2018-02-08	-1643585668	-752676959	92257461	-322208907	-220001958	null	null	null	null	null	null	null	null	null	null	null
2018-02-09	-1169893799	-281445449	78748495	-162587718	-122457111	null	null	null	null	null	null	null	null	null	null	null
2018-02-12	-330144707	154854035	14724793	-8389397	172426754	null	null	null	null	null	null	null	null	null	null	null
2018-02-13	-162576464	333439316	29072463	-31626396	36916448	null	null	null	null	null	null	null	null	null	null	null
2018-02-14	174940083	282131459	-7480196	93914434	-37548347	null	null	null	null	null	null	null	null	null	null	null
2018-02-15	1143328543	925498575	-72241750	270398798	236031299	null	null	null	null	null	null	null	null	null	null	null
2018-02-16	557021415	433768626	-98617455	126822902	364557314	null	null	null	null	null	null	null	null	null	null	null
2018-02-20	409070124	429212991	-76018002	127356477	255738359	null	null	null	null	null	null	null	null	null	null	null
2018-02-21	389178547	582079368	-100409866	211377425	386313497	null	null	null	null	null	null	null	null	null	null	null
2018-02-22	495802813	573568266	-104671333	236122438	297500434	null	null	null	null	null	null	null	null	null	null	null
2018-02-23	891134553	506338483	-108879321	289412114	318988929	null	null	null	null	null	null	null	null	null	null	null
2018-02-26	1921291980	1403588682	-129739019	526446533	398204246	null	null	null	null	null	null	null	null	null	null	null
2018-02-27	1383838214	913727040	-89121959	343721354	380011729	null	null	null	null	null	null	null	null	null	null	null
2018-02-28	606500737	723358651	-83133511	293073400	336452961	null	null	null	null	null	null	null	null	null	null	null
2018-03-01	-174314904	261669377	-23508784	75198359	251739966	null	null	null	null	null	null	null	null	null	null	null
2018-03-02	-1203048187	-117860896	10902382	-86544074	16348414	null	null	null	null	null	null	null	null	null	null	null
2018-03-05	-1262581557	-345401843	21564337	-151903701	-103332167	null	null	null	null	null	null	null	null	null	null	null
2018-03-06	-799321826	128058692	-13947625	47779416	-67177826	null	null	null	null	null	null	null	null	null	null	null
2018-03-07	158654720	331173140	27344257	97199765	-237605996	null	null	null	null	null	null	null	null	null	null	null
2018-03-08	1062968808	823079973	-26689940	310816434	-189670292	null	null	null	null	null	null	null	null	null	null	null
2018-03-09	2282967960	1314207350	-52184625	482938349	62130424	null	null	null	null	null	null	null	null	null	null	null
2018-03-12	1304388129	977564538	-63534954	399168966	-19230417	null	null	null	null	null	null	null	null	null	null	null
2018-03-13	1245306614	528095628	-30765370	223264531	-142283868	null	null	null	null	null	null	null	null	null	null	null
2018-03-14	121982825	-70677368	-54247307	124587649	-135994771	null	null	null	null	null	null	null	null	null	null	null
2018-03-15	-699017083	-313203933	-27755841	26658754	-43931425	null	null	null	null	null	null	null	null	null	null	null
2018-03-16	-495403313	-800403835	-146401	-109489665	-103086498	null	null	null	null	null	null	null	null	null	null	null
2018-03-19	-407164827	-1157863582	68174180	-209378809	-148023957	null	null	null	null	null	null	null	null	null	null	null
2018-03-20	-794320102	-880619223	30361090	-83591123	30466663	null	null	null	null	null	null	null	null	null	null	null
2018-03-21	74418295	-641175961	31139238	-102718602	179108861	null	null	null	null	null	null	null	null	null	null	null
2018-03-22	-56840851	-882756318	72916183	-235608211	-68779567	null	null	null	null	null	null	null	null	null	null	null
2018-03-23	-1186885343	-790787003	78110612	-345578112	-275566972	null	null	null	null	null	null	null	null	null	null	null
2018-03-26	-732983766	-88811185	17843348	-152404658	-66357158	null	null	null	null	null	null	null	null	null	null	null
2018-03-27	-514588208	-482951653	47001408	-254561488	-189860740	null	null	null	null	null	null	null	null	null	null	null
2018-03-28	-382103907	-485868634	87386473	-348369725	-130342070	null	null	null	null	null	null	null	null	null	null	null
2018-03-29	547443956	-11687719	5279688	-118899703	173221397	null	null	null	null	null	null	null	null	null	null	null
2018-04-02	-293740429	-234661080	42128349	-132840466	165062594	null	null	null	null	null	null	null	null	null	null	null
2018-04-03	157283896	-402629257	42902592	-135293517	214605042	null	null	null	null	null	null	null	null	null	null	null
2018-04-04	966478906	298942981	28775345	13003073	200016045	null	null	null	null	null	null	null	null	null	null	null
2018-04-05	532165369	113579774	8791755	216862644	200543931	null	null	null	null	null	null	null	null	null	null	null
2018-04-06	-436192867	-430102235	51873002	42402883	-98048762	null	null	null	null	null	null	null	null	null	null	null
2018-04-09	578584219	48424540	-30794541	260724428	192786852	null	null	null	null	null	null	null	null	null	null	null
2018-04-10	590512730	193172644	-55741303	267600106	202738295	null	null	null	null	null	null	null	null	null	null	null
2018-04-11	397234355	-193119302	-51583643	150949679	106211789	null	null	null	null	null	null	null	null	null	null	null
2018-04-12	897061417	302073722	-99529793	145063994	93737530	null	null	null	null	null	null	null	null	null	null	null
2018-04-13	1197795019	459828462	-89008141	175798875	171654154	null	null	null	null	null	null	null	null	null	null	null
2018-04-16	1499997461	478391194	-80327556	162231208	123743992	null	null	null	null	null	null	null	null	null	null	null
2018-04-17	1693807061	578129132	-69089336	191906014	15565241	null	null	null	null	null	null	null	null	null	null	null
2018-04-18	1711823720	800956603	-84122636	262345292	74651267	null	null	null	null	null	null	null	null	null	null	null
2018-04-19	693418823	259007138	-23915561	81669864	135823447	null	null	null	null	null	null	null	null	null	null	null
2018-04-20	333925126	59660482	-6425553	28093715	270583450	null	null	null	null	null	null	null	null	null	null	null
2018-04-23	-208939402	-169513628	20562135	-17319380	200600252	null	null	null	null	null	null	null	null	null	null	null
2018-04-24	-1182730041	-770390087	94182826	-210296418	169723888	null	null	null	null	null	null	null	null	null	null	null
2018-04-25	-1409285482	-840928578	107409664	-250380894	144392530	null	null	null	null	null	null	null	null	null	null	null
2018-04-26	-422834844	-257583511	44666918	-72007858	6390848	null	null	null	null	null	null	null	null	null	null	null
2018-04-27	502313794	216924263	40224737	59116820	-29166780	null	null	null	null	null	null	null	null	null	null	null
2018-04-30	123981555	-13650955	54089837	8675595	15374794	null	null	null	null	null	null	null	null	null	null	null
2018-05-01	178352321	391282780	10554970	121189286	-120899552	null	null	null	null	null	null	null	null	null	null	null
2018-05-02	-459800523	174801903	42669357	123011367	-148165475	null	null	null	null	null	null	null	null	null	null	null
2018-05-03	-1413788037	-232364551	87341835	-21383664	-310591878	null	null	null	null	null	null	null	null	null	null	null
2018-05-04	-1307518465	479269	18782272	46835638	-229973074	null	null	null	null	null	null	null	null	null	null	null
2018-05-07	-542489646	441380495	-21601641	144720763	-214998241	null	null	null	null	null	null	null	null	null	null	null
2018-05-08	-605792512	70361921	5604585	46744694	232548	null	null	null	null	null	null	null	null	null	null	null
2018-05-09	303650304	439943458	-52128085	74135934	240924299	null	null	null	null	null	null	null	null	null	null	null
2018-05-10	1349731382	897046449	-95324534	226521983	451535341	null	null	null	null	null	null	null	null	null	null	null
2018-05-11	1220890238	341245773	-30925963	46199846	368757163	null	null	null	null	null	null	null	null	null	null	null
2018-05-14	719328530	282860995	-31018632	35289749	351553683	null	null	null	null	null	null	null	null	null	null	null
2018-05-15	352431692	27683773	-24853495	-524641	238395514	null	null	null	null	null	null	null	null	null	null	null
2018-05-16	467303758	33489122	-22791738	43287987	176862994	null	null	null	null	null	null	null	null	null	null	null
2018-05-17	142233101	-293122759	22960078	-87534826	42064045	null	null	null	null	null	null	null	null	null	null	null
2018-05-18	-811206825	-314209313	21344055	-72433209	-43115544	null	null	null	null	null	null	null	null	null	null	null
2018-05-21	31816806	-509786789	24340578	-161188127	-25523967	null	null	null	null	null	null	null	null	null	null	null
2018-05-22	930942952	128445404	-20598857	-9404874	107030703	null	null	null	null	null	null	null	null	null	null	null
2018-05-23	264408856	192462829	-15013361	-91424659	-35355354	null	null	null	null	null	null	null	null	null	null	null
2018-05-24	-622370785	-141131607	-10581358	-103309873	-74516154	null	null	null	null	null	null	null	null	null	null	null
2018-05-25	-554330983	401075021	-48589693	-1651265	-95587647	null	null	null	null	null	null	null	null	null	null	null
2018-05-29	-1771582511	347514038	-4349530	-24736849	-368947304	null	null	null	null	null	null	null	null	null	null	null
2018-05-30	-1373803040	504060430	-13691853	-6411276	-357087255	null	null	null	null	null	null	null	null	null	null	null
2018-05-31	-1851747108	323732353	-462840	-21766929	-379874634	null	null	null	null	null	null	null	null	null	null	null
2018-06-01	-563041140	1151004586	-47848480	89544686	-174184509	null	null	null	null	null	null	null	null	null	null	null
2018-06-04	583630598	1119767974	-55554491	107360803	42242191	null	null	null	null	null	null	null	null	null	null	null
2018-06-05	1111740262	1450361068	-97284937	190489334	141840564	null	null	null	null	null	null	null	null	null	null	null
2018-06-06	1029313304	1284328853	-86877042	162857824	120204703	null	null	null	null	null	null	null	null	null	null	null
2018-06-07	1414111175	777498215	-44756415	121404886	325170898	null	null	null	null	null	null	null	null	null	null	null
2018-06-08	1305542693	234988630	347382	29074654	180826277	null	null	null	null	null	null	null	null	null	null	null
2018-06-11	1372579006	213457927	5122374	6870085	151921354	null	null	null	null	null	null	null	null	null	null	null
2018-06-12	1266954847	245224611	-1251899	14052646	233008102	null	null	null	null	null	null	null	null	null	null	null
2018-06-13	778649120	393027846	-17947873	37921043	139838786	null	null	null	null	null	null	null	null	null	null	null
2018-06-14	1811491592	1066414037	-92804221	167683765	-99808139	null	null	null	null	null	null	null	null	null	null	null
2018-06-15	932030451	701845530	-79266026	128710968	-173141796	null	null	null	null	null	null	null	null	null	null	null
2018-06-18	134837632	678174148	-40845520	44861653	-184242388	null	null	null	null	null	null	null	null	null	null	null
2018-06-19	958796193	679759380	11759178	-27106105	-52651171	null	null	null	null	null	null	null	null	null	null	null
2018-06-20	720941859	779544060	14583761	-6687479	-53076262	null	null	null	null	null	null	null	null	null	null	null
2018-06-21	-765943112	122366687	72112539	-138171344	32357420	null	null	null	null	null	null	null	null	null	null	null
2018-06-22	34213151	187883118	55821350	-104438117	63858009	null	null	null	null	null	null	null	null	null	null	null
2018-06-25	-149817314	-377492590	83213599	-147959733	-157787186	null	null	null	null	null	null	null	null	null	null	null
2018-06-26	-455968435	-457493199	34887263	-63746974	-411435262	null	null	null	null	null	null	null	null	null	null	null
2018-06-27	-276882296	-613786626	39204160	-115128832	-366413053	null	null	null	null	null	null	null	null	null	null	null
2018-06-28	461861016	26440567	-11187102	-50694200	-144623122	null	null	null	null	null	null	null	null	null	null	null
2018-06-29	493534814	181410556	-53127080	-33797484	74304285	null	null	null	null	null	null	null	null	null	null	null
2018-07-02	1164686388	875173602	-112662670	95941888	203239205	null	null	null	null	null	null	null	null	null	null	null
2018-07-03	646335921	459888368	-71441221	5946315	283425966	null	null	null	null	null	null	null	null	null	null	null
2018-07-05	1159636249	526145992	-80889633	37986390	288125778	null	null	null	null	null	null	null	null	null	null	null
2018-07-06	1721885404	572048749	-82294934	100094060	212145274	null	null	null	null	null	null	null	null	null	null	null
2018-07-09	1814626120	971959710	-72740902	173580141	212942713	null	null	null	null	null	null	null	null	null	null	null
2018-07-10	2092894324	706430974	-55000523	123968118	182024646	null	null	null	null	null	null	null	null	null	null	null
2018-07-11	2749380157	1108961727	-38936073	92208972	128417783	null	null	null	null	null	null	null	null	null	null	null
2018-07-12	2796906429	1125010382	-37893790	103493455	71874356	null	null	null	null	null	null	null	null	null	null	null
2018-07-13	2039466258	949233403	-17388678	80635890	-160927051	null	null	null	null	null	null	null	null	null	null	null
2018-07-16	992485046	555028765	10773721	3803486	-184311739	null	null	null	null	null	null	null	null	null	null	null
2018-07-17	916922369	777174376	-3310501	47075292	-26686563	null	null	null	null	null	null	null	null	null	null	null
2018-07-18	731210630	297905331	-21798622	67503640	221816603	null	null	null	null	null	null	null	null	null	null	null
2018-07-19	-165979112	-246659580	30566538	-62287210	73270065	null	null	null	null	null	null	null	null	null	null	null
2018-07-20	229930805	-209676564	28697755	-68147288	328927993	null	null	null	null	null	null	null	null	null	null	null
2018-07-23	1314520481	156885645	18628743	-17161284	423392601	null	null	null	null	null	null	null	null	null	null	null
2018-07-24	1583347417	-148696727	-4840859	-51166377	450205177	null	null	null	null	null	null	null	null	null	null	null
2018-07-25	2130424319	483473792	-47793910	60270157	240478152	null	null	null	null	null	null	null	null	null	null	null
2018-07-26	1938512370	911783830	-78080986	69336925	462111225	null	null	null	null	null	null	null	null	null	null	null
2018-07-27	1309905029	390844329	-37899078	-33116496	513294857	null	null	null	null	null	null	null	null	null	null	null
2018-07-30	169742516	-228017151	-2763941	-132692742	444581682	null	null	null	null	null	null	null	null	null	null	null
2018-07-31	-118397040	207311230	214718	-74576398	154720021	null	null	null	null	null	null	null	null	null	null	null
2018-08-01	-1211068249	153286663	-1666809	-91734184	318406475	null	null	null	null	null	null	null	null	null	null	null
2018-08-02	-94122105	415246124	-13837496	22035377	147435545	null	null	null	null	null	null	null	null	null	null	null
2018-08-03	927910006	845043259	-32876033	138477231	66322898	null	null	null	null	null	null	null	null	null	null	null
2018-08-06	2148019138	1528805766	-83926602	254972094	-3671083	null	null	null	null	null	null	null	null	null	null	null
2018-08-07	2271803960	1366553442	-77480689	265917206	240351720	null	null	null	null	null	null	null	null	null	null	null
2018-08-08	2471161613	1251124914	-53317082	245205725	210880728	null	null	null	null	null	null	null	null	null	null	null
2018-08-09	2413567970	999367629	-45025483	234612575	217490710	null	null	null	null	null	null	null	null	null	null	null
2018-08-10	1129307699	555140104	-27757366	121666720	-15288477	null	null	null	null	null	null	null	null	null	null	null
2018-08-13	825218261	557141469	-39762474	134230563	-202701991	null	null	null	null	null	null	null	null	null	null	null
2018-08-14	467897739	236239803	-34523962	29733615	-193404500	null	null	null	null	null	null	null	null	null	null	null
2018-08-15	-523592522	-287030986	4474741	-76030262	-366773732	null	null	null	null	null	null	null	null	null	null	null
2018-08-16	-229943125	-368055360	-2773885	-61417461	-188939174	null	null	null	null	null	null	null	null	null	null	null
2018-08-17	546812460	-116245119	-19015535	-15283293	-58621737	null	null	null	null	null	null	null	null	null	null	null
2018-08-20	-1863560	-652011413	20364858	-131929991	127431269	null	null	null	null	null	null	null	null	null	null	null
2018-08-21	186238838	-316607536	15629318	-35117430	170840629	null	null	null	null	null	null	null	null	null	null	null
2018-08-22	1735467936	165822333	-28406075	80786326	212785719	null	null	null	null	null	null	null	null	null	null	null
2018-08-23	611149403	195448485	-13814276	46695379	22147958	null	null	null	null	null	null	null	null	null	null	null
2018-08-24	1278049861	597611850	-43536854	129454105	112973214	null	null	null	null	null	null	null	null	null	null	null
2018-08-27	2306894871	1184590032	-75543701	246439439	143225982	null	null	null	null	null	null	null	null	null	null	null
2018-08-28	2030023405	1133686922	-71045052	244996796	-4116204	null	null	null	null	null	null	null	null	null	null	null
2018-08-29	2406724921	1286433432	-95885756	265087715	48793025	null	null	null	null	null	null	null	null	null	null	null
2018-08-30	2235098338	1236184133	-79311397	228584916	35913104	null	null	null	null	null	null	null	null	null	null	null
2018-08-31	1019330116	1198669787	-63455605	232791737	-114632004	null	null	null	null	null	null	null	null	null	null	null
2018-09-04	-433595904	626747044	-20496983	97636912	-157843972	null	null	null	null	null	null	null	null	null	null	null
2018-09-05	-602364583	62824723	23066511	-42280223	-74377534	null	null	null	null	null	null	null	null	null	null	null
2018-09-06	-2000528819	-510663592	94792712	-184216495	-121198446	null	null	null	null	null	null	null	null	null	null	null
2018-09-07	-1661792902	-544543378	90383022	-175363605	-70508786	null	null	null	null	null	null	null	null	null	null	null
2018-09-10	-546524599	-1064181765	83647372	-287650804	27588514	null	null	null	null	null	null	null	null	null	null	null
2018-09-11	427442423	-549205615	45697070	-165241241	-21831436	null	null	null	null	null	null	null	null	null	null	null
2018-09-12	342997849	-456326038	43320698	-159199545	-160721545	null	null	null	null	null	null	null	null	null	null	null
2018-09-13	1395015471	101612278	-13869933	-11341199	-111605748	null	null	null	null	null	null	null	null	null	null	null
2018-09-14	940658305	-276131165	-16488129	-83662316	-5183374	null	null	null	null	null	null	null	null	null	null	null
2018-09-17	-400196340	-311583420	17144924	-94185334	-66905694	null	null	null	null	null	null	null	null	null	null	null
2018-09-18	23103630	-272432664	-1017561	-80816250	4514748	null	null	null	null	null	null	null	null	null	null	null
2018-09-19	556995653	-294796984	-6238287	-55402530	215504344	null	null	null	null	null	null	null	null	null	null	null
2018-09-20	585639215	-280027914	-13816470	-61343009	396095627	null	null	null	null	null	null	null	null	null	null	null
2018-09-21	-153948321	-287413977	-7558828	-12530806	187614889	null	null	null	null	null	null	null	null	null	null	null
2018-09-24	-139972679	236290876	-42127590	48627528	152254696	null	null	null	null	null	null	null	null	null	null	null
2018-09-25	-1068452637	-16905539	-6775561	-11085572	82257846	null	null	null	null	null	null	null	null	null	null	null
2018-09-26	-1228107435	477233965	-44505458	99990614	-167005083	null	null	null	null	null	null	null	null	null	null	null
2018-09-27	-1278860671	516741942	-37388092	101410219	-279988583	null	null	null	null	null	null	null	null	null	null	null
2018-09-28	152151140	644146158	-29536257	101149432	-214975164	null	null	null	null	null	null	null	null	null	null	null
2018-10-01	563569614	293055994	-12267853	87186003	-35133684	null	null	null	null	null	null	null	null	null	null	null
2018-10-02	896452543	441712351	-16139779	112107403	-115832568	null	null	null	null	null	null	null	null	null	null	null
2018-10-03	712512499	506212179	-24825968	118031839	199343985	null	null	null	null	null	null	null	null	null	null	null
2018-10-04	-441712371	-329685365	38431117	-45997835	349505795	null	null	null	null	null	null	null	null	null	null	null
2018-10-05	-853991471	-429833261	66072442	-94318240	397379207	null	null	null	null	null	null	null	null	null	null	null
2018-10-08	-632684075	-593342563	98359133	-151307127	378205311	null	null	null	null	null	null	null	null	null	null	null
2018-10-09	-861309039	-528139346	70218319	-113270375	332701630	null	null	null	null	null	null	null	null	null	null	null
2018-10-10	-1595101621	-1097060099	145111058	-288354608	10883112	null	null	null	null	null	null	null	null	null	null	null
2018-10-11	-1523647680	-459280297	70991142	-151802107	-249305737	null	null	null	null	null	null	null	null	null	null	null
2018-10-12	-1394946463	-320485594	-30695762	-74339588	-271034581	null	null	null	null	null	null	null	null	null	null	null
2018-10-15	-1035107958	97358741	-28905024	-14345490	-329234833	null	null	null	null	null	null	null	null	null	null	null
2018-10-16	-371221058	219907410	-48662253	-7331703	-57186636	null	null	null	null	null	null	null	null	null	null	null
2018-10-17	-133310033	397836069	-89838300	17228431	93034374	null	null	null	null	null	null	null	null	null	null	null
2018-10-18	34634287	28844843	-8002171	-103400049	-29040970	null	null	null	null	null	null	null	null	null	null	null
2018-10-19	798646310	373134559	26959619	-71520147	185348261	null	null	null	null	null	null	null	null	null	null	null
2018-10-22	28523018	442148030	-50218286	-6629121	42061708	null	null	null	null	null	null	null	null	null	null	null
2018-10-23	-792489615	58553123	-9701830	-111582645	-263964847	null	null	null	null	null	null	null	null	null	null	null
2018-10-24	-756726142	-111159336	35892488	-126612232	-438300601	null	null	null	null	null	null	null	null	null	null	null
2018-10-25	-88619097	302389144	-54123631	31314070	-124942041	null	null	null	null	null	null	null	null	null	null	null
2018-10-26	-915907283	215034135	13170381	-65786124	-469467133	null	null	null	null	null	null	null	null	null	null	null
2018-10-29	-304512997	113917761	56978154	-165170432	-192218240	null	null	null	null	null	null	null	null	null	null	null
2018-10-30	74779690	155935747	28603728	-119010846	127724551	null	null	null	null	null	null	null	null	null	null	null
2018-10-31	517906028	656335792	-81051670	52323254	378414842	null	null	null	null	null	null	null	null	null	null	null
2018-11-01	757527695	687171347	-74151716	34536825	356417449	null	null	null	null	null	null	null	null	null	null	null
2018-11-02	394550430	194407947	-61731236	26495547	497262451	null	null	null	null	null	null	null	null	null	null	null
2018-11-05	692175562	-167965089	-31334451	11493256	438258968	null	null	null	null	null	null	null	null	null	null	null
2018-11-06	944060949	60661172	-28664070	46198065	327806234	null	null	null	null	null	null	null	null	null	null	null
2018-11-07	1489758587	206537384	-22958248	43320416	263458563	null	null	null	null	null	null	null	null	null	null	null
2018-11-08	666067742	-293585761	46020582	-72429210	252354039	null	null	null	null	null	null	null	null	null	null	null
2018-11-09	725900928	-158134550	35436062	-85618479	187010743	null	null	null	null	null	null	null	null	null	null	null
2018-11-12	-229960241	-130583206	44253517	-111148419	8002755	null	null	null	null	null	null	null	null	null	null	null
2018-11-13	-814658646	-181892911	41088064	-155982209	93892534	null	null	null	null	null	null	null	null	null	null	null
2018-11-14	-1561607903	-416445868	55293534	-177500923	-66095905	null	null	null	null	null	null	null	null	null	null	null
2018-11-15	-745268688	-22053724	-8296290	-104872485	-87279385	null	null	null	null	null	null	null	null	null	null	null
2018-11-16	292154303	349034174	-52720883	-22460753	10003625	null	null	null	null	null	null	null	null	null	null	null
2018-11-19	284045742	288696805	-40689934	-29190982	37528651	null	null	null	null	null	null	null	null	null	null	null
2018-11-20	88392897	-132417133	49271492	-88756097	-263523214	null	null	null	null	null	null	null	null	null	null	null
2018-11-21	403106006	-60154530	57840656	-92039850	-80065939	null	null	null	null	null	null	null	null	null	null	null
2018-11-23	-347479550	-278147841	83270889	-100709541	-213145423	null	null	null	null	null	null	null	null	null	null	null
2018-11-26	-426423084	-264242716	59724801	-65143493	-105928348	null	null	null	null	null	null	null	null	null	null	null
2018-11-27	538064239	276405435	-10000918	40048088	-82419768	null	null	null	null	null	null	null	null	null	null	null
2018-11-28	1320643489	723356138	-104525711	158335246	163271291	null	null	null	null	null	null	null	null	null	null	null
2018-11-29	1057251113	429628301	-61323311	88335520	-13808681	null	null	null	null	null	null	null	null	null	null	null
2018-11-30	1989680281	689398099	-87503530	127559549	80414954	null	null	null	null	null	null	null	null	null	null	null
2018-12-03	1886796344	388179140	-39797205	19042555	89189056	null	null	null	null	null	null	null	null	null	null	null
2018-12-04	1093067649	-172367674	13924580	-39994792	-43232417	null	null	null	null	null	null	null	null	null	null	null
2018-12-06	537786597	-322577771	36957049	-82573983	-300489857	null	null	null	null	null	null	null	null	null	null	null
2018-12-07	375525712	-513239283	69698325	-143207083	-264611124	null	null	null	null	null	null	null	null	null	null	null
2018-12-10	-416820721	-489775841	71262728	-146751562	-432154515	null	null	null	null	null	null	null	null	null	null	null
2018-12-11	-483995584	-6362492	12720114	-22709538	-544636421	null	null	null	null	null	null	null	null	null	null	null
2018-12-12	63514453	577721745	-71334915	85840369	-250588398	null	null	null	null	null	null	null	null	null	null	null
2018-12-13	-14380498	407603486	-32387131	45166984	-124637410	null	null	null	null	null	null	null	null	null	null	null
2018-12-14	97195232	617592922	-65111144	104342921	-152788250	null	null	null	null	null	null	null	null	null	null	null
2018-12-17	-294069761	279882066	-329727	14028790	-61978708	null	null	null	null	null	null	null	null	null	null	null
2018-12-18	-366787034	321263381	-10860034	16688707	7447026	null	null	null	null	null	null	null	null	null	null	null
2018-12-19	-503480138	89914178	14988288	-42133300	-66005507	null	null	null	null	null	null	null	null	null	null	null
2018-12-20	-423222551	42486447	15382942	-63697948	-122329788	null	null	null	null	null	null	null	null	null	null	null
2018-12-21	-61347361	-2637127	38179259	-76260524	-94336011	null	null	null	null	null	null	null	null	null	null	null
2018-12-24	655041606	90913891	21602568	-52519752	-130642000	null	null	null	null	null	null	null	null	null	null	null
2018-12-26	976058257	13989203	6141028	-57872296	-139239182	null	null	null	null	null	null	null	null	null	null	null
2018-12-27	896101504	-188176210	56459899	-109179295	-286810283	null	null	null	null	null	null	null	null	null	null	null
2018-12-28	881878961	-248748064	32452061	-37064017	-127489389	null	null	null	null	null	null	null	null	null	null	null
2018-12-31	673498732	-386714101	18665521	-19247426	11415415	null	null	null	null	null	null	null	null	null	null	null
2019-01-02	493551994	-169660471	-42942007	63566444	174834729	null	null	null	null	null	null	null	null	null	null	null
2019-01-03	-333839420	-728123260	58705517	4277688	-2108427	null	null	null	null	null	null	null	null	null	null	null
2019-01-04	55658862	-224518251	-29760810	119176501	172664919	null	null	null	null	null	null	null	null	null	null	null
2019-01-07	582211785	147331781	-59599158	145414518	162643106	null	null	null	null	null	null	null	null	null	null	null
2019-01-08	663914585	505133054	-89279037	178002038	-82388201	null	null	null	null	null	null	null	null	null	null	null
2019-01-09	871460293	574910050	-97292421	184337615	-110210973	null	null	null	null	null	null	null	null	null	null	null
2019-01-10	1765429180	1000989027	-186537829	245750580	45223586	null	null	null	null	null	null	null	null	null	null	null
2019-01-11	730354695	416185692	-94981402	116036903	-39730511	null	null	null	null	null	null	null	null	null	null	null
2019-01-14	886878221	300408303	-64871663	80734469	-11689365	null	null	null	null	null	null	null	null	null	null	null
2019-01-15	1351847844	461726065	-109060034	126070484	206928409	null	null	null	null	null	null	null	null	null	null	null
2019-01-16	1335866482	455483072	-100459464	114694315	259064232	null	null	null	null	null	null	null	null	null	null	null
2019-01-17	1007609104	559661993	-80027485	101367758	212391339	null	null	null	null	null	null	null	null	null	null	null
2019-01-18	2771995152	1119035500	-156033370	228987687	329015665	null	null	null	null	null	null	null	null	null	null	null
2019-01-22	1737166417	917020985	-109578218	142045844	153238376	null	null	null	null	null	null	null	null	null	null	null
2019-01-23	1111985164	523274588	-42388935	47175740	67555350	null	null	null	null	null	null	null	null	null	null	null
2019-01-24	557292886	694166266	-26944591	34996616	-17513993	null	null	null	null	null	null	null	null	null	null	null
2019-01-25	886705204	750174213	-41629119	70884371	118872695	null	null	null	null	null	null	null	null	null	null	null
2019-01-28	-954993418	179984152	33158060	-56003969	-136684424	null	null	null	null	null	null	null	null	null	null	null
2019-01-29	-623005362	56216640	13513267	-45641829	-70458812	null	null	null	null	null	null	null	null	null	null	null
2019-01-30	-87137501	438191890	-44805983	67036563	53065688	null	null	null	null	null	null	null	null	null	null	null
2019-01-31	623743411	263082734	-63842175	96962733	-86986585	null	null	null	null	null	null	null	null	null	null	null
2019-02-01	91196848	-107688831	-37010682	23298282	-114038048	null	null	null	null	null	null	null	null	null	null	null
2019-02-04	1198269933	351066151	-101523098	144975064	46539316	null	null	null	null	null	null	null	null	null	null	null
2019-02-05	2033290220	873325045	-155373358	265262985	-10599837	null	null	null	null	null	null	null	null	null	null	null
2019-02-06	1859325492	370301480	-90400834	171520443	-187286583	null	null	null	null	null	null	null	null	null	null	null
2019-02-07	1004979702	-175069628	4281191	29262375	-257626567	null	null	null	null	null	null	null	null	null	null	null
2019-02-08	772316498	-248861432	7748451	-30756387	-443800911	null	null	null	null	null	null	null	null	null	null	null
2019-02-11	-302709595	-702230381	57985902	-150488283	-354545503	null	null	null	null	null	null	null	null	null	null	null
2019-02-12	-285866160	-632069965	49976512	-145196881	-177459900	null	null	null	null	null	null	null	null	null	null	null
2019-02-13	-83056538	-168388199	19514932	-65750098	27415680	null	null	null	null	null	null	null	null	null	null	null
2019-02-14	-24789418	30663372	-51148797	24819726	111041881	null	null	null	null	null	null	null	null	null	null	null
2019-02-15	1353710347	391804335	-64802400	145919559	308785244	null	null	null	null	null	null	null	null	null	null	null
2019-02-19	2373156860	752809181	-100753511	264710348	196757396	null	null	null	null	null	null	null	null	null	null	null
2019-02-20	2168721709	422789384	-56084937	179986891	148322271	null	null	null	null	null	null	null	null	null	null	null
2019-02-21	1140072870	-44915699	-15152016	67836876	-42347008	null	null	null	null	null	null	null	null	null	null	null
2019-02-22	2491867486	349633479	-23605178	115236984	-8386176	null	null	null	null	null	null	null	null	null	null	null
2019-02-25	1995521495	533232765	-27517580	118835222	-47774077	null	null	null	null	null	null	null	null	null	null	null
2019-02-26	2175977092	666862600	-19904437	123953001	-59662117	null	null	null	null	null	null	null	null	null	null	null
2019-02-27	2241198702	802640645	-30671960	159881503	-11082664	null	null	null	null	null	null	null	null	null	null	null
2019-02-28	3076201828	1225532871	-88037278	266100158	71214453	null	null	null	null	null	null	null	null	null	null	null
2019-03-01	1992302336	861025872	-60410210	177787473	292601201	null	null	null	null	null	null	null	null	null	null	null
2019-03-04	1400772074	278356619	-13320222	68696717	182716922	null	null	null	null	null	null	null	null	null	null	null
2019-03-05	201314379	117628397	-30244045	41262843	120688333	null	null	null	null	null	null	null	null	null	null	null
2019-03-06	-1117196704	-287505049	4917016	-43985405	-2808355	null	null	null	null	null	null	null	null	null	null	null
2019-03-07	-2240758459	-815065252	69806601	-173946065	-140354757	null	null	null	null	null	null	null	null	null	null	null
2019-03-08	-2661019101	-858161042	94026400	-190371964	-372595103	null	null	null	null	null	null	null	null	null	null	null
2019-03-11	-1902139401	-304307254	31062348	-70767397	-233553602	null	null	null	null	null	null	null	null	null	null	null
2019-03-12	-326707740	-79071657	16857940	-29586092	-75641020	null	null	null	null	null	null	null	null	null	null	null
2019-03-13	1262486774	658646071	-50109774	119024334	58655482	null	null	null	null	null	null	null	null	null	null	null
2019-03-14	1598158175	925090468	-71000032	187604145	253136760	null	null	null	null	null	null	null	null	null	null	null
2019-03-15	2623966998	1416433306	-130718523	315283847	288226665	null	null	null	null	null	null	null	null	null	null	null
2019-03-18	2347390046	1018265157	-110569483	310740615	295842038	null	null	null	null	null	null	null	null	null	null	null
2019-03-19	1896471108	1117704964	-105560070	321978776	250227136	null	null	null	null	null	null	null	null	null	null	null
2019-03-20	812949997	592766897	-75568057	228676309	24835618	null	null	null	null	null	null	null	null	null	null	null
2019-03-21	1975144032	1089269956	-142739126	315561231	-185217972	null	null	null	null	null	null	null	null	null	null	null
2019-03-22	1053020617	469647691	-56376347	144238415	-308346006	null	null	null	null	null	null	null	null	null	null	null
2019-03-25	749580095	735560405	-68124075	117427108	-488843821	null	null	null	null	null	null	null	null	null	null	null
2019-03-26	682211046	580416706	-54023309	94386626	-408109471	null	null	null	null	null	null	null	null	null	null	null
2019-03-27	452843063	364513959	9340554	43365768	-372655198	null	null	null	null	null	null	null	null	null	null	null
2019-03-28	214650138	60447621	40640753	-6060279	-152156712	null	null	null	null	null	null	null	null	null	null	null
2019-03-29	1147628771	659724135	-35997461	141988648	122317798	null	null	null	null	null	null	null	null	null	null	null
2019-04-01	1580298243	582095295	9890099	120324001	331558634	null	null	null	null	null	null	null	null	null	null	null
2019-04-02	1176135843	516844910	16553582	118991954	238384674	null	null	null	null	null	null	null	null	null	null	null
2019-04-03	1682136475	1128920890	-65960883	223701201	429308277	null	null	null	null	null	null	null	null	null	null	null
2019-04-04	1712305937	816532651	-36858751	148238756	472501037	null	null	null	null	null	null	null	null	null	null	null
2019-04-05	2093458452	805089527	-29562247	153587672	415421356	null	null	null	null	null	null	null	null	null	null	null
2019-04-08	1540882397	677362981	-49384104	179449689	225805936	null	null	null	null	null	null	null	null	null	null	null
2019-04-09	835220220	228023482	-9065655	41672138	78162952	null	null	null	null	null	null	null	null	null	null	null
2019-04-10	1067842920	223097795	-4058766	64308366	-45990138	null	null	null	null	null	null	null	null	null	null	null
2019-04-11	349490725	199554600	-2653428	65774745	-35965298	null	null	null	null	null	null	null	null	null	null	null
2019-04-12	84499731	212682238	-4982802	68245884	91161810	null	null	null	null	null	null	null	null	null	null	null
2019-04-15	-436816035	65266883	12886645	-8726987	60010061	null	null	null	null	null	null	null	null	null	null	null
2019-04-16	-422391064	545433389	-28959420	104231303	297163814	null	null	null	null	null	null	null	null	null	null	null
2019-04-17	-1419765208	542552515	-25762284	104326878	301312524	null	null	null	null	null	null	null	null	null	null	null
2019-04-18	-805149053	963260682	-54720449	219047614	121530624	null	null	null	null	null	null	null	null	null	null	null
2019-04-22	-804372485	719589891	-39819660	182832951	-128663831	null	null	null	null	null	null	null	null	null	null	null
2019-04-23	235444157	1300651190	-76618951	303093138	-691818	null	null	null	null	null	null	null	null	null	null	null
2019-04-24	816891270	946230191	-52558132	245365593	-178627981	null	null	null	null	null	null	null	null	null	null	null
2019-04-25	1908312291	900453178	-20150869	236686555	-153675502	null	null	null	null	null	null	null	null	null	null	null
2019-04-26	1893649095	801754047	6831157	101148110	12836356	null	null	null	null	null	null	null	null	null	null	null
2019-04-29	2276562538	964493595	13096950	96161530	212202997	null	null	null	null	null	null	null	null	null	null	null
2019-04-30	752760092	270619872	58319930	-84131680	99929858	null	null	null	null	null	null	null	null	null	null	null
2019-05-01	269692980	596014400	22860966	-6081739	104846918	null	null	null	null	null	null	null	null	null	null	null
2019-05-02	-437672614	136814861	26831785	-122772343	179389893	null	null	null	null	null	null	null	null	null	null	null
2019-05-03	-109114989	411351383	-12368423	31846996	175094093	null	null	null	null	null	null	null	null	null	null	null
2019-05-06	-408838074	457391016	-37311856	88006473	137822564	null	null	null	null	null	null	null	null	null	null	null
2019-05-07	203254683	408722299	-5370173	94200766	73733344	null	null	null	null	null	null	null	null	null	null	null
2019-05-08	393993496	298572870	46369830	-26170046	193750859	null	null	null	null	null	null	null	null	null	null	null
2019-05-09	729993704	538448209	40777812	23121696	-19643694	null	null	null	null	null	null	null	null	null	null	null
2019-05-10	124060332	-51777573	109196388	-142396182	-150662703	null	null	null	null	null	null	null	null	null	null	null
2019-05-13	-858904907	-533054725	182296124	-319973414	-357034159	null	null	null	null	null	null	null	null	null	null	null
2019-05-14	24371665	-30511687	87614637	-155295682	-91902000	null	null	null	null	null	null	null	null	null	null	null
2019-05-15	790518286	113361772	24223083	-42450989	-246861250	null	null	null	null	null	null	null	null	null	null	null
2019-05-16	1335071348	359688607	-25739825	47642578	-13202639	null	null	null	null	null	null	null	null	null	null	null
2019-05-17	1541145264	342844528	-30545074	59337028	-69500236	null	null	null	null	null	null	null	null	null	null	null
2019-05-20	1365096318	293079670	-34235059	74768834	106382461	null	null	null	null	null	null	null	null	null	null	null
2019-05-21	1310880027	407240560	-23358505	58100103	59785245	null	null	null	null	null	null	null	null	null	null	null
2019-05-22	403915226	-55498324	13757020	-77417336	90156769	null	null	null	null	null	null	null	null	null	null	null
2019-05-23	-507691511	-621543646	93526624	-239431682	-95827910	null	null	null	null	null	null	null	null	null	null	null
2019-05-24	-1097843244	-528663161	28442094	-213151864	52701982	null	null	null	null	null	null	null	null	null	null	null
2019-05-28	-735059044	-219635437	-35816992	-98086734	-88597641	null	null	null	null	null	null	null	null	null	null	null
2019-05-29	-1618809583	-705863504	31692453	-220346558	-255290229	null	null	null	null	null	null	null	null	null	null	null
2019-05-30	-1334728763	-262723722	31081236	-67494395	-221687853	null	null	null	null	null	null	null	null	null	null	null
2019-05-31	-1160656385	-38080050	35771732	-29327387	-215458741	null	null	null	null	null	null	null	null	null	null	null
2019-06-03	-682913819	-42886048	99118615	-45905334	-157519021	null	null	null	null	null	null	null	null	null	null	null
2019-06-04	-221133199	257603460	62124868	-8125688	30588569	null	null	null	null	null	null	null	null	null	null	null
2019-06-05	413094930	252985994	51859237	105983114	145610461	null	null	null	null	null	null	null	null	null	null	null
2019-06-06	719021400	180945467	67041209	64907984	186929924	null	null	null	null	null	null	null	null	null	null	null
2019-06-07	1453405692	509566877	-32254733	176480147	278994244	null	null	null	null	null	null	null	null	null	null	null
2019-06-10	1815495446	1024433633	-116600788	318721150	253835217	null	null	null	null	null	null	null	null	null	null	null
2019-06-11	1020228727	881018210	-94078162	281253969	176173893	null	null	null	null	null	null	null	null	null	null	null
2019-06-12	660810815	860217140	-82640225	169371451	48591634	null	null	null	null	null	null	null	null	null	null	null
2019-06-13	851128177	940279636	-143745865	200014069	125931020	null	null	null	null	null	null	null	null	null	null	null
2019-06-14	-30585081	545665394	-70936719	83894785	95028747	null	null	null	null	null	null	null	null	null	null	null
2019-06-17	-58035395	453977053	-61372722	58134406	-46187042	null	null	null	null	null	null	null	null	null	null	null
2019-06-18	1228403374	562771697	-75159652	100810216	10594191	null	null	null	null	null	null	null	null	null	null	null
2019-06-19	1306885877	691582223	-136258971	138894246	188729971	null	null	null	null	null	null	null	null	null	null	null
2019-06-20	1475531050	239571282	-68712239	29951506	113518263	null	null	null	null	null	null	null	null	null	null	null
2019-06-21	1073203292	419924080	-91246377	69063046	54171729	null	null	null	null	null	null	null	null	null	null	null
2019-06-24	112498893	-58930805	-70266422	55557847	108886997	null	null	null	null	null	null	null	null	null	null	null
2019-06-25	-1676359552	-785183590	40742456	-130941469	16686370	null	null	null	null	null	null	null	null	null	null	null
2019-06-26	-1375644984	-524412818	22136344	-47297083	-10880216	null	null	null	null	null	null	null	null	null	null	null
2019-06-27	-1945625343	-510920804	-38601971	-57401188	83993419	null	null	null	null	null	null	null	null	null	null	null
2019-06-28	-614823660	-654111506	-33317838	-40438435	294373367	null	null	null	null	null	null	null	null	null	null	null
2019-07-01	-643395839	-557298924	13794868	-112103930	386140747	null	null	null	null	null	null	null	null	null	null	null
2019-07-02	135432009	-179336378	-54027203	2136297	271327555	null	null	null	null	null	null	null	null	null	null	null
2019-07-03	301852413	-246315836	-26882426	-33859417	280140179	null	null	null	null	null	null	null	null	null	null	null
2019-07-05	32869678	-301545021	60414516	-72398294	247828152	null	null	null	null	null	null	null	null	null	null	null
2019-07-08	-1103164789	-494729894	100107869	-165799745	46070588	null	null	null	null	null	null	null	null	null	null	null
2019-07-09	-98184420	-159552843	33561674	-71464938	-61076686	null	null	null	null	null	null	null	null	null	null	null
2019-07-10	542644172	168234401	-10309318	18236758	11689628	null	null	null	null	null	null	null	null	null	null	null
2019-07-11	59122730	74273526	-5630602	-66842425	68791432	null	null	null	null	null	null	null	null	null	null	null
2019-07-12	977732737	593354996	-87309182	100917771	78895296	null	null	null	null	null	null	null	null	null	null	null
2019-07-15	1088924950	1014404541	-138046928	242686298	101829530	null	null	null	null	null	null	null	null	null	null	null
2019-07-16	-20963668	521153475	-66619097	66915584	84396606	null	null	null	null	null	null	null	null	null	null	null
2019-07-17	-1113855746	3566705	13379157	-88279611	29610892	null	null	null	null	null	null	null	null	null	null	null
2019-07-18	-597919692	157972600	55060245	2392298	-42838667	null	null	null	null	null	null	null	null	null	null	null
2019-07-19	-985506563	8474904	94843281	-65616170	-97443701	null	null	null	null	null	null	null	null	null	null	null
2019-07-22	-8208320	57282244	59597516	-47749692	-38138220	null	null	null	null	null	null	null	null	null	null	null
2019-07-23	1065219915	307410049	-12261744	79669570	62359490	null	null	null	null	null	null	null	null	null	null	null
2019-07-24	2176812842	746265269	-85064013	221704582	252145476	null	null	null	null	null	null	null	null	null	null	null
2019-07-25	1200319417	306222316	-64622754	82534783	127601512	null	null	null	null	null	null	null	null	null	null	null
2019-07-26	1696273133	395570715	-108244569	157536763	191955498	null	null	null	null	null	null	null	null	null	null	null
2019-07-29	780289980	-69239349	-18171777	-15387481	103529878	null	null	null	null	null	null	null	null	null	null	null
2019-07-30	-127890297	-314758193	51135968	-109640450	-55452043	null	null	null	null	null	null	null	null	null	null	null
2019-07-31	-589022630	-382281861	95948304	-173732289	-111869748	null	null	null	null	null	null	null	null	null	null	null
2019-08-01	-190281467	-119390200	20009431	-46150287	-68927845	null	null	null	null	null	null	null	null	null	null	null
2019-08-02	-912730200	-593676659	129943985	-227678597	-304117663	null	null	null	null	null	null	null	null	null	null	null
2019-08-05	-1250003678	-645925162	185875895	-244887254	-379265021	null	null	null	null	null	null	null	null	null	null	null
2019-08-06	-615787809	-88324969	71232130	-76141231	-200461302	null	null	null	null	null	null	null	null	null	null	null
2019-08-07	-1093931082	-340569157	87056569	-120079583	-416064764	null	null	null	null	null	null	null	null	null	null	null
2019-08-08	-300073826	-135149008	56690110	-45719360	-209351585	null	null	null	null	null	null	null	null	null	null	null
2019-08-09	-448281239	-106763077	38936771	-35209993	-172955214	null	null	null	null	null	null	null	null	null	null	null
2019-08-12	-181534985	-44735409	-1200136	-22438286	-195680443	null	null	null	null	null	null	null	null	null	null	null
2019-08-13	143865584	-25143785	23298266	-23229611	-135160353	null	null	null	null	null	null	null	null	null	null	null
2019-08-14	243402897	-258976288	81199146	-103184756	-132293154	null	null	null	null	null	null	null	null	null	null	null
2019-08-15	-718456255	-694755662	186301719	-231029521	-211253919	null	null	null	null	null	null	null	null	null	null	null
2019-08-16	76005305	-187110292	83635214	-48008877	15631070	null	null	null	null	null	null	null	null	null	null	null
2019-08-19	911612894	297964641	-22159851	127359924	277259777	null	null	null	null	null	null	null	null	null	null	null
2019-08-20	-173429397	-253297991	70451764	-39279250	30670928	null	null	null	null	null	null	null	null	null	null	null
2019-08-21	552073077	279975152	-44930549	123844441	296602420	null	null	null	null	null	null	null	null	null	null	null
2019-08-22	468168125	263769086	-59683711	89001458	300749966	null	null	null	null	null	null	null	null	null	null	null
2019-08-23	-523599885	-214609032	50311109	-89329909	20721691	null	null	null	null	null	null	null	null	null	null	null
2019-08-26	-893289953	-360477857	90239011	-146109632	17297017	null	null	null	null	null	null	null	null	null	null	null
2019-08-27	-392988910	-170742087	53848463	-83097081	5921838	null	null	null	null	null	null	null	null	null	null	null
2019-08-28	-547160711	-247312052	71628279	-97522518	34134721	null	null	null	null	null	null	null	null	null	null	null
2019-08-29	255156537	245682490	-6981901	48312579	35454761	null	null	null	null	null	null	null	null	null	null	null
2019-08-30	210640104	207662297	-20756816	66441429	290238401	null	null	null	null	null	null	null	null	null	null	null
2019-09-03	492815827	117047330	-3262265	25942066	85059622	null	null	null	null	null	null	null	null	null	null	null
2019-09-04	299020515	22272932	9152670	-10676390	298733920	null	null	null	null	null	null	null	null	null	null	null
2019-09-05	558376782	233628292	-20529090	14842359	310072821	null	null	null	null	null	null	null	null	null	null	null
2019-09-06	503755798	20887188	22844739	-116663965	267324436	null	null	null	null	null	null	null	null	null	null	null
2019-09-09	841681651	195374166	-447075	-72046169	330552908	null	null	null	null	null	null	null	null	null	null	null
2019-09-10	514448714	45186669	35584697	-119925241	498205172	null	null	null	null	null	null	null	null	null	null	null
2019-09-11	1584624856	472493746	-20517543	-2069191	448240298	null	null	null	null	null	null	null	null	null	null	null
2019-09-12	1731573950	332793350	6028419	-15008735	319807197	null	null	null	null	null	null	null	null	null	null	null
2019-09-13	764399889	25257788	40828008	-36952006	385689153	null	null	null	null	null	null	null	null	null	null	null
2019-09-16	1500231354	284655743	-18671295	52256918	131575058	null	null	null	null	null	null	null	null	null	null	null
2019-09-17	1716338111	582591462	-89646107	154037354	-20101693	null	null	null	null	null	null	null	null	null	null	null
2019-09-18	497891456	-18270490	-8009968	3305014	-160619739	null	null	null	null	null	null	null	null	null	null	null
2019-09-19	472696881	29337636	-22122313	35511485	-142739478	null	null	null	null	null	null	null	null	null	null	null
2019-09-20	575994229	171538311	-32921860	52300976	-394864376	null	null	null	null	null	null	null	null	null	null	null
2019-09-23	280228017	-125771925	2681268	-2943205	-282405970	null	null	null	null	null	null	null	null	null	null	null
2019-09-24	-81936919	-527944097	64512687	-94005148	-286816310	null	null	null	null	null	null	null	null	null	null	null
2019-09-25	692244266	44907862	-4269686	47942161	-87224079	null	null	null	null	null	null	null	null	null	null	null
2019-09-26	-335848096	-503151043	70501129	-121975953	-220875898	null	null	null	null	null	null	null	null	null	null	null
2019-09-27	25764910	-795611134	96812082	-161851325	72162428	null	null	null	null	null	null	null	null	null	null	null
2019-09-30	136037861	-425841513	76612410	-109582172	7713180	null	null	null	null	null	null	null	null	null	null	null
2019-10-01	-346393427	-390841290	68519822	-108825680	-10595842	null	null	null	null	null	null	null	null	null	null	null
2019-10-02	-1347503783	-1072179174	155218122	-265838845	-266428412	null	null	null	null	null	null	null	null	null	null	null
2019-10-03	-873691096	-606472854	88699777	-130636422	-224500304	null	null	null	null	null	null	null	null	null	null	null
2019-10-04	-206160613	64931997	-6466793	45454811	-279633901	null	null	null	null	null	null	null	null	null	null	null
2019-10-07	-297885350	27211112	14840348	57022554	-298653571	null	null	null	null	null	null	null	null	null	null	null
2019-10-08	-283966985	54931732	28866604	32983665	-308758066	null	null	null	null	null	null	null	null	null	null	null
2019-10-09	757934107	682220267	-70021608	189773822	-74898368	null	null	null	null	null	null	null	null	null	null	null
2019-10-10	1236095682	668727877	-77907332	204755577	157908942	null	null	null	null	null	null	null	null	null	null	null
2019-10-11	1181333692	672501348	-83079171	212406480	216066755	null	null	null	null	null	null	null	null	null	null	null
2019-10-14	763603598	669203300	-115811054	194766339	293997146	null	null	null	null	null	null	null	null	null	null	null
2019-10-15	1971054935	1077382302	-214663237	367924290	590318862	null	null	null	null	null	null	null	null	null	null	null
2019-10-16	1266910207	599655533	-133237967	222475411	440283674	null	null	null	null	null	null	null	null	null	null	null
2019-10-17	1260665582	465956763	-122148776	152648469	342544090	null	null	null	null	null	null	null	null	null	null	null
2019-10-18	217350140	-72489256	-25156143	-33209685	267034350	null	null	null	null	null	null	null	null	null	null	null
2019-10-21	854246792	-61064333	-24040234	-33004383	360392236	null	null	null	null	null	null	null	null	null	null	null
2019-10-22	452506418	-390194769	45013708	-156533183	188139212	null	null	null	null	null	null	null	null	null	null	null
2019-10-23	969905681	55055798	13558569	-8432564	264633994	null	null	null	null	null	null	null	null	null	null	null
2019-10-24	585684084	260949580	-3106049	65213062	110448191	null	null	null	null	null	null	null	null	null	null	null
2019-10-25	1615365137	758650042	-80394011	237067946	108241119	null	null	null	null	null	null	null	null	null	null	null
2019-10-28	1691432766	732945570	-85789112	270779431	103621462	null	null	null	null	null	null	null	null	null	null	null
2019-10-29	1905961755	568123271	-66257251	226930808	237781839	null	null	null	null	null	null	null	null	null	null	null
2019-10-30	1340706633	414712393	-74735717	134821451	128198913	null	null	null	null	null	null	null	null	null	null	null
2019-10-31	624699697	1932091	10101859	-11757723	180203702	null	null	null	null	null	null	null	null	null	null	null
2019-11-01	1101602028	96084050	2449381	1304494	190436161	null	null	null	null	null	null	null	null	null	null	null
2019-11-04	1293341135	94971275	2542543	-17327919	163798553	null	null	null	null	null	null	null	null	null	null	null
2019-11-05	485261036	470203061	-49966141	116308249	129701389	null	null	null	null	null	null	null	null	null	null	null
2019-11-06	461521439	181374940	-13841098	45303842	269905183	null	null	null	null	null	null	null	null	null	null	null
2019-11-07	1529674633	459134633	-69759632	173421161	453065585	null	null	null	null	null	null	null	null	null	null	null
2019-11-08	738722366	323559055	-43145276	132934121	263257313	null	null	null	null	null	null	null	null	null	null	null
2019-11-11	3894352	-18785181	-14930992	-11032404	144723644	null	null	null	null	null	null	null	null	null	null	null
2019-11-12	843446997	29617104	-28443132	47061270	168153244	null	null	null	null	null	null	null	null	null	null	null
2019-11-13	1718666578	189753772	-46664565	115842005	-9809841	null	null	null	null	null	null	null	null	null	null	null
2019-11-14	1479849814	-152877387	-1287443	-20774925	-222343244	null	null	null	null	null	null	null	null	null	null	null
2019-11-15	2068928968	-86898025	-21909358	15088409	-51130764	null	null	null	null	null	null	null	null	null	null	null
2019-11-18	1510755512	-104276863	3105166	28951056	-19617954	null	null	null	null	null	null	null	null	null	null	null
2019-11-19	649867319	-445310108	9420639	-159895600	-61520261	null	null	null	null	null	null	null	null	null	null	null
2019-11-20	76929410	-748757529	2080225	-141398743	-83442670	null	null	null	null	null	null	null	null	null	null	null
2019-11-21	-455169223	-748774205	-24237294	-141458600	-16064501	null	null	null	null	null	null	null	null	null	null	null
2019-11-22	-1802268170	-1229726652	16839792	-303276007	-24143680	null	null	null	null	null	null	null	null	null	null	null
2019-11-25	-676865478	-811569962	-32100309	-167187792	98859930	null	null	null	null	null	null	null	null	null	null	null
2019-11-26	308868608	-476279702	-32382981	-23470456	-42683503	null	null	null	null	null	null	null	null	null	null	null
2019-11-27	1292558421	158891287	-73987246	46150495	156352778	null	null	null	null	null	null	null	null	null	null	null
2019-11-29	1470115794	261215758	-57558064	113853397	155493737	null	null	null	null	null	null	null	null	null	null	null
2019-12-02	1504466646	260839705	-21139526	92073821	-25239911	null	null	null	null	null	null	null	null	null	null	null
2019-12-03	349114058	-224930543	52628185	-83756535	-288696734	null	null	null	null	null	null	null	null	null	null	null
2019-12-04	253357523	-155600692	43155673	-85759194	-134245323	null	null	null	null	null	null	null	null	null	null	null
2019-12-05	-792437011	-343064408	78512305	-157436401	-70592197	null	null	null	null	null	null	null	null	null	null	null
2019-12-06	-135792904	9453461	27755743	-55021216	26242156	null	null	null	null	null	null	null	null	null	null	null
2019-12-09	200288274	247721571	-9657227	40622800	118204107	null	null	null	null	null	null	null	null	null	null	null
2019-12-10	1312780332	646091212	-61858675	219196693	262885983	null	null	null	null	null	null	null	null	null	null	null
2019-12-11	1719239800	649827835	-56664045	236578721	137544366	null	null	null	null	null	null	null	null	null	null	null
2019-12-12	2033742035	900116710	-107181189	340267413	162061241	null	null	null	null	null	null	null	null	null	null	null
2019-12-13	1888507589	979704611	-48944696	181685116	-5706479	null	null	null	null	null	null	null	null	null	null	null
2019-12-16	2832670042	1241653906	-86038215	286669467	116552024	null	null	null	null	null	null	null	null	null	null	null
2019-12-17	3195459823	839291329	-61605485	277094710	190207435	null	null	null	null	null	null	null	null	null	null	null
2019-12-18	3016716698	821498590	-58980587	262429858	212399851	null	null	null	null	null	null	null	null	null	null	null
2019-12-19	3672500984	796762113	-37707675	267313064	107902956	null	null	null	null	null	null	null	null	null	null	null
2019-12-20	4334119803	771782279	-92849592	420578307	171140246	null	null	null	null	null	null	null	null	null	null	null
2019-12-23	4351082519	865092670	-82456886	403316700	27065075	null	null	null	null	null	null	null	null	null	null	null
2019-12-24	3243700000	1058017527	-108701769	300379504	-9561950	null	null	null	null	null	null	null	null	null	null	null
2019-12-26	3247006355	1055002016	-105209283	322485078	66216024	null	null	null	null	null	null	null	null	null	null	null
2019-12-27	1631385793	835281153	-53130602	136712028	-17706194	null	null	null	null	null	null	null	null	null	null	null
2019-12-30	-80398433	324290303	13915338	-36813760	-13955834	null	null	null	null	null	null	null	null	null	null	null
2019-12-31	-1147836124	-228242416	53914237	-146975706	17953241	null	null	null	null	null	null	null	null	null	null	null
2020-01-02	-1137360283	170542197	26261989	-10669129	78355525	null	null	null	null	null	null	null	null	null	null	null
2020-01-03	-1519567171	254034652	11804300	-4644814	-92992046	null	null	null	null	null	null	null	null	null	null	null
2020-01-06	-72917654	522189424	-53232862	195020447	-115889807	null	null	null	null	null	null	null	null	null	null	null
2020-01-07	50443528	853779852	-77541590	250895447	-206646444	null	null	null	null	null	null	null	null	null	null	null
2020-01-08	925275792	1375883666	-138951292	387360289	-63653801	null	443432567	1553626052	533419836	-301297143	829433767	289244739	714272486	-126570535	78036210	null
2020-01-09	1300502012	1289517131	-127123778	357192679	-71019628	null	411428281	846028458	542542071	-362138856	878657339	13953485	733554137	-304532542	-48784758	null
2020-01-10	1161469386	810099183	-94469896	199827831	-39778850	null	683514683	227610764	283786070	-309897232	835803638	2716063	1042589257	-350661596	-174859855	null
2020-01-13	895334412	789952670	-94121071	204887783	84165061	null	735476369	300832568	298236283	-804685586	841072990	33297775	1008874996	-217292822	-273450557	null
2020-01-14	1683502630	563693132	-64626793	183348020	235414491	null	398378442	314715934	382740250	-915130126	484212381	10809589	769729554	-167504088	-232385669	null
2020-01-15	1547091385	399960118	-47061815	153552545	10276590	null	121842736	-491320242	235644297	-658645683	456608115	-108827806	679200970	-145570142	-127398607	null
2020-01-16	1977584404	207189113	-34735784	115119239	36935202	null	158539194	-42074923	66097034	-749230506	136776853	-71029490	647683309	14306524	-17062042	null
2020-01-17	2718839411	535485156	-58599546	288233513	204748426	null	-86478931	-111853245	460411876	-828167865	-20933376	88392189	772398856	91648292	182348990	null
2020-01-21	3311003672	525218718	-48339107	306031646	97933052	null	-224910872	-44329288	275693095	-355666659	-352982491	-375225431	660797060	-33285261	275671071	null
2020-01-22	2607766287	816809643	-109614623	429453350	108280229	null	99491107	-50705271	732457712	248229554	-246796714	-499475932	1068138823	-19337743	323432763	null
2020-01-23	2043465333	542200350	-100520600	357214872	123187170	null	229153920	411918545	767366482	128867972	-498827748	-286049632	1033134905	142211493	167182997	null
2020-01-24	1015999680	96842373	-61764176	223317720	-142789635	null	-79232443	-96896434	632130391	-753351595	-487929371	-53611982	694080672	258138245	-14943071	null
2020-01-27	-255957765	-363148118	15140830	-2252091	-334219072	null	-182321052	337342136	-40310468	-726705750	-417770092	-292089045	88004545	183520020	-92179711	null
2020-01-28	-949778410	-346994220	2346029	-11060372	-190089193	null	-58316443	192282979	197048063	-848171892	-157670969	137734483	147037583	303681580	-85407092	null
2020-01-29	-917688314	-317590701	21278808	-20772640	-193370333	null	-329906029	195165360	258202998	-455765487	127005421	191890320	21732676	266299834	-159773385	null
2020-01-30	-510986035	30276192	-12462281	90501693	-143058229	null	-484922336	382810373	64227607	253157543	400728144	-93602923	-321980120	113487353	-80079016	null
2020-01-31	-521782666	134930521	25070363	48046189	-125499151	null	-487773908	972125898	-251114424	250060954	299612078	-397416105	-466083520	-136836236	-72751465	null
2020-02-03	295685143	675127624	-75257168	286482224	74157737	null	-148994656	1436115934	96570721	1281382212	402925972	32341144	196135702	4905698	-25671182	null
2020-02-04	333280619	646171743	-88121437	295590097	114482191	null	-180632592	1539303812	141504213	1906880327	461171605	28839947	-1756600	17658917	-37499567	null
2020-02-05	1233365790	257542596	-64085197	119657800	177126605	null	64263684	453737240	29433105	875548410	279753973	246063511	-399415557	15776307	13687681	null
2020-02-06	443757438	237777659	-11341422	32624555	194966543	null	230722133	547424015	-44786364	1071832184	-7943064	54898679	150002687	95717190	-93792478	null
2020-02-07	165484416	285883337	-55382066	68609720	268465452	null	306973921	906473269	40211701	2315983992	358609810	313634186	477643122	120699671	78416617	null
2020-02-10	244064044	312980674	-43427374	75246729	160673383	null	418930019	854388782	319684479	2927267780	278365235	242580353	335306238	34465133	105606846	null
2020-02-11	159940930	314055343	-22901322	62105036	99788715	null	520143176	-47844701	52299688	2905253280	-172613608	224851794	602064287	13830647	129792434	null
2020-02-12	172766187	797670146	-73023979	271064756	54762031	null	597782764	854906334	222230932	4204156524	-3350661	434060279	1043829042	-2261327	102293943	null
2020-02-13	1234115286	905881120	-66785881	387232597	52902098	null	686739601	1060018298	536897642	3332726060	307019551	739167038	613047173	-56049196	285783037	null
2020-02-14	1168395073	874459583	-59876734	407944057	104048462	null	1048970723	406097916	683450169	2045359776	292903614	715848074	616832501	-72746525	189097244	null
2020-02-18	496420987	939280729	-60761972	406912865	37116931	null	1058922368	558206222	652742940	1632300542	486625800	783380438	412248666	-91654907	184740839	null
2020-02-19	660458852	904964872	-53814505	418492589	15932820	null	1115588166	1544972059	885109122	1071387617	666062157	654122017	316253831	-87010533	204797163	null
2020-02-20	-75567367	333748363	9676981	179125872	-83474599	null	706172005	735849453	349583568	-51089796	413162824	400152761	-12126572	-231165591	239563283	null
2020-02-21	-1166006274	-104483084	51121296	-126560780	-182504377	null	334088732	-369190661	-184019559	-514941718	-55613228	101575675	-227424693	-281047386	28239472	null
2020-02-24	-895285320	-168837418	93208954	-176891303	-287131107	null	-189238737	-806212875	-136787575	-916092704	-445611883	33586704	-624323333	-307908252	-2906806	null
2020-02-25	-1143465847	-606525711	195917465	-427964725	-330996664	null	-701383888	-1959733031	-767757047	-2380110540	-748363105	-324683296	-808934026	-290319519	-170111017	null
2020-02-26	-1680634024	-799656770	175804107	-510943558	-363870182	null	-818899656	-2047684537	-881994536	-2025151157	-512816066	-123438612	-686679126	-283857220	-232846710	null
2020-02-27	-2154491928	-624102778	185046450	-441357643	-520596660	null	-852782064	-1909753262	-1026609954	-2866814613	-615730958	182421068	-917713060	-288727576	-252015723	null
2020-02-28	-910552740	-329464930	101959891	-241182762	-557343294	null	-404668654	-1290315260	-691701078	-1096254497	-258744270	233696088	-944029103	-211107159	-107039012	null
2020-03-02	-196976500	-34914491	-4812556	-59523976	-319002446	null	-333945943	-250501508	-461134275	-1201842920	-166566938	409185206	-414675417	-34920164	-123131528	null
2020-03-03	261712719	-16283003	-39795624	6468429	-357661892	null	-242693165	-254832704	-152660664	-653887904	-273945670	592919135	-410551031	-39835274	-25120374	null
2020-03-04	156363282	42440847	-33132279	7905288	-240591685	null	-206765613	-1160224354	-160468812	-721632839	-332282306	529912716	-380114684	-48545350	2500056	null
2020-03-05	672502065	1151056	-54747149	37856217	-171104183	null	-128903950	-897206492	34439315	-272932052	-356474280	203787390	-324143491	-16496809	28212428	null
2020-03-06	301659438	-316081456	9599877	-60107635	-122581806	null	-544134365	-1414820443	-254406453	-2128995819	-603267436	41886319	-364895793	-82324272	-35623352	null
2020-03-09	-293700777	-332331944	50422797	-143860950	-342990836	null	-434586731	-2296993872	-515223554	-376513088	-542814721	-334808522	-236585651	-239604904	26567962	null
2020-03-10	-317824907	-149120642	23701432	-113399198	-5085344	null	-84059988	-1905792753	-460045450	1083225646	-440291180	-163590774	226755646	-103931995	-13543506	null
2020-03-11	-440341464	-364154527	110886733	-237411808	-270557807	null	-511078752	-1126620779	-824562141	-343448583	-703048358	-507395519	-408205782	-255511674	-9543812	null
2020-03-12	-490844452	-267526702	104854750	-238773610	-230840385	null	-548014136	-1282291913	-923161943	-720003969	-546941057	-664016837	-485334453	-311536704	-30392374	null
2020-03-13	-788412970	-33202395	58246602	-192445416	30871372	null	-144471983	-1067420434	-758730802	-257854436	-369873523	-299232987	233173706	-359682972	36469500	null
2020-03-16	-198431676	-114851315	88444177	-208361635	60643077	null	-235862948	-976282748	-876469953	-258965559	-409527601	-292577362	-493324663	-390547043	68021448	null
2020-03-17	471236854	-77591682	56246140	-161184243	29089944	null	-287462058	-1056299558	-869869539	-2362560161	-424162262	-316456015	-504478245	-372789022	123843852	null
2020-03-18	1278152596	143613106	11870409	-92336594	95487666	null	-225457829	-1593637467	-668477447	-2156577738	-146951667	-177521556	-577060666	-400848690	55395480	null
2020-03-19	1355924466	416779218	-45289300	-42520166	266350965	null	125291758	-805978565	-434225830	380986298	-18036882	298816107	160514294	-160724999	153046992	null
2020-03-20	1105337715	295700814	-9562467	-80865067	65322104	null	-59113018	-154353909	-372300689	-603203253	-77869105	462014175	-237419784	59411882	86637082	null
2020-03-23	832740615	474980927	-70385014	-30004360	52994497	null	284470053	489119269	-331409396	-344131554	148102547	921711487	-237130691	121229129	94286634	null
2020-03-24	599964614	484778615	-69570072	-34885661	8373109	null	357839448	1156759728	-244215345	-435046018	380656363	610708985	-162686184	163293111	92611911	null
2020-03-25	-768684074	266100919	-80012150	-45875028	142051972	null	603052324	1258733023	-362883199	-1021178107	133025889	414581734	-102958548	389779986	101142350	null
2020-03-26	-446505954	31957858	-88172485	-4621182	126385940	null	649666063	925825213	-205904615	-1361683277	202349220	382471398	-82980560	393599723	111179418	null
2020-03-27	-478566393	-69112661	-86697739	24571398	83082850	null	598921114	290737616	-399309931	-845621152	65358078	83293917	-375841246	210885977	184566592	null
2020-03-30	-293227615	-26920903	-116994305	67531702	215694070	null	679010092	-16505462	-100299746	-947891968	122687840	72004286	271229373	410156622	189896173	null
2020-03-31	-866267141	-278229750	-70453625	8564623	-5632443	null	427815370	-87876991	-231864780	409024008	95869716	381021315	116559503	350198048	81956020	null
2020-04-01	-151508640	-288526047	-43583775	-17103140	-173942033	null	115880969	-187121652	-399837841	1167280013	46055485	381281906	172153641	130274773	91024893	null
2020-04-02	-158305649	-242106045	-17025231	-49219392	-259212331	null	136010312	-590030669	-630212884	-541754263	-157696087	262994608	-20745944	106200779	22353202	null
2020-04-03	-9250974	-262633841	-1216699	-65569900	-226954745	null	-3783178	-682648174	-609322776	-136208471	-164745810	113888857	37734561	159107407	-86546117	null
2020-04-06	15942889	-205116775	15886169	-22202867	-165165113	null	-34262678	-339945397	-481192948	-932354258	-199390357	49647362	120039250	95646400	-24031453	null
2020-04-07	-296899438	-255065529	-2386503	-36679920	46635819	null	-177744565	-238356718	-461062393	-478663047	-247806501	-378525600	-317242943	148131955	50270151	null
2020-04-08	67065217	17866808	-69784485	42574263	221386304	null	203371422	151705559	-45915921	496953983	59036589	-213966653	189347918	336639317	103655796	null
2020-04-09	-323697918	58785812	-45424561	7003853	328724389	null	-221940228	899274728	-114784785	591557362	-43837603	-511173430	-60208272	214208832	147941315	null
2020-04-13	-285819253	338388600	-133524784	98082336	273476311	null	162744444	1690421055	235289885	2222551228	28020265	-54323423	60285311	316429633	289593734	null
2020-04-14	-427378352	334688721	-132948102	84228472	158346432	null	212293289	1867670192	298014368	3291668399	-10486112	61484330	100605426	299417943	273012474	null
2020-04-15	5575810	361677697	-108878428	94574550	-3569705	null	230699729	989784759	472379259	3715220258	-214941687	600548290	144054722	122690186	363231196	null
2020-04-16	-170173818	170798791	-85649083	96689171	-188398602	null	334469477	1196754978	139707208	4459795733	-530223258	961153656	-163265385	57023132	332969328	null
2020-04-17	-295559039	-172767508	-58440693	13720181	-178746783	null	302502096	322287405	52005028	3987410475	-209987104	870729571	190709960	186184131	231842534	null
2020-04-20	-414661076	-298432057	-23031730	-24385320	-156826185	null	-82524069	67277286	-297132473	3832828634	-115227288	834649976	119438701	56104928	223243783	null
2020-04-21	-538755629	-696298619	58743516	-173311441	-210024151	null	-602744509	-963782325	-843227591	1361294165	-362454392	312498305	-491042801	-85194800	39952384	null
2020-04-22	-430093812	-372053554	-7705611	-48624576	-70976637	null	-228778546	-438248189	-662636870	369200685	-32577133	-269958647	-16985297	89633543	16930099	null
2020-04-23	-457435515	-174113943	-14237211	-52382411	56105649	null	-404909152	-1044557437	-334928757	-139854414	285784794	-273570602	294829261	131497117	43631571	null
2020-04-24	32934398	366511967	-93595243	120534218	-24569864	null	-39466262	-90564588	209387320	1222918688	108920255	-239507950	196162134	89242128	166530560	null
2020-04-27	296279391	43604437	-46084235	15274046	129488886	null	370655146	301188513	213262477	-558513014	-32798849	-514489060	402719664	203396196	148837906	null
2020-04-28	128790005	31394746	-45955294	9127361	253003680	null	507631688	362894959	295836197	-473854144	-8697618	-608507528	272016572	286418970	186989095	null
2020-04-29	56114518	61666974	-46651080	19342177	318675921	null	481370365	816643117	268312738	166555795	-12880448	-63426277	501416839	251445313	89314724	null
2020-04-30	-416494032	-345028743	21510561	-85909498	205855989	null	207688991	428008889	-25206946	-169835213	-297624736	-118574473	95199843	138395474	-42614472	null
2020-05-01	-731801467	-719603808	78196081	-200828629	111221260	null	-8732614	-463721621	-163675254	-2131786223	-449182770	58658412	-394361494	-3005339	-179322516	null
2020-05-04	-450045572	-162268203	6267838	-36580767	-31833198	null	-62939126	-556401311	108330372	-406943990	-171667552	382640889	-476960947	-80517679	-153609039	null
2020-05-05	280543571	262108169	-69502891	108422342	-105695456	null	255195678	-388690474	439865607	685349929	167859167	658444411	203311762	-26408020	-178660717	null
2020-05-06	-104227349	239875140	-66216361	83330857	-309165134	null	249978862	-505466600	366507018	610479876	138626593	656398754	-138587897	-57786383	-97206423	null
2020-05-07	774899520	734192204	-106151597	160734565	-139598847	null	641609260	-28990870	634674691	560573546	471304483	487321754	239896005	58050154	-129107143	null
2020-05-08	1183205142	852281862	-127156665	292892919	-21852035	null	963095902	1021873806	636823325	2739048267	570212376	687838141	823308446	188966982	55203487	null
2020-05-11	601892800	671767411	-111997601	255764995	-53185317	null	1016796123	654772873	848233719	2537149831	573062714	594091894	1152626645	210609794	65561077	null
2020-05-12	60616459	411295229	-74040579	177429314	-137187477	null	858704441	1438782608	845893398	2059278423	464188484	662184561	703665733	118102502	109512812	null
2020-05-13	430547328	133391941	-14799888	75526248	-172078611	null	596687538	737663071	534940646	1912123620	202176261	624001121	291778680	22706304	14053940	null
2020-05-14	167352489	-190176262	9905176	45333103	-202593065	null	544246828	503257443	189870505	1447073544	-70874003	675000693	-74636734	-63586148	175679700	null
2020-05-15	-582703250	-358444929	54130308	-98433934	-316618015	null	367531096	-547628431	-13732520	662381187	33911401	656595342	-267458080	-176995122	31233714	null
2020-05-18	140773026	-96043336	30218926	-59178664	-119084533	null	351525228	-478294209	-59275038	435895129	82086227	216411891	-323823035	-98457480	-110623146	null
2020-05-19	76595986	103648564	-3513851	13689785	-105040064	null	523515384	-1229525259	-109532403	2030885307	193046819	290534480	-107130727	-60886260	2190790	null
2020-05-20	404949061	539566098	-63174360	129780866	77708999	null	820921303	-556866601	302952518	2438847522	486514700	-114720819	400946109	46257402	73297261	null
2020-05-21	110388557	368906930	-54255531	59852551	-22721933	null	425042166	-362925665	407970444	1418644718	705635675	-539805266	426120861	36106667	-79502827	null
2020-05-22	922090779	765488278	-121578478	191732657	-17337811	null	601364947	486073160	733497788	1595376985	844567075	-815299197	584458464	89651557	39266465	null
2020-05-26	371716764	217516794	-42771089	14208362	6402779	null	135427704	-217464536	305350561	381628973	525817576	-853087118	758538643	83985724	-8583646	null
2020-05-27	259527233	-113401498	29654449	-124307015	236692014	null	-393637666	-243896967	85899820	-1838518195	144174317	-1144981040	519287882	106487443	-144234190	null
2020-05-28	81344550	-221066152	36039609	-138662090	36280937	null	-412111959	-450867566	31331784	-2513082960	-22686980	-1046923304	382987848	28383058	-143118830	null
2020-05-29	-163997608	75482636	-15220424	-13081628	35844868	null	92189112	342187231	250133863	-943703128	-204282597	-555449037	756430400	127290917	-5096058	null
2020-06-01	-352935351	79988489	-6863113	6911227	161059542	null	-327839918	539399740	240760793	-92028134	-173249403	-278047306	531241072	72730219	-127848414	null
2020-06-02	360119945	-35490013	-8869255	15457153	119844388	null	-264586327	1100186113	285733048	49157074	-207930752	-126682923	106682787	101834520	-96387162	null
2020-06-03	974958908	51569315	-62264519	129000783	70256843	null	-160526282	1873339143	447211746	1173967317	-199359614	-137620509	129977837	173068951	-129642655	null
2020-06-04	517773083	-365078608	-2427383	3670696	285652179	null	-269544381	1390375063	109761514	659939753	-352743785	-160552916	-238174713	119668438	-194185173	null
2020-06-05	927007390	-75269123	-24654614	76261803	517269729	null	-362462247	979050305	339903076	480350072	-111509611	-253331959	-200801248	231582621	-220019905	null
2020-06-08	1439610051	-57801492	-3149911	40620164	569783919	null	-391526396	1033638261	-22006760	578855800	-406800008	-564585553	-253340033	277444539	-245807151	null
2020-06-09	733879383	609403954	-66131101	218300172	394248759	null	63262971	1330737330	371492439	2430075818	-65938693	-170739083	9222432	133085477	-66428493	null
2020-06-10	278833058	964544616	-88063874	252907426	145438324	null	539209360	1572956135	633616362	3646976527	-45910334	104556401	407104871	108119094	69187123	null
2020-06-11	377101000	1013382932	-68000336	221948849	-80952542	null	184844601	1431475605	545197373	2926345245	-130471453	329078192	278919120	61281703	15106226	null
2020-06-12	315049529	558080314	-14257475	78390899	-161410730	null	194701703	766614695	176772585	1775694314	-244453933	73406217	104947593	-11461962	-38525733	null
2020-06-15	102608708	432715905	-59343876	77379842	-182000024	null	654652551	833621011	495898670	1890923122	-5158691	468263173	117624641	28820913	111086915	null
2020-06-16	70585824	297618879	-65373459	13470205	11110523	null	180328753	62700825	464091511	1495700509	41249577	423143367	163646065	172104156	-60152476	null
2020-06-17	-249512466	-9280541	-20623597	-67492617	86923476	null	99020891	-5987608	224262334	958592247	169070340	597329321	13483783	166971668	-51608127	null
2020-06-18	-13934241	103635993	-57628548	-26436456	208299439	null	351893734	995224878	502899848	2422664159	202263818	377210481	80245606	369746232	-42906011	null
2020-06-19	88364643	368595332	-57414130	-30332705	82653449	null	447435334	1253322197	681047516	3918480347	221930003	537992046	-154170212	168264370	42259007	null
2020-06-22	-58730093	461584136	-46518317	20293305	-94009156	null	487496053	140791004	842852809	3708618174	143947880	630774693	79727992	235636562	-3106582	null
2020-06-23	64201383	470461609	-40908409	56336012	-96243103	null	782162044	1170088452	756846267	3973202464	121667661	557868003	75683736	143921617	12439279	null
2020-06-24	197164285	300708305	-3859701	-38540667	-173678725	null	373468319	-192162371	411284105	2621227051	-33319656	107182880	-198117888	8382216	-112474105	null
2020-06-25	430311325	545573070	-13342471	80197539	31352120	null	592413537	-300507013	566540382	2290805413	318235356	375972540	49304310	-98370907	-110531888	null
2020-06-26	48464656	132601841	16484369	6515863	-52176515	null	35876276	-610133162	67906241	634309687	86130072	132756828	-377369370	-6730774	-246439328	null
2020-06-29	129273661	59175586	25680613	-34686333	73378970	null	-376393779	310479578	-99065720	-1093957542	81156407	-159428893	-336070455	-65680790	-346873676	null
2020-06-30	475350343	155167186	12517216	7189468	40938894	null	-200252435	463007915	13465169	-1313906022	38487945	-134827427	-458352628	-5046445	-247221773	null
2020-07-01	1121164524	644362480	-82777420	212445551	140206535	null	177590364	1960172062	476531057	1024539403	512008133	417375133	23159070	5557385	-225798336	null
2020-07-02	950940978	500623469	-100181406	178045078	-5697246	null	105439987	1955584364	327545468	1600490535	245408202	111311608	285381241	67467743	-177354253	null
2020-07-06	1068406767	1124754448	-178328306	401383029	28064789	null	591120706	3643827787	931472984	4340263531	611935798	686354597	1230184984	147231461	-73578857	null
2020-07-07	717961942	1161258587	-167035532	407118927	-92828922	null	943506290	1961652416	895008418	4235539510	761790288	820246349	1179735647	64293538	45066886	null
2020-07-08	158513237	1088553321	-164455970	379731993	-78638577	null	945477724	1355184023	844592265	4779181044	698232993	917317934	1317051382	59892347	-49602643	null
2020-07-09	-392683810	925656524	-137277968	312435343	-135997824	null	1048914000	1277214851	684485212	4586743646	322808349	606866721	1269317421	151759457	105460969	null
2020-07-10	-92700951	1094001891	-120732277	388861224	-15784540	null	785773672	1573414951	806179726	4033374655	292264357	1065050964	1077148189	74284084	59222100	null
2020-07-13	241899117	879821239	-89304316	279706941	198487578	null	656115765	475195660	579918587	3120618787	129409752	796300313	910939973	12931302	57016125	null
2020-07-14	394308164	671840900	-46505529	141358387	272989355	null	324628043	699083733	381273270	2652792170	-302979779	303404232	508622219	69716148	49395795	null
2020-07-15	605746189	178991120	5967828	-22892	333502144	null	-152943855	-485518226	8705182	-312296368	-324510123	-247713318	82727056	-29380647	73247577	null
2020-07-16	691059407	178279415	34329074	-58498978	413622172	null	-674693993	-1265386308	-342012551	-2799300684	-243863027	-349681165	-353523871	-117465789	-79052308	null
2020-07-17	412223682	-110795694	40325086	-100057114	173736379	null	-366110997	-1173457145	-615983639	-4076770969	-117494001	-475498356	-475816167	-32444106	37602747	null
2020-07-20	756828177	142099215	2820304	25438207	-29769211	null	-215463313	-369563833	-372391584	-3048819152	-16241206	-266772945	-481910501	-36647238	101121046	null
2020-07-21	467142605	-86823462	11082879	-27180540	28765865	null	-340182766	-655492407	-643777353	-3078296515	22317980	-173022292	-242858565	-83499801	11098512	null
2020-07-22	845165174	300224458	-7160305	74069192	-203996558	null	120150598	618755023	-446298776	-2732860642	-235921226	145068401	4065218	-75589044	107472018	null
2020-07-23	585184551	30043404	13298391	-36954753	-195566731	null	264696268	-904727615	-507113363	-3258536167	-336392236	-115738457	-13772955	-50973348	112841692	null
2020-07-24	622375186	216510337	-24708455	-71402454	-55260066	null	344766123	-2796659658	-316153951	-1316819670	-217306014	-79729213	-170673157	-133113623	173769987	null
2020-07-27	562826899	83111476	-16679234	-114819525	-79157408	null	353366078	-2636713408	-321658975	-2342514050	-194724422	-99714412	-210521100	-68650541	99911434	null
2020-07-28	177084682	102883572	-27442893	-123993035	-201236742	null	386402911	-1510597710	-131405169	-1302020416	-191934619	-52252868	-426411670	-74230408	146340367	null
2020-07-29	80122881	215030254	-50075683	-69247381	-34049083	null	388810008	-808867143	79814667	686705003	192529817	-120966982	-282044123	5823393	73477785	null
2020-07-30	610464036	716492517	-97616122	145424640	-103469577	null	592801979	414908112	614991011	2755727290	341128332	229850719	-30267615	43033252	186835248	null
2020-07-31	348223792	337548785	-28917497	12752805	-251244618	null	178327572	392980324	603738928	3522841123	361236548	9361062	-392942319	156359791	14708377	null
2020-08-03	349805792	252297370	-20263107	32644941	-90035912	null	214141256	320382758	348592903	1159328895	200049614	-466613	-807266771	150386997	11443022	null
2020-08-04	1233350237	687334524	-47800791	262176303	-103183919	null	660986468	73546348	681373325	2580272637	102031748	478122460	-789481061	269677097	132981067	null
2020-08-05	869724090	160397149	5851632	65281822	-102352939	null	591754211	-1058794422	123408778	2889680402	31827982	320088448	-760652140	222928638	76477737	null
2020-08-06	827621614	68561110	-4563235	91384516	-47770825	null	530611825	-94358842	245306244	2371747907	257615091	427031634	-629483650	175514294	91926159	null
2020-08-07	781576785	94136318	-4466139	90822636	130096151	null	596103748	-39153598	57133107	-328492750	366938741	136203454	-182175124	53810145	71225861	null
2020-08-10	430596674	-280695872	50277599	-115329820	131556588	null	290703228	-1862775458	192415728	177723865	165553340	-303889718	-28579286	6343505	-12133451	null
2020-08-11	-82706387	-676117103	88857066	-354377767	330388988	null	-233083997	-2301890840	-398198999	-1682210585	459332749	-840607741	121325445	-27362699	-228306837	null
2020-08-12	504397823	-43921482	30157484	-98816896	137131934	null	-41744885	-1111835277	159331712	-1787592134	604559149	-443112909	82692986	33914884	-101879245	null
2020-08-13	518259768	2512344	32721085	-92990932	97245448	null	129618411	-674831245	-5126006	-933254735	549316237	-437625906	55000983	7495740	-211766019	null
2020-08-14	966860817	-80266203	15394951	-34266120	27778849	null	455749440	1322354102	-210850136	-572895065	203215442	-35146497	35155526	23104222	-180462066	null
2020-08-17	1440543428	382356640	-35895435	199485701	-169791874	null	868008749	3757688275	-621332043	1020858402	321107093	169548544	292256097	44003876	-5389614	null
2020-08-18	1751727487	865724549	-113478561	480348309	-357146606	null	853699258	5657255005	-6815163	3494602568	248271010	656287692	529497642	-13692436	-19961082	null
2020-08-19	1202207872	516810194	-75258609	251267655	-148663475	null	140096101	3395916153	-111520202	1274894817	156583372	298709634	316792632	-43721990	-169096490	null
2020-08-20	1360094413	542538775	-115230908	274204501	-146636207	null	272958550	3940678868	152593662	1289003147	208347187	390869044	333922831	1090474	-39066866	null
2020-08-21	1604040494	867322865	-173828582	416565468	-210892971	null	426753899	4377901828	774578148	977583974	172868779	133569808	601382851	14977064	93683216	null
2020-08-24	1317013854	297965883	-108626008	161315751	-14148274	null	-284943458	1397824695	909639594	1233462390	426323489	35154833	655713954	26051895	-90431097	null
2020-08-25	673273025	-135196919	-99055698	-33430236	-48536090	null	-208071799	-1020548019	385571323	335661154	543088367	-97872497	669340840	79441630	117053446	null
2020-08-26	1085352886	191851744	-158644214	188656855	-200677721	null	-13846362	1863990122	460059024	3465621761	394517236	511841140	1085601077	88504685	117500685	null
2020-08-27	1058361688	-108824788	-92609462	10113729	30993754	null	-524694221	1882630092	-187011516	1384269455	-110360316	-82147466	679388271	97477526	-101582824	null
2020-08-28	965521599	96035923	-104602291	27175153	96530070	null	-542125058	433918891	-418745391	2975949926	-2587275	33276562	726642615	163109190	-89965085	null
2020-08-31	108073757	568971637	-183315614	252195693	-51346703	null	-160055030	1831169267	-381900045	3106682753	-450088514	98873530	378432049	195970201	126644220	null
2020-09-01	522778020	941070490	-188415234	421124371	25328004	null	439133682	2411008371	-17273034	3554244481	-341107466	397789081	350682997	263248283	-9235144	null
2020-09-02	271095022	361405948	-95883853	113462620	183786690	null	875130956	264006362	-452794530	1529010097	-221087050	-336165576	389178848	357142013	-50438012	null
2020-09-03	-505827666	410524215	-70892227	-25317430	-54006709	null	633734217	-1431902908	-365691429	767879530	-290906176	-326108176	159525407	234839141	4066942	null
2020-09-04	-1304869986	15610017	-25892082	-226643334	-68458164	null	-109685343	-1386532556	-764516021	-1827672692	-487404584	-677607383	-397293366	387194745	-93734687	null
2020-09-08	-988855850	-647082544	30814756	-411317810	-104418765	null	-485614208	-1522691873	-676443927	-4580558243	-414686403	-809524103	-638738408	220904614	-291228066	null
2020-09-09	-900588484	-681541867	21951957	-427753612	23163017	null	-579116150	-516159615	-707366796	-4207655613	-550485748	-1235240697	-536653219	186642760	-183428583	null
2020-09-10	-1464653961	-351051360	-23011210	-348108075	-101487824	null	-930487934	11310311	-787589680	-3707939765	-682649713	-1109035101	-975754040	80206436	-118766543	null
2020-09-11	-1118177085	-867798386	-29360200	-302747514	120522427	null	-802053909	-68800165	-775540030	-2666364548	-549488058	-630497618	-621390609	252597570	-152120695	null
2020-09-14	-506883270	-552923075	-58083055	-159616465	227960770	null	-220190585	205136112	-515151116	-1330843079	-330497409	-369352119	-24752465	120264016	-165397558	null
2020-09-15	103875486	351795720	-105784981	10052564	243895285	null	-84659539	565969814	-664672847	1157616553	8099716	19463018	523570257	272980451	-33345016	null
2020-09-16	124024952	-174097245	-31175349	-218520202	254071819	null	-724438167	347412599	-711381297	-1303151649	-112094967	-54097329	181257218	277043202	-184882056	null
2020-09-17	683333621	-506226555	-29930068	-234071716	295444179	null	-437920619	373533962	-405500038	-3143614307	-312752214	-142487460	-50909403	306675020	-140154622	null
2020-09-18	557442362	-35889812	-4681374	-212442781	164218970	null	-383878692	811099462	-815195508	-3366865741	-355716499	-355108927	-172642600	223949967	-112775298	null
2020-09-21	-101290232	-164519267	38945977	-296829578	-43758793	null	-404854433	584792508	-771387755	-4234006600	-498490851	-18899654	-744287426	80257893	-17760750	null
2020-09-22	-279464948	-403428338	26945940	-309011329	-68332138	null	-356001924	300669329	-650225422	-3307782757	-466389023	-263506968	-712893486	88090690	-161202675	null
2020-09-23	-733308570	-266328638	29806800	-313462583	-228443786	null	-321123056	-23685156	-779614758	-3719206951	-538907723	-292739317	-902492446	-38103154	-159762449	null
2020-09-24	-864556502	219865971	-2521385	-167871666	-205902756	null	-281320411	187057725	-774731975	-1209528014	-234501079	89718941	-446084958	-54255395	-98247057	null
2020-09-25	-231072590	650137032	-101903269	47464170	-203869541	null	299182709	254242537	-139059110	926653946	117771044	267384631	-127032538	25189736	18486339	null
2020-09-28	643797552	1068628136	-169599925	167505477	-25286787	null	194697371	344425574	-115116816	3516042133	171244894	129110278	490372912	181924433	-20742947	null
2020-09-29	151258494	624506524	-93399296	21174057	-2924662	null	701790149	620129555	-160979622	897554845	193194231	186087973	429676346	84878607	130324830	null
2020-09-30	781074889	1159546407	-180103491	251232055	134170639	null	1441544915	1151054924	83534143	3794161851	518548296	550594108	855579664	169385304	305987855	null
2020-10-01	940284369	1339420693	-186703910	295378834	119335564	null	804025706	1170385518	-9004458	4032020762	533939807	746086163	899000452	191388190	335950256	null
2020-10-02	505407671	476994585	-98799216	86335775	149350676	null	437262603	509733488	-231055691	2319302113	291245635	459071685	583877505	76440073	213954658	null
2020-10-05	397790349	347546873	-105489406	131801685	148659298	null	756192158	244536547	-114865908	2200564771	593828125	578128634	500373990	58021222	287345843	null
2020-10-06	491021759	622261765	-141072647	92446623	303697704	null	721642760	-186449386	-207468632	1524197148	205497822	328295404	178057563	99619921	138589510	null
2020-10-07	503151540	514136507	-147654715	117250883	296951695	null	637058649	-181101231	-280732606	1333886553	-214560904	459761841	162414	118082563	117034870	null
2020-10-08	551101839	-71201815	-86402225	-68941466	365730895	null	672741797	-458443696	-332141868	-278922663	-94402464	-147702213	-20322567	115672365	-691735	null
2020-10-09	1048469312	822850008	-175105909	202738316	384701671	null	361119251	178110180	-85335340	1941314291	-11418164	289905021	481790134	256583664	-47990419	null
2020-10-12	1209944891	890168673	-172421343	177063510	357013914	null	342694705	562301073	-17222151	3022975725	79702157	352166481	768765644	277070305	-47465334	null
2020-10-13	1377621592	1185309476	-207383212	357455729	192863000	null	-40885575	1093116361	99082796	5720035600	290345925	822388987	1229094450	250589328	86647341	null
2020-10-14	735812065	665306015	-103305512	77399404	71755028	null	-634454471	1127663851	32278181	2954769267	345863867	428578488	1261675397	191541485	-88199242	null
2020-10-15	488054839	470155612	-88120182	77130813	19761177	null	-343071475	691388001	232735226	1839447463	-128510598	738789168	868086823	75974901	1462630	null
2020-10-16	156501108	320110146	-63643701	-24162360	13091429	null	-105240483	154758249	199549424	491083207	96228039	459329269	853946652	28411671	103613409	null
2020-10-19	-613930379	-241227082	42807441	-316483372	-108517168	null	-827512385	-539468444	-190476667	-2798987441	-389645592	281401231	257498561	-39767494	-85199305	null
2020-10-20	-500083705	-638508876	89196119	-296892761	79917012	null	-510503792	-1243614266	-114905639	-2963678168	-189275190	-183280595	285402488	27178008	-163893279	null
2020-10-21	-47827355	-190804808	15203862	-85905958	85416721	null	-407824368	-1419244096	-100978309	-2322847034	252924850	-399034731	723030193	-18480003	-182963921	null
2020-10-22	242782916	197980961	-6019759	-58717724	127624823	null	-612648160	-1360288839	-270987321	-1973381223	419654209	-691262132	1084888959	39775070	-191153182	null
2020-10-23	226546906	-316706305	68059228	-227274106	134265776	null	-247102929	-1490134085	-429787820	-2735260139	417716596	-694958562	1101174309	-13045799	-100109362	null
2020-10-26	477915799	-345608651	58529463	-151952762	138377834	null	-110843273	-871059327	-266430382	-843316636	457207373	-892746957	1054331610	-89945039	-613299	null
2020-10-27	304519952	108504	10446141	-144359129	-21848420	null	-82662025	-40768705	-210180851	-678306922	418983801	-827688026	848704315	-178466486	-48288673	null
2020-10-28	-179016830	-349702201	96514414	-336804073	-114692784	null	-326621830	-640940581	-149340307	-1256438960	-97376257	-519799958	31147489	-198544454	-3482890	null
2020-10-29	-711473930	-203566603	27515408	-186829365	-157892783	null	257573269	126309165	-39665030	1345464646	178094220	-327088580	170015706	-157181393	29945751	null
2020-10-30	-462992574	-47038453	2066172	-147101567	-94826153	null	-395433345	60253904	-27264322	30397051	-181774001	-583665520	-595275867	-178136047	-111974720	null
2020-11-02	-634393525	63789364	-23301091	-92483756	104164100	null	-102464052	228226418	11726082	-2309501271	-114173839	-245260903	-30560525	-82512088	-194861225	null
2020-11-03	-216236727	79203159	-32533438	-102620175	298465306	null	-94774788	210500975	8518567	-2566637209	-73152619	56498330	91725684	12340378	-42449785	null
2020-11-04	-121239980	538209006	-123285669	127520064	487385815	null	723511975	396790322	18857964	557935783	436615378	274668173	1038868110	164606721	113783692	null
2020-11-05	453015774	686757703	-95129501	157767560	559382860	null	700256269	435344029	102714189	351508492	362447149	613190274	456951448	203542896	-55333136	null
2020-11-06	266584903	1018127420	-154287302	346091308	373759639	null	1370616432	1003133331	-2018782	2340951121	274351235	810952933	741961880	282835662	104130013	null
2020-11-09	14277888	1009405627	-125827608	218213053	346053484	null	787115906	360025538	-323720116	2314927587	72687978	296305225	707519063	314286637	117471735	null
2020-11-10	-412864735	582409589	-55967094	51756503	202440717	null	15364882	-338780340	-488694584	-242460458	-361763390	302435489	121847622	156640764	-73472919	null
2020-11-11	108771500	642181848	-70194866	56841969	64608113	null	-86172987	3543993	-664386088	-949558689	-361970555	291497645	-159553522	143626172	-55952756	null
2020-11-12	-215307218	328448982	-41758089	-53425073	-119536877	null	-92627032	-689503208	-768862395	-2816597433	-380665831	-194879105	88239556	32061275	106991338	null
2020-11-13	34367251	-73459620	22982475	-237060370	30420695	null	-634974423	-1167787657	-748437719	-2876308822	-42827828	-248830384	520596941	51939360	-52439889	null
2020-11-16	1062139834	-85008997	8979326	-118945909	51557141	null	203735699	-1253852303	-238176095	-2001106668	94117289	-113328306	283236731	41194010	123102575	null
2020-11-17	726672536	-28390338	27096512	-177015194	-31039332	null	436172421	-1379420668	-186598876	417799407	84672405	-130148914	487677377	118331394	184485270	null
2020-11-18	871421337	-464718887	91577584	-319707087	97334611	null	274628399	-1066076281	-142722352	-1221987403	-203598963	-235610092	7038699	103290616	80764596	null
2020-11-19	1597169620	-173146396	47562581	-171144488	129552617	null	360904015	-533901567	-101840806	-462304565	-244525702	66418980	103422568	102473169	99652592	null
2020-11-20	1592987642	-41613226	33996255	-126914369	-29725481	null	260175368	-569274722	28525432	-453114111	-597023205	343167159	-221225971	119014372	108353468	null
2020-11-23	776317126	95681029	45426796	-165983055	-58712163	null	126702277	183522669	-377946056	410237547	-691122913	266604496	-463433210	115580908	45199676	null
2020-11-24	1754509607	444187457	-36561660	109934110	153640234	null	68172067	877207566	-248961441	207508272	-205592040	286996073	-146226877	188380571	-13316495	null
2020-11-25	983570564	695343483	-69847136	229048313	2630043	null	223680723	579145034	-34091996	1937304899	-359740604	217818927	4120883	100807682	115865868	null
2020-11-27	371424016	565779017	-44459904	144521291	-777004	null	-60437678	391737559	-178906535	949670625	-319840595	214295296	61547779	166440617	42611955	null
2020-11-30	-177207655	328160760	-39327516	121331549	21430608	null	237639943	238751418	51144529	108885650	-274548178	-45609613	-79360131	129539206	217364670	null
2020-12-01	583102807	534412360	-117408888	382429494	27374793	null	-228963062	-659708689	312422319	1130800732	214294155	428145982	428798718	141680753	192903687	null
2020-12-02	383556539	279318257	-87567163	242253910	28064490	null	301835346	-1193861527	259734501	-238214851	125094649	158131540	490904337	58348225	385216810	null
2020-12-03	1201053664	371177799	-103894757	319933814	145102977	null	-199578934	-939361149	-10811077	-1363490207	87162073	15481511	547078761	101262551	193899589	null
2020-12-04	1657000427	482636459	-118705645	406821644	302707206	null	-41475617	-1342378438	-87288383	-1382092880	-186806782	-32430850	437193453	159880523	312591585	null
2020-12-07	2246257295	887114433	-176968785	598611069	420661300	null	165961110	-453751913	-178755248	-919410813	257760445	330701131	555088860	222341290	113282692	null
2020-12-08	1923161865	686692963	-134741767	471490929	260500490	null	147840667	-51946508	-191608499	-2383942819	-194154057	-60315810	44292288	211844653	-22729108	null
2020-12-09	1092761232	290386079	-77121160	273977862	73261951	null	-408379000	-454190263	-386527011	-2778322826	-508541860	-154519721	-305546831	184386082	-170562118	null
2020-12-10	266290928	344024714	-97574466	266328293	-17841176	null	-80213646	-569153766	-224337592	-2339297631	-131897001	84004187	-590936856	75244493	3277500	null
2020-12-11	-166177944	29297754	-51232967	68732157	-209730234	null	-417178398	-682192226	-124908149	-1623631867	-49920735	-71239951	-674585901	-133900540	-134629800	null
2020-12-14	-940450802	165539014	-51801407	62562285	-307934643	null	-268903768	-738138236	-173038867	-167018809	-42953722	-37041067	-721231726	-130642055	57659545	null
2020-12-15	-936576864	346685144	-98455786	142077672	-182538733	null	-45114802	-1107412115	-65717875	292914121	-36512347	-66009867	-508634423	-86572233	248966699	null
2020-12-16	-769885575	836940594	-160629380	364786680	-83408540	null	20592959	-1075611170	-4279026	2663396046	216688939	260813006	-561976987	71540464	191172915	null
2020-12-17	-339248898	598471892	-114563031	225310777	30980330	null	92091079	-857814880	8791600	2046525801	152758113	303531551	-512070655	258951931	-28736532	null
2020-12-18	-676273828	-88745815	-83995937	125499855	70566546	null	-13497038	-487287309	320711860	1332095065	188086005	361642468	-766218167	427268413	-1237236	null
2020-12-21	-187554656	-703463359	21191298	-162016911	-9827050	null	-319260425	-802135938	318854904	-756018957	-272597852	-104082965	-652954637	263968642	-222237230	null
2020-12-22	-728634138	-1030909914	44274834	-216799682	-182358783	null	-501525149	-813188293	76468596	-1211921888	-389412319	-17129324	-895691661	217735169	-430768919	null
2020-12-23	-117737363	-1402173824	85353549	-360316523	-108069727	null	-445723245	257995711	181739592	-2957263826	-237347056	-281151872	-552293018	72062998	-417045938	null
2020-12-24	233252084	-1272121582	66794734	-268853239	-181989005	null	-658400446	176134782	127779625	-3138575353	-391051495	-442026925	-338774784	16048091	-248322091	null
2020-12-28	866651017	-263743485	-14365102	3204187	-87398169	null	-629220246	590565362	26311473	-757784788	-81405560	-368830129	208401534	10424491	-277246444	null
2020-12-29	457134228	-282794020	-32484058	12491407	-46421283	null	-467698383	227910645	-126093542	1619362832	412949867	44039282	139094243	54349525	-262469123	null
2020-12-30	1116681815	-470325330	31248844	-188561277	90092221	null	-16974326	1201072773	-169149962	1412134840	509520342	27536463	140953014	63179658	-38604751	null
2020-12-31	936034730	-267916795	27931184	-127328534	24072294	null	-46449454	962215234	-318981264	1086053010	297457433	403406657	149952704	145152369	-27076194	null
2021-01-04	416549608	-682573433	115376230	-443264495	-34463259	null	308472609	977875216	-489707427	436199227	145156600	149184009	-81242451	71140025	-89909398	null
2021-01-05	267634862	-623875371	105066629	-397323703	-32622491	null	811753939	933623085	-571636862	-528640632	39589485	38724045	-182580289	36914767	-159985603	null
2021-01-06	1125843087	98192780	3025550	-129220490	147311763	null	401245877	1560474525	-441783655	-1588346791	-146734170	-408644791	-419778622	76523705	-58238747	null
2021-01-07	1473260014	753907247	-88916190	191418964	212876340	null	606127728	1917193031	-184832854	-41898199	307000182	-109511620	90466648	113559072	-27735042	null
2021-01-08	1620100032	1130768348	-167522842	409030665	58506289	null	570458994	1837152976	-43654072	893447390	9982388	-265994822	86298357	122219647	-10640049	null
2021-01-11	1935545773	1118131675	-176686694	441068597	211628324	null	659327598	618659725	-29935360	949708441	-22213466	-222691546	45545820	187294961	128176696	null
2021-01-12	1329383923	648518364	-98663915	184658176	242790796	null	57704800	724095070	-199631726	436198705	-462350132	-421927666	-347440122	244522095	118469870	null
2021-01-13	900688146	504373968	-79456373	194033772	74639301	null	433133997	-135013221	-84456717	1125058188	-593536465	56851054	178938430	282278378	-23503593	null
2021-01-14	-72406747	189173761	-25274677	5094016	1569694	null	-333981858	-325451883	-423023513	-507627881	-1128422915	-296775013	-217837761	268711071	-257179250	null
2021-01-15	-1320403029	-342421569	72920671	-295681332	25334265	null	-289541009	-1012399135	-366574979	-1386513148	-592690862	-505146055	-325707980	122918312	-340878302	null
2021-01-19	-1013638175	40413540	-11121074	-44311264	35509715	null	-768557275	303641092	-185695834	365539712	-159912011	-189696104	267761491	183244847	-524122883	null
2021-01-20	-81920111	488882537	-94966660	214125939	-108361005	null	-193802638	409903050	107901573	1752097847	361685940	555835564	1090644447	171075010	-543437405	null
2021-01-21	67243095	615594847	-74234720	149869890	-124511931	null	26480928	276512418	11774599	2069269155	722644917	-126171510	1485409458	188723034	-281567622	null
2021-01-22	563289090	187057090	-95515473	234696535	-231033744	null	365151239	-881273996	236796883	2058025575	1303317384	-346476402	1902855279	67258547	-155971968	null
2021-01-25	1368644046	241360884	-117376352	296765729	-221280529	null	417533813	189457668	246022454	3211054955	758874187	-566098830	1666921854	124090129	-5625676	null
2021-01-26	1180994286	289354443	-95843024	331331284	-393464970	null	230007620	406388059	202486370	3393331509	855481768	-417195335	1578080084	42941291	184684651	null
2021-01-27	723908296	-241734081	12337886	39716031	-447833194	null	-444326776	-995130940	-57769827	439094905	244667880	-1312293526	228607193	-124046312	145042439	null
2021-01-28	933542807	-277264624	-17592970	73847902	-250236662	null	-487393728	327667545	-84173656	101534558	47369227	-599215773	216843740	-118453568	-33696646	null
2021-01-29	486300940	33502493	29538558	-60375346	-243237419	null	-262680777	46171766	-354532240	-498033432	-526185551	-429594212	-535218149	-55715258	-133152061	null
2021-02-01	971832585	527677620	-48512055	126146441	-101353521	null	126029173	177073746	-469288194	374939589	-290680263	92480105	42277021	68954752	-125593850	null
2021-02-02	1202660876	623924874	-78034851	143143285	86393692	null	642176064	513224675	-484069794	1063848969	-281543982	38429151	277408454	154070603	-243345927	null
2021-02-03	1680116415	471104715	-80629445	172588993	265164222	null	1261320933	672647020	-605622339	1799064716	127966411	287956471	1899132534	179159573	-191772184	null
2021-02-04	1917744514	457241392	-47687768	128626520	275310172	null	1024130540	-666539161	-535661731	-391117994	-302064514	257985378	923122856	114176865	-117715428	null
2021-02-05	2677447084	589218692	-73084422	199295888	433433526	null	587923875	395760494	-429081784	1113425357	187525646	368703685	1663424257	77475184	20695317	null
2021-02-08	2925734562	277954757	-22481007	120036841	483647935	null	835564701	419230335	-393240827	-1102608006	36092593	90446069	1110438917	77015641	163751982	null
2021-02-09	2307437506	187110029	10834342	90435300	368864296	null	312374099	-1385963240	-307411485	-3019821899	15878946	72334457	581663371	23713631	94928178	null
2021-02-10	1259750051	296822963	15771344	80474824	363792963	null	530081622	-1424459472	-143422782	-3240787812	13212015	233837238	-192054802	50040077	266129714	null
2021-02-11	337524553	137640424	10958618	59612019	170635479	null	948126758	-1264778837	-401185470	-2779713980	69856257	-168978963	65552177	135598423	184457336	null
2021-02-12	498058398	216043004	-19764680	169075650	200045967	null	764583562	-2069443706	-305972361	-3461911572	-317504445	-160933990	-294048907	209590561	258982888	null
2021-02-16	-392762908	-86620314	16007856	38496656	236939206	null	689016961	-3530241584	-465005826	-2684903918	116130647	-64844610	183397634	203887624	343106	null
2021-02-17	-614977185	-597288361	86165268	-140477902	357828805	null	504328144	-3131498306	-684597023	-1322798799	-383644258	-386206031	223781647	101307594	-36839208	null
2021-02-18	-549633012	-543330144	89582428	-124215075	183914383	null	-267363286	-2773630998	-701546090	-64873146	-689592578	-514438602	-62776664	166666348	-268614384	null
2021-02-19	-634631165	-737992426	138346136	-201621920	353377875	null	-374381388	-2125610266	-500392488	-657558270	-745343874	-492039397	-51736614	149216982	-94757201	null
2021-02-22	-1428018967	-1104155105	234552993	-438683699	350170449	null	97416866	-2295623234	-582953586	-1227301178	-381572170	-552547474	-344560307	24053718	-336308942	null
2021-02-23	-1049801600	-877199410	239622745	-425291112	298114322	null	-709534098	-1709047703	-509556396	-2102801171	-485528792	-480008621	-897525725	-159472608	-281808894	null
2021-02-24	-387338253	-388156341	150578385	-296937081	252890316	null	-325187262	-971336181	-340075153	-4050259633	-433856604	-245591223	-856388311	-71109355	-136568514	null
2021-02-25	-265205456	-345287553	145348225	-313267474	311835965	null	-597129686	-1259471553	-339911394	-5513343542	-318765223	-226796030	-1067559518	-180524149	-71958560	null
2021-02-26	-235718458	-270400895	69058649	-237336355	76610411	null	-589900114	-1243479452	-370004584	-3134378382	273996389	-404389	-549961231	-158700366	-137160071	null
2021-03-01	-207961116	436887920	-35347570	-51169427	120973441	null	-1044967240	178611493	-42292132	-2604474296	382743710	342947924	18155000	27462798	-64165356	null
2021-03-02	-140904191	379447151	-36011907	-23116935	139966807	null	-946176100	-298935082	-64501568	-1406180986	322781039	309478031	344911226	39249582	-107375388	null
2021-03-03	-775338364	-54140407	56355762	-164433770	198505506	null	-1335672308	-1291752121	-256465898	-1485919603	264484775	-75390397	-26196826	-70838251	-251393183	null
2021-03-04	-723555801	82546475	28027943	-113603842	123289521	null	-1188696911	-1054189395	-198682915	-633996663	661936459	-33079352	895774529	-115764388	-236197782	null
2021-03-05	-549790719	117950735	48681756	-156907991	375034107	null	-1551340918	-1461074486	-204819867	-2130566751	579172213	-216153415	1113378370	-247873718	-274933805	null
2021-03-08	-629849239	-419428673	80833997	-257324739	370940869	null	-1566533024	-2099953155	-545750052	-1505071431	284619230	-551938919	800322742	-527513330	-305416944	null
2021-03-09	-444233296	-146311662	20191886	-121702252	278944847	null	-822139606	-850360945	-315025628	-539901954	437323288	-447386512	1046197934	-279325707	-122494898	null
2021-03-10	-121222838	55540925	-36719219	-50245848	312037510	null	-122921637	-634389241	-230757297	275654504	563692935	-61895045	1339425647	-194855589	-83093024	null
2021-03-11	594092384	405006375	-110602548	86749441	415626368	null	642596907	304948352	-242511438	776249879	604455954	227152177	1101366472	61588852	80371297	null
2021-03-12	1010360904	358250495	-101950760	123877342	411297521	null	358543863	796839449	-197436691	547580079	107109896	142320636	196065259	8280098	130493576	null
2021-03-15	1398465361	692379879	-104741890	219868083	171012833	null	1008478239	1251698027	80576134	-377635109	351639400	122245156	58800267	308332045	274667696	null
2021-03-16	1347206134	730580305	-119747289	212036192	49495581	null	849968823	59782197	50263569	-674189549	361916304	158663087	78923049	299272974	262670914	null
2021-03-17	637100951	672593941	-105243713	221082070	8959444	null	476299153	438048400	57015309	89701990	518635341	-56947062	-55325111	307308803	270656216	null
2021-03-18	-649722960	168798258	-9117879	-6384759	211973883	null	-220235527	-795421940	-93864245	-1192350537	61852687	-461236613	-588872380	56066397	86141786	null
2021-03-19	-2086816284	92761973	13196071	-93997736	-42649907	null	309499885	-1228269198	326908818	429441165	793641563	-117261011	-28071395	153954066	105595355	null
2021-03-22	-1725202946	37841525	-35699064	-52663208	-79180527	null	401944396	-1174396303	445027560	2019159405	808350860	223290100	283015554	146474360	121757876	null
2021-03-23	-2149641570	-161232862	-42042554	-95596844	-115839046	null	220890525	-295652435	384939572	2357598342	689859152	315069840	184667023	-114017363	-50959634	null
2021-03-24	-1685580588	-190433938	-13344711	-168538347	-70382032	null	57328077	-994596103	323396639	1551494137	434077179	225598692	474399651	-127934170	-66577870	null
2021-03-25	-919446811	-165190677	-25948630	-100587767	-195393370	null	136509340	-214517639	453213579	1908138649	488336745	201152725	632692331	1378172	-12870838	null
2021-03-26	588556016	50570836	-21013808	-40121067	80306951	null	41537878	-640043031	-40967773	370035941	309625742	69897657	179488251	104131940	-43676860	null
2021-03-29	-189669156	-294875337	85874135	-161544108	32915579	null	-226947267	-1423619459	-250862690	85325764	298296351	19219485	130219979	-183378120	-166034229	null
2021-03-30	-156610899	-630597845	177015177	-226429720	315621799	null	-508020773	-1225655137	-342221749	-1735839589	-18987526	-367970178	-32648228	-202101409	-157641348	null
2021-03-31	722699679	-324574357	66921710	1215008	50251013	null	126990597	44357395	-9823586	-672458667	476362706	8145483	154040726	-74405753	-24846609	null
2021-04-01	2168164035	185330997	-11989229	200278911	80765079	null	762014743	-300382407	-100758845	939803274	861485648	444140270	687294863	35723627	94407572	null
2021-04-05	1815761959	430357254	-63641775	324845412	84742291	null	814272882	678964498	95300935	2494772368	938647175	243230081	1383872353	30180412	27338366	null
2021-04-06	2239935686	787222376	-155178952	409262063	186127153	null	607914166	725287065	116559857	2434698697	430052707	307952354	970103232	85825658	102924356	null
2021-04-07	1987518304	1473940623	-240187318	536241879	121073408	null	1069191411	-436356253	267209072	4255511151	923755911	487678250	1127964960	152814324	288000848	null
2021-04-08	1535089052	1586655893	-224602260	505209102	123674033	null	975410567	-525166250	253188048	4360138435	320314563	526323088	1145099309	61183940	263878742	null
2021-04-09	815008859	1409012391	-192179675	452847808	165170865	null	573729126	-800564101	528129671	4774861191	-173549452	264252789	842072729	-119640593	100719931	null
2021-04-12	381112354	682489140	-104855798	277507319	133091112	null	571900640	-320992929	235501797	4016511955	-530878463	320692939	93840214	-334121783	536097	null
2021-04-13	455183791	692633270	-111900785	320274679	79038535	null	1299492270	593652745	269153516	4579774205	-118099031	221269229	750924650	-247629461	27083728	null
2021-04-14	1009853706	38205966	-15236224	119965300	138340237	null	561847745	712423372	68494014	2578747238	-743742702	-70230677	429036254	-215060267	-152638482	null
2021-04-15	1321184207	144526280	-33542569	155082277	134866438	null	813700179	-348320496	7804641	2672245011	-130370862	-110010806	426119038	-165159098	-122393291	null
2021-04-16	853402940	57785925	-8847925	102874472	97518185	null	502316080	210617802	-91573436	1872102228	-91379230	-242636937	174253200	-106495458	-172021430	null
2021-04-19	945376994	125505465	11384040	44580349	-111858980	null	-135048693	-1147655038	108924456	1206316342	-312595692	72480593	633934504	-105592212	-125407047	null
2021-04-20	286971779	-323220101	105066143	-169731792	-93200976	null	-1055627899	-2066393089	-129794621	-527900677	-581972552	-176945902	162426992	-185543947	-307774615	null
2021-04-21	738967657	272832603	-3021270	60099279	-123147972	null	-306310287	-867924525	44998375	664248948	-538242692	403199298	-15031968	-230823637	-112833699	null
2021-04-22	488497492	-301321713	80731697	-127332749	-68936127	null	-1170430236	-606080527	-11848552	-846940690	-990296458	-118625140	-502333701	-420992149	-268478168	null
2021-04-23	763105760	186966364	13773035	-19702816	-47642821	null	-490658164	69686423	132052526	-350776020	-542667313	-298412311	-66437351	-321317529	4285781	null
2021-04-26	1464726303	804434799	-101584367	203728147	137507828	null	69622863	1406703667	144267114	1126935958	18054553	-364391825	61292192	-174117366	202070776	null
2021-04-27	1188430317	610454809	-83778335	165516235	375918467	null	223182833	873038946	123035980	1091577542	346099366	-381643784	-170948316	-133286101	350987936	null
2021-04-28	817107549	144128585	-3238001	6136209	375273400	null	-244623330	-75729575	-16325468	2209057422	290190428	-652142155	913819547	-130905267	82076710	null
2021-04-29	330092640	57744612	19903014	-61534074	551873430	null	23220429	-289280999	-277164089	4234474106	462297999	-514094417	1558598746	65282809	79465461	null
2021-04-30	-413730677	-642105111	114786728	-270409415	348648057	null	-529441893	-556996558	-750280759	1578152248	-123204050	13246294	740720673	-91108599	-178886458	null
2021-05-03	-1515838512	-1265123519	185687353	-497459228	346145275	null	-883663797	-1902801484	-735116018	-971134881	-570266895	-292414192	442464040	-191213463	-400473898	null
2021-05-04	-1236928857	-1158569638	187560664	-453661025	204206121	null	-1180743956	-1766861134	-723381275	-1608020826	-1075531830	-335403111	328901180	-241498822	-531344798	null
2021-05-05	-1151671951	-1007683906	124618716	-421730868	177177003	null	-644017364	-1758150731	-624226731	-3427868549	-941000643	-527347948	-209769928	-122404005	-423854165	null
2021-05-06	-559928546	-610843940	108668740	-315677339	162899230	null	-717880637	-1668516677	-330696297	-4172256695	-750140029	-425431121	-645939327	-190852022	-433508577	null
2021-05-07	-331667230	-221771344	21380506	-152739382	231786743	null	-199537643	-1465508256	81711672	-2484983159	-336510893	-413310255	234263374	-63738729	-222102704	null
2021-05-10	-183706374	-335368276	57233064	-202257385	228032084	null	-296193910	-1463609948	-242701363	-2440066984	-507936163	-478936481	-103872972	-101711882	-216318993	null
2021-05-11	302632899	190402486	-56826273	-51847300	83792542	null	-22261586	-880195599	-118509109	-577224649	-379446803	-63066926	-7268456	-11397186	-58315736	null
2021-05-12	-8792936	71227070	29221452	-130378271	-14621500	null	-694141750	-1037259787	-199744661	-1599419094	-552788915	-169387806	-738871103	-181034211	-56838392	null
2021-05-13	-371612146	123548219	-58097568	-56238295	14177786	null	-664183037	-1013326312	-164361212	-1727340185	-443114113	35284589	-458726770	-107743696	-32396338	null
2021-05-14	337609984	128087137	-78402923	-21630455	125307051	null	-622680480	-1366520988	-156394249	-841053853	-212542391	550006	-455400357	-95158913	-41018578	null
2021-05-17	580147448	350839386	-67891965	52257060	86318190	null	-580966315	-1244163338	-70240618	1745614240	-131598616	93729216	-138527067	-62602932	-5276815	null
2021-05-18	-209206075	-206942109	38108386	-116462439	135277516	null	-284784425	-959919317	-227354584	1548812615	-250670279	-60470812	274536815	-21649246	-40260762	null
2021-05-19	-106015991	215764996	-67643888	21410688	48300543	null	-222392342	-741155366	-116136958	2190957446	313770544	15334487	600032343	147624830	64529004	null
2021-05-20	207996765	379169719	-78972116	98685291	-85805535	null	250015770	259141710	-56750438	2257600308	275573203	84500095	557420752	181685026	222670532	null
2021-05-21	-641135462	-343843988	27654828	-113358439	-64088355	null	307518666	-359456528	-328254124	211994049	-233119912	-113062971	20019716	73807474	39440319	null
2021-05-24	245103058	183549003	-80650673	86912377	-28561034	null	1158409472	747014327	35565291	-123121087	325958256	149542823	341747819	202082999	128022500	null
2021-05-25	549991997	141316623	-92901652	90792632	62694116	null	921168557	-98326542	51396178	-234774591	965501684	-1057355	422576779	165319230	14478315	null
2021-05-26	131539443	238920720	-78483440	163330576	234408961	null	1452719636	822681627	-21728598	1279398760	695852693	236154108	756641143	110004038	-58524104	null
2021-05-27	211788004	133999172	-45683798	78308822	310681480	null	585915694	901520246	-159068953	-88425621	691243611	66661346	374520179	70524599	-240401439	null
2021-05-28	1056160982	896070219	-125130413	271193685	213256953	null	735726662	1196221553	-237137822	1393747339	606498327	245123352	699315931	195112583	-29697081	null
2021-06-01	5915781	97964748	-42070252	-481883	193765462	null	-38807371	366688071	-573279644	688035323	322517635	26765658	664373464	92010096	6700101	null
2021-06-02	657648709	515686322	-98993689	142786369	246942110	null	582901427	327043527	-275328768	793219608	23037974	132249739	412307302	168856663	153687642	null
2021-06-03	628024208	-274706109	-7470946	-103558232	243611389	null	729551110	-877527238	-621543970	-676575568	-193247345	-168588180	-29578673	80492900	68799846	null
2021-06-04	858062376	9482720	-25818660	-9110814	114573961	null	1882572607	-895219870	-419142280	683593485	-155117456	-19220697	351844724	147262684	256416096	null
2021-06-07	-314687640	-220622012	-5554209	-29930743	24840138	null	1015982891	-1039060546	-372623955	-370351900	429921328	-228514077	214938529	-59051407	22028996	null
2021-06-08	490481875	129942163	-50052453	126581390	-127986331	null	745224647	-426366246	-105715779	574306662	103292866	-221028565	54837039	52740384	-155725625	null
2021-06-09	551820531	364280520	-70330424	171031295	-288069075	null	90588915	-85593396	-46149463	997970272	-73611668	-321073966	434212380	32217622	-322863961	null
2021-06-10	1435035335	1149371067	-183685382	441491476	-395640046	null	-124294993	1075650467	207590713	2835254866	456240794	-43545792	952897289	173619973	-112491688	null
2021-06-11	720892539	780166327	-129515234	358513527	-253817446	null	-242158964	391489832	157596608	1908502210	-154473199	-36806844	410853445	88292453	-315031725	null
2021-06-14	838710417	1113314866	-134666510	400797899	-287163087	null	260930790	1304492920	570794681	3140431822	-117987407	259759099	341491373	232539446	-293346035	null
2021-06-15	35976556	941932883	-85880185	282721923	-186672309	null	348605580	345389820	271415079	1700185951	117315621	191603659	21841750	124470670	-305395063	null
2021-06-16	-1133462619	550409890	-47662897	160993001	-106961509	null	713309186	658081009	109302100	2091173133	-22891292	370637127	-411283388	442229	-223751489	null
2021-06-17	-680943733	591317411	-49465943	182506661	-232471022	null	1179678099	761387568	464930219	2524296657	49265151	434608299	-421209318	43264026	-179953680	null
2021-06-18	-766495053	-149452007	7554945	42802969	-546287240	null	1210693920	1225130005	356348237	3330986467	63483602	473503669	-587472431	-80384679	-82596627	null
2021-06-21	296810567	-99840522	5449206	20613600	-279346788	null	485295543	433844847	226066482	1770977653	-102205353	48723093	-262287573	-107926375	-80418749	null
2021-06-22	1317643504	545274287	-89676938	293134330	-272474009	null	1396143748	1310735741	559168689	3343458800	299911877	412026112	-123067994	-72892917	140433172	null
2021-06-23	2427942835	940249805	-91134530	391912519	-153892335	null	1671365480	1775484601	480862064	1968419589	930498387	510741187	30867418	98369457	214843361	null
2021-06-24	1952284247	925036816	-69988974	362730922	115016683	null	1473103057	1543555302	163082269	-399251320	927698853	537920505	-61570800	77728073	222684987	null
2021-06-25	2790750673	1279370320	-92480933	365294336	405493936	null	536861343	743699620	-34162485	-2047695113	922048119	550606023	117945666	108707678	112335673	null
2021-06-28	1859890486	1255114674	-109545153	432998651	125450687	null	1720740585	1600082357	45390153	-313953868	1018491290	892393552	-367212131	188339933	304021259	null
2021-06-29	1694130635	1336868106	-75953071	398418648	132414789	null	842629625	721530867	57245064	-1369754814	329946039	659102464	-477742971	244402057	354871311	null
2021-06-30	1751050914	392883070	-39552944	241156027	172433732	null	124438933	746175256	302520897	-689761495	-344161567	354276406	-681239902	95838450	407665873	null
2021-07-01	1479034457	-317834452	37583973	-9298742	99526188	null	253469571	-49468204	236626488	-252504192	-302789956	320853146	-833319972	-12128503	178234994	null
2021-07-02	1596643106	430117584	-32823344	235974881	-30945381	null	1115719494	913884744	587484878	1916873849	-117030446	81656611	-256738240	-38074891	413877183	null
2021-07-06	1109416148	173331217	-25479537	134658178	-11979212	null	968504366	-541977489	443808724	3269786301	-654299258	111171881	156531817	-37379905	298711384	null
2021-07-07	1236881584	-661780394	42678539	-87672391	-27934127	null	685290352	-572915641	273458311	4765558452	-461531381	-4878278	608407960	-155370514	27746691	null
2021-07-08	859515903	26719943	38580598	36853498	-264213512	null	334087530	-707532497	51392513	4778206342	-428377743	7887841	600090828	-143199696	-158532283	null
2021-07-09	1417292526	767682720	-35466455	279204700	-173807372	null	-98463653	-143077540	414382172	4275072379	-539665206	-42871096	640640967	-22485370	363728	null
2021-07-12	1333577491	641528198	-34166015	240939718	-24816937	null	-80710348	101951786	3386673	2789021029	-190236791	-57314356	528774361	155154583	-218779429	null
2021-07-13	1915731124	680951793	-42091933	243348666	-24056589	null	-1048398666	154728842	86472931	797382770	12762946	-62908506	546808541	46157457	-262875466	null
2021-07-14	1724221811	1359860267	-146583621	442329308	-153981474	null	-843180520	420875528	71952604	164907963	-118947380	332435313	537820433	108688322	-236175077	null
2021-07-15	1500135276	981771983	-125570175	278514767	-13110629	null	-928529567	-476485943	-47048151	-1215851832	-134155730	338813793	506931259	103001443	-261025483	null
2021-07-16	51370790	193221880	-45917810	42962622	-224220000	null	-1827462492	-1186338730	-388955716	-1565870059	-630793051	64798049	297259350	-10683520	-421839852	null
2021-07-19	-345626195	-384939366	28174131	-150103852	-454853789	null	-1815056019	-2369720221	-315019756	-2265125460	-1131547764	43169824	-256892010	-187738373	-243840447	null
2021-07-20	97855449	-160266337	37446645	-100157979	-206840579	null	-1485261846	-1249809524	-398740085	-1787397542	-892936128	-118386352	-149804461	-66218820	-139481167	null
2021-07-21	136022266	-157568970	50245462	-93885686	25704691	null	-869440745	-1434455896	-600074354	-3128463171	-368351178	-770518089	-236127216	-12726541	46025553	null
2021-07-22	501484848	418857485	-47752939	184856605	-104604514	null	-171292405	-1607794086	-520952486	-1280103399	202878082	-890130719	243770146	-10316786	269669186	null
2021-07-23	1610264700	1239096074	-118705198	426906012	76364182	null	396894032	-1685246673	-531022	728205065	724898428	-687894989	944134362	83676137	449661007	null
2021-07-26	1814036002	1676159785	-153158782	625437499	295682393	null	-332793402	-708035204	189928697	2733055032	1255241032	-563734821	1451644613	116546299	474886741	null
2021-07-27	1217505923	1152060959	-59793679	366192160	112435832	null	-319743091	-1679079946	36394200	569453855	806545228	-511855900	568225427	-39695205	372453958	null
2021-07-28	666745733	1135824239	-75824704	361720065	-38774452	null	-297898764	-672347438	412439580	1306834342	590962292	-17301450	1613987860	-56442713	409547869	null
2021-07-29	954378740	1131299087	-66271246	350462334	178850924	null	-158529045	724689342	637804942	-769583429	-102987184	149867608	1315945010	33855341	438980603	null
2021-07-30	946291312	960819075	-77420163	329969768	76031565	null	174644098	1911355657	291718102	-3560109977	-624896253	242369209	378653026	-16676903	413074275	null
2021-08-02	-177631705	453854728	-49834666	131344606	-48755260	null	533977736	1971625984	59962501	-3823824786	-1168645150	99227068	195186057	76267834	427035882	null
2021-08-03	463152126	811979431	-119935965	347514647	64183430	null	630037500	2152986603	234185049	-1750908297	-1215492131	-85286526	825944661	176949472	601480336	null
2021-08-04	134584842	571639856	-81531811	301090291	-31705882	null	590671188	1986237876	-116474379	-2506171416	-905701532	-76243265	-666993289	149936385	524090487	null
2021-08-05	292292937	661851696	-76614119	283860483	-47691796	null	621490714	1805990218	-191455242	-637659706	-248251044	104302249	-292510073	90535018	267955743	null
2021-08-06	472780427	-107781226	4775743	46790727	118067198	null	250426560	551589416	-482303222	453356231	20156633	-83468393	-192683438	39450097	186992361	null
2021-08-09	1974472540	576017659	-59701782	222832300	266649449	null	52598602	424386970	-475588019	-695622081	100785403	-55198271	36705350	-42979020	-13219381	null
2021-08-10	2082916077	121811296	-10638283	23254385	299501418	null	-41762715	378954058	-549333299	-1692418524	304783997	-15662716	-25589074	-115147030	-146237501	null
2021-08-11	3089835201	86034662	28187910	-147874307	539621979	null	-384147654	-275868589	-216258519	-2134175213	-242771645	-197018945	151038900	-97497658	-151412217	null
2021-08-12	2734409799	-4585988	39701340	-140719168	476488150	null	-402236165	-510347124	-28401288	-2537753444	-345826636	-388035041	35678714	-104565485	-163659329	null
2021-08-13	2787926183	848973987	-27432603	111441558	232901684	null	-41082791	-202882275	323512061	-2346462827	-241565149	-180791446	491669534	-16244121	-49507612	null
2021-08-16	1961343117	83512989	48148524	-72724465	39940556	null	-175928307	-1342266145	538043005	-2858149059	-89186411	-131528715	99511830	8028077	-69014955	null
2021-08-17	1292789516	-91681519	77180853	-48824994	-184895532	null	-257287269	-1573351981	478030190	-3502385568	-299365043	-23195067	-205989328	-23792217	41735413	null
2021-08-18	116125044	-433399166	44232155	-25820808	-319004869	null	-190342405	-656423892	95669818	-3414236896	-177651700	192345032	-152692540	-111430970	-142887434	null
2021-08-19	217334100	-194634638	-2983139	-26613866	-471246947	null	-289759801	-768363432	-17423243	-3229073546	-341820013	610637402	-180064095	-69313608	10540499	null
2021-08-20	446210889	-257938708	-21365930	-5268651	-314380377	null	-260779798	48226087	40660314	-2482059411	-270699127	635702121	47125660	-109222507	-19837851	null
2021-08-23	931300040	481425861	-112936175	252130583	-125513321	null	37615913	1354023441	156459356	-454933324	40409650	772575531	634104563	-44932516	212739467	null
2021-08-24	1317893843	996741740	-143194649	265203210	111173097	null	116957794	2215377320	182670829	1537503948	586894000	717947242	1205740098	-7212296	18177864	null
2021-08-25	2532436712	1047033666	-111481540	276336081	283501657	null	383910202	2135497266	212418988	1917581160	934945547	453962182	1465708174	95620432	245513485	null
2021-08-26	1916303828	405718734	-5713391	99664208	355561705	null	134582610	1409606677	75563528	2224976696	760114646	202760576	1242401974	97105834	76075405	null
2021-08-27	1735528472	447297892	17866342	79184553	403631349	null	167504056	1470708458	140941071	3007292959	853774609	231765259	1283684777	179167258	138370486	null
2021-08-30	1760046569	474025509	29588849	62685066	229295423	null	-77436941	1492331353	227325164	3098382485	868100841	226830703	1186444312	223488306	69517417	null
2021-08-31	1157755903	-28470289	35255901	21131712	139744421	null	-133908378	1616355887	109675229	3055733139	470854033	249219095	1096310913	206098666	58361276	null
2021-09-01	1000922133	555541545	-19379148	254798403	-92515120	null	-67559547	978996735	457243747	4721917340	513188964	695146897	1193580325	114218755	-166228862	null
2021-09-02	1728411292	615994753	-48560488	283590845	53648678	null	84532074	1630809160	586135356	3961453354	374460049	935194353	820244207	29018879	-65900664	null
2021-09-03	1053265367	660665554	-49598387	302768782	-137440398	null	113017908	465922271	592642476	2666935984	256412229	760895080	514881619	72396394	-69139281	null
2021-09-07	144728989	528387252	-14375799	185918504	-70005066	null	26836359	503781170	469566632	2510576806	210955286	937671585	483729754	-109936439	-259646808	null
2021-09-08	732180267	606664677	-17551733	201006761	-173170862	null	27164562	-385760721	451718491	2393131115	51138883	806865158	50336415	-115401593	-308948888	null
2021-09-09	524756843	372402193	19773051	42451887	20726644	null	-234793166	291511433	169650520	843198078	-14584226	345746340	-183911699	-7475940	-87273967	null
2021-09-10	-554526386	321020928	29188359	-70405675	-166992540	null	51834051	-436136884	-255572804	1075923177	627491787	125563425	33338296	139048945	-96099470	null
2021-09-13	-915919559	-293113696	105732090	-366669100	35352925	null	-378616187	-130950796	-512322345	1217532263	173294352	-68140728	135698722	7361811	-357929506	null
2021-09-14	-1006441800	-540182455	111738802	-450258796	-51046995	null	34144326	-798799417	-780182107	332464492	119310425	-574912480	-16443308	145609876	-109698176	null
2021-09-15	-939380301	-193453914	73640356	-289078270	123038930	null	150166614	-17949349	-760123498	-614786045	90509607	-293241677	312827539	301288601	-80310802	null
2021-09-16	-1181823349	-523961264	103732394	-342519691	-18334253	null	-20917154	-627782431	-720416154	-451805524	-422909162	-161038780	-131819845	162033069	-203648656	null
2021-09-17	-1343391032	-640399179	133513487	-350482029	-642998	null	-417988182	-498532845	-68265300	-1585071188	-1269878568	-392852466	-569172290	-54249451	-353087048	null
2021-09-20	-830429432	-429126454	119891361	-305965567	-252782562	null	-456903097	-876942600	-257828268	-2541464190	-1355447578	-403426138	-1432244759	-171937859	-316455134	null
2021-09-21	-368794171	-756958337	155070505	-369421848	-82015441	null	-517545571	-450219080	-223493177	-2730343215	-1285986606	-204766481	-1303718580	-315269864	-338040199	null
2021-09-22	-762204027	-577483696	105846396	-322006445	-59264276	null	-226677991	-20934929	36247663	-1702182753	-1214727254	-86346660	-1099515820	-338073738	-102213189	null
2021-09-23	-293614012	86675973	41503626	-134388424	152001011	null	171559931	357415814	171261947	-728575145	-649533074	72310543	-445947814	-193482687	29583539	null
2021-09-24	767224224	481875010	-21380291	84556905	311690460	null	136913408	1546981261	-15025377	-292486872	139193748	42575883	440167965	-96120119	231964684	null
2021-09-27	220516021	227417069	-15804748	63072256	572788935	null	163445857	2822005271	49502931	-89684820	402061735	124424910	722028323	-470818	446252179	null
2021-09-28	106597179	388494194	3073580	22127776	372749757	null	-178582366	1973569422	37617233	-1324122502	-152289333	-42425854	-150130660	-15284387	215244854	null
2021-09-29	-17439034	-84605046	106320231	-199805060	383821191	null	-534598814	879690585	-52670770	-1778795646	-189159257	57127029	-605891129	-94849362	-42724136	null
2021-09-30	-1028835109	-803559576	191356319	-429305915	96205286	null	-545780314	138744614	-243453133	-2607509191	-220997334	230454817	-731203870	-199326035	-85405180	null
2021-10-01	-896381384	-677311099	164417009	-445524881	147856167	null	-386319326	-1065652900	-493757498	-2733477070	-181915969	265489676	-474937362	-171429326	-168997457	null
2021-10-04	-603401679	-582635042	183958037	-429544873	-49697650	null	-396827780	-1894872245	-454952999	-2865433661	-424825039	156334251	-819062567	-217773262	-382514489	null
2021-10-05	-263923804	-173772243	71876312	-192696233	213701071	null	18800939	-1473799976	-208732207	-596880772	117718514	791549133	183296995	-63680363	-139050190	null
2021-10-06	251330059	374616598	-46711088	4290821	-31546567	null	301467750	-444768280	-171727660	-396130086	651221750	585464216	534417767	-68068418	128251883	null
2021-10-07	1168511172	962448240	-141340413	179938676	209038935	null	324016302	-189146140	100562773	352743865	487173418	116943087	664714954	43482673	196678728	null
2021-10-08	569346464	435782719	-78964390	31977096	142327883	null	176649374	-356111524	60012808	1013697029	430819743	437006916	577741627	43110234	155786320	null
2021-10-11	930304312	808054271	-188954616	217696247	227957758	null	516539131	463348841	344648193	1644236929	520136519	711242218	1251206506	153184014	340939195	null
2021-10-12	1211474268	328275369	-91615919	137001837	82619829	null	455046434	1110379167	19566091	1046798098	-16697334	240099911	335082551	14004198	272116224	null
2021-10-13	1096411700	418379562	-72860009	145031036	92038379	null	509731404	199016452	758650	1216946132	-28577487	173095563	426906097	-51097670	274642400	null
2021-10-14	1307058882	688502180	-68635195	193062687	66690508	null	518583056	555663952	105085552	1043454947	205016084	480987714	553095483	-45864415	276747455	null
2021-10-15	1780312480	1560600452	-111312697	391975806	94359908	null	670846118	1896840620	441824317	2638062296	-323722194	114352649	314531745	73715889	289344944	null
2021-10-18	2004178887	1802969216	-109450660	473086753	103806434	null	736286766	2023191710	564987989	3790458917	233937006	201279362	499930406	4086963	306799043	null
2021-10-19	1974594528	2393042979	-187319622	572292083	190948154	null	514749776	1236535469	858420051	2947057787	783864835	17000888	1281548704	151912271	234762801	null
2021-10-20	2321606452	1930456114	-135011399	469501073	431347936	null	178879048	2121386067	828730689	1772737551	788443326	-414074682	722197202	247823762	140974397	null
2021-10-21	1805735269	1687698396	-126271410	473530055	249836937	null	202149473	2862711139	552967318	1688205517	588138026	-77645932	62474822	211561802	167935061	null
2021-10-22	1363607139	815678884	-85646802	249930408	258433869	null	332464219	2950574541	161343002	-996188390	596957100	411819385	-600999061	167959276	341109866	null
2021-10-25	1477108024	815151176	-83260090	246068236	160591247	null	323438371	2921555097	-109749472	-2151913597	454253041	379262716	-1175677249	257458624	344805155	null
2021-10-26	1003310853	398877363	-45001838	76893247	184857051	null	563209377	3007234958	-66195194	-797033295	-196912281	471610945	-791050053	300271647	460811070	null
2021-10-27	779526791	808603100	-95738143	204422593	-90886409	null	757321470	3385580618	-93399127	597041286	-590455057	714557434	632651394	179216469	455937553	null
2021-10-28	1429155116	950649691	-105579698	223397215	86407227	null	719346278	3538846193	118911372	1524685742	-543963162	439569760	538719417	197652693	123129394	null
2021-10-29	1712970961	1364501862	-128997924	537891828	-59658959	null	810598646	3855588369	279158074	3960766119	-52048128	344590282	1507552778	156649468	-50719981	null
2021-11-01	728996654	826828013	-63455262	268296772	-41029400	null	455872164	3895043071	128962946	3390580984	74479599	18272325	1193610590	22519298	-6831829	null
2021-11-02	1088056709	1198255044	-97184210	482141285	-61623618	null	531752414	3089137260	229054949	1878481214	290614031	-30280908	1090706247	-11061051	60876376	null
2021-11-03	835585944	975971341	-102812260	489941306	153355801	null	469449025	2741175468	388626418	2025481335	642349945	244169684	-48370772	102404471	161651110	null
2021-11-04	861781445	964500420	-106937720	478383397	-75712408	null	474283833	2770263211	66160891	2454700376	872193866	-313685866	836527881	118752373	470812292	null
2021-11-05	991737457	1098862260	-141384585	386508033	50424056	null	225462331	2548269241	42791708	2869060291	1065879400	-859919696	998351883	195680193	490135717	null
2021-11-08	1761723484	1367490821	-196632765	615302309	204122152	null	663722960	2790266569	33242833	3798583100	440392101	-473631847	1908430737	335202591	489306067	null
2021-11-09	1084084198	539209466	-127697650	300711795	-16803418	null	272708798	2235306235	9162566	5914167672	286783340	-169011193	1178651701	212448988	132811638	null
2021-11-10	926101438	-25585289	-28066054	46921423	-79331132	null	-209559	2447001352	-330035443	4531129840	-333777010	-465671806	716565601	142069659	-110438177	null
2021-11-11	585576468	-135107251	-15029510	-12361053	131410671	null	-27883975	378159631	-153860320	3151578377	-611009973	68620113	286989484	130875444	-151604275	null
2021-11-12	968249161	-52912845	-5602821	21990612	-30850577	null	-251623602	-1526903169	100140613	2017683271	-669182576	639203937	-5548272	93914000	7574348	null
2021-11-15	60448313	-566114151	78886179	-259214876	-47851759	null	-791645343	-3247536093	356665674	3146586619	-42949691	266024328	-361719885	39599803	-296402157	null
2021-11-16	950023747	254645305	-320104	61106406	107476120	null	-516800835	-878464875	295276872	1872008832	12008322	219769195	-368051325	117658014	89202982	null
2021-11-17	557744967	1033970473	-42147062	293226057	-45247346	null	-582194700	-743333355	710651897	3174751341	251689101	549240741	101404343	188706854	170841514	null
2021-11-18	163806795	1062947426	-35539687	290392019	-228426330	null	-660904650	-74690526	923419950	4842026270	-164136470	200349872	382844627	192557041	185704397	null
2021-11-19	-973390847	785736490	-41120146	247327818	-303516514	null	-108901169	1793890571	1026226718	5144398059	-162663248	-32736698	147097714	13090093	34147442	null
2021-11-22	-545424060	726398720	-78442309	251827270	-287086704	null	-101625222	3459040858	891127204	2897075009	-631722268	-33486836	-98296584	-89476078	43598844	null
2021-11-23	-1116328500	258188151	181636	-25144287	-167785680	null	-420911656	1755577128	752712350	2377803023	-619007459	-272809510	-197936196	-139278793	-253496666	null
2021-11-24	-309215083	8616916	-15226473	-75382795	-61967002	null	206746197	1310411752	493101439	1267929717	-231097919	-345563891	-298231227	-181693934	-56450966	null
2021-11-26	11953206	-555481548	26207743	-222619277	-75433872	null	-19872020	1736333278	227238345	-1438565009	-112075740	-21996561	-1214378987	-344358023	-212725974	null
2021-11-29	776094522	-398532118	15390840	-189212440	134132161	null	-203591506	1795688803	-12531974	-1346594153	-157518619	-177439123	-779385563	-142296733	15120145	null
2021-11-30	10733606	-194532325	32060339	-139792625	233673907	null	-165982075	1602450582	174152992	-704750864	-366625058	-120576978	-828841229	-143096832	72139700	null
2021-12-01	-621673022	-156572689	12388630	-147437556	220052558	null	-228083322	1611304248	95385364	-1223795842	-225234529	-58307067	-169718047	-17542013	70917944	null
2021-12-02	-763559390	-67888461	-18829045	-195148906	400268058	null	-363819580	149315020	67434579	-770478183	-565722177	-178596785	230751790	-55417683	-59731515	null
2021-12-03	-991025628	-167025997	6409848	-249079431	329303162	null	-386877179	-944979829	63253697	-1280293617	-667664325	-607494132	400328176	118823871	-122303713	null
2021-12-06	-1269657040	-216750874	46612129	-265305402	431311103	null	-648421445	-2692443732	21545700	-1544156953	-677879836	-290018522	-43326679	132202312	-391853219	null
2021-12-07	17236203	366315826	-46487287	-5781726	411323981	null	-253096404	-2539969990	52588079	302293965	-140217473	41844995	812212653	370905683	-234772348	null
2021-12-08	1087796350	-1788334	-14922902	17901843	190666689	null	-169596378	-1756590966	292086763	926464668	260595534	65830573	485642655	157904755	-238935564	null
2021-12-09	697278331	-684164906	75768428	-122684662	-9134072	null	-583985365	-1783572485	274019025	140048922	636570451	-73012650	119299195	102961337	-417119947	null
2021-12-10	1250847055	32393792	2174480	64692925	125582120	null	-622456518	-514241136	593109156	409250765	733325615	118529556	521828339	309825756	-433647597	null
2021-12-13	832516192	-253048588	58647215	-200236780	-150348818	null	-693387951	-615559949	323088609	-1034404680	706753654	-200823647	227029748	78424122	-458089484	null
2021-12-14	545911748	-850841983	168166296	-383844292	-162436822	null	-928010506	-2011118855	190026245	-2916267285	313921623	-562481251	-673131439	-278727303	-505556153	null
2021-12-15	-124210654	-409445572	137725761	-284810161	-58138137	null	-588666671	-2492398881	27325070	-3134785199	-183683175	-597893590	-886112010	-48411781	-256887166	null
2021-12-16	-38346699	-312504459	147955158	-318308499	164275886	null	-663276429	-2312849034	-48187309	-3597114219	-806428979	-658208376	-1078696903	-159974704	-210827522	null
2021-12-17	-423762675	-493307924	174450026	-350166298	115416861	null	-363358236	-1883423506	-76647013	-2675744722	-834999086	-681415762	-1711256589	-296978197	-67968569	null
2021-12-20	31345959	-363353767	106051910	-194352926	104386956	null	28602337	-1641390536	85513057	-2853974922	-1413210388	-367522605	-1755908108	-33203828	6992758	null
2021-12-21	381090835	404071435	35928274	-108744885	73078360	null	289583176	-906182703	8288075	-1563030693	-970461842	-54519043	-1073309633	2212778	659840	null
2021-12-22	1078139272	809509030	-25923052	10353820	160911087	null	325608946	491066896	41142049	-1130737537	-1085985674	162308974	-620816483	3072303	-199786373	null
2021-12-23	1563997683	1626701824	-128032357	334173824	86080532	null	882149678	2117833353	392653669	131693528	-397603884	359514474	-29930043	407864214	20537567	null
2021-12-27	2087055290	1871635881	-156642966	434383123	279571577	null	1112594143	2279825778	298037824	-491428150	149856810	361255337	697462992	377536503	124527417	null
2021-12-28	2124591847	1599548882	-106595750	313746191	476438530	null	672529463	2080113096	243005632	1107457278	642301580	191995118	781796651	147989731	95557050	null
2021-12-29	1994432278	825085831	-51070844	164822976	369950826	null	213569600	937629364	88746795	124227402	173303782	7543624	507124432	405592897	-34472369	null
2021-12-30	2018580835	683156459	-27339722	94687483	313612843	null	77419210	-413762477	-25362798	515788102	797261414	-35228404	242822411	219342161	-79657365	null
2021-12-31	1443714638	-222982231	49677440	-208764673	229117101	null	-302488485	-1749478673	-409573019	-326302224	195403496	-136590148	-262918839	55187511	-224816360	null
2022-01-03	512456319	-427485655	48443952	-243532712	272198215	null	-348439227	-1917968660	-335095140	746855848	155173776	-197114452	-299968520	-133820724	-257056259	null
2022-01-04	108477601	-544637798	74575413	-300049253	325872639	null	-327646247	-2304645936	-304442205	-961393345	-261131276	-477881607	-213072356	55732308	-274337042	null
2022-01-05	-1453439953	-881501022	109818789	-389840606	322104325	null	-316258332	-1119472312	-286053748	-1497552986	-341859870	-615808676	-836790031	-246618424	-237868606	null
2022-01-06	-2003471280	-810667528	85292052	-453146652	420559367	null	-252426064	-1689593659	-375786725	-2536912192	-220570368	-1015529545	-587587870	-373535626	-144896461	null
2022-01-07	-2398396847	-584240235	98244368	-406598082	564343764	null	-292644184	-2157135069	-360461409	-2331604799	250726886	-1091490620	-674553597	-558388861	-241533657	null
2022-01-10	-2981406133	-932235008	176480410	-559945252	256061138	null	-661322134	-2855279148	-615534471	-4215999182	-353938165	-1125089082	-978217868	-663367075	-405486355	null
2022-01-11	-2411121381	-368932430	78503403	-337640051	191571399	null	-219815078	-2251223634	-481339111	-2147562598	68249380	-824771320	-766480020	-713274018	-235598331	null
2022-01-12	-1015024582	316473266	-16693362	-181200932	77982541	null	195183090	-1540745764	-269608405	-892856145	293082719	-773918617	235422762	-424114219	-124842906	null
2022-01-13	-1424547658	-172097516	68731926	-285687975	47075463	null	-156048013	-1802431406	-249271014	-833747959	-316499717	-676225517	-189078988	-380938910	-232864833	null
2022-01-14	-411314868	201124936	13441144	-166840831	-230220340	null	113693561	-1152506233	-219475264	-604127685	-164411930	-552145887	391126237	-274725197	-12083934	null
2022-01-18	240981297	-50061448	20051290	-223726425	-183922870	null	104411263	-415080641	-253811048	-244937584	-193900932	-590976119	161541719	-290362755	1202167	null
2022-01-19	-184714157	-331044510	51357554	-320275890	-378055942	null	-223483986	-533709003	-407720907	-2137405241	-30210556	-380787160	324838313	-418268069	-141167987	null
2022-01-20	-508164300	-531775714	42676771	-317827796	-198865374	null	-437986665	-930525229	-659923489	-2473326069	271381160	-142267240	155686653	-458011994	-162274924	null
2022-01-21	656681786	-935058217	15520923	-265977359	-436704737	null	-167358504	-770683899	-606909002	-3528580152	283285976	-88744335	96088088	-395528835	-14712265	null
2022-01-24	483056185	-1240818682	18521653	-264755816	-487238477	null	-364032904	-1250291246	-658795609	-4831226795	-179011143	-287236474	-1064070862	-484832972	-155193033	null
2022-01-25	589631473	-971219247	-17979094	-158574193	-434225104	null	-255912873	-2342563049	-652596098	-5019777982	-111226122	-355855364	-1169489948	-407581598	-139625877	null
2022-01-26	503681621	-939202690	-32490165	-164387398	-215133830	null	-69216311	-1049074923	-600934615	-3774528053	-363497546	-401232306	-803434952	-68354716	-74797533	null
2022-01-27	469340848	-851951555	7149346	-162360951	-337680658	null	-185247528	-2462459226	-470698038	-2649218212	-337173637	-196305482	-662165814	-170974463	-174118194	null
2022-01-28	174010710	282648118	-56468801	-73377580	-213895489	null	-148838808	-1456012234	-186608495	-518094255	45480786	-310124624	-108400510	-5114385	-183938915	null
2022-01-31	393833191	1074879866	-116260147	-14859084	-15603889	null	87503122	162122222	-47706835	1860629564	393553092	294994402	986208137	324196726	-74030534	null
2022-02-01	185769489	743039905	-104561698	-58177376	165506208	null	-72198170	-190475848	-168505126	2673728009	906730545	903614317	1910705697	455030483	7464364	null
2022-02-02	270214867	760715717	-66849426	-65876451	137791553	null	-274234067	-1484873246	-155900866	1890149307	627046206	336219917	208423130	333337541	44692338	null
2022-02-03	377333595	563926566	-41559480	-115445210	98731351	null	-72388166	70030456	-59513063	-909986796	426135979	-194625865	-656346512	282447364	111574793	null
2022-02-04	-64186887	83050971	-9742252	-131584955	247063540	null	-340801511	316628745	-422075847	-895087031	254360272	51973739	-927494002	284513575	101573285	null
2022-02-07	-324568044	-657724033	55679286	-212907856	309835031	null	-222645949	-891400328	-324310917	-766607924	-164336036	-544579024	-1667351665	189874955	150618561	null
2022-02-08	254753741	-53424082	-21985028	-106526916	315840627	null	59235524	357479477	-41719493	82874712	-539532314	-903629743	-2489859577	246187201	251086612	null
2022-02-09	619728386	227277425	-94124390	-1968012	407500471	null	398350794	1801550977	-133916246	715832243	-214288975	-370617090	-865102953	237966064	284476813	null
2022-02-10	179345936	242931857	-100989918	-2634149	479992476	null	311187581	883938103	-363025353	1467684836	-336669294	-419796502	-787176014	241912168	284992893	null
2022-02-11	-81630843	9890758	-62364552	-82960449	315300734	null	388503732	-146293211	-301615396	-51077595	-462131748	-603159973	-1289835925	80772446	221518810	null
2022-02-14	-551171175	348942885	-103230994	-20805840	114930005	null	243982065	869822599	-270101582	-141076619	-260694105	-207323060	-495700155	105890992	176133441	null
2022-02-15	-783909638	258766274	-105443650	-20647290	122729591	null	221569726	1103902978	-393552895	-981121576	-238759576	24211708	196653452	175215243	172622076	null
2022-02-16	-999884116	-93155870	-23224897	-82370690	-43886777	null	-81991941	-247709408	-350646862	-1118980149	-442382876	-332283383	-397484787	-64261018	38729816	null
2022-02-17	-1245806866	-117683911	12102152	-106231887	-160817435	null	-240842748	-829719856	-366255124	-380324869	-560822825	-220569470	-366976311	-41638995	-27062037	null
2022-02-18	-1236317751	-297556297	-2323449	-96733617	-150721945	null	-190360850	-883956679	-320508644	-80533179	-590009928	222211094	-134937162	43552619	30617807	null
2022-02-22	-898538581	-23118863	7288252	-129134399	87173500	null	-121750229	-1894159924	-338482370	-1946231346	-472893285	-49981225	-613945830	-40175974	-37649232	null
2022-02-23	-1178147464	-363820713	83625516	-274605906	-182185750	null	-405505863	-3657637311	-493414271	-2373658892	-435423366	-380995160	-1040821602	-207778528	-256117455	null
2022-02-24	-730945221	175482987	-23485202	-196916272	-233855853	null	-130932795	-2411222924	-467823530	-1957114778	-231613415	13856450	-701621223	-29222257	-135441811	null
2022-02-25	54240141	543612464	-123697907	-50114311	21678509	null	114345809	-1191585862	-209997527	-1325479620	192756360	30854957	67422156	147007735	28768729	null
2022-02-28	588470083	1011380195	-136910662	9101077	180874094	null	347034932	341751290	-139805892	-1148007375	469222684	-151892021	153717499	94673081	36507969	null
2022-03-01	369765300	169665775	-91032349	-53260681	-182783368	null	41254229	330171850	-354693904	-868056937	177501583	-157682470	204969077	-35827313	-40057488	null
2022-03-02	492346394	511941174	-179008706	63113981	129938976	null	382019524	1427011452	-137612768	25072372	434325113	-204647923	519560839	97118080	85323344	null
2022-03-03	135562311	-97243712	-80381232	-89160828	170939735	null	44778599	82417260	-152251728	-1383679491	144933500	-580513136	215092497	-87951584	-65840772	null
2022-03-04	59547745	-412928138	-22664615	-189501192	-160527554	null	-163513334	194041649	-340984485	-2581265724	-146266530	-596302453	-458222031	96658134	-261770338	null
2022-03-07	-206016950	-558622437	22055133	-262811908	-413609953	null	-482548616	-293616263	-417102924	-3151910756	-491236355	-668771451	-872107565	27136916	-337645928	null
2022-03-08	115078164	-98731213	-12203556	-191927395	-101270544	null	-229596008	691006161	-254753536	-2992897255	-146086200	-662830973	-366359510	216925299	-230465815	null
2022-03-09	77957208	-128502555	-15404935	-176797293	-119844344	null	-299558535	1177435286	-326944887	-2376767148	-135051230	-278219976	-97942119	242761473	-203452907	null
2022-03-10	12554587	-139337955	-2722138	-142135430	-242848067	null	-239231797	1193611648	-421569220	-332765309	-152637807	13051396	-369533160	271729198	-163843968	null
2022-03-11	-287630232	-270964920	25975825	-172413031	46801274	null	-236732344	-187766862	-555682838	1009767241	-232291869	29241012	-219745455	-78665630	-97185499	null
2022-03-14	-239918926	-482369153	14011575	-163478523	319127733	null	-253542984	-1104487389	-688068001	1723013320	-7227081	-130704995	-73091579	-100193624	-57305965	null
2022-03-15	-84306691	-281135233	-62864545	-144553175	382212645	null	-242160155	-1099014046	-650692109	3132500045	-16915384	148398298	-181308340	-21606351	-21704529	null
2022-03-16	435689921	-86336584	-56699086	-161361754	366377816	null	-324569403	-958303726	-568214838	3381905081	60852896	100726083	-241516478	-58322162	-60830460	null
2022-03-17	868669723	54180171	-106885658	-122128969	525129251	null	-296210813	431051688	-387501199	3028132774	386841059	180785579	107568919	-54903709	-33683918	null
2022-03-18	1177509707	806472439	-244494161	27365214	441573099	null	-233541746	1815669843	409989092	3590138074	906112054	546992167	412333648	163547781	76228762	null
2022-03-21	1020254210	751964387	-247768785	62124588	161892940	null	-8971689	3200768529	582427492	3918448924	672247575	547675371	656895561	158893409	139094860	null
2022-03-22	1068812903	730060469	-219038118	81335929	124752402	null	-150222494	3315906231	631415776	3917492437	687302892	528173359	801145706	84014155	20280378	null
2022-03-23	170737175	115244663	-115514290	-26184335	-118948783	null	-292241565	3170656102	615468802	2732498781	250139001	237442455	111453588	-76973795	7015439	null
2022-03-24	106950913	369077243	-170809365	37455025	-28354921	null	3170833	3225881567	740709537	1130229979	304554702	4748555	303994708	173452599	136602007	null
2022-03-25	169493809	-351720792	-62991007	-88096581	125274576	null	27497957	1905882738	193026454	664373749	2400525	-342297457	53483299	34811937	15631969	null
2022-03-28	340754267	243093798	-149584167	-5638035	121339162	null	67556270	1950119664	244638582	1668748648	115023571	-193552995	-103447952	123923037	13402941	null
2022-03-29	336513377	285106279	-133352644	-37351038	93920169	null	177706290	1011913275	236629424	1077557179	141609879	-106737736	-152869480	104109646	103885771	null
2022-03-30	537688523	270998946	-160959458	-34074883	76318657	null	59291927	1204200751	126523170	425445365	308248197	-122920256	-39105649	61980572	-1640291	null
2022-03-31	-620650752	-403833706	-46142420	-175206784	-136488082	null	-276978146	-243694670	-132184735	416208116	-104186234	-211965606	-604647394	-33317156	-251371694	null
2022-04-01	-655790225	-386660307	-32809584	-183412877	-391756203	null	-343668072	612942114	-128102653	507544720	15733808	-80188568	-267818018	-87312105	-249803962	null
2022-04-04	-184793615	-239343214	-35437819	-135532586	-369794213	null	-247325160	866295542	-17443824	399048482	346659873	156580866	374427941	24435795	-216535239	null
2022-04-05	-994825581	-814061194	75293847	-256879241	-434272212	null	-535981195	-83932323	-199710011	-806417630	-10754531	-224725233	-256758427	-116921249	-306975248	null
2022-04-06	-981086082	-615223691	68330782	-231703605	-433134882	null	-486778038	-1803990561	-157467080	-1111477287	-161288289	-230134823	-474555172	-138103554	-290260497	null
2022-04-07	-40176725	-254856745	1197833	-156895617	-410276800	null	-455820293	-1199909979	-51309784	-1198838729	-88065926	-278890974	-356840213	-242699909	-183153431	null
2022-04-08	171499315	-229180006	6035653	-155378172	-195683955	null	-474646674	-2093687860	-197981143	-2504862519	-189617753	-424594125	-773649426	-300679540	-205588252	null
2022-04-11	-416356104	-1083863824	111958862	-330996317	-104629374	null	-780990813	-3823356165	-486235373	-4017397129	-609841312	-763755598	-1586162383	-464068337	-290423920	null
2022-04-12	299506742	-802954607	42426597	-269429419	-166688439	null	-739501499	-1894743743	-346630827	-2744143235	-378948777	-580125311	-1332786514	-285165419	-275721471	null
2022-04-13	981701275	-346574628	-20822302	-161778403	-181309910	null	-402803917	-449927982	-213358844	-1023000828	-54833563	-338190401	-639029049	-65987174	-101662882	null
2022-04-14	469797865	-664371059	50701377	-233921271	-232171193	null	-481689042	-1082288266	-441841345	-827749544	-94722339	-287491915	-741957888	-193633747	-189215503	null
2022-04-18	474821183	-285572224	-33006361	-126009667	-279569492	null	-189826952	481463220	-172893412	85982751	-62270120	-305655205	-305428162	50012224	-62506636	null
2022-04-19	947338568	439417391	-135513198	13925554	-165911454	null	18244185	1971123100	99151818	1482397994	287177625	-10255471	416396680	228733024	61636455	null
2022-04-20	858130461	304137789	-118769634	-19438871	36159130	null	12231644	272469434	68676281	143115612	22179562	-141030707	144586983	196101421	12536985	null
2022-04-21	216760020	-124041365	-52978033	-150610933	119802982	null	-406599526	-735119951	-75012483	-1023434920	-370730146	-354166364	-402221549	141360803	-150047106	null
2022-04-22	140255504	6414662	-67509422	-145225113	68472058	null	-426470328	129027584	-43191577	-1064409583	-370506445	-317921426	-686402473	276992971	-53724907	null
2022-04-25	-385595046	66199806	-60046932	-198763833	-94870808	null	-501878541	-1061051541	-187581821	-890169827	-338618292	-309488285	-393534263	8713645	-73467030	null
2022-04-26	-980210637	-385806591	25874750	-357585381	-386996312	null	-717648034	-2834191169	-460856289	-2524684078	-623406757	-677316725	-1323305542	-254655260	-262806920	null
2022-04-27	-1091945248	-254266916	1618900	-322186713	-401585965	null	-644618820	-1418182838	-473726550	-1892606386	-435040134	-713331719	-1996614163	-249977685	-176982502	null
2022-04-28	-1035039911	-401292621	-94834977	-239432345	-265042401	null	-298499267	-1470509378	-496942875	-279419162	-195913476	-472768281	-1252998327	-182602901	-97669153	null
2022-04-29	-806740825	-388804004	-34613503	-214793421	-230160130	null	-243111507	-1550492043	-394668035	-1536718972	-66376739	-466062265	-1035160351	-254163522	-122546611	null
2022-05-02	-517778908	-496837661	-26176956	-202278081	-297567592	null	-171746076	-1263825383	-494197702	-3228794449	-90392940	-169866042	-1311247087	32373546	-129272336	null
2022-05-03	-628608551	-347915473	-111873996	-133022971	51750877	null	-133642542	269790595	-265339722	-2474833743	8409502	34423800	-439051718	282867221	-63534289	null
2022-05-04	-292631156	-47218808	-146753065	-114899177	83883945	null	-74501544	-156774216	-263825264	-2960399412	55045801	73949438	712824476	233826953	-115726442	null
2022-05-05	-431066000	-95195151	7301508	-229282906	-228891337	null	-305734419	-516470559	-397560382	-5410646065	-142209185	-209670695	-275845378	-46620195	-210117827	null
2022-05-06	-166668901	-237494884	-79702482	-198646142	-269728792	null	-210401412	-797145477	-387304946	-4067045282	-197601710	-295971243	-106411539	52238248	-147199444	null
2022-05-09	-151849469	-293594309	-52749966	-252696874	-282414450	null	-447187663	-1423127197	-356055869	-4074332134	-425242168	-565045741	-738542829	-261058078	-251179052	null
2022-05-10	56643418	-326740115	-26629554	-234346882	-604304275	null	-344786735	-2145345003	-435519650	-4382534921	-412357440	-450105852	-518500171	-174877841	-186020105	null
2022-05-11	-57531086	-887900852	10952268	-251855195	-708034364	null	-394459761	-2993243912	-578348031	-4423407658	-566561130	-450054737	-731769832	-309534501	-130716475	null
2022-05-12	244135543	-541026587	-97934693	-167339822	-633039434	null	-316487566	-2437067137	-516933089	-2544965898	-350321411	-154922775	-762362291	-176564254	-73295045	null
2022-05-13	131786028	-40308007	-208228499	-111112761	-297373909	null	-182857364	-1726549814	-301117740	-1022159262	-119840766	162636015	-153801426	-78212660	-67146940	null
2022-05-16	329563974	-207510780	-211361238	-77674992	-266626295	null	-115575317	-1670805803	-276039987	-513867141	156597967	387857858	-39950911	30497195	-11806917	null
2022-05-17	355877849	-68271288	-232844911	-71492638	790757	null	-110116761	-987055369	-323584215	767117906	188193578	215168066	-216855689	21598995	-4899959	null
2022-05-18	98942469	4418522	-140045971	-108987842	-185368815	null	-151640893	-760914855	-340736241	555868101	158004972	199399946	-566523675	-13791110	-137487326	null
2022-05-19	353148054	153177051	-189224286	-48859355	-192649638	null	-57883775	110482039	-315008285	791800790	263841597	202996272	-149020433	-154016988	-130171507	null
2022-05-20	792712739	-188598927	-57907779	-122635481	-407836503	null	-179495113	-941127905	-622096887	-204255435	176439963	-14500085	-887934618	-399267039	-189131572	null
2022-05-23	694571741	-53495418	-99118815	-103680515	-128904601	null	-138189029	-617814385	-492355044	-83353849	-89103	-215092855	-223960214	-604698821	-167261692	null
2022-05-24	669732911	-278088185	-51955085	-146093722	-392182106	null	-257069192	-1748491212	-530826460	-1759105544	-64532629	-271236926	-1194827744	-854082945	-255552031	null
2022-05-25	708172444	-157690080	-197935746	-59678564	-160923131	null	-59015843	-605480014	-438596382	-65283763	83564990	-22348021	-1070234183	-614826565	-139741353	null
2022-05-26	562509336	-223986117	-195479453	-51682500	30346051	null	23320658	-633938538	-284951644	86842354	102917291	-59951779	-555074996	-229041428	-17869176	null
2022-05-27	575387978	422609580	-313584999	38855778	222732392	null	136872492	656354584	-51591423	823200887	202456391	137705741	187928858	117495485	106701399	null
2022-05-31	475969114	416124345	-243737177	22972131	-16984972	null	83033485	1062102976	-40666043	2539775765	286097075	270571456	238200635	321285494	104625737	null
2022-06-01	178548093	272849808	-224317082	20564482	-4252827	null	68379098	1162654442	-56101699	4541310928	227225007	321907008	1293260753	356637391	74289133	null
2022-06-02	212879516	513380479	-257699537	20507393	-60729915	null	114052534	1187445265	107215518	4260062067	391207767	322845440	1872437876	187025742	207478629	null
2022-06-03	12624510	179206445	-101568854	-101343257	-193053156	null	-137930146	-41285336	-47612450	2350955355	58523703	119512206	1211878783	-126667502	48219473	null
2022-06-06	-518534142	-169275635	-9273504	-195235849	-348792950	null	-338555265	-1256536822	-146718918	1584575391	-45820712	-49827481	1155189948	-345425298	-36337648	null
2022-06-07	-402469951	101971385	-105405683	-154456493	-223620598	null	-296939650	-940700758	-150604433	491592523	-93538490	-89683221	754682493	-215898271	-42011603	null
2022-06-08	-150821995	238158584	-128465837	-149055016	-179421782	null	-318316329	87833757	-103008268	-667897141	160277918	77410578	627058571	-236961074	-51672549	null
2022-06-09	-511930652	-201671467	19834981	-239925894	-349443892	null	-525871873	-793452568	-351323475	-1190527511	-165850107	-166329066	208498000	-114111313	-257522911	null
2022-06-10	-876499656	-140281112	-81582798	-185552333	-404670179	null	-485227718	-680175643	-403158353	-277897504	-222338568	-191562238	32014227	-118912109	-259824617	null
2022-06-13	-627021909	-324906665	-16343182	-182012386	-518787940	null	-486436855	-644175689	-270526255	-216387723	-445110893	-270611411	-799099320	-232721487	-295790869	null
2022-06-14	-953377055	-757811980	66319433	-235979869	-598184315	null	-543503237	-933615224	-402092586	-294209236	-599009377	-364778624	-606196408	-252803061	-352162704	null
2022-06-15	-544678962	-609254816	-13778813	-191488436	-370746595	null	-386987760	-952325886	-360038230	-221663430	-575944238	-333850996	-405192249	-85129992	-251854863	null
2022-06-16	-235377258	-376341071	-18068332	-169567243	-430435994	null	-327574429	-1207240206	-250611480	-305610222	-541243668	-333565635	-641830953	-266597323	-259478707	null
2022-06-17	259497945	-111795711	-47920274	-127959202	-148851998	null	-156665258	8531656	291190161	80450902	-247564849	-60153839	90022446	-189366300	-206438121	null
2022-06-21	267830716	205537428	-167311415	-58659903	104052280	null	23282344	1191985105	324272689	99232568	-207374848	-4611960	1041857332	-68232180	-131765433	null
2022-06-22	588162316	729034079	-220412159	3543154	290760496	null	185663820	1598592018	425966957	181319326	58777824	253470779	1027700232	-261892947	-57484611	null
2022-06-23	209374775	882465718	-176836964	22841732	3602123	null	58738989	984514994	524408588	190378640	19844800	133203378	751182261	-338926925	-91028407	null
2022-06-24	678561964	1187988333	-297877233	152101336	288040825	null	231317281	2207355036	722851205	450713986	361916174	362387902	1475760845	-123905853	103918157	null
2022-06-27	457819668	744680296	-228966132	62876073	67713578	null	93190719	917024512	246355642	70233431	183967765	87487939	807238156	-113756617	75729741	null
2022-06-28	213312357	364898193	-125255459	-42546564	-44178956	null	-69208640	-313453473	13136391	-40102406	209333110	69073916	28691167	-117894765	-58378739	null
2022-06-29	-3730658	-65850058	-109229139	-68924766	-310872215	null	-232344075	-1304772946	1924084	-26979722	205732525	-174531801	-285411233	-37481191	-133743386	null
2022-06-30	697687124	45293580	-147085922	-112250950	-146272716	null	-146591782	-861982229	-75384044	-104691307	119436909	-296611642	-830494060	-91358043	-97180990	null
2022-07-01	166008478	-355401999	-120651366	-169549930	-159941667	null	-406890193	-1115993803	-134484960	-104006858	-218455478	-328566850	-1609241493	-262970675	-245272980	null
2022-07-05	227828541	12542222	-235802031	-66315593	-196547893	null	-297929673	-403785004	-34185815	65629114	17618103	-139582630	-1143331193	-327951328	-169847524	null
2022-07-06	338817939	437743541	-303850688	26965540	-252274625	null	-143560046	-324227773	109874620	188658733	89913307	-148721270	-680763888	-192025219	-85173053	null
2022-07-07	897089767	681656489	-348044344	56892377	-19342173	null	30297644	951068767	173529377	187577443	88479855	42024302	-88996727	-13222981	34292077	null
2022-07-08	351153738	519873308	-286413292	70978672	-9767763	null	-3733471	1233502787	211969666	125320020	-93597370	44795189	352629869	4467665	46705890	null
2022-07-11	239672250	352360677	-195123344	-14885768	-179355374	null	-10765893	135588190	86182528	-134418371	-117985838	-138070830	424021799	4748279	45408436	null
2022-07-12	609496861	386951156	-79441129	-42068800	29281632	null	19796703	194323795	226603282	-249893457	-132491806	-275774897	179787785	163352801	-34674085	null
2022-07-13	363120258	255865405	-155101932	-39981684	-55413214	null	57016499	1227865947	149594036	-248965087	-9438334	-225623953	-420887836	69640022	54685247	null
2022-07-14	-147802334	185760048	-89051191	-78439178	-252598134	null	-35921371	101358240	160158077	-352077088	-278092247	-434285277	-1274018492	-43676837	9516154	null
2022-07-15	899877341	849869030	-183137576	-33451704	-168699675	null	83232425	-174038131	260301971	-34364050	-5744145	-168775063	-863306095	64544418	64223039	null
2022-07-18	915503383	967545375	-199871564	1306890	-71664125	null	249747348	719545605	156355182	156431614	296061898	101202427	-657315042	126451768	144573131	null
2022-07-19	861077505	1177584417	-303595074	70789209	-49202055	null	300259747	1132064490	181209236	331496917	333489766	360309951	-359538913	154222643	273274743	null
2022-07-20	1311396042	1418290697	-279509365	78718347	125714834	null	333823362	771218287	307177611	412204418	449654243	322696447	129188979	233601401	237115417	null
2022-07-21	1665014767	1569371155	-340825707	116528235	212656481	null	449149577	1911994236	229589745	538333767	439938185	594977897	473706415	262361628	300568079	null
2022-07-22	563300474	454802678	-215001231	28782087	62665492	null	224233910	1994719995	-5574780	233660956	90479306	348005903	-100283071	120932708	142614707	null
2022-07-25	924899281	442345605	-238160046	32895646	128737383	null	116152325	1161105724	54115410	145492031	-211311505	170274700	-96799552	81661619	76901268	null
2022-07-26	419664385	-170732588	-93242050	-104477866	-35147953	null	-114667401	-10327787	-237791106	-36926815	-558720971	-131241618	-333405393	-55617057	-118510003	null
2022-07-27	479849186	-346573270	-153602748	-63538406	50168890	null	-137266463	471463366	-235178807	-37115822	-593607640	97916247	-316302926	-59667388	-77470541	null
2022-07-28	451015804	-428918894	-136730685	-55396893	61485840	null	-151994422	252267102	-181371929	-38898645	-529885559	-96683657	-146529005	-50603367	-74746103	null
2022-07-29	881474168	-276251637	-162980133	9374807	208632824	null	10164715	580045014	-58831249	111389010	-485850184	-4723662	102769662	54368894	96905000	null
2022-08-01	611605431	-20069244	-202157815	46206415	29738498	null	162296137	1658620153	-62670678	248635538	-249611290	57559494	80993601	130274595	177845661	null
2022-08-02	957979559	386933969	-296362805	114409497	33926956	null	371763311	2896519478	686389	407307942	14546403	168706451	269668810	131039222	321813637	null
2022-08-03	1046826205	545716179	-259069301	111700738	5449564	null	415576102	2963560954	45569170	435571402	39685036	140849650	328860455	108886015	329178342	null
2022-08-04	526982562	518961382	-248566844	90259534	-68714420	null	398789365	1958697144	-122014866	492356749	109533388	303134410	108861026	146099146	355422886	null
2022-08-05	-133570077	380732791	-223777945	38390718	-82520524	null	269307171	501832235	-350405360	405698078	109301859	174341096	-93308808	69803187	175017525	null
2022-08-08	-200959468	79726684	-182862824	-20505083	76114412	null	119915865	434904463	-263372311	211847078	187798941	293204797	-27194385	9258568	56081002	null
2022-08-09	-365821010	-304288897	-113563422	-87516854	233138104	null	-71175275	-729647884	-189622621	49932692	54634592	192076920	-215116209	-41548563	-51110558	null
2022-08-10	-447624414	-315622948	-84886026	-103002260	251246919	null	-105043784	-1015038945	-106898072	44764269	24620811	248689506	-228463262	-43834857	-65813313	null
2022-08-11	-306065701	-736813173	8174536	-195121832	442346374	null	-186193492	-1221224941	-2056518	-225261252	54542194	180978782	-148771305	-106139427	-178159803	null
2022-08-12	473959955	-75334463	-61426477	-70384785	471542214	null	74744817	240484696	361458961	-164712730	426499893	432493459	75624044	27390979	-24446839	null
2022-08-15	969388533	489307073	-157113342	36603894	440811188	null	241650784	616072483	447270345	-124260543	340803971	294021352	205652072	41581870	73423356	null
2022-08-16	1224702547	490090583	-186064380	87678301	447140766	null	172632579	1229436110	463068926	16315639	240069418	310355327	198897367	58402277	74127282	null
2022-08-17	802619342	94719222	-99078086	-22100164	265314140	null	-82523620	290527992	368165269	-305638731	-77386412	-564274	-25643113	-129394798	-47990968	null
2022-08-18	1072465988	683210073	-201560384	81536163	103719745	null	40098150	1369776503	411551650	-126366721	23921338	-76699810	65011807	-2127342	37265749	null
2022-08-19	42190067	-46898942	-84825325	-78646302	-83834540	null	-348172988	-209039480	122150427	-420658685	-397483764	-340712799	-219069089	-183306562	-154700596	null
2022-08-22	-629444858	-852950174	49752387	-227167387	-195258022	null	-616617400	-1713706387	-202791330	-472356651	-624067063	-492142767	-443917620	-221955238	-248618100	null
2022-08-23	-1155456077	-387330796	61570383	-230685986	-325646327	null	-351403475	-1030557693	-187552791	-534719787	-568268484	-423643795	-376468862	-99817853	-110101416	null
2022-08-24	-702390153	41830670	-25566330	-124433485	-184377773	null	-126145975	91395928	-241570259	-268104915	-271142931	-171051601	-222918663	-24033218	14126653	null
2022-08-25	-983013419	-320971338	7713658	-160687556	-79211260	null	-70951339	-528278301	-484500897	-153665834	-236703859	-76789733	-204910603	-66846893	47307586	null
2022-08-26	-871563406	-379256259	31882252	-188212863	-75503448	null	-18288403	-16585670	-647997574	-50352174	-160514241	-28832588	-170864993	-65573690	36981565	null
2022-08-29	-540198147	294794055	-75179840	-86097922	-104751277	null	111996447	853753132	-388165582	174956740	2787415	215749086	-26754565	-48517699	54958471	null
2022-08-30	-419793760	-113358726	-70626519	-152182915	-177617338	null	-108286526	-150830295	-577122014	71670425	-6416838	177332272	-123186580	-166586084	-86472038	null
2022-08-31	-945964218	-586332941	18068193	-270355200	-252156689	null	-317903873	-1046875824	-836676737	-116612493	-41022939	176689896	-247416845	-224298396	-189915751	null
2022-09-01	-526244340	-604538594	-102504177	-275928601	-414801620	null	-578841788	-871221878	-661173122	-268481794	-151663575	86863529	-248219648	-466912893	-354554984	null
2022-09-02	-73266159	-328525816	-97177395	-195287952	-310090401	null	-347600719	-782863375	-495974641	-103427045	-100525221	134281716	-180349262	-191318346	-273911338	null
2022-09-06	-199528187	-807868531	-52325609	-264530879	-268299858	null	-403140137	-1092333905	-692597370	-308192568	-230654667	-127081914	-326806773	-211059419	-286594718	null
2022-09-07	404672465	-363212129	-157366520	-148960343	-66530076	null	-181574060	-553593312	-629032760	-114639571	-47200654	90976158	-87671251	-47660433	-183076701	null
2022-09-08	945063357	-114988561	-240067714	-84286344	27429776	null	56811280	-106551759	-471059846	-28507469	-117841929	-148606782	-82984271	86915169	-82034267	null
2022-09-09	938128758	128641126	-187389907	-31247927	231824191	null	178309021	271571305	-351112256	8254580	27519641	670115	-64766917	338525331	14975703	null
2022-09-12	1184278952	376420437	-312384549	-31693997	312015757	null	39101894	694419614	-178774264	93170904	-1977423	154567615	-77665219	226308044	-9763058	null
2022-09-13	941378985	361643381	-235413154	-32541565	295097198	null	-25602065	550030536	-283475454	-12411196	-52817368	155607585	-92398646	182568984	-35473802	null
2022-09-14	791986869	310777877	-192113696	-39684512	152149471	null	-210236992	668994850	-218178281	-97409908	-275012602	95323796	-300753379	179132003	-76513465	null
2022-09-15	464397371	-133001882	-133349258	-70163805	197187561	null	-378487769	585953375	-274655016	-197423538	-397998326	408689086	-334835763	-107520547	-170157034	null
2022-09-16	-254835545	-404024973	-49623181	-137066213	-16482079	null	-305176427	18995464	-95109250	107681549	-635478120	213911157	-636289749	-317793989	-235816258	null
2022-09-19	-373789	-41912587	-95252670	-90081567	-32118505	null	-147361133	164356571	-144176561	178720725	-372607965	161900808	-632824802	-463478142	-205484237	null
2022-09-20	143386026	126259843	-153202293	-81606610	-37736707	null	-22167653	502777895	140618199	310604852	-296023027	455898808	-593925162	-414698815	-209212726	null
2022-09-21	-168682352	186426185	-133083632	-110950985	23714401	null	115577376	144882228	24117245	225098458	-229056181	311517302	-489910256	-513334122	-158554654	null
2022-09-22	-262971193	311451885	-179768626	-104445661	-201581945	null	59117482	-323517196	77050597	269426297	-54626971	123344186	-289511620	-357417627	-171264099	null
2022-09-23	140694822	237070427	-174738379	-131531114	-216175102	null	-116059989	-376747602	-459979942	-274108598	-126747445	17344899	-209696113	-350045338	-203303591	null
2022-09-26	-196079833	-247033730	-179057581	-197722081	-421889226	null	-269663462	-515375213	-431142868	-351129620	-374164332	-66397712	-143200074	-323395857	-205486345	null
2022-09-27	-106415720	-206843944	-186370921	-203573799	-409094480	null	-259616426	-524008612	-482804589	-334488527	-352438443	-228841606	-95763384	-214513501	-150286498	null
2022-09-28	396996572	-80158078	-195907448	-172727915	-310788106	null	-205519577	-400002615	-442729928	-155299372	-131211990	51916359	-6222318	-218918161	-152589286	null
2022-09-29	360269639	-17096778	-48355998	-177513487	-298207930	null	-231662558	-359518120	-557182789	-167831360	-368382843	-11135863	-169231987	-272009708	-179845750	null
2022-09-30	378273159	70283377	-24023602	-158036721	-171987066	null	-179280645	-161055851	-468325850	7121713	-159344917	111499244	-88003099	-187041302	-155338171	null
2022-10-03	359804566	209263807	-16170861	-94715991	41868506	null	-17486954	-592361940	-420481373	26496137	59119211	241771676	-81599158	-71142156	-17392193	null
2022-10-04	885094305	589890853	-102625099	-7087870	229035987	null	77951134	-719978004	-454800034	156384065	137466644	92198801	63474289	16461780	39497259	null
2022-10-05	514037860	199953461	-106175169	-45001287	35683507	null	-91133057	-984579922	-460955023	-15479914	-119200103	-302117677	-96693145	44663609	-42984438	null
2022-10-06	377482964	250629018	-201280781	-56445118	38634563	null	7207046	-786748815	-358166241	-50238245	96259131	-151078112	67262036	147166830	53269520	null
2022-10-07	120717781	-56912662	-200609933	-90611668	-41741637	null	-44398519	-974408755	-245094281	-147735103	-103365566	-272200545	13314257	76045316	-30579297	null
2022-10-10	-223632768	-194865822	-135733142	-144713911	-187486518	null	-217866907	-648866760	-324460686	-277331913	-166229180	-240884229	-62108909	-143123422	-117664019	null
2022-10-11	-728991879	-457958658	-73714006	-212008399	-281481884	null	-275161309	-591810997	-242049170	-302582267	-272679292	-287995478	-124817740	-364357253	-106595191	null
2022-10-12	-904714047	-503274635	-44107999	-213496797	-107300658	null	-306813656	-508297032	-285691280	-284392521	-231981018	30772921	-1798842	-331460545	-90117303	null
2022-10-13	-282727278	-130809542	-249310192	-130364327	35122801	null	-181599345	-197067822	-163605550	-139268114	-219753043	34275098	-34447755	-241845194	-80662490	null
2022-10-14	-30899557	-124407220	-173488428	-147772627	32902541	null	-243905611	-156473995	-230674302	-97687450	-202742457	135160122	-8836765	-207923086	-13313662	null
2022-10-17	260272821	216672636	-182227508	-75792257	193355188	null	-50194093	-93239757	-132283219	276421	-151670905	209406727	169434548	16150113	24178524	null
2022-10-18	-57614045	64694570	-128686294	-114840514	169061174	null	-158025117	-181923297	-242218523	-101890535	-152497407	168995689	74332265	144512276	-28596003	null
2022-10-19	64325751	-113740040	-136517566	-157375878	-4112388	null	-36301329	-283740278	-203705498	-154339616	-118978809	37601302	-67562076	90343965	-54938666	null
2022-10-20	-410759262	-441237362	27149717	-202851748	-98168376	null	-10650634	-534895314	-198920858	-113404591	-195852680	-14281811	-21317324	23218068	-27463098	null
2022-10-21	473482153	239213483	-174783419	-89116771	81833600	null	176750507	-101007017	-103657060	13206165	-22726190	276107017	114554453	188534012	35879091	null
2022-10-24	435887119	167189164	-285678917	-84315780	40042706	null	158121498	-335039921	-119109504	-73569443	-84225756	-161288937	-5701967	233502144	-63135776	null
2022-10-25	1000493999	540121716	-371676990	-11475304	127255999	null	394976037	-94651787	71662863	56948818	141893707	301174028	137889636	276393051	45081097	null
2022-10-26	1648820311	807892094	-329984753	-1272719	300835899	null	436923529	217417983	120761495	132358538	196131890	541523762	97964968	344501033	73370891	null
2022-10-27	1851523607	636454229	-291138644	-24698131	444938041	null	242867426	60809629	28420768	-9269152	159602844	635331493	-52596177	339055126	18483486	null
2022-10-28	1144253828	606100868	-291217176	3408764	450633139	null	256365368	-41862232	195355679	211164243	113208675	282760026	-17887757	328396539	69326373	null
2022-10-31	839890064	95697654	-131386150	-101404862	284967802	null	93036614	-53527126	-153876599	150248864	-30594218	331536396	-92848478	126444116	61242971	null
2022-11-01	605292240	-450035049	-30259194	-188429044	276187821	null	4232087	-228815265	-393509074	-149997539	-73033194	16389398	-248862899	13669131	-15124377	null
2022-11-02	-81387921	-665475212	-14073385	-251962374	128211539	null	-30449140	-540864212	-402467639	-206013730	-188706618	-437380895	-228919182	-21327393	-48820491	null
2022-11-03	-269771054	-518947119	7282671	-243756481	-66054073	null	136990600	-338781127	-490005356	-200670519	-196955625	-576827157	-300225441	-111331954	-25934623	null
2022-11-04	-435619740	-585571330	12295524	-303466274	-49452416	null	155118016	-433769465	-716839925	-409843899	-173778634	-654065871	-401581425	-94365460	-84897442	null
2022-11-07	-109516005	-139247157	-59455086	-251951477	88417836	null	210451170	-501433013	-498252659	-387846727	13288380	-627929085	-243934066	50507792	-40686038	null
2022-11-08	8564765	154689358	-90494764	-227033569	109279585	null	164655088	-525712335	-151516300	-184107483	-103771962	-384440600	-92208890	193526050	-30596924	null
2022-11-09	-276929107	5752000	-122824065	-173959131	75753240	null	29348869	-614569270	-216679290	-179484920	93721526	-335240699	-40592536	85151339	-41790424	null
2022-11-10	148013699	327479394	-250609675	-78460007	329554500	null	31974852	-666503545	-26137516	-31895243	188803428	-147640887	135900738	306005503	-13019974	null
2022-11-11	-99123536	17643267	-240154774	-39624237	299357265	null	-53505674	-531520023	-17314590	-51503387	140547449	218757858	201699297	295162453	10501970	null
2022-11-14	-222302532	-64581540	-248105718	-36773008	148481466	null	45638456	-444781699	-434311	-63576278	169463367	563664398	85147477	272741092	3032	null
2022-11-15	-120279849	81616012	-278221805	37561095	165399887	null	74511412	-342912362	-259418359	-133735368	275926363	623451200	84270914	293706921	-22426030	null
2022-11-16	137305133	91302611	-275649795	30458392	332883024	null	102139634	-268993828	-182621223	-118623763	82471627	584225563	197559194	291681969	-15912444	null
2022-11-17	-258604663	-185830590	-197910666	-79195274	94819291	null	-117647810	-276805525	-248856982	-255444956	-39138066	188677078	92718848	105634565	-7872887	null
2022-11-18	333503712	-412849626	-98982565	-167541090	93793754	null	-235905017	-530792845	-70602519	-333446420	-59825159	-153497940	-91121222	64677530	-101147301	null
2022-11-21	302432461	-747849732	5560682	-238632771	257830127	null	-252195981	-673559637	-209398776	-264839971	-276183687	-491191277	-77125620	56128875	-143930465	null
2022-11-22	601104128	-744234358	-29855178	-205392374	225796820	null	-178242263	-605575499	-21162187	-125136414	-239035933	-800878626	-141830788	27389195	-65797751	null
2022-11-23	865096672	-134959947	-70087989	-99999065	226362570	null	16011063	-353641199	128651134	-3844055	-38813501	-541305100	-112578866	184529578	22340637	null
2022-11-25	847607617	-203021218	-24806935	-75248805	337662676	null	90623341	-357201338	-4368132	-35984834	-37623213	-429884854	-142597250	215937836	-90649484	null
2022-11-28	230275413	-188660100	-2025599	-62718087	170200784	null	64749176	-250921019	-249210352	30024023	-124410433	-325207903	-139095657	49101568	-84495167	null
2022-11-29	-148205835	-225762328	-10615177	-46093940	196833202	null	-102886123	-163386929	-246008560	-69788297	72840551	-317828643	-180258684	-11353016	56202197	null
2022-11-30	-459482407	-335781188	-71784733	-28754458	82323732	null	-65637766	-90717629	-247309816	-89933121	105555805	3286860	-105011954	-10895445	-17795206	null
2022-12-01	-646725091	-506678727	-80432662	-90066187	-122900649	null	-159307741	-298250306	-404910026	-152766014	154081516	150017637	-103060756	-154829745	-117513280	null
2022-12-02	-390329034	-419218793	-109382326	-99235600	-244346331	null	-250540588	-261718661	-267921413	-181134863	339415167	414000010	-106862696	-202175688	-130160146	null
2022-12-05	-543538657	-426608187	-124109808	-128758496	-285710883	null	-256515171	-382087774	-239401638	-306988278	384533380	286232522	-42399712	-184833578	-155519387	null
2022-12-06	-348988197	-370868142	-124307836	-148825644	-489996874	null	-255863719	-294870812	-234413634	-287365795	193412779	229968629	-65989071	-245023848	-293391009	null
2022-12-07	-659801155	-729020018	-14923487	-265159639	-474582123	null	-387272051	-558771743	-445942565	-380613203	10455040	109783850	-246646185	-406775272	-286415361	null
2022-12-08	-324144795	-590008303	-34981361	-210836415	-322204721	null	-284277980	-499804287	-282881199	-289886555	-24219537	-34904722	-428556578	-219644941	-225333596	null
2022-12-09	-811114452	-600581355	-34897217	-211963538	-168230747	null	-17899800	-431063592	-247239092	-265245484	-20837460	14105269	-362410563	21820951	-213109330	null
2022-12-12	98655150	-84930192	-136866344	-104268106	52011025	null	276939323	-545816402	-75443670	-211451023	-54007155	-9150979	-420082464	179038233	-49123592	null
2022-12-13	310300749	129859608	-112042690	-82958036	242261019	null	393979800	-861434620	139619729	-199797529	134515352	399026535	-239399768	452432629	39195609	null
2022-12-14	517568611	566438475	-115202252	-51409570	266100919	null	256480148	-677661693	356196860	-197501109	283278715	332959289	-88902025	681110230	-28663842	null
2022-12-15	-79115326	147254640	-5329469	-147526976	131187954	null	35480752	-569937211	105213962	-294613592	58031425	37005826	-26120161	412489427	-73283641	null
2022-12-16	-1031781049	-187186282	18399091	-149382879	-55733525	null	-238571894	-636982523	261859367	-392369529	11471054	-26533494	82977456	76470284	-52132177	null
2022-12-19	-1646142210	-619901019	123329053	-268742398	-258038729	null	-527708940	-440577987	61696978	-440155611	4071260	79017793	100337199	-112727724	-199024556	null
2022-12-20	-1117320276	-460708048	13249108	-226867777	-233700892	null	-642492642	-362440085	-17324810	-274960365	12974744	-272025762	24064729	-433037896	-153215256	null
2022-12-21	-821888083	-331768470	-68779880	-190403129	-153374818	null	-390394712	-481910417	-21388284	-156791045	22369961	-185286659	35224830	-443836208	1821254	null
2022-12-22	-723200595	-447695969	-106824509	-179985648	-107832813	null	-409056262	-730712350	5080960	-240854779	54202778	-128394778	-33533793	-424735056	-29849785	null
2022-12-23	1266131430	44516554	-186635940	-155126252	49028099	null	-303478733	-695129737	-313039356	7143883	62454458	-385649117	-56078986	-305106725	36333099	null
2022-12-27	1169430269	115807310	-175157159	-121863532	172828107	null	-288193391	-816985775	-320658373	41340398	51554856	-424469918	-75342864	-130109875	32505486	null
2022-12-28	612260619	-316284208	-94227547	-185258905	87441055	null	-221939075	-447680305	-509503703	-133358486	-116431607	-443449135	-151651639	-51891206	-84460240	null
2022-12-29	788847687	-413796864	-87004351	-140923143	76617743	null	-255917096	-371105434	-586286772	-143200954	-93392227	-351392424	-116350520	-107905614	-97908157	null
2022-12-30	932095041	-154696263	-91216649	-113374119	66415100	null	-232382633	-167239784	-588043926	-102035810	-85123447	-225504081	-85035365	-25130628	28361244	null
2023-01-03	117239208	-521566081	9161007	-149926047	-51165843	null	-307718338	-346017975	-645206421	-158703578	-66721403	-257937170	-72122474	-20317126	-86400278	null
2023-01-04	396561450	-295829322	-41032925	-95498457	44915906	null	-94686225	-52262368	-515988417	-168823442	189443252	102489994	-56326184	11990360	16689001	null
2023-01-05	218186683	-355521791	-48246206	-67756833	-93712824	null	-160888242	-114167552	-425478299	-172496467	216038110	347531250	-87024569	-11936638	21372928	null
2023-01-06	153557853	-359773275	-106325195	-71300178	-63765690	null	-139798002	22333058	-401061166	-165778637	186912721	192804732	-243365785	100074195	-55151022	null
2023-01-09	240358570	-188409117	-159281751	-20342494	70906517	23658391	10937485	14741917	-206536941	-9589318	376673552	369741023	-102064151	263912912	-48754208	-63074159
2023-01-10	637156205	223923213	-264809142	47089417	199133768	80844499	239267412	154185706	-44911769	71635269	402949481	772847435	-139215314	101730804	97337442	32158133
2023-01-11	726125520	342075900	-347275037	88588441	181069566	52957149	47527531	35975373	14212896	261225870	240298309	363587225	22186494	-29381875	111071245	166980805
2023-01-12	1300589176	693375849	-404658420	157992599	393708375	95803939	230961034	5868030	57950613	278138923	379184190	23563393	11198386	102026521	168128466	267096226
2023-01-13	863384250	482100623	-306360035	100756208	302211378	34743004	209417588	-91003503	15955627	282235458	397627803	141406940	71514433	-208151079	112616547	151947558
2023-01-17	1014477266	510719258	-294772569	106086208	138509915	47335438	304324892	1986528	3215626	18746134	147328556	-194457973	-120593933	-325617933	156789221	122404370
2023-01-18	536187409	171322094	-151300156	39429272	-45167687	13494016	123670078	-177670705	-45466194	-77337409	-54619747	-585771747	-249857939	-125301781	35150073	20372810
2023-01-19	158457121	-223728927	-33325414	-48104637	-267791860	-42787715	75558680	-247440674	-98423792	-278849283	112060293	-622190150	-217361742	-205905245	-88019148	-84801091
2023-01-20	-384987184	305711346	-85449655	-10477927	-261174164	-9597304	235372908	-134872000	-79990396	-185493654	151881947	-243462166	50106187	-269982354	-42664000	-13807418
2023-01-23	32330690	445779524	-118396684	66745032	-125446151	76433647	338228084	-52886963	-43478983	-259207166	166776064	-129164708	174256390	-33935433	101806086	128397395
2023-01-24	-440031696	151598317	-72249647	13937652	14413620	2028890	201765315	-168836775	27252392	-135717532	352676240	311684455	213294094	19836865	-62929014	3763956
2023-01-25	-365456057	320929645	-165132650	83325567	165447098	26419919	262613113	56620981	34835985	-86963304	296822403	353137523	161313791	11277360	10152785	-6361334
2023-01-26	138684836	701667797	-259582976	168337852	327249705	72998747	484614775	78814091	43734735	45090188	270673958	375819322	117891537	271473565	19518624	120957790
2023-01-27	614030438	401025697	-249233779	148879272	290460607	61203956	390690342	370297420	207247783	119296694	265248717	34051032	89721656	176725353	49057172	147157785
2023-01-30	-57173348	-206128810	-113406071	23665830	115475381	-47505077	93827776	-108793165	36196937	63695449	-36127700	-365556847	-148358246	-33279580	-118282108	12837915
2023-01-31	622568892	83422093	-215635161	89417558	129510602	41284224	165489163	19582671	-23668937	226288109	-34696240	-558301461	24421234	34717742	42512171	113828409
2023-02-01	882716265	264148429	-266798949	117582011	34661467	83159691	312273416	50088908	-10840513	163243506	168181810	-302110740	119981492	182996553	97982941	231257309
2023-02-02	858017674	208029864	-275459523	122009548	45006222	118878690	308058760	52476130	-143038407	124505189	119852970	58306747	129654747	159046218	214375100	275186408
2023-02-03	204391645	-456957135	-215167550	67219487	-62907702	93472578	224009487	-255722844	-52486969	28293780	107457079	375333909	114078812	180436206	153445930	139653740
2023-02-06	182490550	-72716175	-283394765	115832172	-119593503	113765995	464918718	119513650	-90572016	38427090	359552215	332994234	144912439	339857792	160948705	113728976
2023-02-07	-125837770	-134098313	-229377225	94637236	-127838710	99298068	539905752	32328267	-135626735	-112333386	414662866	151631181	97221834	325451817	84095796	32555297
2023-02-08	-713930776	-512805236	-92058558	-14036122	-87871518	6214613	378114877	95113042	-213444522	-248795808	194903282	23558875	55879942	127394956	-28812302	-46027787
2023-02-09	-1324534831	-882283827	44751297	-149456841	-192184765	-19863662	355718047	154640562	-227566461	-328817169	-32267077	-57716325	-131418259	38158509	-148499049	-88905209
2023-02-10	-1077125845	-721378971	83964601	-161610262	-177371114	-72186174	113427906	-169671878	-626442471	-403706653	-264738883	-412715904	-270583235	-19593753	-243982096	-127289233
2023-02-13	-494056884	-193669478	19912152	-113146912	-26024664	-5436300	137694581	-300646857	-328450996	-219314170	-205953218	-72326696	-216662034	15763387	-92158689	24296122
2023-02-14	-755226053	-487298503	17181217	-122793781	-137106225	-14671711	163049029	2523224	-510928151	-252928444	-307176056	50325845	-314721863	-98477351	-27810667	140012221
2023-02-15	-216760266	-36103364	-116323629	-34982997	-167673502	52313830	7896210	-83424048	-291603457	48078822	-282818215	-30078277	-122049154	-14501671	-100360103	228873275
2023-02-16	-251665836	663459	-150495194	255274	-211799834	4669736	-211961749	-245996325	-162190813	57800794	-282427388	-280347513	-46661754	-126546124	-135454748	71399368
2023-02-17	-433988579	-146882720	-158947126	-6790532	-253876736	4666341	-190742858	17364508	-232715654	64467576	-190697410	-221169180	-105725346	-77914970	-150049379	30206018
2023-02-21	-1266721905	-764035765	-14759613	-106175353	-416682396	-77238107	-499228986	-89444740	-551818447	-190061000	-446990457	-604057782	-175710895	-287836688	-315194328	-95148654
2023-02-22	-894141378	-632328715	10631650	-134269949	-379847041	-115207031	-599605368	-487484381	-536576070	-84774284	-576472903	-652172102	-127065573	-385184507	-380926084	-145079851
2023-02-23	-1024212094	-1214805726	63279969	-207857538	-316342499	-135847768	-340296547	-647230662	-834459628	-287711697	-416833152	-897892757	-332517720	-329362781	-301867329	-229640367
2023-02-24	-1023378339	-1333641448	100618450	-192294509	-285964038	-130272446	-291653064	-537288928	-1004888151	-274010809	-381381987	-903776638	-383050093	-324577311	-287657327	-209025852
2023-02-27	-606665197	-651170737	44536587	-130262157	-149244113	-49768326	6031164	-497409937	-624886619	-280264835	-431372176	-564601360	-188426380	-122371055	-148627373	-26149347
2023-02-28	-10517323	-330836237	-61482541	-49693486	41560626	28841248	243325013	-446010089	-360893859	-78132680	-128446199	-303513764	-10732193	74353992	-19472069	1403390
2023-03-01	-566757812	-623364571	10545660	-69931915	-15402501	57159920	23184073	-477177010	-379437819	-208666342	83317690	-338568335	78275963	151654760	-86735857	11433584
2023-03-02	-329134194	39625103	-65320701	34186582	-125696833	47753967	110962085	-388992108	-218255113	-174777464	120053257	-157738323	269412139	83920726	-57529593	-102426823
2023-03-03	595574006	755622484	-229173790	144159750	41129895	104315409	347971891	-229329436	42803870	-36764489	444047578	191306342	465829484	422051378	49123800	64411946
2023-03-06	601734576	564638132	-208296537	127045196	45468505	62649497	88605817	-468983512	-40037230	32786796	631920654	110367083	488372902	439709734	3072052	65243754
2023-03-07	39350155	121637337	-122007180	36243853	-191397015	-16843517	-7776882	-448223344	-258181522	-24278143	344227205	-33661903	309166435	247600621	-7359456	52195161
2023-03-08	440926090	277162097	-222875292	76048356	-132515520	13965764	273910368	-500131344	-47875914	10102060	138505656	123578496	310782671	415936087	126158325	461205
2023-03-09	-80692797	-106064904	-136021998	-17601040	-201770520	23573642	39051981	-715622744	-41774092	47915581	58504174	28988187	230009759	425172009	143715186	72697468
2023-03-10	-790624030	-697312775	-15193850	-151398662	-411460382	-31040494	-204305070	-823496231	-217080930	-71095490	-109161455	-276182897	59907035	44956046	126640278	-134880828
2023-03-13	-1066923685	-751752546	-42054114	-156688227	-584230820	-48037555	-193313021	-522115732	-270978458	-38689673	-376553669	-280005675	-38986428	-960516	91550275	-122804891
2023-03-14	-410183919	-360780116	-168845187	-88750124	-224724822	36771621	23175164	-334267740	-101561553	8480234	-97182409	-156934765	106120814	226828432	143487727	-53156829
2023-03-15	-497420918	-368489029	-163380182	-129665390	-400083807	-53918544	-200250875	-220077033	-244433580	126306391	-16283693	-32307255	58580991	-28279590	108029876	-95122350
2023-03-16	-30676562	-423441059	-247657690	-50062612	-77789035	-928678	159398975	170254030	-163837338	230543782	-62900920	323739951	163434522	82239115	184531480	-60988984
2023-03-17	889068845	-403833530	-261079154	-59155604	-99379061	-2814189	525207851	140986285	-648640246	305704831	-205177223	343040812	179941980	32856547	144957796	-21478085
2023-03-20	1092013743	-215337262	-266738774	-54900476	129015695	56458070	716557464	91788351	-546309643	206794665	35489898	305321910	210755332	103277609	99616977	-156969629
2023-03-21	876941946	44656671	-246533514	-31607506	66203269	234213	492105040	131275794	-490431191	252648354	-287385510	233498051	266835389	-167243714	-52063087	-120254035
2023-03-22	701472007	186410392	-261726858	11974955	153726203	75518512	648292049	110927017	-404052165	111056100	-141258945	-119763299	295215344	72819681	-48835294	-114697526
2023-03-23	834230468	304237540	-217184406	-19480108	20431175	59050760	441447327	11915376	-441369202	1558550	107797793	-34531603	262423957	114335349	-107048141	-12549302
2023-03-24	165526788	293043712	-219130380	3704957	3567373	52071217	12972450	82243768	149664523	-110511953	181495768	325958703	280265811	189155021	-157437721	-702122
2023-03-27	196220263	-121654323	-125736215	-69678390	23697936	-12367654	-244563554	-13629339	-153218297	-52436811	-64785799	261345008	124908120	-32314020	-131295872	29268986
2023-03-28	-48500170	-655804931	-5525758	-156101432	-176524868	-46527287	-421640857	-216423099	-406652053	-254157614	-76624682	215069706	-80891858	22869356	-142819391	-22283965
2023-03-29	525516423	-341204013	-7525554	-112435281	65107971	-29128506	-349332372	-187498612	-254057991	-35909256	-2155596	534056428	-239369160	51129323	-143291208	87238290
2023-03-30	333834596	-215765718	-16850073	-70882392	-4844772	-23391418	-251656913	-81442183	-176559290	73130916	-37527705	449942068	-435828030	29842425	-129340486	81440623
2023-03-31	838808720	351545850	-88434679	49894180	262866056	61788026	174213072	249303712	-45573944	241731388	185286215	371098576	-290715313	183767078	-100785518	249652388
2023-04-03	990448709	413666541	-95360292	94595790	147462190	50226847	279226347	14423911	371981693	243466482	223133930	524754642	-262753197	228347470	-147557050	205913434
2023-04-04	940391481	454035805	-118969892	121021565	95763044	50455987	312768164	-6254201	390877455	447878013	498004559	488785608	-80708835	240245822	-130415159	303344867
2023-04-05	237861583	113387157	-19532238	-1927117	-143292467	-49177438	-872055	-215891811	64689810	204534701	127662570	181380143	-65590662	4432254	-243655250	160121147
2023-04-06	492626085	182248476	-25972525	-40497282	-17090467	-78095115	-33710179	-329333486	63443248	142930809	65490050	-140152018	193806600	-212938171	-231317810	22926163
2023-04-10	-287627310	-504883705	62946171	-167847612	-145662905	-81283032	22498466	-651852998	-164752646	-66233437	-279467227	-379672892	-26751778	-227293412	-53273036	-105712854
2023-04-11	-563820508	-619717852	83218034	-215490892	-30517739	-66418672	-96358811	-372772064	-503020701	-121727931	-115521210	-397914253	-66977563	-289276891	-54426894	-167777153
2023-04-12	-149323835	-474646176	39397857	-219133574	131778877	-62700392	-175486154	-454894303	-295527461	-392235087	-98187949	-396549379	-180291828	-228473656	-88021232	-194029618
2023-04-13	731071996	48774332	-88474971	-68885228	346260533	24349409	169310674	-61939435	82407101	-180545690	303794039	-43525120	238928	-38394671	11606254	-37048815
2023-04-14	244552726	-428905587	15142022	-132824174	388084520	-30230374	105162985	-111392241	-101637253	-319327223	175417496	-68126517	-73026345	-33022983	-116418992	-35506653
2023-04-17	390083630	-363066660	53413852	-131927155	429542352	-112658658	-212592125	-249756406	-159427386	-283842628	144863489	-176781881	-75046911	11043054	-294018624	37738185
2023-04-18	312527715	-256767855	24364682	-124424961	309470016	-61582280	78968565	-412792276	69151807	-324532211	-56959588	-261901457	-66367969	194424845	-161939775	146683888
2023-04-19	350886490	-97785081	-32558066	-54621741	273678611	-63788009	525337539	-208862158	157471306	-75825181	-321405508	-385623913	-28998853	215548059	237167	23491913
2023-04-20	12489953	-281538053	5792545	-120314533	52369846	-69069799	271121521	-594340480	37237121	-107650912	-633437538	-374189744	-24403941	108633671	39599285	-96673939
2023-04-21	173764331	416735169	-46479704	-57944301	-140974315	-71515636	24049997	-518232533	-73364760	27570117	-634389698	-195220079	-112101811	109919566	2810656	23349941
2023-04-24	547025938	742189937	-76691245	-28933252	-225823971	-55152651	13828271	-449201779	79332901	35376884	-500598421	112900279	79744442	92175589	-39069590	-92363974
2023-04-25	197790588	582867754	-30303155	-60768232	-368175946	-130745587	-292722465	-270972702	-3651066	27394107	-555125508	-54399930	69420517	-96522010	-162189650	-168944196
2023-04-26	-164661636	163900576	62073743	-142567315	-497086077	-97986219	-281192959	-477993727	-296182230	-190358001	-221192159	205307402	44751127	-210078295	-172050370	-13964960
2023-04-27	267295948	-21135257	18047398	-81388291	-270021739	-167973328	-370741674	-116436878	-209088883	-248941322	116528397	84179905	54404155	-248941750	-173488591	41815250
2023-04-28	828099023	-238528248	-50153411	-59682735	-53893553	-97007158	66645164	-77980800	78467112	-379625168	77703231	206233579	-43305135	-106719077	-24595258	-99162992
2023-05-01	663168476	-489048176	-49638037	-62883540	50728251	-32115337	311703439	-178603090	150867553	-442169328	128788128	-83642198	-142628632	-79039371	151750359	-98129163
2023-05-02	501205241	-645128523	-15805840	-73523190	26220481	-20004306	306878566	-323924220	-62688775	-215688953	129239459	-72097109	-180495435	-182765039	237026155	-50951838
2023-05-03	798579270	-267270813	-67936108	-20914900	154069904	-6150999	-64623194	-153457837	175889917	-19461693	-70530189	54660054	-71820984	49631966	81481074	-147161848
2023-05-04	102151830	-621072794	85042982	-151488077	-65880776	-3628890	-111454270	-331804854	-39536832	65366222	-391651525	58873774	-267235859	-9086556	127199272	-54976261
2023-05-05	-214145660	-388682770	89336976	-132265061	-86856119	-856968	-180744099	-206139315	56719923	246770968	-415273993	60292022	-73192838	63219399	185369708	42604889
2023-05-08	-595644625	-297698831	48266252	-92282042	-47415999	-26910718	-252204014	-128946003	-46900335	365956675	-398391917	399060786	67236572	-118682650	234642167	166952498
2023-05-09	-443502629	-67389280	21598755	-58955431	20270098	-32795323	-241031119	-97314430	-19049832	398495714	-113521111	712878558	264623000	-24438501	296002319	280206314
2023-05-10	-527690198	53983672	-2963350	-38172135	-100472350	1862198	9782698	-140052502	-38655440	385165845	-89666982	628348969	304104750	-38362436	415755570	367952305
2023-05-11	-888506354	163935856	-64608959	-6486181	-106484243	-1464397	-10862943	-8588592	-4971631	367663145	171379185	706550760	438839491	26212930	290032748	202441484
2023-05-12	-1571872702	-701873294	81939080	-153371178	-292472047	-71287373	-463957234	-371221525	-355849570	135236862	91778332	446214557	441703039	-69862756	106348679	117468788
2023-05-15	-1583586372	-643776901	86820935	-165071183	-291866724	-39102245	-413365275	-444286603	-425709068	165274336	306179309	166616971	247649700	82257346	26176528	108659723
2023-05-16	-1559207537	-299958760	-34927693	-58921617	-305010073	41336442	32052869	-270400485	-121771087	109106738	89824087	-144305059	310518492	274547656	88295651	20619534
2023-05-17	-1320134045	-121320007	-43192521	-26426983	-97125865	56669461	192790440	-4233758	-279505387	131617075	295898094	-100835428	217778530	310799418	138197639	-27037386
2023-05-18	-126935083	360762204	-106444846	52681065	-10460604	147782394	604281590	-21606093	-62454756	209131499	266275154	60929935	282865505	520643814	263631412	157586622
2023-05-19	846019501	517156885	-147951954	83877202	8245810	142666440	641144212	229449671	139275805	224229599	209209697	-39502335	143628750	630722596	252932268	111247110
2023-05-22	1680364403	913869721	-204747864	154923014	444156	135722527	549998475	454810843	134667081	55309787	263420506	88725901	313298131	446104239	330471135	130491145
2023-05-23	1531434506	351747230	-72268690	11099288	-13715251	56874774	91676364	264506193	-135175697	115030325	472987193	-8166206	38004644	579226730	287523189	134219078
2023-05-24	915754213	-328400991	31227945	-134943665	-255205561	-37267157	-313189514	-16181614	-121220534	118800219	330401231	88427966	-138837639	270204411	244264398	168871343
2023-05-25	274800648	-531595774	32946475	-139129849	-208481498	-20888132	-525142009	-156238259	-261593992	-169424986	423536682	-342595793	-184380026	438046944	232734389	-130521375
2023-05-26	-21857825	-80113502	-69173779	-23063458	-49886066	81651393	-227285273	-88158264	-85405078	128886257	904889437	189406458	3076190	817657316	343488770	95365443
2023-05-30	-851109652	-569895253	19370175	-132233761	-252256074	13553940	-228722020	-275836590	50187371	241258186	820988196	419786136	-81753987	1318504161	90242160	132436319
2023-05-31	-1038335864	-595506823	-23867487	-114181120	-304390195	1492825	-274257080	-69637705	239609574	-39896948	772886474	726587682	191792254	1392746206	-98562907	288967052
2023-06-01	-152196924	-10509650	-124536157	7090941	-76893195	96766104	55793480	46836627	458661065	16200819	893827149	772208397	484308597	1007754324	-85481535	250816562
2023-06-02	389129075	157771092	-113159960	10459321	42665380	-30743903	-301266106	176095749	476201694	249127101	804555651	786390495	510135312	1103430073	-256493934	575680373
2023-06-05	136303354	222765601	-89586295	-23672199	-169987910	-141243253	-200285558	-47199663	192815053	186196312	761215998	776790888	506608037	340837438	-210277689	575304041
2023-06-06	526391255	221575655	-77552935	-52441591	63071646	-65284055	-563821321	110832848	58892150	384147230	779158985	324675440	589040639	-370486363	2030224	555385260
2023-06-07	1086157207	314526216	-58787166	-73955014	232249185	3669190	-479105635	-133896576	-41265043	420641471	553139082	538774668	458408873	-460041838	1497921	293591326
2023-06-08	983821290	317609466	-73206867	-53929931	65283470	-2692499	-482342656	125281226	-93096696	376099333	466912300	506759085	325629631	225312117	38175438	304919960
2023-06-09	530895921	209806148	-58207057	-104371780	-31473528	83379822	70595447	-116022521	-52604642	249731274	414015432	892551028	302777409	-50682908	213437223	99464917
2023-06-12	897798362	385253543	-76049705	-50848652	24298186	193738971	-278181854	24645446	224936851	263022750	457886349	600460509	255210584	581927014	155103370	-55380499
2023-06-13	866823597	683321132	-129937883	8467989	14631947	167805512	98046750	52033822	366740124	34733560	304730412	1094682927	46411618	652193398	-46090221	-124943611
2023-06-14	1190532162	1082730663	-217803178	106951554	20275602	164239127	609999186	-66972588	488115079	40461421	644248372	1079871253	-39467896	785854778	-37143234	94643953
2023-06-15	1043495313	1255844234	-208489839	121202954	176183661	68697015	483457648	-429735641	520389705	-70110822	769119138	1096730306	-9315771	379860774	-164337220	161947545
2023-06-16	82969537	1999087494	-185313902	71767727	153344746	-23465400	689615924	-10588252	840973038	72469486	1107571541	476738807	-27979888	57486401	-495364981	113231646
2023-06-20	-804123412	1499122929	-119008424	-32410351	127534431	-131613806	1174186371	96162739	776120406	49809476	951837235	668964397	-215902915	-213362980	-583093808	62747443
2023-06-21	-1029304383	877961230	-70993959	-99389847	52149780	-209790669	737911417	-490427546	619496313	53825081	630758933	171122486	-214829975	-131917209	-531546355	-44878514
2023-06-22	-698049840	1234673984	-102688418	-35020073	-53746400	-175497634	630208293	-77971102	784167569	304659334	629271970	-308013670	28662300	-685921190	-555160505	-66749910
2023-06-23	-1258752122	398370764	-3683950	-172876370	-69655293	-168680053	366111370	-252843181	778601114	362028280	430519311	-696917080	-118474531	-709434431	-548604156	-176026314
2023-06-26	-796781720	-698914534	33383764	-203886929	-81200612	-69791420	-300294799	-780602219	199575077	94916101	-268814550	-475900656	-262021228	-366009226	-413864281	-106445082
2023-06-27	144977921	-329574572	-39359221	-123348061	103732555	31629487	-452522412	-808165189	234266002	72883842	-93688108	-531594990	-82082135	-292588249	-264627269	87237650
2023-06-28	263411184	245210362	-133433151	-12815884	-22667538	118556418	-38645172	-244417201	535258868	134267689	50072749	-77050896	107094162	-132757608	-128560326	323644473
2023-06-29	118116949	-765658481	-18778912	-159333794	177611032	21997005	-543754660	-464210805	445479516	-146649791	-297870800	-82536950	-124870623	258471737	58503582	135873251
2023-06-30	632860907	-301008127	-104358335	-32054064	201410733	126081428	-132516644	-117312531	349865842	-42932798	-76614914	330468280	112330903	719081857	157498105	220132644
2023-07-03	883472225	-160879511	-106297155	11448262	238718077	105863558	206284680	118766266	331247005	89398090	147238981	282684062	201696911	566121724	297735509	281841914
2023-07-05	1018199184	-126468569	-103203348	-760635	182494240	-3223092	305119135	128728869	19401359	188404882	174255804	8131017	279871990	245981599	153221216	69491619
2023-07-06	359275801	-671551853	15893584	-111732909	181941009	-86721300	-82747244	-89110309	-102363223	14601553	67557032	-448799974	51973555	82246906	108076555	-157668465
2023-07-07	236106711	295961219	-88758163	37144949	142016142	1867409	438291631	-142491694	-156443527	286132325	401253009	-148180090	215214553	-9013507	160179013	-4196415
2023-07-10	636580837	618141593	-89034750	19334371	137044092	-6436032	53999754	-382705285	-342661735	61795399	309333986	-264318738	-25314340	86757719	114609917	-223655823
2023-07-11	1092960430	787112765	-115439270	70427830	178630237	-75352577	-7743527	-353664670	-431946627	203829615	621147625	-319767805	57114802	6778729	-42525020	-169089633
2023-07-12	966042295	828907701	-97902025	70705650	239073673	26423303	55903070	-547108677	-86036832	160297433	556142547	12042680	19008845	383214349	118680833	-62332275
2023-07-13	2120222284	1566065198	-210982186	234750278	408497904	134130279	808350107	-309337978	-128923672	391035070	1004625531	387323178	289217064	454467046	56073708	147021374
2023-07-14	2314867671	1224139301	-188590606	191888297	248462694	66194911	449770631	-1291070	-317543768	433584263	667143071	135778680	352151269	446893665	-45823706	81014391
2023-07-17	1879785661	1036326552	-202212201	234748625	245493502	76463154	693833213	209095920	1703168	442501916	604435336	231989123	357612655	424388424	-11780677	269347688
2023-07-18	1565157850	1101407308	-207474811	241309438	265352757	103038664	936394810	311051667	70433887	217610180	336149198	903125810	161485422	232389141	-30701064	258342893
2023-07-19	1778398890	817666149	-162709365	172577929	285970353	-6754087	435755644	142743361	-71854052	269130657	443166801	848890935	6326376	-213164246	-233136559	235535686
2023-07-20	647369199	336110289	-51125105	-24781464	328806735	-122939782	-365186997	-480355911	-255307531	84111378	-7812742	277596166	-185406086	-274418312	-311868782	-9927139
2023-07-21	188729642	237058169	2449283	-102009915	343532812	-44463450	-373206006	-728355728	-372292764	-131535649	-90042829	22275944	-221547973	-72672039	-249027715	78843638
2023-07-24	630552366	3504162	97246280	-248704965	349668414	-123009121	-121903260	-712521716	-215875477	-243809883	-501298920	-535797271	-20339161	-196835030	-294270195	-54342397
2023-07-25	894905340	156245514	63803657	-210960146	153826185	-38288353	25180883	-980176337	122319884	-12274381	-226109715	-959470083	22360034	230425648	-65969049	-53951014
2023-07-26	-88788595	7473724	111162385	-261589929	122009097	-27671741	-77895388	-852764779	213032235	-121314351	-734788797	-1335166335	-74024750	242992922	-40562275	-141329976
2023-07-27	248937943	83839195	53099861	-185849210	-79585804	79673813	366054941	-688630196	301138958	29720675	-810579170	-1039389983	33898189	510849345	101855854	-10027038
2023-07-28	922136636	393085171	-27482076	-66456696	26822888	80751005	782603701	-490578822	596339196	186165893	-129074845	-393526670	58914667	369498795	71934738	22409933
2023-07-31	377864956	803451005	-85091102	43241510	6163088	134400213	245561105	-524878492	390791073	506270987	-142443058	131021890	-41407847	134823024	78003226	146008865
2023-08-01	-496153244	342132779	-12596465	-55143575	24230138	93603239	-381335834	-508975667	-9644241	135690765	-245808692	226098656	-74104946	142277645	74796626	21873493
2023-08-02	-573476585	-41403175	-29972972	-47294020	-154184228	73650728	-445548354	-548828379	-373907864	-101942101	-291055532	250612476	-75337599	101924795	39348945	46062494
2023-08-03	-182710111	414210905	-79963092	32097813	-77510932	57013898	-178108580	-92577540	-219905472	-80159724	155197241	586314776	-16453168	-105745819	92568002	-92078482
2023-08-04	-701997389	191944825	-20366565	-70477964	-51715921	-7188591	-383265554	-364122590	-656562618	-333914873	-123919290	490139780	-113857658	-296960246	162755080	-79936724
2023-08-07	-491352854	-479928287	38508592	-156633482	-36225362	-71205288	115778083	-482040030	-956834237	-403507327	444210756	445542185	13344893	-91513764	196829712	-184181947
2023-08-08	-479814683	-630111858	56012436	-195300537	-46446900	-142583112	99861432	-295692488	-717455356	-298776922	22599898	150887589	20869158	-394174727	-21479995	-271846276
2023-08-09	-462884535	-506003570	72531243	-206542036	-28768672	-127332989	92471418	-257887208	-577964416	-286991524	-27986316	214542948	40585810	-386787204	12135750	-219581397
2023-08-10	-432236752	-1532389876	122887567	-301470035	79410730	-190392692	-515650295	-361446819	-636416873	-460548997	-236065860	244528614	40730913	-318726123	-89556589	-54496770
2023-08-11	-554912866	-1796094885	151941094	-306108141	86071097	-216850353	-984531668	-371703886	-377800790	-380912090	-599280429	-64744552	-52173657	-423287952	-320596363	-218445792
2023-08-14	-732036153	-1145975183	47208028	-202112337	-65489652	-147233189	-836782785	-248819169	-35677139	-320553386	-880307859	-68789764	-154551767	-391107060	-220464153	-234756953
2023-08-15	-540329030	-1351758814	61394554	-207488019	-72972819	-135497121	-410026555	-424753889	-159358560	-361664282	-846543834	-10146436	-190510082	-383613097	-124300214	-132101386
2023-08-16	-283977915	-1266555478	64738485	-212891009	39686096	-133102404	-88876555	-472305283	-44110397	-357642319	-812675927	-19701331	-161225876	-185022525	-129228252	-121137252
2023-08-17	-370791249	-777500947	111336910	-223923667	-78760726	-122701420	-104426947	-590530907	-321519196	-281320016	-982319924	-502285497	-160035518	-142967743	-185068410	-227495079
2023-08-18	-167133386	-662918198	70601134	-200433873	-194592466	-78435170	124258632	-509063351	-205986157	-222958779	-1085767098	-290289252	-246350135	-136116490	16109816	-203021874
2023-08-21	-55432972	-766647420	75624757	-221214658	-201194362	-70008077	-65708102	-383264629	-405515123	-333964520	-818351132	-440279931	-242023460	-19672695	-29096963	-77892707
2023-08-22	-203549587	-683075757	83502331	-222679054	-241086663	-82158551	-702832842	-309136603	-194361840	-216961040	-755204341	-185335625	13024375	25204663	-144853105	26402228
2023-08-23	367301847	-257670921	-35664339	-39611623	-198840771	21315736	-333396733	-82458144	-82516337	13794297	-210150204	263286900	256301061	169725149	45951427	155800229
2023-08-24	-139708826	-431572723	-17528799	-93609240	-158243646	-4453442	-556177904	-93045299	-28480809	-80091423	-223150345	274301360	47537373	74556395	-31343115	91802428
2023-08-25	-29959779	-146257822	-71145658	-63281290	-19475050	-13443725	-612067145	75577882	58079520	-67197562	-98357774	426050610	101973653	143819918	-60604131	199633158
2023-08-28	125192676	-156318850	-41413864	-82874441	143715327	-27556814	-872272247	-180431449	243820767	-221732126	-103072199	435315777	170831738	-9624481	-167801157	57664010
2023-08-29	1045053044	566280864	-190286369	63492899	382672351	82474195	-11932719	302811898	364286597	-23977848	315258602	428617803	170395107	273188398	85461361	64723352
2023-08-30	830220428	588253018	-164643901	4906683	371811207	77622875	-239556876	306023449	334892596	-40717794	-257408842	298911404	138415023	152790992	67656600	739590
2023-08-31	1144584054	1162791989	-271456806	151585714	322476800	178768020	315275695	538102423	623212531	308725978	258219341	536914164	347927438	618410247	182117347	170870041
2023-09-01	459941083	701056987	-181046469	85866238	355917475	222308457	102050732	87282887	612359958	190891193	620067726	556359082	336386518	199499048	258247045	149184988
2023-09-05	106286052	676560680	-191448666	119090432	244699351	225025767	324681081	350166687	643285388	192695367	642835177	774282547	201774929	272661750	353982714	256333741
2023-09-06	-731785897	123667908	-62135945	-5166353	67292828	121004436	-502604908	-166382700	234065607	-40775371	152537219	465430940	-37980651	-6826234	149396438	146217750
2023-09-07	-1112664609	-668606020	30046040	-107580026	-63044023	27829518	-894637643	-334981107	-11735334	44365203	463026477	177236537	-112892141	-226653911	-45806498	128892634
2023-09-08	-701795412	-901134304	70483588	-137962514	76142850	-62990438	-1310468396	-510071969	-11860063	-57778859	326554773	98187736	-96455429	-626744076	15850242	171427580
2023-09-11	-89894364	-391835404	3773168	-52909675	46440319	-152933541	-1345721441	112186806	-206634945	138722319	496453215	-24266025	82042743	-157380819	-215616845	214347177
2023-09-12	-325364260	-986565569	96122518	-190647721	147734588	-194165149	-1576218491	-214523545	-560713059	220137941	-15427896	-405919832	11751292	-444029594	-231698022	133699720
2023-09-13	125475653	-467712511	-10888343	-92007886	268773715	-103092618	-813350478	-70099479	-464142608	421678571	468570520	-516336919	208713334	-263449050	-38876125	125219971
2023-09-14	884210762	609103891	-114919795	37320727	417386846	-60401428	-831092234	126098834	-128517570	432534475	742572442	-654075097	326269603	105963983	9577929	35532517
2023-09-15	-392889975	132319593	-45619077	-52936744	216400447	-90269374	-665883954	261964981	-828036120	355338629	408978852	-667283356	-33847916	-120850625	-226533265	-122208668
2023-09-18	-379379222	85165457	-36920692	-63318941	41783377	-24183424	-148655356	-146879233	-542669046	141844313	331424841	-877093517	35445190	-133806149	-202042836	-253302525
2023-09-19	-300484839	126100031	-38380591	-48363504	-100317469	-72621684	-289144182	-27951336	-314544362	73317965	638061337	-710660234	7337916	-104800926	-354087367	-278662066
2023-09-20	-253118654	-440744684	64487008	-168569536	-109367212	-116765197	-795459784	-59983307	-394787724	-143084597	352288809	-567761442	-230940010	-314194883	-380187601	-232218436
2023-09-21	-1367838350	-1374989872	182737091	-321962938	-291599347	-161800388	-785682307	-344070754	-694011154	-446708914	-231141514	-241566290	-527782180	-767322472	-417270207	-261691249
2023-09-22	-401737254	-709013257	83994458	-213858229	-262250222	-48089676	-348672562	-684346821	-8687350	-471596522	246831232	-275436124	-272584625	-297443519	-174982610	-152443150
2023-09-25	-93530286	-1010062398	141994839	-274584860	-189362564	-61642664	-142697665	-640794340	-98127599	-272259750	-66545257	-15353433	-360198263	-188027008	-47321204	-92588374
2023-09-26	-103491221	-766485768	133317910	-257288211	-214664402	-63572356	252511358	-591283483	-349114239	-211997978	-397077226	-183965869	-346085673	-217203753	-13795652	-68826323
2023-09-27	-8671789	-751385531	117488179	-213190637	-313357887	-80066800	384591741	-737560461	-290349046	-151371924	-307843529	-82051139	-74066039	-137911709	-17110364	-66649726
2023-09-28	1211738401	-91968417	-4543121	-93593475	-41540111	1716314	943410715	-456591055	-130243094	75125	217134665	-257094820	144419695	290535730	193583317	35005413
2023-09-29	1403323514	-408724917	33002054	-140036467	-22181446	-64231505	761611785	-258504335	-170035131	55995881	-22056879	-39327314	94361400	54442742	190286719	48286328
2023-10-02	712296967	-580940566	18069979	-150429699	-138557865	-105620035	820360036	-102952742	-169453991	92691847	312146714	-60540693	166681808	-14800972	62571957	-28371974
2023-10-03	799189649	-870294010	32949576	-183024430	-159005482	-97760595	233367068	-253989132	-118998667	-4568633	349094981	19335114	217626104	-19900598	23218744	-43021582
2023-10-04	780058503	-231012148	-51438642	-92885194	-80978453	-40737150	593231857	162151859	104212433	138450074	571498514	24060850	208033729	98289145	47439754	4772555
2023-10-05	38374540	-732357907	47858362	-173472465	-257309751	-119797413	669754218	-9164676	54569422	-40697649	57699319	-27652471	15073002	-52755799	-140509446	-36512043
2023-10-06	-4348514	-529842637	-5369534	-108468684	-154131702	-54642526	965360076	202910893	159528708	619401	271574436	-22696240	165322377	71952331	-73558124	-13470992
2023-10-09	537635055	-45157203	-82141895	5101424	-77469749	-25487067	601414825	109009253	236569819	-42089194	340610883	-259967401	155649797	119388752	79404851	80094516
2023-10-10	993667430	606209806	-174878726	103817636	147203540	65141905	1160441707	382938456	348921168	232230016	845039814	-339517531	314768217	358571886	283158478	196733561
2023-10-11	791594188	493974829	-162051139	66343754	107717074	32516074	1120004789	24412388	258557587	218418212	890861482	-458399330	307809496	347994204	50576039	176239264
2023-10-12	392018095	775804651	-195624009	79182360	-15327177	90993747	744970457	62203005	287677205	420885169	1122391477	-412171615	283236052	750807600	210978140	164543949
2023-10-13	88626408	412502277	-88548383	-57944627	31389586	-11050528	58787253	-236974736	-46570867	197112923	587986074	-725849691	65079744	550017398	8610275	48171909
2023-10-16	-184527997	445091409	-90848677	-60273898	168101034	53324302	482501095	-127418460	-367274084	222514092	548864910	-453350099	76990653	674848071	35884481	55046027
2023-10-17	-684114471	-99325588	-7438128	-104007559	134112055	-45327409	126174457	-191590513	-565101400	12259843	458653950	-497355560	-9012377	316358610	-150543105	-48062760
2023-10-18	-859070229	-675899460	67398867	-192442646	45275588	-97518729	-406399294	-322575287	-699110848	-165573041	-129608587	-563911755	-79343259	346840726	-98741334	-125947799
2023-10-19	-545211986	-642851293	74852031	-177064767	46787587	-124101970	-187283604	-698237442	-732705335	-154186028	-70414822	-103431127	100168759	-222779874	-138027215	-27860057
2023-10-20	44129215	-685478067	57637528	-167493674	-188549460	-104655249	-40318563	-571340980	-852536615	-204800386	25862811	120563949	55600650	-238387422	-53058220	-49521060
2023-10-23	76988798	-674975535	61502985	-169121375	-275311678	-132506988	-56949072	-634123151	-632009097	-217565603	21907125	122936025	3071270	-315468114	-174760180	-69130996
2023-10-24	205602357	-521554308	6150547	-160106545	-253533147	-82373355	-66550253	-716571479	-496769716	-154846959	-179221049	538872374	151856545	61282069	-149406647	15984278
2023-10-25	4585012	-524542144	35325226	-197681335	-220756976	-82178456	-58756871	-539343247	-559857850	-148877307	-208468138	737112993	-78668490	-229642719	-148027628	6775822
2023-10-26	210295985	-678203318	31710103	-233532249	-49484798	-34727052	-428590393	-247507044	-658339526	-131305363	-280455442	279669948	-73100262	-263190217	-120661764	-22518186
2023-10-27	-173850302	-309456809	-16964587	-147407964	-43545596	-5140460	-462725817	-201129716	-220241585	115935479	135360525	93580249	5883033	-27337214	-1984024	76760458
2023-10-30	114028340	-152758298	187502	-184749920	94838831	-70479886	-794053436	-463998466	-121022826	122243249	91561568	146155347	52650357	-123456999	-26865986	77706912
2023-10-31	343547006	232242546	-51905274	-113145889	104397166	-36096991	-744478441	-332058513	15445714	315178872	-168474511	-152951536	-194330306	-267212280	87034686	59008951
2023-11-01	1056675911	1115045592	-189337250	67022427	317794893	53053837	-269428289	-249910640	298998925	494338143	388469940	45717783	106939836	1898725	368404772	77858011
2023-11-02	1903104733	1382804639	-266575086	201001874	394193656	73914749	190099879	-112000718	585978329	473302728	198487754	307418338	180683621	368138857	272245219	-17716628
2023-11-03	1905069583	1699715112	-332397878	267771369	605965476	144815767	725762851	-144615873	569588512	558580021	270641959	621315679	391287475	403974982	292171431	9957731
2023-11-06	1400490795	1334314959	-301175009	243924512	385095802	139843088	913368327	6701772	583487040	643733714	285538119	382336384	424967778	307731886	254943324	-93759029
2023-11-07	1447901370	1367009715	-279684496	296039443	207435381	153943429	1307005719	10149694	731654658	618141216	831777395	509431519	639615137	462065125	288985072	3861116
2023-11-08	1043747598	878365410	-254575935	220829647	52203558	127991697	1388110121	-66882490	749450955	372151509	537615901	359453352	708841780	492365027	126386156	-11551269
2023-11-09	228733454	774601024	-175165328	140613550	-87990663	101042385	1183288010	-300049539	558104688	233740480	963084306	275448351	528674143	529457150	197225132	97749243
2023-11-10	996443501	705572315	-168397798	194417169	-77559522	108058798	1252487895	-225364702	569368189	259023317	982263702	318079926	521023214	708847302	206932361	83496332
2023-11-13	1129207534	303272199	-183026209	228677786	-74442459	98351897	1285802359	83390433	171541089	33118932	982870631	233751807	443708233	643062429	202323139	101441098
2023-11-14	1605091685	429413429	-181010745	223248125	116695932	138717804	1190058391	55808715	168211473	-19953511	982312288	346193851	430988125	706754374	166186112	70700283
2023-11-15	1564439690	84158233	-93630952	125877203	205208010	129674749	536600535	105750807	235639086	18887060	785418663	531539313	384215138	622440663	26508793	132640023
2023-11-16	1373689856	64839582	-102865382	107007998	290259134	118023090	690678767	34374890	388500407	32506933	432688547	628413253	564160748	185923622	89314622	41610720
2023-11-17	362229177	-405476334	-24534006	-17536602	271491592	116536336	125290529	3565898	43249593	77331532	60426939	293279596	236852768	13315600	38061664	13689837
2023-11-20	1026415970	587910052	-70845486	67578030	389679483	244090734	345250036	-88246170	505934042	245005093	121463160	582994685	327388046	328679472	173595360	140454962
2023-11-21	-140563838	-150222704	16010726	-129643728	269966052	85094241	-115174025	-74246202	168175779	4722835	-368507604	487168475	313402291	-266712322	-22498628	56438969
2023-11-22	280367548	408332666	-73258593	55748939	311952130	123845716	-23315344	-168738387	201830651	318837650	94829478	403875269	322660232	-557396593	183578423	108371649
2023-11-24	886165184	215190277	-43815749	32528023	279536738	134443916	-351224622	74896488	-179794271	450623498	167950311	330651790	129281220	-242486274	100341815	186372306'''

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
        for a in columns[i]:
            if a == "null":
                total_null = total_null + 1

        if total_null > 0:
            date_list = (columns['Date'][total_null:])
        else:
            date_list = columns['Date']
        # Start Date & End Date
        start_date = date_list[0]
        end_date = date_list[-1]

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
        for date, ohlc_html in zip(columns['Date'], ohlc_html_list):

            ohlc_html = ohlc_html.replace("@replace_with_date", date)
            final_ohlc_html_list.append(ohlc_html)

        for date, nci in zip(columns['Date'], columns[i]):

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
            if not os.path.exists(f"ETF/{file_name}"):
                # Create the file if it doesn't exist
                with open(f"ETF/{file_name}", 'w') as file:
                    file.write('')  # Creating an empty file
                file.close()

            with open(f"ETF/{file_name}", "w") as file:
                file.write(formatted_html)
            file.close()

        elif asset_type == "STOCK":
            # Check if the file exists
            if not os.path.exists(f"STOCK/{file_name}"):
                # Create the file if it doesn't exist
                with open(f"STOCK/{file_name}", 'w') as file:
                    file.write('')  # Creating an empty file
                file.close()
            with open(f"STOCK/{file_name}", "w") as file:
                file.write(formatted_html)
            file.close()
        print(file_name)
