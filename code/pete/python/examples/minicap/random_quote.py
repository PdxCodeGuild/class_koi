import requests

def random_quote():
    url = 'https://officeapi.dev/api/quotes/random'
    response = requests.get(url)
    data = response.json()
    # print(data)
    character = data['data']['character']
    quote = {
        'quote': data['data']['content'],
        'character': character['firstname'] + ' ' + character['lastname']
    }

    return quote

if __name__ == '__main__': # this block will only run if this file is run directly
    # it will not run if this is imported into another module
    quote = random_quote()
    print(quote)

