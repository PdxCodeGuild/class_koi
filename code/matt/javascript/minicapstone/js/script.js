// generate app
const { createApp } = Vue
createApp({
    data () {
        return {
            // main API endpoint and modifiers
            baseURL: `https://www.thecocktaildb.com/api/json/v2/${API_KEY}/`,
            listURL: 'list.php',
            searchURL: 'search.php',
            filterURL: 'filter.php',
            // object to hold full ingredient list
            ingredientsObj: {},
            // user ingredient search input
            ingredientSearchInput: '',
            // current search results
            filteredIngredients: [],
            // user's selected ingredients
            myIngredients: [],
            // recipes containing at least one of user's ingredients
            myRecipes: {},
        }
    },
    created () {
        this.loadFromLocal()
        this.getIngredients()
        // console.log(this.ingredientsObj)
    },
    methods: {
        // gets full list of ingredients from API
        getIngredients () {
            axios({
                url: this.baseURL + this.listURL,
                method: 'get',
                headers: {
                    Accept: 'application/json',
                },
                params: {
                    i: 'list',
                }
            }).then(res => {
                // iterate through response and add each ingredient to array as an object
                res.data.drinks.forEach(item => {
                    // loosely correct capitalization errors on API
                    let itemName = item.strIngredient1[0].toUpperCase() + item.strIngredient1.substring(1)
                    // add name key with string value and recipes key with empty array to each ingredient
                    this.ingredientsObj[itemName] = {
                        name: itemName,
                        recipes: [],
                    }
                })
                console.log(this.ingredientsObj)
            })
        },
        // searches full list of ingredients against user input
        ingredientSearch () {
            // reset search results
            this.filteredIngredients = []
            // iterate through ingredients Object
            Object.keys(this.ingredientsObj).forEach(item => {
                // add to filtered/results array if input is not blank AND the current string is found in ingredients Object keys
                if (!(this.ingredientSearchInput == '') && (item.toLowerCase().includes(this.ingredientSearchInput.toLowerCase()))) {
                    this.filteredIngredients.push(item)
                    this.filteredIngredients.sort()
                }
            })
        },
        // adds a given ingredient to an array storing the user's ingredients
        addToMyIngredients (ingredient) {
            // only run if the ingredient isn't already added
            if (!(this.myIngredients.includes(ingredient))) {
                // add to array and sort
                this.myIngredients.push(ingredient)
                this.myIngredients.sort()
                // save to local storage
                this.saveToLocal()
                // get list of recipes for this ingredient
                this.ingredientRecipes(ingredient)
            }
        },
        // gets all cocktails that a given ingredient is used in
        ingredientRecipes (ingredient) {
            axios({
                url: this.baseURL + this.filterURL,
                method: 'get',
                headers: {
                    Accept: 'application/json',
                },
                params: {
                    i: ingredient,
                }
            }).then(res => {
                // iterate through response and add recipe names to ingredient object
                res.data.drinks.forEach(item => {
                    this.ingredientsObj[ingredient].recipes.push(item.strDrink)
                    })
                    // console.log(this.ingredientsObj)
            })
            //////////////////////////THIS IS WHERE I'M AT - STARTED recipeDetails AND I NEED TO FINISH THAT AND CALL IT AFTER I ADD RECIPE NAMES
        },
        // gets details of recipes
        recipeDetails (recipeName) {
            axios({
                url: this.baseURL + this.searchURL,
                method: 'get',
                headers: {
                    Accept: 'application/json',
                },
                params: {
                    s: recipeName,
                }
            })
        },
        // saves myIngredients array to local storage
        saveToLocal () {
            const parsedMyIngredients = JSON.stringify(this.myIngredients)
            localStorage.setItem('myIngredients', parsedMyIngredients)
        },
        // loads myIngredients array from local storage
        loadFromLocal () {
            if (localStorage.getItem('myIngredients')) {
                this.myIngredients = JSON.parse(localStorage.getItem('myIngredients'))
            }
        },
        // resets local storage
        clearLocal () {
            this.myIngredients = []
            localStorage.clear()
        },
    }
}).mount('#app')


/*
***API call to get all ingredients
?Save ingredients to local storage
***List all possible ingredients
***User selects ingredients they have
***Save user's ingredients to local storage
***API call per ingredient -> save drink name/ID
API call per saved drink
?? save drinks to local storage ??
per drink, check if all ingredients are on user ingredient list (increment counter if not)

*/

/*
filter = {
    "drinks": [
        {
            "strDrink": "155 Belmont",
            "strDrinkThumb": "https://www.thecocktaildb.com/images/media/drink/yqvvqs1475667388.jpg",
            "idDrink": "15346"
        },
    ]
}

*/


/*

myRecipes Object of Objects {
    ==strDrink==: {
        name: string, // strDrink
        glass: string, // strGlass
        instructions: string, // strInstructions
        image: string, // strDrinkThumb
        ingredients: {
            ==strIngredient[1-15]==: ==strMeasure[1-15]==
        }
    
    }
}
    

*/