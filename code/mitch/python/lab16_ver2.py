# Lab 16: Dad Joke API
# Part 2
# Mitch Chapman

import requests
import time

def print_sleep():
    time.sleep(0.5)
    print("...")
    time.sleep(0.6)

print('\nWelcome to the Dad Joke headquarters!')
while True:
    time.sleep(1)
    print("\n-----------------------------------------MAIN MENU-----------------------------------------")
    user_input = input("Would you like to [s]earch for a topic for the Dad Joke or see a [r]andom dad joke: ")
    if user_input not in ['s', 'r', 'q']:
        print("Invalid response. Please enter 's' to search, 'r'for random, or 'q' to quit.")

    elif user_input == 's':
        search_term = input("Please enter a search term for realated dad jokes: ").lower()
        response = requests.get(f'https://icanhazdadjoke.com/search?term={search_term}', headers={'Accept': 'application/json'}).json()

        print(f"\nHere are some jokes related to the phrase '{search_term}':")
        for data in response['results']:
            for _ in range(4):
                print_sleep()
            print(data['joke'])
            time.sleep(3)
            print("😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂")
    elif user_input == 'r':
        response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'}).json()

        print("\nDad joke incoming...")
        for _ in range(4):
            print_sleep()
        print(response['joke'])
        time.sleep(3)
        print("😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂 😂")
    
    elif user_input == 'q':
        break
