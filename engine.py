from constants import BRICK, SPACE, GATE
from ui import display_board

def create_board(width=5, height=5):
    #build an empty board
    board = []
    for _ in range(height):
        board.append([SPACE] * width)

    #build bricks wall around board
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == 0 or i == height - 1:
                board[i][j] = BRICK
            elif j == 0 or j == width - 1:
                board[i][j] = BRICK

    #build two gates at sides
    board[2][0] = GATE
    board[3][width-1] = GATE

    return board




def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    pass
