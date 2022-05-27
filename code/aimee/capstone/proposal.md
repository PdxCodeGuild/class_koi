# Fiber Amie

## Project Overview

Major features:
- Needle and/or crochet hook virtual organization
- Yarn stash database
- Project tracker

There is currently a gap in the fiber app/website market where no mobile-friendly, accesible, English-language knitting/crochet companion app exists. This application is intended to fill that gap. 

## Features

### As a user, I want to keep track of which needles/hooks I have, because I don't want to get up to go look.
> - Allow users to input which needles/hooks they have (and how many of each)
> - Allow users mobile-friendly access to their list of tools
> - Allow users to select whether a pair of needles or hook is currently being used
> - Allow users to toggle whether they want to track only knitting, only crochet, or both

### As a user, I want to keep track of all of the yarn in my stash, so I can easily find out if I have the right fiber for a new project.
> - Give users a form to input yarn into their stash database (w/ multiple fields)
> - Allow users to upload pictures of the yarn

### As a user, I want to keep track of what projects I'm doing because I want to track my progress.
> - Allow users to add "New Project" and input date started, photos, notes, and upload the pattern if they have it.
> - Filter/sort projects by date

### As a user, I want a mobile-friendly, accessible application because the largest knitting/crochet website, Ravelry.com, recently introduced a new design and many people are no longer able to use the site. 
> - Accessible and low-contrast design
> - Small-scale usability testing will be conducted, if time allows

## Data Model
>Needle/Hook Database 
>- Straight Needles
>    - NeedleSize
>    - NeedleLength
>    - Material
>- Circular needles 
>    - CordLength (if fixed)
>    - NeedleSize
>    - NeedleLength
>    - Material 
>- Double Pointed Needles
>    - NeedleSize
>    - NeedleLength
>    - Material
>- Hooks
>    - HookSize
>    - Material 

>Yarn Stash Database
>- FiberType
>- Yardage
>- Weight (DK, Worsted, etc)
>- Brand 
>- Colourway
>- Image
>- Weight (in oz) - possibly

>Project Tracker
>- PatternName
>- PatternFile (upload)
>- DateStarted
>- DateCompleted
>- Notes
>- Image(s)

>User System 
>- Username
>- Password
>- FirstName
>- LastName

## Schedule

Essential Features and order of implementation:
- Set up project (Django, Vue) - 1-2 day(s)
- Set up User process - create account, log-in - 1 day - MILESTONE!
- Complete very basic styling - 1 day
- Set up needle/hook storage - 2 days - MILESTONE
- Set up yarn stash - 2 days - MILESTONE
- Project tracking -2 days - MILESTONE
- Final styling - 2-3 days - MILESTONE

Really want to have:
- Ability to upload images (probably 2 days)
- Responsive design - 2 days
- Database for circular needle cords - 1 day

Nice to have: 
- Custom icons 
- User testing - several days minimum for feedback

After capstone:
- Figure out if there's a way to actually turn this into a mobile app



