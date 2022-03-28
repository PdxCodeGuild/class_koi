# defining strings

message1 = 'this is æ string'

message2 = "this is also a string"

message3 = '📸'

print(message1, message2, message3)

message4 = 'single on the outside "double on the inside"'

message5 = "double on the outside 'single on the inside'"

sentence = "I use double quotes if it's more than just a word"

print(message4, message5, sentence)

# escape sequences

escape_message1 = 'Use \'backslashes\' for escaped characters'
print(escape_message1)

formatted_message = 'Esteemed sir,\n\tYou are cordially invite somewhere.\nBest,\nThe Countess'
print(formatted_message)

backslash_string = 'here is the backslash: \\'
print(backslash_string)

# unicode characters with \uXXXX

print('\u0391 \u0392 \u0393 \u0394 \u0395 \u0396')

print('\u0678 \u0259 \u1afe')

# raw string: strings prefixed with r will treat escape characters as their literal values
print(r'this is a raw string \n\t\\')

# ord and chr

# for i in range(97, 97 + 26):
#     print(chr(i))

# for i in range(200):
#     print(chr(i))

# concatenation

first_name = 'Pete'
last_name = 'Jones'
print(first_name + ' ' + last_name)

grocery_list = ['apples', 'bananas', 'oranges']

grocery_string = ''

for grocery in grocery_list:
    grocery_string += grocery + ', '

print(grocery_string)


# string multiplication
print()
print('-'*40)
print('the important thing I\'m looking for is here')
print('-'*40)

# strings and lists
# len function works just the same way
numbers = [1, 2, 3, 4, 5]
message = 'strings are cool'
print(len(numbers), len(message))

# access str[i] wroks like list[i]
print(message[5])

# slicing also works the same way
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
print(colors[2:])

print(message[-4:])

# assginment list[i] = value DOES NOT work for strings: str[i] = value

colors[-1] = 'purple'

print(colors)

# message[0] = 'S' # TypeError: 'str' object does not support item assignment

# string methods
capitalized_message = message.capitalize()
# message = message.capitalize() # if you want to keep the same variable name
print(capitalized_message, message)

# string.find(character)

print(message.find('r')) # 2
print(message.find('gs')) # 5
print(message.find('Z')) # -1

from string import ascii_lowercase

print(ascii_lowercase)

for char in ascii_lowercase:
    index = message.find(char)
    if index == -1:
        print(f'{char} is not in {message}')
    else:
        print(f'{char} is in {message}')

# string.replace(old_substring, new_substring)
print('hello world'.replace('hello', 'goodbye')) # goodbye world
print('hello world'.replace('hello', 'goodbye').replace('goodbye', 'hello')) # hello world
print('hello world'.replace('hello', 'goodbye').replace('goodbye', 'hello').title()) # Hello World

# string.strip
numbers = ['forty-eight', 'forty-nine', 'fifty-', 'fifty-one', 'fifty-two']

for number in numbers:
    print(number.strip('-'))

lots_of_whitespace = '     \n\t\n  \t here is the stuff \n\n more stuf\n\t   '
print(lots_of_whitespace)
print('-'*40)
print(lots_of_whitespace.strip())

from string import punctuation

print(punctuation)
message = '%!(%here is ^$%# the stuff^$#@'
print(message)
print(message.strip(punctuation))
print(message.strip('@!%#'))

print(list(sentence)) # ['I', ' ', 'a', 'm', ' ', 'l', 'e', 'a', 'r', 'n', 'i', 'n', 'g', ' ', 'a', 'b', 'o', 'u', 't', ' ', 's', 't', 'r', 'i', 'n', 'g', 's', ' ', 't', 'o', 'd', 'a', 'y', '.']
# str.split and str.join

sentence = 'I am learning about strings today.'

sentence_list = sentence.split()
print(sentence_list) # ['I', 'am', 'learning', 'about', 'strings', 'today.']

for i, word in enumerate(sentence_list):
    sentence_list[i] = word.capitalize().replace('.', '!')


print(sentence_list)

new_and_improved_sentence = ' '.join(sentence_list)
print(new_and_improved_sentence) # I Am Learning About Strings Today!

slug = '10-islands-you-must-visit-with-your-cat'

title_list = slug.split('-')
print(title_list) # ['10', 'islands', 'you', 'must', 'visit', 'with', 'your', 'cat']

print(slug.split('-', 4)) # ['10', 'islands', 'you', 'must', 'visit-with-your-cat']

print(slug.rsplit('-', 4)) # ['10-islands-you-must', 'visit', 'with', 'your', 'cat']

# using rsplit to find the file type
filename = 'this-is-a-filename.why-does-it.have-dots-before-the-extension.txt'
print(filename.split('.')) # ['this-is-a-filename', 'why-does-it', 'have-dots-before-the-extension', 'txt']
print(filename.rsplit('.', 1)) # ['this-is-a-filename.why-does-it.have-dots-before-the-extension', 'txt']
print(filename.rsplit('.', 1)[1]) # txt

# f-strings
number = 7

# print('print my lucky number is ' + number) # TypeError: can only concatenate str (not "int") to str
print('my lucky number is ' + str(number)) # my lucky number is 7
print(f'my lucky number is {number}') # my lucky number is 7
print(f'here is a list {[1, 2, 3]}') # here is a list [1, 2, 3]

# these are older versions of python formatted strings, before f-strings 
print('my favorite number is {}'.format(number))
print('my favorite number is {lucky_number}'.format(lucky_number=number))

# docstrings: multi line python strings for documentation
def add(x, y):
    """Given numbers x and y, returns their sum"""
    return x + y

print(add(1, 2))