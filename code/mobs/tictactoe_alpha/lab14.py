'''
Lab 14: Tic Tac Toe

Mitch Chapman
Chris Roos
Matt Walsh
'''

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
        
    def __str__(self):
        return f"Name: {self.name} --- Token: {self.token}"


class Game:

    def __init__(self):
        self.board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]


    def __str__(self):
        board_string = ""
        for line in self.board:
            board_string += ('|'.join(line)) + "\n"
        return board_string
    
    
    def move(self, x, y, player):
        if x not in range(3) or y not in range(3):
            print("This is not a valid positional argument.")
            return True
        
        elif self.board[y][x] == ' ':
            self.board[y][x] = player.token
            return False
        else:
            print("This position is already occupied.")
            return True
            
            
    def calc_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != ' ':
                return self.board[i][0]
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != ' ':
                return self.board[0][i]
            elif i == 1 and self.board[i-1][i-1] == self.board[i][i] == self.board[i+1][i+1] and self.board[i+1][i] != ' ':
                return self.board[i][i]
            elif i == 1 and self.board[i+1][i+1] == self.board[i][i] == self.board[i-1][i-1] and self.board[i+1][i] != ' ':
                return self.board[i][i]

        
        # for row in self.board:
        #     if row[0] == ' ':
        #         return None
        #     elif row[0] == row[1] == row[2]:
        #         return row[0]
        # for col in self.board[0]:



            
            
            
    def is_full(self):
        ...
            
            
    def is_game_over(self):
        ...
            
            
            
            
game_1 = Game()


player_1 = Player(name="Chris", token="X")
player_2 = Player(name="Matt", token="O")

player_list = (player_1, player_2)

while True:
    for player in player_list:
        print(f"{player.name}, it is your move. You are placing {player.token}'s.")
        
        keep_going = True
        while keep_going:
            
            
            
            x = int(input(f"{player.name}, enter the x position you want to go (0, 1, or 2): "))
            y = int(input(f"{player.name}, enter the y position you want to go (0, 1, or 2): "))
            keep_going = game_1.move(x=x, y=y, player=player)
        print(game_1)
        print(game_1.calc_winner())
    break
   






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