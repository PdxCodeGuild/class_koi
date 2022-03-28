'''
PDX Code Guild - Class Koi
Optional Lab - Magic 8 Ball
Matt Walsh
'''

 
# Version 1
""" 
from random import choice

# dictionary of responses
responses = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]

# prompt for question
question = input('Ask the Magic 8 Ball a question: ')
# display response
print(choice(responses))
 """


# Version 2

from random import choice

# dictionary of responses
responses = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]

# put magic 8 ball in a function
def magic_8_ball():
    # prompt for question
    question = input('Ask me a yes or no question: ')
    # display response
    print(choice(responses))

# call funtion
magic_8_ball()

while True: # allow user to keep playing or exit
    what_next = input('Would you like to ask me another question? Type "yes" or "no": ').lower()
    if what_next == 'yes':
        magic_8_ball()
    elif what_next =='no':
        break
    else:
        print('I didn\'t understand that.')