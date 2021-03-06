from constants import BRICK, SPACE, GATE, FOOD, FOOD_SUPPLIES, ROW, \
    COL, CURRENT_BOARD, CENTRAL, LEFT, RIGHT, ICON, LIVE
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
    #change to board left, left gate at board central
    if player[ROW] == LEFT_MAIN_DOOR_ROW and player[COL] == LEFT_MAIN_DOOR_COL:
        board = build_an_empty_board(width, height)
        board = build_gates_at_left_board(board)
        player[ROW] = LEFT_MAIN_DOOR_ROW
        player[COL] = width - 2
        player[CURRENT_BOARD] = LEFT
        return player, board

    # change to board central, right gate at board left
    if player[ROW] == LEFT_MAIN_DOOR_ROW and player[COL] == width - 1:
        board = build_an_empty_board(width, height)
        board = build_gates_at_central_board(board)
        player[ROW] = LEFT_MAIN_DOOR_ROW
        player[COL] = LEFT_MAIN_DOOR_COL + 1
        player[CURRENT_BOARD] = CENTRAL
        return player, board
    # change to board right, right gate at board central
    if player[ROW] == RIGHT_MAIN_DOOR_ROW and player[COL] == width -1:
        board = build_an_empty_board(width, height)
        board = build_gates_at_right_board(board)
        player[ROW] = RIGHT_MAIN_DOOR_ROW
        player[COL] = LEFT_MAIN_DOOR_COL + 1
        player[CURRENT_BOARD] = RIGHT
        return player, board

    # change to board central, left gate at board right
    if player[ROW] == RIGHT_MAIN_DOOR_ROW and player[COL] == LEFT_MAIN_DOOR_COL:
        board = build_an_empty_board(width, height)
        board = build_gates_at_central_board(board)
        player[ROW] = RIGHT_MAIN_DOOR_ROW
        player[COL] = width - 2
        player[CURRENT_BOARD] = CENTRAL
        return player, board

    return player, board

def set_food_on_board(board, room):
    for row, col in FOOD_SUPPLIES[room]:
        board[row][col] = FOOD[ICON]
    return board

def build_gates_at_central_board(board):
    width = len(board[0])
    height = len(board)
    board = build_an_empty_board(width, height)

    board[LEFT_MAIN_DOOR_ROW][LEFT_MAIN_DOOR_COL] = GATE
    board[RIGHT_MAIN_DOOR_ROW][width - 1] = GATE

    board = set_food_on_board(board, CENTRAL)
    board = build_board_content_central(board)

    return board

def build_gates_at_left_board(board):
    width = len(board[0])
    height = len(board)
    board = build_an_empty_board(width, height)

    board[LEFT_MAIN_DOOR_ROW][width - 1] = GATE

    board = set_food_on_board(board, LEFT)

    board = build_board_content_left(board)
    return board

def build_gates_at_right_board(board):
    width = len(board[0])
    height = len(board)
    board = build_an_empty_board(width, height)
    board[RIGHT_MAIN_DOOR_ROW][0] = GATE

    board = set_food_on_board(board, RIGHT)

    board = build_board_content_right(board)
    return board

def clear_player_previous_position(board, row, col):
    board[row][col] = SPACE

def check_if_inventory(player, board, row, col):
    if board[row][col] == FOOD[ICON]:
        player[LIVE] += FOOD[LIVE]
        board[row][col] = SPACE

        temp_tuple = (row, col)
        for item in FOOD_SUPPLIES[player[CURRENT_BOARD]]:
            if item == temp_tuple:
                FOOD_SUPPLIES[player[CURRENT_BOARD]].remove(item)

        #TODO - remove food from food suplies
    return board

def can_player_move(player, board, row, col):
    board = check_if_inventory(player, board, row, col)

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
    row = int(player[ROW])
    col = int(player[COL])
    board[row][col] = player[ICON]
    pass