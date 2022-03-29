books = [
    {'title': 'Tropic of Cancer', 'author': 'Henry Miller', 'checked_out': True},
    {'title': 'The Way of the Peaceful Warrior', 'author': 'Dan Millman', 'checked_out': False},
    {'title': 'The DaVinci Code', 'author': 'Dan Brown', 'checked_out': False},
    {'title': 'To Kill a Mockingbrid', 'author': 'Harper Lee', 'checked_out': True},
]

def donate():
    """Creates a new book and adds it to list"""
    print('donate functionality not yet implemented')

def search():
    """Retrieves the book"""
    search_term = input("Enter an author you'd like to search for: ").lower()
    for book in books:
        if search_term in book['author'].lower():
            checked_out_status = 'checked out' if book['checked_out'] else 'available'
            print(f"Here are the results:\n * {book['title']} by {book['author']} is {checked_out_status}")

def checkout():
    """Updates book checked_out status"""
    title = input("Please enter the title of the book you'd like to check out: ").lower()
    for book in books:
        if title in book['title'].lower():
            if book['checked_out']:
                print(f"Sorry, {book['title']} is checked out.")
            else:
                print(f"Here is your copy of {book['title']} by {book['author']}.\nPlease return it in 14 days or else...")
                book['checked_out'] = True
            return
    print('Book not found')

def buy():
    """Deletes or removes book from list"""
    print('buy functionality is not yet implemented')

print('Welcome to the library.')
while True:
    command = input('Would you like to [s]earch, [c]heck out, [d]onate, [b]uy or [q]uit? ').lower()
    if command not in ['q', 's', 'c', 'd', 'b']:
        print('Please enter "s" for search, "c" for check out, "d" for donate, "b" for buy, or "q" for quit.')
    if command == 'q':
        print('Thanks for your patronage.')
        break
    if command == 's':
        search()
    if command == 'c':
        checkout()
    if command == 'd':
        donate()
    if command == 'b':
        buy()