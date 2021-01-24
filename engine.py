from constants import BRICK, SPACE, GATE
from ui import display_board
from levels import build_board_content_central, build_board_content_left, build_board_content_right

LEFT_MAIN_DOOR_ROW = 2
LEFT_MAIN_DOOR_COL = 0
RIGHT_MAIN_DOOR_ROW = 8

def build_an_empty_board(width, height):
    board = []
    for _ in range(height):
        board.append([SPACE] * width)

    board = build_bricks_wall_around_board(board)

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
    return board

def check_if_change_board(player, board):
    width = len(board[0])
    height = len(board)
    #change to board two, left gate at board one
    if player['row'] == LEFT_MAIN_DOOR_ROW and player['col'] == LEFT_MAIN_DOOR_COL:
        board = build_an_empty_board(width, height)
        board = build_gates_at_left_board(board)
        player['row'] = LEFT_MAIN_DOOR_ROW
        player['col'] = width - 2
        return player, board

    # change to board one, right gate at board two
    if player['row'] == LEFT_MAIN_DOOR_ROW and player['col'] == width - 1:
        board = build_an_empty_board(width, height)
        board = build_gates_at_central_board(board)
        player['row'] = LEFT_MAIN_DOOR_ROW
        player['col'] = LEFT_MAIN_DOOR_COL + 1
        return player, board
    # change to board three, right gate at board one
    if player['row'] == RIGHT_MAIN_DOOR_ROW and player['col'] == width -1:
        board = build_an_empty_board(width, height)
        board = build_gates_at_right_board(board)
        player['row'] = RIGHT_MAIN_DOOR_ROW
        player['col'] = LEFT_MAIN_DOOR_COL + 1
        return player, board

    # change to board one, left gate at board three
    if player['row'] == RIGHT_MAIN_DOOR_ROW and player['col'] == LEFT_MAIN_DOOR_COL:
        board = build_an_empty_board(width, height)
        board = build_gates_at_central_board(board)
        player['row'] = RIGHT_MAIN_DOOR_ROW
        player['col'] = width - 2
        return player, board

    return player, board

def build_gates_at_central_board(board):
    width = len(board[0])
    height = len(board)
    board = build_an_empty_board(width, height)

    board[LEFT_MAIN_DOOR_ROW][LEFT_MAIN_DOOR_COL] = GATE
    board[RIGHT_MAIN_DOOR_ROW][width - 1] = GATE

    build_board_content_central(board)
    return board

def build_gates_at_left_board(board):
    width = len(board[0])
    height = len(board)
    board = build_an_empty_board(width, height)

    board[LEFT_MAIN_DOOR_ROW][width - 1] = GATE
    build_board_content_left(board)
    return board

def build_gates_at_right_board(board):
    width = len(board[0])
    height = len(board)
    board = build_an_empty_board(width, height)
    board[RIGHT_MAIN_DOOR_ROW][0] = GATE
    build_board_content_right(board)
    return board

def clear_player_previous_position(board, row, col):
    board[row][col] = SPACE

def can_player_move(board, row, col):
    if board[row][col] == BRICK:
        return False
    else:
        return True

def create_board(width=5, height=5):
    board = build_an_empty_board(width, height)
    board = build_gates_at_central_board(board)

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
