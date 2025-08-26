from IPython.display import clear_output
import random



# ------ Display Board ------
def display_board(board):
    clear_output() # Remember, this only works in jupyter!
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' +board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' +board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' +board[3])
    print('   |   |')



# ------ Player Input ------
def player_input():
    
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? : ').upper()
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')



# Position of marker
def place_marker(board, marker, position):
    board[position] = marker
    


# Wining Check
def win_check(board, marker):
    
    return ((board[7] == marker and board[8] == marker and board[9] == marker) or # across the top
    (board[4] == marker and board[5] == marker and board[6] == marker) or # across the middle
    (board[1] == marker and board[2] == marker and board[3] == marker) or # across the bottom
    (board[7] == marker and board[4] == marker and board[1] == marker) or # down the middle
    (board[8] == marker and board[5] == marker and board[2] == marker) or # down the middle
    (board[9] == marker and board[6] == marker and board[3] == marker) or # down the right side
    (board[7] == marker and board[5] == marker and board[3] == marker) or # diagonal
    (board[9] == marker and board[5] == marker and board[1] == marker)) # diagonal
    
    

#  Randomly giving chance to any of the two players
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


    
# Indicating whether a space on the board is freely available
def space_check(board, position):
    return board[position] == ' '



# checks if the board is full and returns a boolean value. True if full, False otherwise
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True



# Choose player's next position (1 - 9)
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position (1-9): '))
        
    return position



# Replay the game
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')



# Game Execution
print('Welcome to Tic Tac Toe')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are your ready to play? Enter Yes or No: ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)
            
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! {} have won the game!'.format(turn))
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        
        else: 
            # Player2's turn
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
            
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations! {} have won the game!'.format(turn))
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    
    if not replay():
        break