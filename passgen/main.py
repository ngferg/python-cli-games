import string
import random

letters = string.ascii_letters
symbols = ['!', '@', '-', '_', '$', '#', '%']
numbers = string.digits


def int_input(field_name: str) -> int:
    print(f'How many {field_name} would you like?', end='')
    field = input(': ')
    if field.isnumeric() and float(field).is_integer() and int(field) >= 0:
        return int(field)
    else:
        print('Not a positive whole number')
        exit(1)


print('Welcome to passgen!')

letters_count = int_input('letters')
symbols_count = int_input('symbols')
numbers_count = int_input('numbers')

total_length = letters_count + symbols_count + numbers_count
password_list = []

for c in range(0, letters_count):
    password_list.append(random.choice(letters))

for c in range(0, symbols_count):
    password_list.append(random.choice(symbols))

for c in range(0, numbers_count):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ''.join(password_list)

print(f'Your password is {password}')
