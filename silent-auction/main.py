import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

auctions = dict[str,float]()
running = True

print('Time for a silent auctions')

while running:
    name = input('Please enter your name: ')
    bid = input('Please enter your bid: ')
    auctions[name] = float(bid)
    more = input('Is there another bidder? (y/n): ').lower()[0]
    
    if more != 'y':
        running = False
    cls()

winner = ''
winning_bid = 0.0

for bidder, bid in auctions.items():
    if winning_bid < bid:
        winning_bid = bid
        winner = bidder

print(f'{winner} wins with a bid of {winning_bid}')