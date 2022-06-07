// Alpha Vantage API Key: ZXNGDI9TXSC9K8AL

const url = 'https://www.alphavantage.co/query'
const apikey = 'ZXNGDI9TXSC9K8AL'

function buildUrl(symbol, userTimeSeries) {
    return url + "?function=" + userTimeSeries + "&symbol=" + symbol + "&apikey=" + apikey;
}

const App = {
    data () {
        return {
            ticker: '',
            rawJSON: {},
            timeSeriesData: {},
            jsonFormatted: {},
            userTimeSeries: 'TIME_SERIES_DAILY', // 'TIME_SERIES_INTRADAY'
            // intervalInput: '15min', for intraday
            xLabels: [],
            closingPrices: [],
            companyName: '',
            companyOverview: '',

        }
    },
    methods: {
        searchTicker () {
            this.ticker = this.ticker.toUpperCase();
            // get company stock price info
            axios({
                url: buildUrl(this.ticker, this.userTimeSeries),
                method: 'get',
            }).then (res => {
                // this.mostRecentClose = res.data["Meta Data"]["3. Last Refreshed"]
                console.log('RES.DATA:', res.data)
                this.rawJSON = res.data
                console.log('rawJSON [index]', this.rawJSON['Time Series (Daily)'])
                this.createAxesData(this.rawJSON['Time Series (Daily)'])
                this.timeSeriesData = res.data['Time Series (Daily)']
                this.jsonFormatted = JSON.stringify(res.data, null, "\t")
                this.buildChart()
            }),
            // get company general info
            axios({
                url: buildUrl(this.ticker, 'OVERVIEW'),
                method: 'get',
            }).then (res => {
                this.companyName = res.data['Name']
                this.companyOverview = res.data['Description']
            })
            message = 'stock data incoming...'
            // this.createData(this.rawJSON)
            
        },
        createAxesData (jsonData) {
            console.log('BEGIN CREATING AXIS DATA...')
            this.xLabels = []
            this.closingPrices = []
            for (item in jsonData) {
                this.xLabels.push(item)
                this.closingPrices.push(parseFloat(jsonData[item]["4. close"]))
            }
            this.xLabels.reverse()
            this.closingPrices.reverse()
        },
        // chart.JS
        buildChart () {
            console.log('BUILDING CHART...')
            var chartExists = Chart.getChart('myChart') // check to make sure chart DNE
            
            if (chartExists != undefined) {
                chartExists.destroy()
                console.log('CHART DESTROYED.')
            }

            const ctx = document.getElementById('myChart');
            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: this.xLabels,
                    datasets: [{
                        label: 'Stock Price at Close',
                        data: this.closingPrices,
                        fill: false,
                        borderColor: [
                            'rgba(0, 127, 255, 1)',
                        ],
                        borderWidth: 2
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: false
                        }
                    },
                    responsive: true,
                    maintainAspectRatio: false
                }
            });
        },
    }
    
}

const app = Vue.createApp(App)
app.mount('#app')
