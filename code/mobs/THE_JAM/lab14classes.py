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
        return(f"""
        {board["1"]}|{board["2"]}|{board["3"]}
        {board["4"]}|{board["5"]}|{board["6"]}
        {board["7"]}|{board["8"]}|{board["9"]}
        """)
    
    def move(self, box, player,):
        if self.board[box] != " ":
            print("That space is already taken!")
            return False
        else:
        # places current player's token on the game board
            self.board[box] = player
            return True

    def calc_winner(self, token):
        list = [['7','5','3'],
                ['1','5','9'],
                ['1','2','3'],
                ['4','5','6'],
                ['7','8','9'],
                ['1','4','7'],
                ['2','5','8'],
                ['3','6','9']]

        for i in list:
            count = 0
            for j in i:
                if(self.board[j] == token):
                    count += 1
                if(count == 3):
                    return True

    def is_full(self):
        if " " not in self.board.values():
            return True
        else:
            return False

    def is_gameover(self, name, token):
    # name, token
        if(self.calc_winner(token)):
            print(f"{name} won!")
            return True
        elif(self.is_full()):
            print("Its a draw!")
            return True
        return False
