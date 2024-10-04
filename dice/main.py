import random
import ascii


print('### Dice Game ###')

die_count=''
last_die_count=''

while True:
    die_count = input('How many dice you want?: ')

    if die_count == '':
        die_count = last_die_count
    if (not die_count.isnumeric() or not float(die_count).is_integer() or int(die_count) < 1):
        print('Not a valid number, get outta here!')
        exit(0)
    
    last_die_count = die_count

    for die in range(0, int(die_count), 1):
        roll = random.randint(1,6)
        print(ascii.get_die(roll))
