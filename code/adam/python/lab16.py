#Lab 16 - Dad JOke API

# Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ 
# with the accept header as application/json. This will return a dad joke in JSON format. 
# You can then use the .json() method on the response to get a dictionary. 
# Get the joke out of the dictionary and show it to the user.

import requests

headers = {'Accept': 'application/json'}

response = requests.get('http://icanhazdadjoke.com/', headers=headers)
dadjoke_data = response.json()
dadjoke_joke = dadjoke_data['joke']
print(f'Here is a random Dad joke:\n ')
print(f'{dadjoke_joke}\n')

#--------------------------------------------------------------------------
# Part 2
# Add the ability to "search" for jokes using another endpoint. 
# Create a REPL that allows one to enter a search term for dad jokes on different subjects. 
# You can show all (up to 20) jokes at once, or use time.sleep 
# to keep them coming at a steady pace. As a bonus, you can ask the user 
# if they want to see the next 20 jokes.

import time

response2 = requests.get('http://icanhazdadjoke.com/search', headers=headers)
dadjoke_search_data = response2.json()

while True:
    #get subject search term for dad jokes from user
    search_term = input("Enter the subject of dad joke or 'random' for a random joke or 'exit' to exit: ")
    search_term_url = 'http://icanhazdadjoke.com/search?term='+ search_term
    # print(dadjoke_search_data)
    
    if search_term == 'exit':
        break
    if search_term == 'random':
        response = requests.get('http://icanhazdadjoke.com/', headers=headers)
        dadjoke_data = response.json()
        dadjoke_joke = dadjoke_data['joke']
        print(f'\nHere is a random Dad joke: ')
        print(f'{dadjoke_joke}\n')
    else:
        response_search = requests.get(search_term_url, headers=headers)
        response_search_data = response_search.json()
        dadjoke_search_jokes = response_search_data['results']
        result_length = len(response_search_data['results'])
        print(f'Here are {result_length} dad jokes mentioning "{search_term}":\n')
                
        i = 0 
        k = 1
        while i < result_length:
            time.sleep(0.35)
            print(f"{i+1} - {response_search_data['results'][i]['joke']}")
            i += 1
            
        while result_length == 20:
            more_jokes = input(f'\nWould you like the next available Dad jokes about {search_term} [y]es or [n]o: ').lower()
            if more_jokes == 'n':
                break
            elif more_jokes =='y':
                k += 1
                l = str(k)
                next_jokes_url = 'https://icanhazdadjoke.com/search?term=' + search_term + '&page=' + l
                next_jokes_raw = requests.get(next_jokes_url, headers=headers)
                next_jokes_data = next_jokes_raw.json()
                next_jokes = next_jokes_data['results']
                next_jokes_length = len(next_jokes_data['results'])
                j = 0
                print(f"Here are the next {next_jokes_length} jokes: ")

                while j < next_jokes_length:
                    time.sleep(0.35)
                    print(f"{j+1} - {next_jokes_data['results'][j]['joke']}")
                    j += 1
                    if j == next_jokes_length:
                        break
                if j < 20:
                    break



