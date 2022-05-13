let newItem = document.querySelector("#type_text")
let addButton = document.querySelector("#add_button")
let todoList = document.querySelector("#todo_list")
let completeList = document.querySelector("#complete_list")

addButton.addEventListener("submit", function(evt){
    evt.preventDefault()
    let toDoTask = document.createElement("li")
    let toDoName = document.createElement("p")
    toDoName.innerText = newItem.value
    toDoTask.appendChild(toDoName)
    let toDoRemove = document.createElement("button")
    // toDoRemove.setAttribute("id", "remove_button" )
    let toDoComplete = document.createElement("button")
    // toDoComplete.setAttribute("id", "complete_button")
})