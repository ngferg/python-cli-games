import game_state

def print_main_menu(post_roll=True):
    print('(q)uit (r)oll ', end='')
    if (post_roll):
        print('(1-5) keep die number (e)nd turn', end='')
    print('')

def print_start_turn(state: game_state.state):
    print(f'Starting player {state.current_player}\'s turn')
    print_score_card(state, False)
    
def print_score_card(state: game_state.state, with_available_scores: bool):
    print(f'Player {state.current_player} score card:')
    print_score_card_line()
    for category in state.categories.values():
        print(f'| {category.name}: {category.scores[state.current_player-1]}{' '*(17 - str(category.name).__len__() - str(category.scores[state.current_player-1]).__len__())}| ', end='')
        if (with_available_scores and category.hotkey != '' and state.category_not_scored(category.name)):
            print(f'{category.hotkey} {category.score_method()}', end='')
        print()
        if (category.print_line_after):
            print_score_card_line()
    print_score_card_line()
    if (with_available_scores):
        print('Press the button for the score you want to keep')

def print_score_card_line():
    print(f'+--------------------+')
