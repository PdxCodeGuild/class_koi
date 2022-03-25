'''
Lab 17: Quotes API

-Version 1: Get a random quote. DONE
-Version 2: List quotes by keyword
    -> prompt user for keyword, 
    -> list the quotes, 
    -> prompt for next page or new keyword
'''

import requests

headers = {
    'Content-Type': 'application/json',
}

response = requests.get('https://favqs.com/api/qotd', headers=headers)

response_dict = response.json()
quote_dict = response_dict['quote'] # {'id': , ... , 'body': 'sentences.'}

print(quote_dict['body'], '\n -- ', quote_dict['author'])
