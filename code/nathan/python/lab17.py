import requests

def random_quote():
    random = requests.get('https://favqs.com/api/qotd')
    random_data = random.json()
    print(f"{random_data['quote']['body']}\n- {random_data['quote']['author']}\n")

def keyword_quote(keyword):
    page_number = 1
    next_page = 'next page'

    while(next_page == 'next page'):
        keywords = requests.get('https://favqs.com/api/quotes', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params={'filter' : keyword, 'page' : page_number})

        keywords_data = keywords.json()

        for i in keywords_data['quotes']:
            print(f"{i['body']}\n- {i['author']}\n")
        
        next_page = input(f"Enter 'next page' of 'done': ")
        page_number += 1

        while(next_page != 'next page' and next_page != 'done'):
            next_page = input("Invalid Input! Please enter 'next [age] or 'done': ")


random_quote()

repl_flag = 'y'
while(repl_flag == 'y'):
    keyword = input("Enter a keyword to search for quotes: ")
    keyword_quote(keyword)

    repl_flag = input("Do you want to search for another quote? (y/n): ")
    while(repl_flag != 'y' and repl_flag != 'n'):
        repl_flag = input("Invalid input! Please enter y or n: ").lower()
print("Thank you buh bye!")