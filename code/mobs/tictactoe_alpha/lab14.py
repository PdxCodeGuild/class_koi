'''
Lab 14: Tic Tac Toe
'''

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

    

class Game:

    def __init__(self):
        self.board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

    def __str__(self):
        for line in self.board:
            print('|'.join(line))
            
game_1 = Game()

# print(game_1)

# print(str(game_1))


#01234
# | | 0
# | | 1
# | | 2

#

# REPL starts
# call game class for each update/move
# put update/move back into Game

# create a game method called update_board() inside method called move()

# board storage
# board could always be blank

# move() adjusts board