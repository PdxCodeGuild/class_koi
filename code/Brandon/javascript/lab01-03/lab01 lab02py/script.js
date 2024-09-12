// // Version 1
// let numbers;
// let sums = 0;

// numbers = [5, 0, 8, 3, 4, 1, 6];
// sums = 0;

// for (let i = 0; i < numbers.length; i++) {
//   sums += numbers[i];
//   console.log(sums);
// }

// Version 2
numbers = [];
let total = 0;
// while (true) {
//   let user_input = parseInt(
//     prompt("Add a number to the list. Hit cancel to calculate the average. ")
//   );
//   if (isNaN(user_input)) {
//     for (let i = 0; i < numbers.length; i++) {
//       sums += numbers[i];
//     }
//     total = sums / numbers.length;
//     console.log(numbers);
//     console.log(total);
//     break;
//   }
//   numbers.push(user_input);
//   console.log(numbers);
// }

let input = document.querySelector("#user-input");
const button1 = document.querySelector("#total");
const output = document.querySelector("#output");
const submit = document.querySelector("#submit");
let p = document.querySelector("p");

let number_list = [];
let sums = 0;

submit.onclick = function () {
  number_list.push(input.value);
  p.innerText = number_list;
};

button1.addEventListener("click", function () {
  for (let i = 0; i < number_list.length; i++) {
    sums += +number_list[i];
  }
  total = sums / number_list.length;
  p.innerText = `Your average is ${total}. `;
});
