'''
PDX Code Guild - Class Koi
Lab 17 - Quotes API
Matt Walsh
'''


# Version 1
'''
# import api requests, cowsay, and randint modules
import requests
import cowsay
from random import choice

# request quote and use json method to convert to dictionary
response = requests.get('https://favqs.com/api/qotd')
response = response.json()

# assign quote and name to variables
quote = response['quote']['body']
name = response['quote']['author']
first = name.split()[0]
last = ' '.join(name.split()[1:])

# make dictionary and list of cowsay characters
char_dict = cowsay.chars
char_choice = choice(list(char_dict))

# display quote in randome cowsay character
char_dict[char_choice](f'{quote}\n--{first} "{char_choice.title()}" {last}')
'''


# Version 2

# import modules
from requests import get
from modules.input_validation import valid_str
import cowsay
from time import sleep
from random import choice

def get_quotes(keyword,page):
    """
    Gets a page of quotes from QOTD
    """
    # get response from API and convert to dictionary
    header = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    response = get(f'https://favqs.com/api/quotes?page={page}&filter={keyword}',headers=header)
    response = response.json()
    # assign quotes from response to dictionary
    quotes_dict = response['quotes']
    # assign last page bool to variable
    is_last = response['last_page']
    # return error if no quotes found
    if quotes_dict[0]['body'] == 'No quotes found':
        return None
    # return dictionary of quotes and last page bool
    return quotes_dict,is_last

def display_quotes(quotes_dict,page):
    """
    Displays quotes received from QOTD
    """
    # find number of quotes being displayed
    num_quotes = len(quotes_dict)
    print(f'Viewing quotes {(page * 25) - 24}-{((page - 1) * 25) + num_quotes}')
    # loop through quotes
    for each_quote in quotes_dict:
        # pause before displaying each quote
        sleep(2)
        # assign quote and name to variables
        quote = each_quote['body']
        name = each_quote['author']
        first = name.split()[0]
        last = ' '.join(name.split()[1:])
        # make dictionary and list of cowsay characters
        char_dict = cowsay.chars
        char_choice = choice(list(char_dict))
        # display quote in randome cowsay character
        char_dict[char_choice](f'{quote}\n--{first} "{char_choice.title()}" {last}')

# set starting variables
keep_going = True
page = 1
is_last = False
while keep_going:
    # ask for keyword from user
    keyword = input('Please enter a keyword you would like to read quotes about: ')
    # process keyword for proper searching
    keyword = f' {keyword.strip()} '
    # save results to tuple
    quote_results = get_quotes(keyword,page)
    # display error and loop back to top if no quotes were found
    if quote_results == None:
        print(f'No quotes found for {keyword.strip()}')
        continue
    # split results to variables
    quotes_dict = quote_results[0]
    is_last = quote_results[1]
    # display results
    display_quotes(quotes_dict,page)
    # allow display of more quotes if available
    while not is_last:
        # set variables for prompt and pass to function
        prompt = f'There are more "{keyword.strip()}" quotes available. Would you like to see more? Y/N? '
        choices = ['y','n','q']
        error = 'Enter "Y" to see more, "N" to enter a new keyword, or "Q" to quit.'
        display_more = valid_str(prompt,choices,error,False,'lower')
        # handle responses
        if display_more == 'y':
            # increment page number, get, and display quotes
            page += 1
            quote_results = get_quotes(keyword,page)
            quotes_dict = quote_results[0]
            is_last = quote_results[1]
            display_quotes(quotes_dict,page)
        elif display_more == 'n':
            # set variables for prompt and pass to function
            prompt = 'Would you like to look at more quotes? Y/N? '
            choices = ['y','n']
            error = 'Enter "Y" search again or "N" to quit.'
            search_again = valid_str(prompt,choices,error,False,'lower')
            if search_again == 'n':
                keep_going = False
            break
        elif display_more == 'q':
            keep_going = False
            break
    # tell user they've reached the end of the quotes for that keyword
    if is_last:
        print(f'There are no more quotes about "{keyword.strip()}".')