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
        'col': PLAYER_START_Y
    }
    return player

def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    ui.display_board(board)
    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.key_pressed().lower()
        if key == 'q':
            is_running = False
        elif key == 'd':
            engine.clear_player_previous_position(board, player['row'], player['col'])
            player['col'] += 1
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()

'''
    1 - creature (human? alien? ant? hacker?)
    2 - wild world (forest? planet? table? meetups?)
    3 - will be levelling up, getting tougher, collecting powerful items, and finally be able to defeat an ultimate boss
    4 - obstacles (rivers? craters? drops of milk? firewalls?) 
'''












