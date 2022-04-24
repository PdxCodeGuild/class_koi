import requests
import time

#  *'-.-'*'-.-'*'-.-'*'--'*
#     Project: Python 
#   Lab 16: Dad Joke API
#       Version: 1.0 & 2.0
#   Author: Shaine Warren
#   Email: mwarren86@gmail.com
#       Date: Mar, 2022
# *'-.-'*'-.-'*'-.-'*'--'*

while True:
    user_input =  input('Select [r]andom, [s]earch, or [q]uit: ')
    if user_input == 'r':
        response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
        data = response.json()
        print(f'''
        {data['joke']}
        ''') 
    elif user_input == 's':
        search = input('''
        Enter search for dad joke: ''')
        response = requests.get(f'https://icanhazdadjoke.com/search?term={search}', headers={'Accept': 'application/json'})
        data = response.json()
        results = data['results']

        for x, result in enumerate(results):
            print(f'''
            {x+1}. {result['joke']}''')
            time.sleep(2)
    else:
        break
