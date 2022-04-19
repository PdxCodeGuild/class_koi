
import requests
from time import sleep
# VERSION 1
response = requests.get('https://icanhazdadjoke.com/',  headers={'Accept': 'application/json'})

data = response.json()

print(data['joke'])

# VERSION 2

play_again = 'Y'
while play_again == 'Y':
    
    search_term = input("What dad jokes would you like to search for? ")
    search = requests.get('https://icanhazdadjoke.com/search', headers={'Accept': 'application/json'}, params={'limit': '20', 'term':search_term})  
    searches = search.json()
    x = searches['results'] 
    i=0
    while i < len(x):
        print(x[i]['joke'])
        sleep(.5)
        i+=1
    play_again = input("Would you like to search for more jokes? Y or N ").title()