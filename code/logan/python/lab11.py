from string import punctuation

# f = open('iliad.txt')
with open('gatsby.txt', 'r', encoding = 'utf-8') as f:
    contents = f.read()

# Maybe in a future version I'll code a way to not make
# "Dr. T. J. Eckleburg" count as four sentences....

stringscrub = contents
stringscrub = stringscrub.replace("!", "~")
stringscrub = stringscrub.replace(".", "~")
stringscrub = stringscrub.replace("?", "~")
stringscrub = stringscrub.replace("\n", "")
sentence_list = stringscrub.split("~")
sentence_list.pop()

#Here is our sentence count:
sentence_count = len(sentence_list)

#Now let's get the number of words...

# This isn't getting all the punctuation, 
# some chars in the file must not be standard
# marks caught by punctuation from string 

for char in punctuation:
    stringscrub = stringscrub.replace(char, "#")
stringscrub = stringscrub.replace(" ", "#")


word_counter = 0
for i in range(len(stringscrub) -1):
    if (stringscrub[i] != "#") and (stringscrub[i +1] == "#"):
        word_counter += 1

# finally, let's count characters

stringscrub = stringscrub.replace("#", "")
char_counter = len(stringscrub)

## Debugging
print(stringscrub)
# print(word_counter)
# print(sentence_count)
# print(sentence_list)













# f.close()