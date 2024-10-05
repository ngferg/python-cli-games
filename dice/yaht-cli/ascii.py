import game_state

one = ['+-------+', '|       |', '|   *   |', '|       |', '+-------+']
two = ['+-------+', '| *     |', '|       |', '|     * |', '+-------+']
three = ['+-------+', '|     * |', '|   *   |', '| *     |', '+-------+']
four = ['+-------+', '| *   * |', '|       |', '| *   * |', '+-------+']
five = ['+-------+','| *   * |', '|   *   |', '| *   * |', '+-------+']
six = ['+-------+', '| *   * |', '| *   * |', '| *   * |', '+-------+']

ascii_dice = [one, two, three, four, five, six]

def get_die(face: int) -> str:
    return ascii_dice[face-1]

def print_dice(dice: list, keeps: list):
    print(' (1)        (2)        (3)        (4)        (5)')
    for i in range(0,5):
        for die in dice:
            print(f' {ascii_dice[int(die)-1][i]} ', end='')
        print('')
    print('keep:    ', end='')
    for i in range(0, 5):
        print(f'{keeps[i]}          ', end='')
    print('')