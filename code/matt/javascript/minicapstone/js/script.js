// generate app
const { createApp } = Vue
createApp({
    data () {
        return {
            // main API endpoint and modifiers
            baseURL: `https://www.thecocktaildb.com/api/json/v2/${API_KEY}/`,
            listURL: 'list.php',
            lookupURL: 'lookup.php',
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
            // array of arrays of recipes indexed according to number of missing ingredients
            possibleRecipes: [],
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
                        recipes: {},
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
                // get list of recipes for this ingredient
                this.ingredientRecipes(ingredient)
                // save to local storage
                this.saveToLocal()
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
                // iterate through response and add recipes to ingredient object as objects
                if (!(res.data.drinks == "None Found")) {
                    res.data.drinks.forEach(item => {
                        // format each object as drinkNameString: drinkID
                        this.ingredientsObj[ingredient].recipes[item.strDrink] = item.idDrink
                        // request full recipe for each drink returned
                        this.recipeDetails(item.idDrink)
                    })
                }
                // console.log(this.ingredientsObj)
            })
        },
        // gets details of recipes
        recipeDetails (recipeID) {
            axios({
                url: this.baseURL + this.lookupURL,
                method: 'get',
                headers: {
                    Accept: 'application/json',
                },
                params: {
                    i: recipeID,//change to int id
                }
            }).then(res => {
                // assign drink response to variable for easier access
                let recipeResponse = res.data.drinks[0]
                // construct recipe object
                this.myRecipes[recipeResponse.strDrink] = {
                    name: recipeResponse.strDrink,
                    id: recipeID,
                    glass: recipeResponse.strGlass,
                    instructions: recipeResponse.strInstructions,
                    image: recipeResponse.strDrinkThumb,
                    ingredients: {}
                }
                // get arrays of keys for ingredients and measures
                let recipeIngredients = Object.keys(recipeResponse).filter(eachString => {return eachString.includes('Ingredient')})
                let recipeMeasures = Object.keys(recipeResponse).filter(eachString => {return eachString.includes('Measure')})
                // iterate over non-null ingredients and add them and their measures to object
                recipeIngredients.forEach((item, index) => {
                    if (recipeResponse[item]) {
                        this.myRecipes[recipeResponse.strDrink].ingredients[recipeResponse[item]] = recipeResponse[recipeMeasures[index]]
                    }
                })
                this.saveToLocal()
                // console.log(this.myRecipes)
            })
        },
        // finds number of missing ingredients per recipe
        missingIngredientCount () {
            // iterate through each recipe
            Object.keys(this.myRecipes).forEach(thisRecipe => {
                // reset counter for missing ingredients
                let numMissing = 0
                // iterate through each ingredient in the recipe
                Object.keys(this.myRecipes[thisRecipe].ingredients).forEach(thisIngredient => {
                    // increment counter if a missing ingredient is found
                    if (!(this.myIngredients.includes(thisIngredient))) {
                        numMissing++
                    }
                })
                // add an empty array at the index matching the number of missing ingredients if an array is not already present
                if (!(this.possibleRecipes[numMissing])) {
                    this.possibleRecipes[numMissing] = []
                }
                // add recipe to possibleRecipes array at the index position matching the number of missing ingredients
                this.possibleRecipes[numMissing].push(thisRecipe)
            })
            // console.log(this.possibleRecipes)
        },
        // saves myIngredients and myRecipes arrays to local storage
        saveToLocal () {
            const parsedMyIngredients = JSON.stringify(this.myIngredients)
            localStorage.setItem('myIngredients', parsedMyIngredients)
            const parsedMyRecipes = JSON.stringify(this.myRecipes)
            localStorage.setItem('myRecipes', parsedMyRecipes)
        },
        // loads myIngredients and myRecipes arrays from local storage
        loadFromLocal () {
            if (localStorage.getItem('myIngredients')) {
                this.myIngredients = JSON.parse(localStorage.getItem('myIngredients'))
            }
            if (localStorage.getItem('myRecipes')) {
                this.myRecipes = JSON.parse(localStorage.getItem('myRecipes'))
            }
        },
        // resets local storage
        clearLocal () {
            this.myIngredients = []
            this.myRecipes = {}
            localStorage.clear()
        },
    }
}).mount('#app')