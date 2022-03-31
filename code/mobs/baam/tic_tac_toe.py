
class Player:

    def __init__(self,name,token):

        self.name = name
        self.token = token

class Game:

    def __init__(self):        
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
      
        

    def __str__(self):
        '''returns a string representation of the game board'''
        output = ''
        output += f'{self.board[0][0]}|{self.board[0][1]}|{self.board[0][2]}\n'
        output += f'{self.board[1][0]}|{self.board[1][1]}|{self.board[1][2]}\n'
        output += f'{self.board[2][0]}|{self.board[2][1]}|{self.board[2][2]}'
        return output

    def move(self,x,y,player):
        '''Place a player's token character string at a given coordinate'''
        self.x = x
        self.y = y
        self.player = player
        
        if self.board[x][y] != ' ':
            print('Space already occupied. Try again.')
            return False
            
        self.board[x][y] = player.token
        return True                  

    def calc_winner(self):

        for i, row in enumerate(self.board):
            if 'X' == row[0] == row[1] == row[2]:
                return 'X'
            if 'O' == row[0] == row[1] == row[2]:
                return 'O'
            if 'X' == self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return 'X'
            if 'O' == self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return 'O'
            

        '''returns the winner, or None if no one wins'''
        

    def is_full(self):
        '''returns true if game board is full'''
        pass

    def is_game_over(self):
        '''returns true if the game board is full or a player has won'''
        pass

game = Game()
    # player = Player()
    # game.__str__()

print('Welcome to Tic-Tac-Toe!\n')
player1 = input('Player 1, enter your name: ').title()
player2 = input('Player 2, enter your name: ').title()
player1_player = Player(name = player1, token = 'X')
player2_player = Player(name = player2, token = 'O')

players = [player1_player, player2_player]
i = 0

while True: 
    player = players[i%2]   
    while True:
        
        print(f'It is {player.name}\'s turn.')
        x_move = int(input(f'{player.name}, enter the x position you want to move to: '))
        y_move = int(input(f'{player.name}, enter the y position you want to move to: '))
         
        valid_move = game.move(x_move, y_move, player)
        print(game)
        if valid_move:                
            break
    
    i += 1 
    
    if game.calc_winner() in ['X','O']:
        print(f'{player.name}WINS!')
        break
        
    # check if no winner (board full)
    










# table = Game.__str__()
    



# if self.board[x][y] != ' ':
        #         print('Space already occupied. Try again.')


# players = [player1_player, player2_player]
    # turn = 0
    # while turn < 9:
    #     if turn % 2:
    #         player1_move_x = int(input('1.Enter the x position to move your token to. '))
    #         player1_move_y = int(input('1.Enter the y position to move your token to. '))
    #         turn += 1
    #         game.move(player1_move_x, player1_move_y, player1_player)
    #         game.__str__()
    #         # continue
    #     else:
    #         player2_move_x = int(input('2.Enter the x position to move your token to. '))
    #         player2_move_y = int(input('2.Enter the y position to move your token to. '))
    #         turn += 1
    #         game.move(player2_move_x, player2_move_y, player2_player)
    #         game.__str__()
    #         # continue
