'''
PDX Code Guild - Class Koi
Optional Lab - Connect Four
Matt Walsh
'''

 
# Version 1

class Player:
    def __init__(self,name,color):
        """
        Initializes game and assigns parameters to variables.
        """
        self.name = name
        self.color = color
        if color == 'Yellow':
            self.token = 'Y'
        elif color == 'Red':
            self.token = 'R'

    def __str__(self):
        """
        Converts player to string for display.
        """
        return f'{self.color}: {self.name}'

class Game:
    def __init__(self):
        """
        Initializes game and sets up empty board.
        """
        self.board = [
            [None,' ',' ',' ',' ',' ',' ',' '],
            [None,' ',' ',' ',' ',' ',' ',' '],
            [None,' ',' ',' ',' ',' ',' ',' '],
            [None,' ',' ',' ',' ',' ',' ',' '],
            [None,' ',' ',' ',' ',' ',' ',' '],
            [None,' ',' ',' ',' ',' ',' ',' '],
        ]
    
    def get_height(self,position):
        """
        Determines filled height of given column.
        Returns height of column as integer.
        """
        # assign height variable
        height = 0
        # iterate through rows and increment height if a token is found
        for row in self.board:
            if row[position] != ' ':
                height += 1
        # return height as integer
        return height
    
    def move(self,player, position):
        """
        Handles player moves.
        Returns None if move is invalid (column full).
        """
        if self.get_height(position) < 6:
            self.board[5 - self.get_height(position)][position] = player.token
        else:
            return None
        ...

    def calc_winner(self):
        """
        Determines winner based on board.
        """
        ...
    
    def is_full(self):
        """
        Determines if the board is full.
        Returns True if full, False if not.
        """
        # check top row for empty spaces
        if ' ' in self.board[0]:
            return False
        return True
    
    def is_game_over(self):
        """
        Uses calc_winner and is_full to determine if the game is over.
        Displays message indicating status and returns True if over, False if not.
        """
        if self.calc_winner() is not None:
            ...
        elif self.is_full():
            print('Whoops, you filled the board with no winner! You\'re both loooosers!')
            return True
        return False
    
    def __str__(self):
        """
        Displays game board.
        """
        board_str = ''
        for row in self.board:
            board_str += '|' + '|'.join(row[1:8]) + '|\n'
        return board_str





game = Game()
player_1 = Player('Bob','Yellow')
player_2 = Player('Harry','Red')

print(player_1)
print(player_2)
print(game)
with open('code/matt/python/optional/connect_four_moves.txt','r') as moves_file:
    for i, line in enumerate(moves_file):
        Game.move(game,player_1 if i % 2 == 1 else player_2,int(line))
        print(game)