
def get_cypher() -> int:
    print(f'Type the cypher number', end='')
    field = input(': ')
    if field.isnumeric() and float(field).is_integer():
        return int(field)
    else:
        print('Not a whole number')
        exit(1)

def encrypt(msg: str, cypher: int) -> str:
    encrypted_msg = ''
    for c in msg.lower():
        c = ord(c)
        if c >= 97 and c <= 122:
            c += cypher
            while c > 122:
                c -= 26
            while c < 97:
                c += 26
        encrypted_msg += chr(c)
    return encrypted_msg

def go_again() -> bool:
    again = input('Encyrpt another message? (y)/(n): ').lower()[0]
    return again == 'y'

running = True

while running:
    action = input('type e to entrypt or d to decrypt: ').lower()[0]
    
    msg = ''

    if action == 'e':
        msg = input('Type the message to encrypt: ')
        cypher = get_cypher()
        print(f'Your encyrpted message is: {encrypt(msg, cypher)}')
        running = go_again()

    elif action == 'd':
        msg = input('Type the message to decrypt: ')
        cypher = get_cypher() * -1
        print(f'Your decyrpted message is: {encrypt(msg, cypher)}')
        running = go_again()
