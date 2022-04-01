import requests
from pprint import pprint

#----- Version 1 -----#

# response = requests.get('https://icanhazdadjoke.com/', headers = {'accept':'application/json'})

# print(response)
# print('-'*72)
# print(response.text)
# print('-'*72)
# dad_joke = response.json()
# print(dad_joke['joke'])
# print('-'*72)

#----- Version 2 -----#

print('\nWelcome to Dads Have Jokes...\n')

while True:

    search_term = input("\nWhat term would you like to search by? Enter a word or 'Q' to exit:\n").upper()

    if search_term == 'Q':
        print("\nGo ask Mom for jokes. Good-bye.\n")
        break
    
    else:
        response = requests.get('https://icanhazdadjoke.com/search', params = {'term':search_term, 'limit':'1'}, headers = {'accept':'application/json'})
        dad_joke = response.json()                    #or-->search?term=search_term'
        print(dad_joke)