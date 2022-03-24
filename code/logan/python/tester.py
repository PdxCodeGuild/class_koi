string = "Look at that dog.  What a cute dog!  Whose dog is that?"

exceptions = ["Mr.", "Dr.", "Sr.", "Jr.", "Ms.", "Mrs.", "P.S."]


# testsplit = string.split("." or "!")

stringscrub = string.replace("!", "~")
stringscrub = stringscrub.replace("?", "~")
stringscrub = stringscrub.replace(".", "~")

newlist = stringscrub.split("~")

print(newlist)
# print(testsplit)


