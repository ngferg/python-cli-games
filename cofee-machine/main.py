import machine

coffee_machine = machine.machine()
action = ''


while action != 'q':
    print('Coffee machine menu: ')
    action = input('What drink do you want? (l)atte, (e)sspresso: ').lower()[0]
    if (action == 'l'):
        coffee_machine.make_drink(machine.latte())
    elif (action == 'e'):
        coffee_machine.make_drink(machine.espresso())
    elif (action == 'r'):
        coffee_machine.report()
