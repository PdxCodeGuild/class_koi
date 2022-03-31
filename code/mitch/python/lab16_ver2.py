# Lab 16: Dad Joke API
# Part 2
# Mitch Chapman

import requests
import time

search_term = "hipster"

response = requests.get(f'https://icanhazdadjoke.com/search?term={search_term}', headers={'Accept': 'application/json'}).json()

for data in response['results']:
    print(data['joke'])
    time.sleep(4)



print('Welcome to the Dad Joke headquarters!')
while True:
    user_search_response = input("Would you like to search for a topic for the Dad Joke ('y' or 'n'): ")
    if user_search_response not in ['y', 'n']:
        print('Invalid responce.')

    elif user_search_response == 'y':
        ...
        
    elif user_search_response == 'n':
        ...
