import random

games = 0
pieces_needed = 4
drop_rate = 12

print('Got a piece at: ', end='')
while pieces_needed > 0:
    games += 1
    if random.randint(1, drop_rate) == 1:
        pieces_needed -= 1
        print(f'{games} ', end='')

print(f'\nFinished at {games}')