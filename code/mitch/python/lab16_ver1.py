# Lab 16: Dad Joke API
# Part 1
# Mitch Chapman

import requests
import time


response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'}).json()


print("\nDad joke incoming...")
time.sleep(1)
print("...")
time.sleep(1)
print("...")
time.sleep(1)
print(response["joke"])












