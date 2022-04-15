# LAB 16: Dad Joke API ----------- #

import requests
import time
    
# REPL ------------------------------------- #

while True:
    print('*'*78)
    print('Welcome to the Dad Joke generator!')
    command = input(f'''What would you like to do?
    (r)andom joke | (s)earch for joke | (e)xit
    Enter your selection: ''')
    print('\n')  
    if command == 'r':             
        response = requests.get('https://icanhazdadjoke.com/?limit=1', headers = {'Accept':'application/json'})
        joke = response.json()
        print(f"{joke['joke']}\n")
    elif command == 's':   
        search_term = input('Enter a term to find dad jokes: ').lower()
        response = requests.get('https://icanhazdadjoke.com/search', headers = {'Accept':'application/json'}, params={'term':search_term, 'limit':20}) 
        data = response.json()
        results = data['results']
        for result in results:
            print(f"\n- {result['joke']}\n")        
            time.sleep(1.5)          
    elif command == 'e':
        print('Goodbye!')
        break
    else:
        print('Please enter a valid selection.')