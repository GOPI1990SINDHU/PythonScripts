def space_check(board,position):
    position_empty = ' '
    if board[position] == 'X' or board[position] == 'O' :
        position_empty = False
    else:
        position_empty = True
    return position_empty

def is_board_full(board):
    board_full = ''
    for symbols in board:
        if symbols == ' ':
            board_full = False
            break
        else:
            board_full = True
    return board_full

def print_board(board):
    print(board[6]+"|"+ board[7]+"|"+ board[8])
    print("-----")
    print(board[3]+"|"+ board[4]+"|"+ board[5])
    print("-----")
    print(board[0]+"|"+ board[1]+"|"+ board[2])

def win_check(board,marker):
    you_win = ' '
    if (board[6] == board[7] == board[8] == marker) or (board[3] == board[4] == board[5] == marker) or (board[0] == board[1] == board[2] == marker) :
        print("Congratulations, You Won!")
        you_win = True
    else:
        you_win = False
    return you_win

def player_input():
    marker = ['X', 'O']
    marker_selected = input("To start the game, Player 1 , please choose your marker X or O:")
    while marker_selected not in marker:
        print("Oops wrong choice, please try again!")
        marker_selected = input("Player 1 , please choose your marker X or O:")
    player1 = marker_selected
    if marker_selected == 'O':
        player2 = 'X'
    else:
        player2 = 'O'
    return(player1,player2)

def position_input_on_board(board):
    player1,player2 = player_input()
    game_on = True
    replay_choice = False
    while game_on:
        if replay_choice:
            player1,player2 = player_input()
            replay_choice = False
        for symbol in (player1,player2):
            position_choice = input("Please enter your position  player_info[] (1-9):")
            space_check_result = space_check(board,int(position_choice)-1)
            while not position_choice.isdigit() or int(position_choice) > 9 or int(position_choice) < 1:
                print("Oops invalid choice, please enter a digit which is in between [1-9]")
                position_choice = input("Please enter your position (1-10):")
            while not space_check_result:
                print(f"Position selected position {int(position_choice)} is not free! Choose another position")
                position_choice = input("Please enter your position (1-10):")
                space_check_result = space_check(board,int(position_choice)-1)
            board[int(position_choice)-1] = symbol
            print_board(board)
            check_result = win_check(board,symbol)
            board_full_result = is_board_full(board)
            if check_result:
                print(f"Player with marker {symbol} won!")
                replay_choice = input("Do you want to replay the game: [Yes or No]")
                print(replay_choice)
                if replay_choice.lower() == "yes":
                    board.clear()
                    board = [' ']*10
                    print_board(board)
                    break
                else:
                    game_on = False
                    break
            if is_board_full(board):
                print("Game is a tie!")
                replay_choice = input("Do you want to replay the game: [Yes or No]")
                if replay_choice.lower() == "yes":
                    board.clear()
                    board = [' ']*9
                    print_board(board)
                    break
                else:
                    game_on = False
                    break
					
if __name__ == "__main__":					
	board = [' ']*9
	position_input_on_board(board)