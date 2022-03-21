# (If you’re on a Mac, replace ctrl with cmd)


#### TIP: ALWAYS LOOK AT WHAT BRANCH YOU'RE ON BEFORE DOING ANY WORK, OR COMMITTING/PUSHING/PULLING CODE-------------------------------------------------------------------------------

###  General computer commands 
# Ctrl + a = select everything
# Ctrl + c = copy 
# Ctrl + x = cut
# Ctrl + v = paste
# Ctrl + z = undo
# Ctrl + y = redo
# Ctrl + f = find in page (works on all internet browsers, vs code, the terminal, and more)

#-------------------------------------------------------------

###  VSCode tips and tricks
# -Comment out the current line, or all selected lines in any programming language: 
#       ctrl + ?
# -Highlight all instances of a word: 
#       highlight the word/phrase, and hit ctrl + d
# -Copy a word or multiple lines of code directly above or below: 
#       highlight the word/lines of code, and hit alt + shift + up/down arrow key
# -Move a line or lines of code up or down as far as you want without copying it (if you want to move a bunch of lines, roughly highlight everything; if it’s just one line, you only need to click on it - no highlighting needed): 
#       alt + up/down arrow key
# -Cycle through old cli commands already entered: 
#       up arrow key
# -Create a new line without splitting the line you're on: 
#       ctrl + enter/return
# -Turn on word wrap (your code will never be out of sight, and it won't change your line numbers): 
#       alt + z

# -Which pip packages do I already have installed? 
#       python3 -m pip list

# cd into a directory without having to type up the whole name:
#       type 'cd ' followed by the first letter(s) of the folder you want to move into, and hit tab to finish the word. if the first suggestion isn't quite right, keep hitting tab until you get what you need.

#-------------------------------------------------------------

###  Some git explanations and command line tricks (including branch help)
# -Remote repository: the repo as it exists on github
# -Local repository: the repo as it exists on your computer
# -git push: code from your local repo is sent to the remote repo on github; this is done through the terminal.
# -git pull: pull code from the remote repo on github to your local repo; this is done through the terminal. 
# -pull request (pr): code from one branch is merged into main; it’s called a pull request because you’re pulling your code from one branch to another. These are made by on github, not through the terminal. 

# –Which branch am I in?
#       Git status

# -Create a branch:
#       git checkout -b <newbranchname>

# -Push a new branch to github:
#   git add . (or filename, if you don't want to add everything)
#   git commit -m 'made a new branch'
#   git push --set-upstream origin <branchname>
#   note: if you follow the standard committing procedure below, github will tell you the push command you need, which makes it nice and easy to do. 

# –Switch branches (replace branchname with the name of your own branch)
#   git checkout <branchname>

# –Commit all changes to github:
#   git add .
#   git commit -m ‘this is my commit message’
#   git push

# –Commit only some changes to github
#   git add <filename>
#   git commit -m ‘commit only this to github’
#   git push



