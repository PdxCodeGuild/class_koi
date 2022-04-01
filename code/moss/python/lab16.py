import requests
from pprint import pprint

response = requests.get('https://icanhazdadjoke.com/', headers = {'accept':'application/json'})

print(response)
print('-'*72)
print(response.text)
print('-'*72)
dad_joke = response.json()
print(dad_joke['joke'])
print('-'*72)