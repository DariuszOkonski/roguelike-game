from constants import BRICK, FOOD

def build_board_content_central(board):
    board[5][5] = BRICK
    board[6][5] = BRICK
    board[7][5] = BRICK
    board[8][5] = BRICK

    board[3][8] = FOOD['icon']
    board[10][10] = FOOD['icon']

    return board

def build_board_content_left(board):
    board[5][18] = BRICK
    board[6][8] = BRICK
    board[7][8] = BRICK
    board[8][8] = BRICK
    return board

def build_board_content_right(board):
    board[5][8] = BRICK
    board[5][9] = BRICK
    board[5][10] = BRICK
    board[5][11] = BRICK
    return board