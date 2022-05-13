localStorage.clear()

let newItem = document.querySelector("#type_text")
let addButton = document.querySelector("#add_button")
let todoList = document.querySelector("#todo_list")
let completeList = document.querySelector("#complete_list")


let toDoArray = []
let completedArray = []

if(localStorage.getItem('toDoArray')) {
    toDoArray = JSON.parse(localStorage.getItem('toDoArray'))
} else {
    toDoArray = []
}

if(localStorage.getItem('completedArray')) {
    completedArray = JSON.parse(localStorage.getItem('completedArray'))
} else {
    completedArray = []
}

function buildItem (newItem) {
    let toDoTask = document.createElement("li")
    let toDoName = document.createElement("p")
    toDoName.innerText = newItem
    toDoTask.appendChild(toDoName)
    let toDoRemove = document.createElement("button")
    let toDoComplete = document.createElement("button")
    toDoRemove.innerText = "Remove"
    toDoComplete.innerText = "Complete"
    toDoTask.appendChild(toDoRemove)
    toDoTask.appendChild(toDoComplete)
    todoList.appendChild(toDoTask)

    toDoRemove.addEventListener("click", function(_) {

        toDoArray.remove(toDoTask)
        localStorage.setItem('toDoArray', JSON.stringify(toDoArray))
    })
    toDoComplete.addEventListener("click", function(evt) {
       toDoTask.remove() 
       toDoComplete.remove()
       completeList.appendChild(toDoTask)
       let index = toDoArray.indexOf(newItem)
    //    alert(newItem)
       let completed = toDoArray.splice(index,1)
       completedArray.push(completed)
       alert(`todo:${toDoArray}completed:${completedArray}`)
       localStorage.setItem('toDoArray', JSON.stringify(toDoArray))
       localStorage.setItem('completedArray', JSON.stringify(completedArray))
    })
}


addButton.addEventListener("click", function(evt){
    evt.preventDefault()

    toDoArray.push(newItem.value)
    localStorage.setItem('toDoArray', JSON.stringify(toDoArray))


    buildItem(newItem.value)

})