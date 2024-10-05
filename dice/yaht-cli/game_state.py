import menus

class category(object):
    def __init__(self, name: str, hotkey: str, max_players: int, score_method, print_line_after=False):
        self.name = name
        self.hotkey = hotkey
        self.max_players = max_players
        self.scores = ['_'] * self.max_players
        self.print_line_after = print_line_after
        self.score_method = score_method

class state(object):
    def __init__(self, players: int):
        if (players < 1):
            print('At least one player requried')
            exit(1)
        self.max_players = players
        self.current_player = 1
        self.categories = dict[str, category]()
        self.categories['ones'] = category('ones', '(1)', players, self.score_ones)
        self.categories['twos'] = category('twos', '(2)', players, self.score_twos)
        self.categories['threes'] = category('threes', '(3)', players, self.score_threes)
        self.categories['fours'] = category('fours', '(4)', players, self.score_fours)
        self.categories['fives'] = category('fives', '(5)', players, self.score_fives)
        self.categories['sixes'] = category('sixes', '(6)', players, self.score_sixes, True)
        self.categories['bonus'] = category('bonus', '', players, self.score_bonus)
        self.categories['top total'] = category('top total', '', players, self.score_top_total, True)

        self.roll_num=0
        self.dice = [0] * 5
        self.keeps = ['n'] * 5
        self.scoring_mode = False
        self.game_mode = True

    def category_not_scored(self, category: str) -> bool:
        return self.categories[category].scores[self.current_player-1] == '_'
    
    def reset_dice_state(self):
        self.roll_num=0
        self.dice = [0] * 5
        self.keeps = ['n'] * 5

    def next_turn(self):
        self.scoring_mode=False
        self.game_mode=True
        self.reset_dice_state()
        self.current_player += 1
        if (self.current_player > self.max_players):
            self.current_player = 1

        if (self.max_players > 1):
            menus.print_start_turn(self)

        menus.print_main_menu(False)

    def set_score_mode(self):
        self.scoring_mode=True
        self.game_mode=False
        menus.print_score_card(self, True)

    def set_score(self, category: str):
        if (self.category_not_scored(category)):
            self.categories[category].scores[self.current_player-1] = self.categories[category].score_method()
            self.score_top_total()
            menus.print_score_card(self, False)
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
        
    def score_bonus(self) -> int:
        if (self.sum_top() >= 63): 
            self.categories['bonus'].scores[self.current_player-1] = 35
            return 35
        else: 
            self.categories['bonus'].scores[self.current_player-1] = 0
            return 0
    
    def score_top_total(self) -> int:
        total = self.sum_top() + self.score_bonus()
        self.categories['top total'].scores[self.current_player-1] = total
        return total
    
    def sum_top(self) -> int:
        sum = self.get_int_score_from('ones')
        sum += self.get_int_score_from('twos')
        sum += self.get_int_score_from('threes')
        sum += self.get_int_score_from('fours')
        sum += self.get_int_score_from('fives')
        sum += self.get_int_score_from('sixes')
        return sum
    
    def get_int_score_from(self, category: str) -> int:
        if (self.categories[category].scores[self.current_player-1] == '_'): return 0
        return int(self.categories[category].scores[self.current_player-1])