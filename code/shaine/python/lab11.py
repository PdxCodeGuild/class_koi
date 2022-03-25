import string

#  *'-.-'*'-.-'*'-.-'*'--'*
#     Project: Python 
#   Lab 11: Compute Automated Readability Index
#       Version: 1.0
#   Author: Shaine Warren
#   Email: mwarren86@gmail.com
#       Date: Mar, 2022
# *'-.-'*'-.-'*'-.-'*'--'*


with open('class_koi/code/shaine/python/data/little_women.txt', mode='r', encoding='utf-8') as f:
    contents = f.read().split('\n')

# print(contents)


str_cont = str(contents)
# print(str_cont)

sentences = str_cont.count('.') + str_cont.count('!') + str_cont.count('?') 



# https://stackoverflow.com/questions/16050952/how-to-remove-all-the-punctuation-in-a-string-python
remove_puncs = "".join(char for char in str_cont if char not in string.punctuation)

split = remove_punc.split()

words = strip.split(" ")

print(words.count("''"))

# sentences = len(contents.split('. '))

# print(sentences)

# use .count(.) to count sentences

# use len() to count the splits in a list

# strip(string.punctuation) maybe use this to count sents

# new = str(sentences)

# print(new)

# more_new = new.count('. ')

# print(more_new)