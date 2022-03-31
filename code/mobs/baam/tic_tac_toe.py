class Player:

    def __init__(self,name,token = 'X' or 'O'):

        self.name = name
        self.token = token

class Game:

    def __init__(self):
        
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        
        

    def __str__(self):
        
        print(f'{self.board[0][0]}|{self.board[0][1]}|{self.board[0][2]}')
        print(f'{self.board[1][0]}|{self.board[1][1]}|{self.board[1][2]}')
        print(f'{self.board[2][0]}|{self.board[2][1]}|{self.board[2][2]}')

    def move(self,x,y,player):
        pass

    def calc_winner(self):
        pass

    def is_full(self):
        pass

    def is_game_over(self):
        pass

# while True:

game = Game()
game.__str__()
# table = Game.__str__()

