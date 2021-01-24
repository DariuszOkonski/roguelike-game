from constants import BRICK, SPACE, GATE
from ui import display_board

def build_an_empty_board(width, height):
    board = []
    for _ in range(height):
        board.append([SPACE] * width)
    return board

def build_bricks_wall_around_board(board):
    height = len(board)
    width = len(board[0])
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == 0 or i == height - 1:
                board[i][j] = BRICK
            elif j == 0 or j == width - 1:
                board[i][j] = BRICK

def build_gates_at_sides(board):
    width = len(board[0])
    board[2][0] = GATE
    board[3][width - 1] = GATE

def clear_player_previous_position(board, row, col):
    board[row][col] = SPACE

def can_player_move(board, row, col):
    if board[row][col] == BRICK:
        return False
    else:
        return True

def create_board(width=5, height=5):
    board = build_an_empty_board(width, height)
    build_bricks_wall_around_board(board)
    build_gates_at_sides(board)

    # TODO - he game has at least 3 boards/levels with different inhabitants.

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
    row = int(player['row'])
    col = int(player['col'])
    board[row][col] = player['icon']
    pass
