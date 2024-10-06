import ascii

print('Welcome to treasure Island.  Your mission is to find the treasure!')

direction=''
while not(direction == 'left' or direction == 'right'):
    direction = input('Will you go (left) or (right)? ').lower()

if direction == 'right':
    print('You fell into a hole... game over!')
    exit(0)

print('You come to a lake...')

while not(direction == 'wait' or direction == 'swim'):
    direction = input('will you (wait) by the lakeside, or try to (swim) across? ').lower()

if direction == 'swim':
    print('You were attacked by a viscous trout and lost your life.  Game over')
    exit(0)

print('A strange old man on a boat sees you waiting and picks you up.')
print('He ferries you across the lake and he drops you off at a temple with three doors...')

while not(direction == 'red' or direction == 'blue' or direction == 'yellow'):
    direction = input('Will you go through the (red), (yellow), or (blue) door? ').lower()

if direction == 'red':
    print('You are horribly burned by a fire trap. Game over!')
    exit(0)
elif direction == 'blue':
    print('Mangy beasts eat you alive.  Game over.')
    exit(0)
else:
    print('You found the treasure... you win!')
    print(ascii.treausre)
