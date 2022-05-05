from lab14classes import Player as player
from lab14classes import Game as game
## Mob Lab 14 ##
## Shaine, Nathan, Logan ##
## Code ##


player1 = player("player1", "X")
player2 = player("player2", "O")

player1 = player("player1", "X")
player2 = player("player2", "O")

repl_flag = 'y'
new_game = game()
while(repl_flag == 'y'):
    game = new_game
    repeat_flag = True
    count = 0
    while(repeat_flag == True):
        current_player = player("temp", " ")
        player_move = ''

        if(count % 2 == 0):
            current_player = player1
        else:
            current_player = player2
        
        valid_move = False
        while valid_move == False:
            print(f"It is {current_player.name}'s turn!")
            player_move = input(f"""Where do you want to move?

        1|2|3
        4|5|6
        7|8|9

        """)
            valid_move = game.move(player_move, current_player.token)
            print(game)

        if(game.calc_winner(current_player.token)):
            print(f"{current_player.name} won!")
            break
        elif(game.is_full()):
            print("Its a draw!")
            break
        
        count += 1

    repl_flag = input("Do you want to play again? (y/n): ").lower()

    for key in game.board:
        game.board[key] = " "

    while(repl_flag != 'y' and repl_flag != 'n'):
        repl_flag = input("Invalid input! Please enter y or n: ").lower()