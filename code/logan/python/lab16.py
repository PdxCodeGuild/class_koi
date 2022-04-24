## Lab 16 ##
## Code ##

## Imports
import time
import requests
from pprint import pprint

## Version 1 ##
# response = requests.get("https://icanhazdadjoke.com/", headers = {"Accept":"application/json"})
# response_j = response.json()
# time.sleep(1)
# # pprint(response_j)
# print(f"\n{response_j['joke']}\n")

## Version 2 ##
game_over = False
while game_over == False:
    search_term = input("\nGive me a term to search\n...")
    response = requests.get(f"https://icanhazdadjoke.com/search?term={search_term}", headers = {"Accept":"application/json"})
    response_j = response.json()

    counter = 1

    for dict in response_j["results"]:
        print(f"\n{counter}. {dict['joke']}\n")
        time.sleep(1)
        counter += 1
    
    while True:
        pg = input("\nInput 0 if you'd like to quit, or 1 if you'd like to play again.\n...")
        if pg not in ["0", "1"]:
            print("Invalid response.")
        elif pg == "1":
            break
        elif pg == "0":
            game_over = True
            break

print("\nGoodbye!\n")

###################################
## Debugging
# print(response)
# time.sleep(1)
# pprint(response_j)
# print(f"\n{response_j['joke']}\n")

## Scrap
# headers ={"Accept:" "application/json","User-Agent": "Bogan Dougbass"})