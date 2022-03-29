# Count Words Version 1

import string
# Open the file
with open('data/metamorphosis.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

translator = str.maketrans('','', string.punctuation + '“”')
# strip punctuation and Make everything lowercase
string_without_punct = contents.translate(translator).lower()
# split into a list of words on the space
word_list = string_without_punct.split()

stopwords = ['the','to','and','he','his','of','was','had','in','it','my','we','you','that','a','as','with','she','him','her','not','would'
'at','but','for','they','on','all','at','be','out','have']
word_dict = {}
for word in word_list:
    if word not in stopwords:
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1

print(word_dict)

words = list(word_dict.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(words[i])

