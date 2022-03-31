
class Player:

    def __init__(self,name,token):

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
        self.x = x
        self.y = y
        self.player = player
        if self.board[x][y] == ' ':
            self.board[x][y] = player1_player.token
        else:
            print('Space already occupied. ')

    def calc_winner(self):
        pass

    def is_full(self):
        pass

    def is_game_over(self):
        pass

while True:

    game = Game()
    # player = Player()
    game.__str__()

    print('Welcome to Tic-Tac-Toe!\n')

    player1 = input('Player 1, enter your name: ').title()
    player2 = input('Player 2, enter your name: ').title()

    player1_player = Player(name = player1, token = 'X')
    player2_player = Player(name = player2, token = 'O')
    players = [player1_player, player2_player]
    turn = 0
    while turn < 9:
        if turn % 2:
            player1_move_x = int(input('1.Enter the x position to move your token to. '))
            player1_move_y = int(input('1.Enter the y position to move your token to. '))
            turn += 1
            game.move(player1_move_x, player1_move_y, player1_player)
            game.__str__()
            # continue
        else:
            player2_move_x = int(input('2.Enter the x position to move your token to. '))
            player2_move_y = int(input('2.Enter the y position to move your token to. '))
            turn += 1
            game.move(player2_move_x, player2_move_y, player2_player)
            game.__str__()
            # continue

    players = [player1_player, player2_player]
    for player in players:
        print(f'It is {player.name}\'s turn.')
        x_move = int(input(f'{player.name}, enter the x position you want to move to: '))
        y_move = int(input(f'{player.name}, enter the y position you want to move to: '))
        
        game.move(x_move, y_move, player)
    
        game.__str__()
        

    
       
    break
# table = Game.__str__()
    