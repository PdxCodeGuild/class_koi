const addBtn = document.querySelector("#add-btn");
const addItem = document.querySelector("#grocery-input");

addBtn.addEventListener("click", function (e) {
  e.preventDefault();
  const li = document.createElement("li");
  const newItem = addItem.value;
  const ul = document.getElementById("grocery-list");
  li.innerText = newItem;
  ul.appendChild(li);
});

// form.addEventListener("submit", function (e) {
//   e.preventDefault(); // this stops the default form submission of the event, so the page doesn't refresh
//   const color = input.value;
//   // creating the figure, settting backgound color, appending to main

//   const figure = document.createElement("figure");
//   figure.style.backgroundColor = color;
//   main.appendChild(figure);

//   // creating the p tag, setting innerText, appending to figure
//   const p = document.createElement("p");
//   p.innerText = `Click me to set the background color to ${color}.`;
//   figure.appendChild(p);

//   figure.addEventListener("click", function (_e) {
//     // console.log(_e)
//     document.body.style.backgroundColor = color;
//   });
// });
