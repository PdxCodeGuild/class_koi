import random

# optional lab, magic 8 ball ---- #

predictions = [
    'It is certain',
    'Without a doubt',
    'You may rely on it',
    'The outlook is good',
    'Reply hazy, try again',
    'Ask again later',
    'Very doubtful',
    'Don\'t count on it',
    'Looks like no',
]

while True:
    print('Hi, I\'m the magic 8-ball!')
    question = input('Ask me a question or type done: ')
    if question == 'done':
        break
    prediction = random.choice(predictions)
    print(prediction)