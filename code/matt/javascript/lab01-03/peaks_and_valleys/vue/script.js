// build table from data
function buildTable (inputData) {
    // assign height and width to variables
    let height = Math.max.apply(null, inputData) - Math.min.apply(null, inputData) + 1
    let width = inputData.length
    // declare variable to hold table rows
    let allRows = ''
    // iterate through rows
    for (let y = height; y > 0; y--) {
        // declare variable to hold each row
        let eachRow = ''
        // iterate through each column in row
        for (let x = 0; x < width; x++) {
            // find maximum values to left and right and assign to variables
            let maxLeft = Math.max.apply(null, inputData.slice(0,x))
            let maxRight = Math.max.apply(null, inputData.slice(x,))
            // set cell to land if value of data is less than or equal to current row
            if (inputData[x] >= y) {
                thisCell = 'land'
            // set cell to water if higher points are to the left and right
            } else if (inputData[x] < maxLeft && inputData[x] < maxRight && y <= maxLeft) {
                thisCell = 'water'
            // set cell to sky if it was not found to be land or water
            } else {
                thisCell = 'sky'
            }
            // add class to each cell and add to row variable
            eachRow += '<td class="' + thisCell + '"></td>'
        }
        // add each row to table variable
        allRows += '<tr>' + eachRow + '</tr>'
    }
    // return results nested in table element
    return '<table>' + allRows + '</table>'
}

// generate app
const { createApp } = Vue
createApp({
    data () {
        return {
            // set up variables
            inputData: [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9],
            results: '',
        }
    },
    mounted() {
        // run method on page load
        this.$nextTick(() => {
            this.pageLoad()
        })
    },
    methods: {
        // method for page load
        pageLoad () {
            // assign results of buildTable to results variable
            this.results = buildTable(this.inputData)
        }
    }
}).mount('#app')