import requests
import time

def random_joke():
    random = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
    random_data = random.json()
    return (random_data['joke'])

def search_joke(search_term, search_limit):
    user_next_page = 'y'
    count = 1

    while(user_next_page == 'y'):
        
        search = requests.get('https://icanhazdadjoke.com/search', headers={'accept': 'application/json'}, params={'term' : search_term, 'limit' : search_limit, 'page' : count})
        search_data = search.json()

        for i in search_data['results']:
            time.sleep(.5)
            print(f"\n{i['joke']}\n")

        user_next_page = input(f"Do you want to see the next {search_limit} jokes? (y/n): ")

        while(user_next_page != 'y' and user_next_page != 'n'):
            user_next_page = input("Invalid Input! Please enter y or n: ")
        
        count += 1


repl_flag = 'y'

print("Welcome to the Dad joke generator!")
input("Press enter to continue... ")

while(repl_flag == 'y'):
    user_input = int(input(f"""1. Generate a random joke
2. Search for a joke
3. Exit
Please choose what you would like to do (1-3): """))

    if(user_input == 1): # generate a random joke
        random_repeat = 'y'
        while(random_repeat == 'y'):
            time.sleep(.5)
            print(f"\n{random_joke()}\n")

            random_repeat = input("Would you like to get another joke? (y/n): ")

            while(random_repeat != 'y' and random_repeat != 'n'):
                random_repeat= input("Invalid input! Please enter y or n: ").lower()
    
    elif(user_input == 2): # search for a joke
        search_repeat = 'y'

        while(search_repeat == 'y'):
            joke_count = int(input("How many jokes would you like to see per page? (max 20): "))
            joke_term = input("What term would you like to search? ")

            search_joke(joke_term, joke_count)

            search_repeat = input("Would you like to search for another joke? (y/n): ")

            while(search_repeat != 'y' and search_repeat != 'n'):
                search_repeat = input("Invalid input! Please enter y or n: ").lower()
    
    elif(user_input == 3): # exit
        break

    else: # invalid input
        print("Invalid Input! Please enter a number between 1-3")
        continue

