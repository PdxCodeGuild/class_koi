# capstone_demo_macro_tracker

## Overview
For fitness enthusiasts on the internet, there has yet to be a single place where users can calculate and track macronutrients.  (sentence explaining macronotrients).  The goal of this project is to have one web app that users can visit to track their fitness goals & progress.  The project will be built in Django and Vue.js.

## Features
#### As a **fitness enthusiast**, I want a **simple, easy to way to calculate macronutrients for rest days and training days** because **I'd like to know how much of which macronutrients to eat on which days**.
### Tasks:
* Create Django models for daily nutrition intake (calories, fat, protein, carbs, rest/training day)
* Create a form for the user to fill out with limited information (weight, bf%, activity level, goal (weight loss/muscle gain))
* Create a view that parses the form, does the calculations, saves those to the db, and present the user with that information.
* Create a template that shows the macronutrients to the user in a pleasing fashion (chart.js pie chart?!?)

#### As a **fitness enthusiast**, I want to **track calorie and macronutrient intakes throughout the day** because **I want to know how much more I have left to eat each day and what types of food**.
### Tasks:
* Create Django models representing meals that a user tracks each day (calories, fat, protein, carbs, name)
* Create a form for the user to submit that has the information about each meal.
* Create a view that receives the form submission, saves the meal to the db, and returns the macronutrient and calorie totals for the day to the user.
* Show on the frontend (custom canvas animated bar graph?) how the user's progress is coming throughout the day.

#### As an **admin**, I want to **be able to delete comments that break community rules** because **I want this site to remain a positive, supportive place for everyone**.
### Tasks:
* Create an admin Group which has the ability to delete any comment or post.
* For the admin UI, add a delete button to each comment/post.
* Create a view for deleting comments/posts.

### Additional Features:
* API to look up nutrition facts live on the page
* FAQ about macronutrients and strength training
* Hotpink & Greenyellow

## Schema (Data Model)
* NutritionGoal
  - training_day (boolean field, `True` for training day, `False` for rest day)
  - calories (integer field, calorie goal for the day)
  - fat (integer field, fat (g) goal for the day)
  - carbs (integer field, carbs (g) goal for the day)
  - protein (integer field, protein (g) goal for the day)
  - user (foreign key to User)
* DiaryEntry
  - name (charfield, name of the food)
  - calories (integer field, calorie goal for the day)
  - fat (integer field, fat (g) goal for the day)
  - carbs (integer field, carbs (g) goal for the day)
  - protein (integer field, protein (g) goal for the day)
  - date (foreign key to Day)
* Day
  - date (datefield)
  - training_day (boolean, true for training day, false for rest)
  - user (foreign key to User)

## Schedule
### Week 1
* Create & Clone Repo
* Create Virtual Environment
* Start Django Project
* Write Models
* MVP of macronutrient goal creation (user enters info, site gives user macronutrients for rest and training days)
  
### Week 2
* MVP of daily meal tracking (user enters meals, site logs meal and shows user macronutrient/calorie totals and amounts remaining for that day)
* start css (hotpink & greenyellow placeholder color scheme 🥺)
* chart.js pie charts for macronutrient totals

### Week 3
* Custom dynamic bar chart (animated in canvas) for daily totals
* more css tweaking
* add calendar to go between days
  
### Week 4
* deploy to heroku
* additional styling tweaks
* add comment/like system


## Feature Tiers:
### Must Haves
* Macronutrient goal creation
* Daily tracking
* User creation
  
### Should Haves
* Sleek UI
* Ability to change day from rest to training (or vice-versa)
* Graphic aids to information (macronutrients and daily tracking)

### Can Haves
* Custom Dynamic Bar Chart
* Calendar
* API for looking up nutrition info

### Won't Haves
* user comments and likes
* a color scheme that is not hotpink/greenyellow