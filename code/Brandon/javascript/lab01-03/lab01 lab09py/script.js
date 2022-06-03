// Version 1
let data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9];

function peaks() {
  for (let i = 0; i < data.length; i++) {
    var len = data.length;
    let current = data[i];
    let previous = data[(i - 1) % len]; //
    let next = data[(i + 1) % len];
    if ((current > next) & (current > previous)) console.log(data[i] + " peak");
  }
}

function valleys() {
  for (let i = 0; i < data.length; i++) {
    var len = data.length;
    let current = data[i];
    let previous = data[Math.floor((i - 1) % len)]; //
    let next = data[Math.floor((i + 1) % len)];
    if ((current < next) & (current < previous))
      console.log(data[i] + "valley \x20;");
  }
}

function peaks_and_valleys() {
  for (let i = 0; i < data.length; i++) {
    var len = data.length;
    let current = data[i];
    let previous = data[Math.floor((i - 1) % len)]; //
    let next = data[Math.floor((i + 1) % len)];
    if ((current > next) & (current > previous))
      display.innerText += data[i] + "  peak \x0A";

    if ((current < next) & (current < previous))
      display.innerText += data[i] + " valley \x0A";
  }
}
let display = document.querySelector("#display");
let p = document.querySelector("p");
const submit = document.querySelector("#submit");
p.innerText = data;
let x;

peaks();
valleys();
console.log("----------------------");
// peaks_and_valleys();

submit.addEventListener("click", function () {
  peaks_and_valleys();
});
