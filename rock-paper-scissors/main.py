import random
import ascii

rps = {
    0: 'r',
    1: 'p',
    2: 's'
}

ascii_map = {
    'r': ascii.rock,
    'p': ascii.paper,
    's': ascii.scissors
}

print("Let's play Rock Paper Scissors!")

choice = ''

while not(choice == 'r' or choice == 'p' or choice == 's'):
    choice = input("You choose!  (r)ock, (p)aper, or (s)cissors? ").lower()[0]

print(ascii_map[choice])

cpu_choice = rps[random.randint(0, 2)]

print(f'computer chooses... {cpu_choice}')
print(ascii_map[cpu_choice])

if choice == cpu_choice:
    print("It's a draw!")
elif (choice == 'r' and cpu_choice == 's') or (choice == 'p' and cpu_choice == 'r') or (choice == 's' and cpu_choice == 'p'):
    print('You win! :)')
else:
    print('CPU wins... :(')
