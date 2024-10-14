import random
from typing import List
import ascii

words = []
with open('resources/words_alpha.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        words.append(line.strip())

found_letters = []
chosen_word = random.choice(words)
state = 0

def process_game_logic(chosen_word: str, found_letters: List[str]) -> bool:
    won = True
    print('')
    print('')
    for c in chosen_word:
        if found_letters.__contains__(c):
            print(f' {c} ', end='')
        else:
            won = False
            print(' _ ', end='')
    print('')
    return won

print('Welcome to hangman ###')

while state < 7:

    won = process_game_logic(chosen_word, found_letters)
    if won:
        print('')
        print('GZ!')
        print('You win!')
        exit(0)

    print('')
    print('')
    print(ascii.hangmans[state])
    letter = input('Guess a letter: ').lower()[0]
    if (chosen_word.__contains__(letter)):
        print('You got a letter! ')
        if not found_letters.__contains__(letter):
            found_letters.append(letter)
    else:
        print('oof, not there')
        state += 1

print(ascii.hangmans[state])
process_game_logic(chosen_word, found_letters)
print('You lose! Good day sir!')
print(f'Answer was: {chosen_word}')
