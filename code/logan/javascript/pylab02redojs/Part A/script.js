// V1

// let nums = [5, 0, 8, 3, 4, 1, 6]

// let total = 0

// for (let i=0; i<nums.length; ++i) {

//     total += nums[i]    

// }

// let avg = (total/nums.length)

// alert(avg)

//

let nums = []
let total = 0

let input = ""

while (input != "done") {

    input = prompt("input a digit or 'done':  ")
    if (input != "done") {
        nums.push(parseInt(input))
    }
}

for (let i=0; i<nums.length; ++i) {

    total += nums[i]    

}

let avg = (total/nums.length)

alert(avg)