import os

def clear_console():
    '''Clears Console'''
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_console_pycharm():
    print('\n' * 80)

def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    clear_console()
    print("\n")
    for i in range(len(board)):
        temp_str = ''
        for j in range(len(board[i])):
            temp_str += board[i][j] + ' ';
        print(temp_str)

    print("\n")
    print("SCORE: 123")
    print("MOVES w - s - a - d")
