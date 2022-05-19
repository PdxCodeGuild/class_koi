#Part 1
import time 
import requests
import json

def returnJoke ():
    url = 'https://icanhazdadjoke.com/'
    response = requests.get(url,  headers={'accept': 'application/JSON'})
    data = response.json()
    joke = data['joke']
    time.sleep(5)
    return joke
    
   
print(returnJoke())
# Part 2
def search_dad_joke():
        term = input("What would you like to search by?")
        url = 'https://icanhazdadjoke.com/search'
        response = requests.get(url,  headers={'accept': 'application/JSON'}, params={'term': term,'limit': 20})
        data = response.json()
        return data

while True:
    print (search_dad_joke())
    
    
    
