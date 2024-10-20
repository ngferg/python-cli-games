import coffee

coffee_machine = coffee.Machine()
action = ''


while action != 'q':
    print('Coffee machine menu: ')
    action = input('What drink do you want? (l)atte, (e)sspresso, (h)ot water: ').lower()[0]
    if (action == 'l'):
        coffee_machine.make_drink(coffee.Latte())
    elif (action == 'e'):
        coffee_machine.make_drink(coffee.Espresso())
    elif (action == 'h'):
        coffee_machine.make_drink(coffee.HotWater())
    elif (action == 'r'):
        coffee_machine.report()
