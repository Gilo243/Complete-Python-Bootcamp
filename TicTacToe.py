from IPython.display import clear_output
import time
import random

def display_board(board):
    clear_output()
    print('     |     |    ')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3] + ' ')
    print('     |     |    ')
    print('-----------------')
    print('     |     |    ')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6] + ' ')
    print('     |     |    ')
    print('-----------------')
    print('     |     |    ')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] + ' ')
    print('     |     |    ')

def player_input():
    marker = ''
    while not (marker == 'O' or marker == 'X'):
        marker = input('Player 1: Do you want to be X or O?').upper()
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
def place_marker(board, position, marker):
    board[position] = marker
    
def win_check(board, mark):
    
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    else:
        return True
    
def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Choose your next position: (1-9) ')
    return int(position)

def replay():
    
    return input('Do you want to play again? Enter Yes or No').lower().startswith('y')

print('SUP..so you wanna play some tic tac toe?')

while True:
    Board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn, 'will go first!')
    time.sleep(1)
    game_on = True
    
    while game_on:
        
        if turn == 'Player 1':
            
            display_board(Board)
            print('turn: {}'.format(turn))
            position = player_choice(Board)
            place_marker(Board, position, player1_marker)
            
            if win_check(Board, player1_marker):
                display_board(Board)
                print('Congrats Bruv! Player 1 won the game!')
                game_on = False
                
            else:
                if full_board_check(Board):
                    display_board(Board)
                    print('Game be a draw!')
                    break
                else:
                    turn = 'Player 2' 
        
        if turn == 'Player 2':
            
            display_board(Board)
            print('turn: {}'.format(turn))
            position = player_choice(Board)
            place_marker(Board, position, player2_marker)
            
            if win_check(Board, player2_marker):
                display_board(Board)
                print('Congrats Bruv! Player 2 won the game!')
                game_on = False
                
            else:
                if full_board_check(Board):
                    display_board(Board)
                    print('Game be a draw!')
                    break
                else:
                    turn = 'Player 1'
                    
    if not replay():
        break
