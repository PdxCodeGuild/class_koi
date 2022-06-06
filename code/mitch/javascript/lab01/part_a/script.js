
let nums = []
let running_sum = 0

while (true) {
    let user_input = prompt("Please enter a number or 'done'.")
    if (user_input == 'done') {
        break
    }else {
        nums.push(parseInt(user_input))
        running_sum += parseInt(user_input)
    }
    
}

let average = running_sum / nums.length

alert(`The average of ${nums} is ${average}`)








