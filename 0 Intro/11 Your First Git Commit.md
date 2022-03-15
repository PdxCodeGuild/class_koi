# Your Fist Git Commit

## Step 1: Clone The Repo

First of all, decide where you want the class repo to be in your computer's filesystem.  This is a personal preference, but it makes sense for it to be somewhere that's relatively quick and easy for you to navigate to in your terminal. 

In my home, `/Users/pete`, I have a `code-guild/` folder.  So, I keep all my class repos in there:
```sh
> pwd # I'm in my home directory
/Users/pete
> cd code-guild
> pwd # now I'm in the code-guild directory
/Users/pete/code-guild
```
Now I'm where I want to be to clone the repo.

### `git clone [repo-url]`
`git clone` will pull down the repo from origin (in this case GitHub).  You can get the repo URL by clicking on the green "Code" button on the main page of the repo:

![Green Code Button](green-code-button.png)

You can copy that url, or just run this command here:
```sh
> git clone https://github.com/PdxCodeGuild/class_koi.git
> # there will be a bunch of output here showing the repo being downloaded...
> # then you can cd into it
> cd class_koi
```

#### Note: do recent changes requiring multi-factor authentication on GitHub, some users might have to run `git clone git@github.com:PdxCodeGuild/class_koi.git` instead.



## Using Git With VS Code:
[https://code.visualstudio.com/docs/editor/versioncontrol](https://code.visualstudio.com/docs/editor/versioncontrol)