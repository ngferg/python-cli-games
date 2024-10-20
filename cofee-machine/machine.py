
class drink(object):
    def __init__(self):
        self.water = 0
        self.milk = 0
        self.coffee = 0
        self.name='generic drink'
    
class espresso(drink):
    def __init__(self):
        super().__init__()
        self.water = 50
        self.coffee = 100
        self.name = 'espresso'

class latte(drink):
    def __init__(self):
        super().__init__()
        self.water = 100
        self.coffee = 50
        self.milk = 50
        self.name = 'latte'

class machine(object):
    def __init__(self):
        self.water=500
        self.milk=100
        self.coffee=200
    
    def make_drink(self, drink: drink):
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