import requests
from pprint import pprint

response = requests.get('https://officeapi.dev/api/quotes/random')

# print(response)
# print(response.text)
# print(type(response.text)) # <class 'str'>

data = response.json()
# print(data)
# print(type(data)) # <class 'dict'>



# pprint(data)

print(data['data']['content'])
character = data['data']['character']
print(f"––{character['firstname']} {character['lastname']}")

# response = requests.get('https://cnn.com')
# print(response.text) # the entire html of the cnn home page