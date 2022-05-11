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
      console.log(data[i] + "valley");
  }
}

function peaks_and_valleys() {
  for (let i = 0; i < data.length; i++) {
    var len = data.length;
    let current = data[i];
    let previous = data[Math.floor((i - 1) % len)]; //
    let next = data[Math.floor((i + 1) % len)];
    if ((current > next) & (current > previous)) console.log(data[i] + " peak");

    if ((current < next) & (current < previous))
      console.log(data[i] + "valley");
  }
}

peaks();
valleys();
console.log("----------------------");
peaks_and_valleys();
