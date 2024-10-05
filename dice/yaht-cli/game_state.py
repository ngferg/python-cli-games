
class state(object):
    def __init__(self, players: int):
        if (players < 1):
            print('At least one player requried')
            exit(1)
        self.max_players = players
        self.current_player = 1
        self.score_sheet = dict()
        self.score_sheet['ones'] = ['_'] * self.max_players
        self.score_sheet['twos'] = ['_'] * self.max_players
        self.score_sheet['threes'] = ['_'] * self.max_players
        self.score_sheet['fours'] = ['_'] * self.max_players
        self.score_sheet['fives'] = ['_'] * self.max_players
        self.score_sheet['sixes'] = ['_'] * self.max_players
        self.roll_num=0
        self.dice = [0] * 5
        self.keeps = ['n'] * 5



    def print_score_card(self, player: int):
        print(f'Player {player} score card:')
        print(f'+--------------------+')
        for category, scores in self.score_sheet.items():
            print(f'| {category}: {scores[player-1]}{' '*(16 - str(category).__len__())}|')
        print(f'+--------------------+')
    
    def reset_dice_state(self):
        self.roll_num=0
        self.dice = [0] * 5
        self.keeps = ['n'] * 5
