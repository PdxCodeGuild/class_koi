from lab14classes import Player as player
from lab14classes import Game as game

player1 = player("player1", "X")
player2 = player("player2", "O")

# game = game()

# game = game()
# game.__str__()

player1 = player("player1", "X")
player2 = player("player2", "O")

repl_flag = 'y'
while(repl_flag == 'y'):
    game = game()
    repeat_flag = True
    count = 0
    while(repeat_flag == True):
        current_player = player("temp", " ")
        player_move = ''

        if(count % 2 == 0):
            current_player = player1
        else:
            current_player = player2
        
        print(f"It is {current_player.name}'s turn!")
        player_move = input("Where do you want to move? ")
        game.move(player_move, current_player.token)
        game.__str__()

        if(game.calc_winner(current_player.token)):
            print(f"{current_player.name} won!")
        elif(not(game.is_full())):
            print("Its a draw!")
        
        count += 1

        # if(game.is_game_over()):
            # repeat_flag = False

    repl_flag = input("Do you want to play again? (y/n): ").lower()

    while(repl_flag != 'y' and repl_flag != 'n'):
        repl_flag = input("Invalid input! Please enter y or n: ").lower()

'''
Task list:
    Game over funtion to terminate repl
    REPL to account for spaces already taken
    Allow users to change name
'''