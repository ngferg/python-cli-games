import game_state

def print_main_menu(post_roll=True):
    print('(q)uit (r)oll ', end='')
    if (post_roll):
        print('(k+num) keep die number (e)nd turn', end='')
    print('')

def print_start_turn(state: game_state.state):
    print(f'Starting player {state.current_player}\'s turn')
    state.print_score_card(state.current_player, False)
    