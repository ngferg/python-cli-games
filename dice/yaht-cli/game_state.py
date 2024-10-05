import menus

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
        self.category_hot_keys = {
            'ones': '(1)',
            'twos': '(2)',
            'threes': '(3)',
            'fours': '(4)',
            'fives': '(5)',
            'sixes': '(6)'
        }
        self.category_score_methods = {
            'ones': self.score_ones,
            'twos': self.score_twos,
            'threes': self.score_threes,
            'fours': self.score_fours,
            'fives': self.score_fives,
            'sixes': self.score_sixes
        }

        self.roll_num=0
        self.dice = [0] * 5
        self.keeps = ['n'] * 5
        self.scoring_mode = False
        self.game_mode = True

    def category_not_scored(self, category: str) -> bool:
        return self.score_sheet[category][self.current_player-1] == '_'

    def print_score_card(self, player: int, with_available_scores: bool):
        print(f'Player {player} score card:')
        print(f'+--------------------+')
        for category, scores in self.score_sheet.items():
            print(f'| {category}: {scores[player-1]}{' '*(16 - str(category).__len__())}| ', end='')
            if (with_available_scores and self.category_not_scored(category)):
                print(f'{self.category_hot_keys[category]} {self.category_score_methods[category]()}', end='')
            print()
        print(f'+--------------------+')
        if (with_available_scores):
            print('Press the button for the score you want to keep')
    
    def reset_dice_state(self):
        self.roll_num=0
        self.dice = [0] * 5
        self.keeps = ['n'] * 5

    def next_turn(self):
        self.reset_dice_state()
        self.current_player += 1
        if (self.current_player > self.max_players):
            self.current_player = 1
        self.scoring_mode=False
        self.game_mode=True
        menus.print_main_menu(False)

    def set_score(self, category: str):
        if (self.category_not_scored(category)):
            self.score_sheet[category][self.current_player-1] = self.category_score_methods[category]()
            self.print_score_card(self.current_player, False)
            self.next_turn()
    
    
    def score_top_numbers(self, num: int) -> int:
        score = 0
        for die in self.dice:
            if (die == num):
                score += die
        return score
    
    def score_ones(self) -> int:
        return self.score_top_numbers(1)
    def score_twos(self) -> int:
        return self.score_top_numbers(2)
    def score_threes(self) -> int:
        return self.score_top_numbers(3)
    def score_fours(self) -> int:
        return self.score_top_numbers(4)
    def score_fives(self) -> int:
        return self.score_top_numbers(5)
    def score_sixes(self) -> int:
        return self.score_top_numbers(6)
        