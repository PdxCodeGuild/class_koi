const docData = document.getElementById('data')
const docPeaksAndValleys = document.getElementById('peaks_and_valleys')
const docShowPeaksAndValleys = document.getElementById('show_peaks_and_valleys')
const docGraph = document.getElementById('graph')
const docGraphWithPools = document.getElementById('graph_with_pools')

function peaks(data)
{
    let result = [];

    for(let i = 1; i < data.length; i++)
    {
        if(data[i] > data[i - 1] && data[i] > data[i + 1]) result.push(i);
    }

    return result;
}

function valleys(data)
{
    let result = [];
    
    for(let i = 1; i < data.length; i++)
    {
        if(data[i] < data[i -1] && data[i] < data[i + 1]) result.push(i);
    }

    return result;
}

function showPeaksAndValleys(data, peaks, valleys)
{
    let newData = [];

    for(let i of data) newData.push(' ');
    for(let peak of peaks) newData[peak] = 'P';
    for(let valley of valleys) newData[valley] = 'V';

    return newData
}

function peaksAndValleys(data, peaks, valleys)
{
    let newData = [];
    let newArray = [];

    for(let i of data) newData.push(' ');
    for(let peak of peaks) newData[peak] = 'P';
    for(let valley of valleys) newData[valley] = 'V';

    newArray = peaks.concat(valleys);
    // for(i of newArray) console.log(typeof i)
    newArray = newArray.sort((a, b) => (a - b));
    return newArray
}

function showGraph(data)
{
    for(let i = Math.max(...data); i > 0; i--)
    {
        for(let j = 0; j <= data.length; j++)
        {
            if(data[j] >= i) process.stdout.write('x' + '  ')
         
            else
            {
                process.stdout.write(' ' + '  ')
                // console.log(' ' + '  ')
            }
        }
        console.log('\n')
    }
}

function showGraphWithPools(data)
{
    for(let i = Math.max(...data); i > 0; i--)
    {
        let tempMax = 0;
        for(let j = 0; j <= data.length; j++)
        {
            if(data[j] >= i)
            {
                tempMax = data[j];
                process.stdout.write('x' + '  ')
            }
            else if(data[j] < tempMax) process.stdout.write('o' + '  ')
            else
            {
                process.stdout.write(' ' + '  ')
            }
        }
        console.log('\n')
    }
}

let data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9];

// console.log(peaks(data))
// console.log(valleys(data))
// console.log(peaksAndValleys(data, peaks(data), valleys(data)))
// showGraph(data)
// showGraphWithPools(data)
docData.innerText = data
docPeaksAndValleys.innerText = peaksAndValleys(data, peaks(data), valleys(data))
docShowPeaksAndValleys.innerText = showPeaksAndValleys(data, peaks(data), valleys(data))