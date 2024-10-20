
class Drink(object):
    def __init__(self, water: int, name: str, milk=0, coffee=0):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.name=name
    
class Espresso(Drink):
    def __init__(self):
        super().__init__(water=50, coffee=100, name='espresso')


class Latte(Drink):
    def __init__(self):
        super().__init__(water=100, coffee=50, milk=50, name='latte')

class HotWater(Drink):
    def __init__(self):
        super().__init__(water=200, name='hot water')

class Machine(object):
    def __init__(self):
        self.water=1000
        self.milk=100
        self.coffee=200
    
    def make_drink(self, drink: Drink):
        if self.water < drink.water:
            print('Not enough water')
        elif self.milk < drink.milk:
            print('Not enough milk')
        elif self.coffee < drink.coffee:
            print('Not enough cofee')
        else:
            self.water -= drink.water
            self.milk -= drink.milk
            self.coffee -= drink.coffee
            print(f"Here's your {drink.name}")
    
    def report(self):
        print(f"""
Water: {self.water}
Milk: {self.milk}
Coffee: {self.coffee}
              """)