import game_state

def print_main_menu():
    print('Main menu: ')
    print('(q)uit (r)oll')

def print_start_turn(state: game_state.state):
    print(f'Starting player {state.current_player}\'s turn')
    state.print_score_card