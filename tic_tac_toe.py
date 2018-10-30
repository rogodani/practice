"""
Here are the requirements:
2 players should be able to play the game (both sitting at the same computer)
The board should be printed out every time a player makes a move
You should be able to accept input of the player position and then place a symbol on the board
"""

from IPython.display import clear_output
from random import randint

def display_board(board):
    clear_output()
    print('{:^3}|{:^3}|{:^3}'.format('', '', ''))
    print('{:^3}|{:^3}|{:^3}'.format(board[7], board[8], board[9]))
    print('{:^3}|{:^3}|{:^3}'.format('', '', ''))
    print('-' * 11)
    print('{:^3}|{:^3}|{:^3}'.format('', '', ''))
    print('{:^3}|{:^3}|{:^3}'.format(board[4], board[5], board[6]))
    print('{:^3}|{:^3}|{:^3}'.format('', '', ''))
    print('-' * 11)
    print('{:^3}|{:^3}|{:^3}'.format('', '', ''))
    print('{:^3}|{:^3}|{:^3}'.format(board[1], board[2], board[3]))
    print('{:^3}|{:^3}|{:^3}'.format('', '', ''))


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O?: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return (board[1:4] == [mark, mark, mark] or board[4:7] == [mark, mark, mark] or board[7:] == [mark, mark,mark]) or \
           (board[7] == board[4] == board[1] == mark) or (board[8] == board[5] == board[2] == mark) or \
           (board[9] == board[6] == board[3] == mark) or (board[7] == board[5] == board[3] == mark) or \
           (board[9] == board[5] == board[1] == mark)

def choose_first():
    if randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, len(board)):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.: ')

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
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
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