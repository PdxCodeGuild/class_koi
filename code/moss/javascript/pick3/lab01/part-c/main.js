let distance = document.getElementById("distance_input")

const App = {
    data() {
        return {
            header_title: "Unit Conversion",
            dinstance_input: "",


        }
    },
    methods: {
        clickButton () {

        }

    }

}

const app = Vue.greateApp(App)
app.mount("#app")

let from_unit = document.getElementById("from_unit")

let to_unit = document.getElementById("to_unit")

let button = document.getElementById("convert_btn")

let result = document.getElementById("result")

let convr_unit_m = {

    'in': .0254,
    'ft': .3048, 
    'yrd': .9144,
    'mi': 1609.34,
    'm':  1,
    'km': 1000,
}

button.addEventListener("click", function(e) {
    
    let to_meters = distance.value * convr_unit_m[from_unit.value]
    
    let output = to_meters / convr_unit_m[to_unit.value]
    
    result.innerText = `${distance.value} ${from_unit.value} is ${output} ${to_unit.value}`

    console.log(result)
    console.log(distance)
})
