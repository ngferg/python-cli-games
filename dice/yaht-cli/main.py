import keyboard
import menus
import game_state

print('### Welcome to Yaht-cli ###')

state = game_state.state(2)
print(f'Starting a {state.max_players} game')

def roll():
    print ('pressed roll')
    state.current_player += 1
    if (state.current_player > state.max_players):
        state.current_player = 1
    menus.print_start_turn(state)
    menus.print_main_menu()



menus.print_main_menu()
menus.print_start_turn(state)

keyboard.add_hotkey('r', roll)

keyboard.wait('q')

