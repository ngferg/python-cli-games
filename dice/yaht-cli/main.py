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

def set_score_mode():
    state.print_score_card(state.current_player, True)
    state.scoring_mode=True
    state.game_mode=False

def roll():
    if (state.game_mode):
        state.roll_num += 1
        print(f'roll {state.roll_num}')

        for i in range(0,5):
            if (state.keeps[i] == 'n'):
                state.dice[i] = random.randint(1, 6)

        ascii.print_dice(state.dice, state.keeps)

        if (state.roll_num >= 3):
            set_score_mode()
        else:
            menus.print_main_menu()

def end_turn():
    if (state.game_mode):
        set_score_mode()

def keep(die: int):
    if (state.game_mode and state.roll_num > 0):
        current_keep = state.keeps[die-1]
        if (current_keep == 'n'):
            state.keeps[die-1] = 'y'
        else:
            state.keeps[die-1] = 'n'
        ascii.print_dice(state.dice, state.keeps)
        menus.print_main_menu()

def keep1(): keep(1)
def keep2(): keep(2)
def keep3(): keep(3)
def keep4(): keep(4)
def keep5(): keep(5)
def keep6(): keep(6)

def score1(): 
    if (state.scoring_mode): state.set_score('ones')
def score2(): 
    if (state.scoring_mode): state.set_score('twos')
def score3(): 
    if (state.scoring_mode): state.set_score('threes')
def score4(): 
    if (state.scoring_mode): state.set_score('fours')
def score5(): 
    if (state.scoring_mode): state.set_score('fives')
def score6(): 
    if (state.scoring_mode): state.set_score('sixes')

menus.print_start_turn(state)
menus.print_main_menu(False)

keyboard.add_hotkey('r', roll)
keyboard.add_hotkey('k+1', keep1)
keyboard.add_hotkey('k+2', keep2)
keyboard.add_hotkey('k+3', keep3)
keyboard.add_hotkey('k+4', keep4)
keyboard.add_hotkey('k+5', keep5)
keyboard.add_hotkey('k+6', keep6)
keyboard.add_hotkey('1', score1)
keyboard.add_hotkey('2', score2)
keyboard.add_hotkey('3', score3)
keyboard.add_hotkey('4', score4)
keyboard.add_hotkey('5', score5)
keyboard.add_hotkey('6', score6)

keyboard.wait('q')

