

# Lab 7:  Jackalope Simulator –– Mob

<<<<<<< HEAD
### Note1: there is now a `code/mobs/` folder in the repo.  Create a folder for your mob team inside of that folder and put your python script in there: `code/mobs/team-jackalope/lab07.py`

### Note2: this is a mob lab.  There is only need for one branch.  Whoever drives (types) first can create the branch and push it up.  Then the next driver will checkout the branch and start working on their computer.
=======
#### Note 1: there is now a `code/mobs/` folder in the repo.  Create a folder for your mob team inside of that folder and put your python script in there: `code/mobs/team-jackalope/lab07.py`

#### Note 2: this is a mob lab.  There is only need for one branch.  Whoever drives (types) first can create the branch and push it up.  Then the next driver will checkout the branch and start working on their computer.
>>>>>>> 595f0c6ff23f6b8bdcafff063e70fcf34b5894b2

### Git Setup:
```sh
> git checkout main
> git pull
> git checkout -b your-team-name/python/lab07
```

## Version 1

The goal is to calculate how many years it will take for two age 0 jackalopes to create a population of 1000.

- Jackalopes are reproductive from ages 4-8 and die at age 10.
- Gestation is instantaneous. Each gestation produces two offspring.
- Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do

With these conditions in mind, we can represent our population as a list of ints.

## Version 2 (Optional)

Now let's give the jackalopes distinct sexes and extend their gestation period to one year. We can represent each jackalope with a dictionary, thus our population will be a list of dictionaries. A jackalope will have the following properties:

- name
- age
- sex
- whether they're pregnant

Jackalopes can only mate with those immediately around them. Every generation Jackalopes are randomly shuffled.

### Git Add, Commit & Push:
```sh
> git add files-to-be-added
> git commit -m "your commit message goes here"
> git push -u origin your-team-name/python/lab07
```

### Git Checkout Existing Branch
When it's time for a new driver to type:
```sh
> git fetch # this will pull down the new branch if that hasn't happened yet
> git checkout your-team-name/python/lab07
```
Now you can work on the same branch locally.  Add, commit, and push when done (after the branch has been pushed up to GitHub, `git push` alone will suffice).

Once the work is finished, go to the repository to create a PR.
