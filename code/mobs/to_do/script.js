let newItem = document.querySelector("#type_text")
let addButton = document.querySelector("#add_button")
let todoList = document.querySelector("#todo_list")
let completeList = document.querySelector("#complete_list")


// alert("script's runnin'")

addButton.addEventListener("click", function(evt){
    evt.preventDefault()
    let toDoTask = document.createElement("li")
    let toDoName = document.createElement("p")
    toDoName.innerText = newItem.value
    toDoTask.appendChild(toDoName)
    let toDoRemove = document.createElement("button")
    // toDoRemove.setAttribute("id", "remove_button" )
    let toDoComplete = document.createElement("button")
    // toDoComplete.setAttribute("id", "complete_button")
    toDoRemove.innerText = "Remove"
    toDoComplete.innerText = "Complete"
    toDoTask.appendChild(toDoRemove)
    toDoTask.appendChild(toDoComplete)
    todoList.appendChild(toDoTask)

    toDoRemove.addEventListener("click", function(_) {
        toDoTask.remove()



    })

    toDoComplete.addEventListener("click", function(evt) {
        

    })



})