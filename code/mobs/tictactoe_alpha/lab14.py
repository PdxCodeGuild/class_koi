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
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != ' ': # check horizontals
                return self.board[i][0]
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != ' ': # check verticals
                return self.board[0][i]
            elif i == 1 and self.board[i-1][i-1] == self.board[i][i] == self.board[i+1][i+1] and self.board[i][i] != ' ': # bottom left to top right
                return self.board[i][i]
            elif i == 1 and self.board[i-1][i+1] == self.board[i][i] == self.board[i+1][i-1] and self.board[i][i] != ' ': # bottom right to top left
                return self.board[i][i]
            
    def is_full(self):
        for i in range(3):
            if ' ' in self.board[i]:
                return None
        return True
            
    def is_game_over(self):
        if self.calc_winner() is not None:
            if self.calc_winner() == "X":
                print(f"{player_1.name} has won the game!")
            elif self.calc_winner() == "O":
                print(f"{player_2.name} has won the game!")
            return True
        elif self.is_full():
            print("The board is full, you are both losers....")
            return True
        pass

game_1 = Game()

print("Welcome to the Tic-Tac-Toe Game!")
player1_name = input("Please enter the name of the first player: ").title().strip()
player2_name = input("Please enter the name of the second player: ").title().strip()

player_1 = Player(name=player1_name, token="X")
player_2 = Player(name=player2_name, token="O")

player_list = (player_1, player_2)

game_result = False

while not game_result:
    for player in player_list:
        print(f"{player.name}, it is your move. You are placing {player.token}'s.")
        
        keep_going = True
        while keep_going:
            x = int(input(f"{player.name}, enter the x position you want to go (0, 1, or 2): "))
            y = int(input(f"{player.name}, enter the y position you want to go (0, 1, or 2): "))
            keep_going = game_1.move(x=x, y=y, player=player)
        print()
        print(game_1)
        game_result = game_1.is_game_over()
        if game_result:
            break
   

