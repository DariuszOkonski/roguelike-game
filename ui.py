import os
from constants import CURRENT_BOARD, LIVE

def display_board(board, player):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    for i in range(len(board)):
        temp_str = ''
        for j in range(len(board[i])):
            temp_str += board[i][j] + ' ';
        print(temp_str)

    print("\n")
    print(f"BOARD: {player[CURRENT_BOARD]}")
    print(f"LIVE: {player[LIVE]}")
    print("MOVES w - s - a - d")
