
let nums = []
let running_sum = 0

while (true) {
    let user_input = document.querySelector('#number_input')
    if (user_input == 'done') {
        break
    }else {
        nums.push(parseInt(user_input))
        running_sum += parseInt(user_input)
    }
    
}

// run_bt.onclick = function() {
//   let name = name_input.value;
//   //alert(name);
//   output_div.innerText = 'Hello, ' + name + '!';
//   //output_div.innerHTML = '<b>Hello, ' + name + '!</b>';
// }

let average = running_sum / nums.length

alert(`The average of ${nums} is ${average}`)








