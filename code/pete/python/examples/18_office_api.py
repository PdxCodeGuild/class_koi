import requests
import cowsay
import random
from pprint import pprint


characters_dict = cowsay.chars
characters = list(cowsay.chars.keys())
# pip install requests
# pip3 install requests
# py -m pip install requests

response = requests.get('https://officeapi.dev/api/quotes/random')

# print(response) # <Response [200]>
# print(type(response))
# print(response.text)
# print(type(response.text)) # <class 'str'>

data = response.json()
# print(data)
# print(type(data)) # <class 'dict'>
# pprint(data) # pretty printer makes it easier to parse dictionary visually

cowsay_char = random.choice(characters)

characters_dict[cowsay_char](data['data']['content'])
character = data['data']['character']
print(f"––{character['firstname']} {character['lastname']}")