'''
PDX Code Guild - Class Koi
Optional Lab - Count Words
Matt Walsh
'''

 
# Version 1
'''
# import punctuation to strip
from string import punctuation
punctuation += '“”‘’—'
punctuation = punctuation.replace("'",'')
punctuation = punctuation.replace("-",'')

# open and read file
with open('code\matt\python\optional\count_words.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

# strip all punctuation and convert to lowercase
translator = str.maketrans('', '', punctuation)
contents = contents.replace('-',' ')
words_list = contents.translate(translator).lower().split()

# construct dictionary of unique words
word_dict = {}
for word in list(set(words_list)):
    word_dict[word] = 0

# count number of word instances
for word in word_dict:
    word_dict[word] = words_list.count(word)

# define words to ignore then remove from dictionary
stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
for word in stop_words:
    if word in word_dict:
        word_dict.pop(word)

# create list of tuples from word_dict with word and count
words = list(word_dict.items())
# sort largest to smallest, based on count
words.sort(key=lambda tup: tup[1], reverse=True)
# begin displaying results
print(f'\nThe top 10 most used words are:\n\nCOUNT\tWORD\n{"="*20}')
# print the top 10 words, or all words if there are fewer than 10
for i in range(min(10, len(words))):
    print(f'{words[i][1]}\t{words[i][0]}')
'''


# Version 2
'''
# import punctuation to strip
import enum
from string import punctuation
punctuation += '“”‘’—'
punctuation = punctuation.replace("'",'')
punctuation = punctuation.replace("-",'')

# open and read file
with open('code\matt\python\optional\count_words.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

# strip all punctuation and convert to lowercase
translator = str.maketrans('', '', punctuation)
contents = contents.replace('-',' ')
words_list = contents.translate(translator).lower().split()

# iterate through words_list and update to hold word pairs
for i,word in enumerate(words_list):
    if i < len(words_list) - 1:
        words_list[i] = words_list[i] + ' ' + words_list[i + 1]
words_list.pop(-1)

# construct dictionary of unique word pairs
word_dict = {}
for word in list(set(words_list)):
    word_dict[word] = 0

# count number of pair instances
for word in word_dict:
    word_dict[word] = words_list.count(word)

# create list of tuples from word_dict with word pairs and count
words = list(word_dict.items())
# sort largest to smallest, based on count
words.sort(key=lambda tup: tup[1], reverse=True)
# begin displaying results
print(f'\nThe top 10 most used words are:\n\nCOUNT\tWORD\n{"="*20}')
# print the top 10 pairs, or all pairs if there are fewer than 10
for i in range(min(10, len(words))):
    print(f'{words[i][1]}\t{words[i][0]}')
'''


# Version 3

# import punctuation to strip
from string import punctuation
punctuation += '“”‘’—'
punctuation = punctuation.replace("'",'')
punctuation = punctuation.replace("-",'')

# import custom module - run from class_koi
import sys
sys.path.append('./code/matt/python/modules')
from input_validation import valid_str

# open and read file
with open('code\matt\python\optional\count_words.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

# strip all punctuation and convert to lowercase
translator = str.maketrans('', '', punctuation)
contents = contents.replace('-',' ')
words_list = contents.translate(translator).lower().split()

# construct dictionary of unique words with dictionary for words that follow
all_words = list(set(words_list))
word_dict = {}
for word in all_words:
    word_dict[word] = {}

# add following word to word instances in word_dict
for i, word in enumerate(words_list):
    if i < len(words_list) - 1:
        if words_list[i + 1] in word_dict[word]:
            word_dict[word][words_list[i + 1]] += 1
        else:
            word_dict[word][words_list[i + 1]] = 1

x = valid_str('enter',all_words)


print(word_dict[x])



'''
# count number of word instances
for word in word_dict:
    word_dict[word] = words_list.count(word)

# define words to ignore then remove from dictionary
stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
for word in stop_words:
    if word in word_dict:
        word_dict.pop(word)

# create list of tuples from word_dict with word and count
words = list(word_dict.items())
# sort largest to smallest, based on count
words.sort(key=lambda tup: tup[1], reverse=True)
# begin displaying results
print(f'\nThe top 10 most used words are:\n\nCOUNT\tWORD\n{"="*20}')
# print the top 10 words, or all words if there are fewer than 10
for i in range(min(10, len(words))):
    print(f'{words[i][1]}\t{words[i][0]}')
'''