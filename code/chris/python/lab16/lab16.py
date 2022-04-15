'''
Lab 16: Dad Joke API

-only shows 20 jokes
-have not added the bonus to ask the user
 if they want to see the next 20 jokes
'''

import requests
import time

headers = {
    'User-Agent': 'https://www.github.com/cpr2mc',
    'Accept': 'application/json',
}

response = requests.get('https://icanhazdadjoke.com', headers=headers)

response_dict = response.json() # {'id': 'idtext138d', 'joke': 'Sentence 1. Sentence 2.', 'status': 200}

dad_joke = response_dict['joke']

print('Part 1, Random Dad Joke: ', dad_joke)

print('\n')

def dad_joke_search(search_params):
    search_response = requests.get('https://icanhazdadjoke.com/search', headers=headers, params=search_params)

    search_data = search_response.json()
    search_results = search_data['results']

    print(search_data['total_jokes'], ' jokes found.')

    for result in search_results:
        print(result['joke'])
        print('- - - - - - - - - - - - - - -')
        time.sleep(2)

user_term = ''

while user_term != 'exit': # REPL loop
    user_term = input('Part 2: What term would you like to search for (\'exit\' to exit)? ')
    if user_term == 'exit':
        break
    search_term = {'term': user_term}

    dad_joke_search(search_term)
    