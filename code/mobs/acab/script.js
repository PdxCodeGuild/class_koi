const addBtn = document.querySelector("#add-btn");
const addItem = document.querySelector("#grocery-input");

addBtn.addEventListener("click", function (e) {
  e.preventDefault();
  const li = document.createElement("li");
  const newItem = addItem.value;
  const ul = document.getElementById("grocery-list");
  li.innerText = newItem;
  li.id = newItem
  let removeBtn = document.createElement("button");
  removeBtn.innerHTML = "Remove";
  removeBtn.type = "submit";
  removeBtn.id = `${li.innerText}`
  console.log(li)
  console.log(removeBtn)
  li.appendChild(removeBtn); 
  ul.appendChild(li);
  document.querySelector('#grocery-input').value='';
  removeBtn.addEventListener('click', function(){
    console.log(removeBtn.id)
    li.remove(removeBtn.id)
    // removeItem = document.getElementById('removeBtn.id')
  })

});

// function removeListItem(removeBtn) {
  // let listItem = document.querySelector(`${li.innerText}`)
// }


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
