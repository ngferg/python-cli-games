import game_state

def print_main_menu(with_keep=True):
    print('(q)uit (r)oll ', end='')
    if (with_keep):
        print('(k+num) keep die number', end='')
    print('')

def print_start_turn(state: game_state.state):
    print(f'Starting player {state.current_player}\'s turn')
    state.print_score_card(state.current_player)