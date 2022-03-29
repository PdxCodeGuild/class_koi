'''
classes:
    player:
        attributes:
            name
            token
        methods:

    game:
        attributes:
            board
        methods:
            __str__()
            move()
            calc_winner()
            is_full()
            is_gameover()


main:
    repl
'''

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
    ...

class Game:

    board_values = {
    "1" : " ", "2" : " ", "3" : " ",
    "4" : " ", "5" : " ", "6" : " ",
    "7" : " ", "8" : " ", "9" : " "
    }

    def __init__(self, board = board_values):
        self.board = board
    
    def __str__(self, board = board_values):
        print(f"""
        {board["1"]}|{board["2"]}|{board["3"]}
        {board["4"]}|{board["5"]}|{board["6"]}
        {board["7"]}|{board["8"]}|{board["9"]}
        """)
    
    def move(self, box, player):
        ...

    def calc_winner():
        ...

    def is_full():
        ...
    
    def is_gameover():
        ...