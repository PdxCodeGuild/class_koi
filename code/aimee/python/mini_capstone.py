'''
Python Mini Capstone

Choose Your Own Adventure
by Aimee Young
'''
import time
from colorama import init
init()

# welcome
print(f'''Welcome to <Name>, a choose-your-fate story adventure. 
When prompted, make your choice by entering in the corresponding number. 
Make your decisions, and see if you live \n\nor die...\n''')
time.sleep(2)
your_name = input('Enter your name: ')
# friends_name = input('Enter the name of a friend: ')
time.sleep(1)

# brief introduction
print('-'*80 + '\n\n'  + 'HOW IT BEGINS') # (back.MAGENTA) colorama isn't working
print('It\'s a cold Friday night in February, and you and your four friends have rented'\
    ' an Airbnb for the weekend. The house is a beautiful, classic A-frame situated' \
        ' on a remote road outside of Snoqualmie, Washington. There\'s fresh snow' \
            ' on the ground, and you spend the first night cooking together and enjoying the view from the balcony.')

print('...') + time.sleep(1)
risk_counter = 0 

while True:
    print('\n\n2AM SATURDAY MORNING\n')
    print('You wake up with a start, hearing the echo of a scream in the air. Or are you imagining it?'\
        f' You tense in the darkness of the room you\'re sharing with your friend Taylor.'\
            ' They are still sleeping soundly, softly snoring in their bed. It must\'ve been your '\
                'imagination, right? Or the several beers you had with dinner...')
    ch_1_p1 = input('Do you...\n 1) Get out of bed and check on your other friends, or \n 2) Try to go back to sleep \n'\
        'Make your choice: ')