import random

def shuffle_deck() -> list:
    deck = list('22223333444455556666777788889999JJJJQQQQKKKKAAAA')
    random.shuffle(deck)
    return deck

def score_cards(cards: list[str]) -> int:
    aces = 0
    score = 0
    for card in cards:
        if (card.isdigit()):
            score += int(card)
        elif (card == 'A'):
            score += 11
            aces += 1
        else:
            score += 10
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score

def print_hand(cards: list[str], score: int, is_dealer: bool, hide_card=False):
    if is_dealer:
        print('Dealer\'s Hand: ', end='')
    else:
        print('Player\'s Hand: ', end='')
    
    if hide_card:
        print('* ', end='')
        cards = cards[1:]
    for card in cards:
        print(f'{card} ', end='')
    
    if not hide_card:
        print(f'Score: {score}', end='')
    print('\n')
            
print('Welcome to Blackjack!')


play_again='y'

while play_again == 'y':
    deck = shuffle_deck()
    player_cards = [deck[0], deck[1]]
    player_score = score_cards(player_cards)
    dealer_cards = [deck[2], deck[3]]
    dealer_score = score_cards(dealer_cards)
    card = 4

    print_hand(dealer_cards, dealer_score, True, True)
    print_hand(player_cards, player_score, False)
    blackjack = player_score == 21
    players_turn = not blackjack

    while players_turn:
        action = input('What will you do? (h)it, (s)tand: ').lower()[0]

        if action == 's':
            players_turn = False
        elif action == 'h':
            player_cards.append(deck[card])
            card += 1
            player_score = score_cards(player_cards)
            if player_score >= 21:
                players_turn = False
            print_hand(player_cards, player_score, False)
    
    if blackjack:
        print('Blackjack!  You win this hand!')
    elif player_score > 21:
        print('Bust!  The house wins again...')
    else:
        while dealer_score < 17:
            dealer_cards.append(deck[card])
            card += 1
            dealer_score = score_cards(dealer_cards)
        print_hand(dealer_cards, dealer_score, True)
        if dealer_score > 21:
            print('Dealer Busts, you win!')
        elif player_score > dealer_score:
            print(f'Your {player_score} beats dealer\'s {dealer_score}, you win!')
        elif player_score < dealer_score:
            print(f'Dealer\'s {dealer_score} beats your {player_score}, you lose!')
        else:
            print(f'It\'s a tie, both scoring {player_score}')
    

    play_again = input('play another hand? (y/n): ').lower()[0]

