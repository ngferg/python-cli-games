import keyboard
import menus
import game_state
import random
import ascii

print('### Welcome to Yaht-cli ###')
players_input = input('How many players do you want?: ')
players = 1
try:
    players = int(players_input)
    if (players < 1): raise ValueError('must have at least one player')
except:
    print('Funny guy? you get to play by yourself')
    players = 1

state = game_state.state(players)
print(f'Starting a {state.max_players} game')

def roll():
    if (state.game_mode):
        state.roll_num += 1
        print(f'roll {state.roll_num}')

        for i in range(0,5):
            if (state.keeps[i] == 'n'):
                state.dice[i] = random.randint(1, 6)

        ascii.print_dice(state.dice, state.keeps)

        if (state.roll_num >= 3):
            end_turn()
        else:
            menus.print_main_menu()

def end_turn():
    if (state.game_mode):
        state.set_score_mode()

def keep(die: int):
    if (state.game_mode and state.roll_num > 0):
        current_keep = state.keeps[die-1]
        if (current_keep == 'n'):
            state.keeps[die-1] = 'y'
        else:
            state.keeps[die-1] = 'n'
        ascii.print_dice(state.dice, state.keeps)
        menus.print_main_menu()

def pressedr():
    if (state.game_mode): roll()
def pressede():
    if (state.game_mode): end_turn()
def pressed1():
    if (state.game_mode): keep(1)
    elif (state.scoring_mode): state.set_score('ones')
def pressed2():
    if (state.game_mode): keep(2)
    elif (state.scoring_mode): state.set_score('twos')
def pressed3():
    if (state.game_mode): keep(3)
    elif (state.scoring_mode): state.set_score('threes')
def pressed4():
    if (state.game_mode): keep(4)
    elif (state.scoring_mode): state.set_score('fours')
def pressed5():
    if (state.game_mode): keep(5)
    elif (state.scoring_mode): state.set_score('fives')
def pressed6():
    if (state.game_mode): keep(6)
    elif (state.scoring_mode): state.set_score('sixes')
def pressedc():
    if (state.scoring_mode): state.set_score('chance')
def pressedt():
    if (state.scoring_mode): state.set_score('3 of a kind')
def pressedf():
    if (state.scoring_mode): state.set_score('4 of a kind')
def pressedy():
    if (state.scoring_mode): state.set_score('yahtzee')
def pressedh():
    if (state.scoring_mode): state.set_score('full house')
def presseds():
    if (state.scoring_mode): state.set_score('small straight')
def pressedl():
    if (state.scoring_mode): state.set_score('large straight')

menus.print_start_turn(state)
menus.print_main_menu(False)

keyboard.add_hotkey('r', pressedr)
keyboard.add_hotkey('e', pressede)
keyboard.add_hotkey('1', pressed1)
keyboard.add_hotkey('2', pressed2)
keyboard.add_hotkey('3', pressed3)
keyboard.add_hotkey('4', pressed4)
keyboard.add_hotkey('5', pressed5)
keyboard.add_hotkey('6', pressed6)
keyboard.add_hotkey('c', pressedc)
keyboard.add_hotkey('t', pressedt)
keyboard.add_hotkey('f', pressedf)
keyboard.add_hotkey('y', pressedy)
keyboard.add_hotkey('h', pressedh)
keyboard.add_hotkey('s', presseds)
keyboard.add_hotkey('l', pressedl)

keyboard.wait('q')

