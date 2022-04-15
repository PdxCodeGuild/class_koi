import requests
import time
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
    
    print('-'*72)
    search_term = input("\nWhat term would you like to search by? Enter a word or 'Q' to exit:\n").upper()
    # more_jokes = int(input("\nHow many jokes would you like? Enter a number with maximum of 20.\n"))
    
    if search_term == 'Q':
        print("\nGo ask Mom for jokes. Good-bye.\n")
        break

    else:
        response = requests.get('https://icanhazdadjoke.com/search', params = {'term':search_term, 'limit': 5 }, headers = {'accept':'application/json'})
                                                                              #'page':num_page,'limit':more_jokes
        # print(response)
        # print('-'*72)
        # print(response.text)
        # print('-'*72)
        jokes_data = response.json()['results']
        
        for j in jokes_data:
            joke = j['joke']
            time.sleep(1)
            print('-'*72)
            print(f'\n{joke}\n')
            
            
    