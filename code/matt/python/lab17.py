'''
PDX Code Guild - Class Koi
Lab 17 - Quotes API
Matt Walsh
'''


# Version 1

# import api requests, cowsay, and randint modules
import requests
import cowsay
from random import choice

# request quote and use json method to convert to dictionary
response = requests.get('https://favqs.com/api/qotd')
response = response.json()

# assign quote and name to variables
quote = response['quote']['body']
name = response['quote']['author']

# make dictionary and list of cowsay characters
char_dict = cowsay.chars
char_list = list(char_dict)

# display quote in randome cowsay character
char_dict[choice(char_list)](quote + '\n--' + name)



# Version 2