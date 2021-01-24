import os


def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    print("\n")
    for i in range(len(board)):
        temp_str = ''
        for j in range(len(board[i])):
            temp_str += board[i][j] + ' ';
        print(temp_str)

    print("\n")
    print("SCORE: 123")
    print("MOVES w - s - a - d")
