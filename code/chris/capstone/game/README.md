# storied_game

## Overview
Games are fun. For some, games are like sports and getting better at the game in a competitive setting is what makes it fun. For others, a game is like a movie or a book where the story and the characters are the center of what makes it fun. The goal of this project is to create a RPG-style game with a central focus on story, and small competitive elements, styled after wordle.  The project will be built in Django and Vue.js.

## Features
#### As a **lover of stories**, I want a **quick and socialized daily dose of RPG gaming** because **I'd like to game but not for a long time**.

### MVP:
  * input field for user to enter commands
  * a place for responses to render
  * an ending alert or change in state
  * track completion of this story

### Tasks:

* Create Django models
  * Playable character (name, health points (?))
  * Inventory (swords, shields, books, first aid kits)
  * enemies
  * game environment/map -- text based
    * the map might be the same as the story because it's text-based
* Create a place where all this info can render.

### Additional Features:
* API usage (?)
* Daily release of new stories
* Track user completion of stories and let them build streaks
  * 2 days in a row: Player
  * 5 days in a row: Hero
  * 14 days in a row: Mage
  * 30 days in a row: Master
  * 45 days in a row: Master Mage
  * 90 days in a row: Storied Hero
  * 180 days in a row: Legendary
* Additional stories availabe for purchase

## Schema (Data Model)
* Story
  - name (charfield, name of the story)
  - one to many rxship with prompts
* StoryPrompts ()
  - prompt (textfield, prompt to the user on what's happening)
  - story (foreign key to story)

## Schedule
### Week 1
* Create & Clone Repo
* Create Virtual Environment
* Start Django Project
* Write Models
* MVP of text-based game where user enters commands and goes through a basic map
  
### Week 2
* Continue development of first MVP game
* MVP of tracking daily game completion
* start css

### Week 3
* more css tweaking
* add calendar to go between days
  
### Week 4
* deploy to heroku
* additional styling tweaks
* Develop a back log of games to release on a daily basis, ideally have them release automatically at a certain time


## Feature Tiers:
### Must Haves
* game prompts with user input field
* Daily tracking
* multiple stories
  
### Should Haves
* Sleek UI
* user sign-up and login

### Can Haves
* graphic interface
* 

### Won't Haves
* social media integration
* games for sale
* 