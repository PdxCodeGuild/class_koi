// // Version 1

// var single_digit = {
//   0: "",
//   1: "one",
//   2: "two",
//   3: "three",
//   4: "four",
//   5: "five",
//   6: "six",
//   7: "seven",
//   8: "eight",
//   9: "nine",
// };

// var double_digit = {
//   0: "ten",
//   1: "eleven",
//   2: "twelve",
//   3: "thirteen",
//   4: "fourteen",
//   5: "fifteen",
//   6: "sixteen",
//   7: "seventeen",
//   8: "eighteen",
//   9: "nineteen",
// };

// var tens = {
//   0: "",
//   1: "eleven",
//   2: "twenty",
//   3: "thirty",
//   4: "forty",
//   5: "fifty",
//   6: "sixty",
//   7: "seventy",
//   8: "eighty",
//   9: "Ninety",
// };

// let x = prompt("Please enter a number 1-999 to convert: ");

// let tens_digit = Math.floor((x / 10) % 10);
// let ones_digit = Math.floor(x % 10);
// let hundreths = Math.floor(x / 100);

// if ((x >= 1) & (x <= 9)) {
//   console.log(single_digit[x]);
// }
// if ((x >= 10) & (x <= 19)) {
//   console.log(double_digit[x]);
// }
// if ((x >= 20) & (x <= 99)) {
//   console.log(tens[tens_digit], single_digit[ones_digit]);
// }
// if (
//   (x >= 100) &
//   (x <= 999) &
//   (ones_digit != 0) &
//   (tens_digit != 1) &
//   (tens_digit != 0)
// ) {
//   console.log(
//     single_digit[hundreths],
//     "hundred and",
//     tens[tens_digit],
//     single_digit[ones_digit]
//   );
// } else if (ones_digit == 0) {
//   console.log(single_digit[hundreths], "hundred and", tens[tens_digit]);
// } else if (tens_digit == 1) {
//   console.log(single_digit[hundreths], "hundred", tens[tens_digit]);
// } else if (tens_digit == 0) {
//   console.log(single_digit[hundreths], "hundred and", single_digit[ones_digit]);
// }

// Version 2

const single_digit = {
  0: "",
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
};

const double_digit = {
  0: "ten",
  1: "eleven",
  2: "twelve",
  3: "thirteen",
  4: "fourteen",
  5: "fifteen",
  6: "sixteen",
  7: "seventeen",
  8: "eighteen",
  9: "nineteen",
};

const tens = {
  0: "",
  1: "eleven",
  2: "twenty",
  3: "thirty",
  4: "forty",
  5: "fifty",
  6: "sixty",
  7: "seventy",
  8: "eighty",
  9: "Ninety",
};

const submit_numbers = document.querySelector("#submit_numbers");
let x = document.querySelector("#user-input");
let p = document.querySelector("p");

// let x = prompt("Please enter a number 1-999 to convert: ");

submit_numbers.addEventListener("click", function () {
  let tens_digit = Math.floor((x.value / 10) % 10);
  let ones_digit = Math.floor(x.value % 10);
  let hundreths = Math.floor(x.value / 100);
  if ((x.value >= 1) & (x.value <= 9)) {
    p.innerText = single_digit[x.value];
  }
  if ((x.value >= 10) & (x.value <= 19)) {
    p.innerText.value = double_digit[x.value];
  }
  if ((x.value >= 20) & (x.value <= 99)) {
    p.innerText = tens[tens_digit] + " " + single_digit[ones_digit];
  }
  if (
    (x.value >= 100) &
    (x.value <= 999) &
    (ones_digit != 0) &
    (tens_digit != 1) &
    (tens_digit != 0)
  ) {
    p.innerText =
      single_digit[hundreths] +
      " hundred and " +
      tens[tens_digit] +
      single_digit[ones_digit];
  } else if (ones_digit === 0) {
    p.innerText = single_digit[hundreths] + " hundred and " + tens[tens_digit];
  } else if (tens_digit === 1) {
    p.innerText = single_digit[hundreths] + " hundred and " + tens[tens_digit];
  } else if (tens_digit === 0) {
    p.innerText =
      single_digit[hundreths] + " hundred and " + single_digit[ones_digit];
  }
});
