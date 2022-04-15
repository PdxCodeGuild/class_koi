import easygui

from random_quote import random_quote

test_quote = {
	'quote': "At least once a year I like to bring in some of my Kevin's Famous Chili. The trick is to undercook the onions. Everybody is going to get to know eachother in the pot. I'm serious about this stuff. I'm up the night before, pressing garlic, and dicing whole tomatoes. I toast my own ancho chiles. It's a recipe passed down from Malones for generations - it's probably the thing I do best.",
	'character': 'Kevin Malone',
}

while True:
    # quote = test_quote
    quote = random_quote()

    message = f"""
{quote['quote']}
––{quote['character']}
"""

    another_quote = easygui.boolbox(message, 'The Office Quote', ['Another Quote', 'Done'])
    if not another_quote:
        break
# user_input = easygui.textbox('type something')

# easygui.msgbox(f'you typed: {user_input}')

# user_input = input('type something')

# print('you typed ' + user_input)