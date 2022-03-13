# Command Line Cheat Sheet

Check out the [Command Line Crash Course](https://cglab.ca/~morin/teaching/1405/clcc/book/cli-crash-course.html)

Recommended bash emulator for Windows: [cmder](https://cmder.net)

#### Note: this guide is for bash consoles.  Most, but not all, of these command will work on Windows' PowerShell console.

## Read-Only Commands: `pwd` & `ls`
These commands are your best friends when trying to understand where you are in your filesystem and what other files and directories are there with you.

### `pwd`
`pwd`, or **print working directory**, prints the filepath to your working directory, where you currently are:

```sh
> pwd
/Users/pete/code-guild/class_koi
```

The `/` at the very start represents the root of the filesystem.  On Windows, this is the C: drive.  In this Mac filesystem, there is a directory at the root called `Users/`.  Inside of that is the directory for the user `pete/`, and so on and so forth.

#### Note: the `>` in the examples is not something that you type.  It represents the terminal cursor.  You would just type `pwd` in the example above.

### `ls`
`ls`, or **list**, prints out the files and folders in your working directory:

```sh
> ls
0 Intro/  1 Python/  2 Flask/  3 HTML + CSS/  4 Django/  5 JavaScript/  6 Capstone/  code/  koi.png  LICENSE  README.md
```

#### Note: the terms "directory" and "folder" are used interchangeably here.  They mean the same thing.

### `ls -a`
`ls -a` or **list all** is an example of the use of a flag.  The `-a` is a flag that will list hidden files and folders as well:

```sh
> ls -a
.  ..  .git/  .gitignore  0 Intro/  1 Python/  2 Flask/  3 HTML + CSS/  4 Django/  5 JavaScript/  6 Capstone/  code/  koi.png  LICENSE  README.md
```
Now you can see a hidden file: `.gitignore` 

And hidden directories: `.`, `..` & `.git`

#### Note: `.` and `..` are special notations that are always in your working directory. `.` always represents where you currently are and `..` always represents the parent directory.  We'll come back to this later when talking about `cd`.

### `ls [filepath]`
You can also give `ls` a filepath argument.  By default, `ls` shows the contents of the working directory.  But, given a valid filepath to another direcoty, it will list the contents of that one instead:

```sh
> ls code
dustin/  lisa/  pete/
```
The `code/` folder contains folders of the work of students and staff.  Everyone who contributes to the repo will have their own folder here to upload assignments.  `ls code` here shows us the child folders of `code`, one for each staff member.

## Navigation: `cd`

### `cd [filepath]`
`cd`, or "change directory" is used for changing your working directory.  Given a valid filepath to another directory, it will change your working directory to that one.

#### Note: just like Python, `#` can be used for comments in the terminal.  Anything after `#` will be ignored and won't be interpreted as a command:

```sh
> # use pwd to double check where we are
> pwd
/Users/pete/code-guild/class_koi
> # cd into the code directory
> cd code
> # check filepath now
> pwd
/Users/pete/code-guild/class_koi/code
> # see what's inside this folder
> ls
dustin  lisa  pete
```

### `cd ..`
`..` is a special notation that *always* represents the parent folder of the working directory.  Therefore, you can *always* use `cd ..` to "go up" one directory:
```sh
> pwd
/Users/pete/code-guild/class_koi/code
> # we're still in the code folder, let's go back into class_koi
> cd ..
> pwd
/Users/pete/code-guild/class_koi
> # let's go up another and get outside of class_koi
> cd ..
> pwd 
/Users/pete/code-guild
> # by the way, you can chain together a longer filepath to traverse multiple directories in one command
> cd class_koi/code
> pwd
/Users/pete/code-guild/class_koi/code
```

### `cd /`
The previous arguments given to `cd` have been **relative filepaths**.  This is an example of an **absolute filepath**.  `cd /` takes you to the root of your filesystem.  It is the parent folder of all of the data saved on your computer.  Use `ls` there to take a peek at what all is stored at the root.

#### Note: an **absolute filepath** represents the same location in the filesystem no matter where your working directory is.  A **relative filepath** is relative to the working directory.

### `cd ~`
`~` represents the current user's home directory in the file system.  For me, that is `/Users/pete`.  Let's say I've `cd`-ed into many folders and I'm now here:
```sh
> pwd
/Users/pete/code-guild/class_koi/code/lisa/javascript/examples/vueseum
> cd ~
> pwd
/Users/pete
```

#### Note: in most bash terminals, `cd` with no arguments has the same effect as `cd ~`.  Both commands go to the home directory.