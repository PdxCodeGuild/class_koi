'''
Lab 17: Quotes API

-Version 1: Get a random quote. DONE
-Version 2: List quotes by keyword. DONE
    -> prompt user for keyword, 
    -> list the quotes, 
    -> prompt for next page or new keyword
-Potential Improvement: incorporate classes?
'''

import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
}
# -- PART ONE -- #

response = requests.get('https://favqs.com/api/qotd', headers=headers)

response_dict = response.json()

quote_dict = response_dict['quote'] # {'id': , ... , 'body': 'sentences.'}

print(quote_dict['body'], '\n -- ', quote_dict['author'])

# -- PART TWO -- #

print('# -- PART 2 -- #')

page_number = 1

def get_user_search(): # gets the user term to search for and returns it as string
    while True:
        user_search_term = input('Enter a term to search for related quotes or done: ').lower()
        if user_search_term == 'done':
            exit()
        return user_search_term

def search_dict_fn(tag, p_num): # takes the user search term and page number and creates a dict for params
    search_terms = {
        'filter': tag,
        'page': p_num,
    }
    return search_terms

def quote_search(header_dict, search_params): # search params defined by search_dict_fn()
    search_response = requests.get('https://favqs.com/api/quotes', headers=header_dict, params=search_params)
    search_data = search_response.json()
    return search_data

def print_quotes(data_input): # prints quotes on the selected page
    for quote in data_input['quotes']:
        print(quote['body'], '--', quote['author'], '\n')

def quote_nav(data): #navigates through the pages, modifying page_number as necessary
    while True:
        if data['last_page'] == False: # if not last page:
            print_quotes(data) # print the quotes
            next_page = input('Enter next for next page page or done for done: ') # user decides to keep going or be done
            if next_page == 'next':
                global page_number # call the global page_number
                page_number += 1 # add 1
                search_tags = search_dict_fn(user_tag, page_number) # I guess this is a local version of search_tags, which is fine
                data = quote_search(headers, search_tags) # quote_search() makes the request with the same headers and the new page_number
            elif next_page == 'done':
                break
            else:
                print('invalid entry.')
        elif data['last_page'] == True:
            print_quotes(data)
            print('Last page.\n------------------------------------')
            break

while True:
    
    page_number = 1 # reset page number parameter

    user_tag = get_user_search()

    search_tags = search_dict_fn(user_tag, page_number)

    quote_data = quote_search(headers, search_tags)

    quote_nav(quote_data)
