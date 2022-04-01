# LAB 16: Dad Joke API ----------- #

# JSON - JavaScript Object Notation 

# Application Programming Interface

import requests

response = requests.get('https://api.ipify.org')


print(response) # response[200] is a successful response
print(response.text)
print(type(response.text))

data = response.json()
print(data)
print(type(data)) # <class 'dict'>

print(data['data'])
print(data['data']['character']['firstname'])