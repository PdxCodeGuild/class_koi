'''
PDX Code Guild - Class Koi
Lab 16 - Dad Joke API
Matt Walsh
'''


# Version 1
'''
# import api requests module
import requests

# set header
header = {'Accept': 'application/json'}

# request joke and use json method to convert to dictionary
response = requests.get('https://icanhasdadjoke.com/', headers=header)
response = response.json()

# display joke
print(response['joke'])
'''


# Version 2

# import api requests and sleep modules
import requests
from time import sleep

def get_jokes(search_term,page):
    """
    Returns and displays dad jokes based on search term
    """
    # set header
    header = {'Accept': 'application/json'}

    # request joke and use json method to convert to dictionary
    response = requests.get('https://icanhasdadjoke.com/search?term=' + search_term + '&page=' + page, headers=header)
    response = response.json()

    # assign jokes list to variable
    jokes_list = response['results']

    # assign total number of jokes, pages, and current page to variables
    num_jokes = response['total_jokes']
    num_pages = response['total_pages']
    current_page = response['current_page']
    if current_page < num_pages:
        current_jokes = f'{(current_page * 20) -19}-{current_page * 20}'
    else:
        current_jokes = f'{(current_page * 20) -19}-{num_jokes}'

    # display info about search
    if num_jokes == 0:
        print(f'There weren\'t any jokes about {search_term}.\n')
    else:
        print(f'There are {num_jokes} jokes about {search_term}. You are viewing {current_jokes}.\n')

    # display jokes
    for joke in jokes_list:
        sleep(1)
        print(joke['joke'] + '\n')

    # return bool based on whether there are more jokes for the current search term
    if current_page < num_pages:
        return True
    else:
        return False

while True:
    # ask for user input and set starting page to 1
    search_term = input('What would you like to see dad jokes about (enter "quit" to exit)? ')
    page = '1'
    # allow user to exit
    if search_term.lower() == 'quit':
        break
    else:
        while True:
            # let user choose to view more jokes or return to search prompt
            if get_jokes(search_term,page):
                keep_going = input('Would you like to view more? Y/N? ')
                if keep_going.lower() == 'y':
                    # convert page variable to int for maths, then back to string
                    page = str(int(page) + 1)
                else:
                    break
            else:
                break