from  constants import BRICK

def build_board_level_one(board):
    board[5][5] = BRICK
    board[6][5] = BRICK
    board[7][5] = BRICK
    board[8][5] = BRICK

def build_board_level_two(board):
    board[5][18] = BRICK
    board[6][8] = BRICK
    board[7][8] = BRICK
    board[8][8] = BRICK

def build_board_level_three(board):
    board[5][8] = BRICK
    board[5][9] = BRICK
    board[5][10] = BRICK
    board[5][11] = BRICK