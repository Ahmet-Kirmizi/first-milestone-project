import random


def display_board(board):
    print('\n'*100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    marker = ''
    while marker != 'X' or marker != 'O':
        marker = input('Player 1 Choose a character "X" or "O": ').upper()
        for mark in marker:
            if mark == 'X':
                return ('X','O')
                print('X')
            elif mark == 'O':
                return ('O','X')
                print('O')
            else:
                break


def place_marker(board, marker, position):
    board[position] = marker


# place_marker(test_board,"GG",2)
# display_board(test_board)

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark))


"""
def display_board_with_index(board):
    print('and this is the index positions that you can sellect:')
    print('{}|{}|{}'.format(board[7], board[8], board[9]))
    print('{}|{}|{}'.format(board[4], board[5], board[6]))
    print('{}|{}|{}'.format(board[1], board[2], board[3]))


index_positions = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# display_board_with_index(index_positions)
"""


def choose_player_randomly():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# print(choose_player_randomly())
def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(0, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Enter your next position(1-9): '))
    return position


def replay():
    choice = input('Do you want to play again? Type "Yes" or "No": ')
    return choice == 'Yes'


print('Welcome to my Tic Tac Toe Game!!!!!')

while True:
    the_board = [' '] * 10
    player1_Marker, player2_Marker = player_input()  # we assign this to x or o assignment
    turn = choose_player_randomly()  # this is assigned to the function made by random module
    print(turn + ' will go first')  # tells which player will go first using the result from random modules result

    play_game = input('Are you ready to play the game? Enter Yes or No: ')

    if play_game.lower()[0] == 'y':  # if the players are ready the game will start:
        game_on = True
    else:
        game_on = False
        # game play part

    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            # once the board is seen lets let them choose their place
            # choose a position:
            position = player_choice(the_board)
            # place the marker on the position:
            place_marker(the_board, player1_Marker, position)
            # check if they've won:
            if win_check(the_board, player1_Marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):  # check if they tied:
                    display_board(the_board)
                    print('TIE GAME!!')
                    game_on = False
                else:  # no tie no win? next players turn:
                    turn = 'Player 2'

        else:
            display_board(the_board)
            # once the board is seen lets let them choose their place
            # choose a position:
            position = player_choice(the_board)
            # place the marker on the position:
            place_marker(the_board, player2_Marker, position)
            # check if they've won:
            if win_check(the_board, player2_Marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):  # check if they tied:
                    display_board(the_board)
                    print('TIE GAME!!')
                    game_on = False
                else:  # no tie no win? next players turn:
                    turn = 'Player 1'

    if not replay():
        break
