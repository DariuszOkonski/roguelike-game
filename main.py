import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = {
        'icon': PLAYER_ICON,
        'row': PLAYER_START_X,
        'col': PLAYER_START_Y,
        'live': 50
    }
    return player

def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    ui.display_board(board, player)
    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board, player)

        key = util.key_pressed().lower()
        engine.clear_player_previous_position(board, player['row'], player['col'])
        row = player['row']
        col = player['col']
        if key == 'q':
            is_running = False
        elif key == 'd':
            #move right
            if engine.can_player_move(board, row, col + 1):
                player['col'] += 1
        elif key == 'a':
            #move left
            if engine.can_player_move(board, row, col - 1):
                player['col'] -= 1
        elif key == 'w':
            #move up
            if engine.can_player_move(board, row - 1, col):
                player['row'] -= 1
        elif key == 's':
            #move down
            if engine.can_player_move(board, row + 1, col):
                player['row'] += 1
        else:
            pass

        player, board = engine.check_if_change_board(player, board)
        util.clear_screen()


if __name__ == '__main__':
    main()

'''
    1 - creature (human? alien? ant? hacker?)
    2 - wild world (forest? planet? table? meetups?)
    3 - will be levelling up, getting tougher, collecting powerful items, and finally be able to defeat an ultimate boss
    4 - obstacles (rivers? craters? drops of milk? firewalls?) 
'''












