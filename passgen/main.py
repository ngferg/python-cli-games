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
password = ''

for c in range(0, total_length):
    c_type = random.randint(0,2)
    
    if c_type == 2 and symbols_count > 0:
        symbols_count -= 1
        password += symbols[random.randint(0, symbols.__len__())]
    else: c -= 1
    if c_type == 1 and numbers_count > 0:
        numbers_count -= 1
        password += numbers[random.randint(0, numbers.__len__())]
    else: c -= 1
    if c_type == 0 and letters_count > 0:
        letters_count -= 1
        password += letters[random.randint(0, letters.__len__())]
    else: c -= 1


print(f'Your password is {password}')
