import random
import copy


class MyPlayer:
    """Prisoner's dilemma destroyer 4000B"""
    def __init__(self, payoff_matrix, number_of_iterations=None):
        self.number_of_iterations = number_of_iterations
        self.games_played = 0
        self.streak_counter_opponent = 0
        self.opponent_first_move = None
        self.opponent_second_move = None
        self.opponent_third_move = None
        self.opponent_last_move = None
        self.opponent_defect = 0
        self.copy_counter = 0
        self.my_last_move = None
        self.my_second_to_last_move = None
        self.Coop_Coop = payoff_matrix[0][0][0]
        self.Defect_Defect = payoff_matrix[1][1][0]
        self.Defect_Coop = payoff_matrix[1][0][0]
        self.Coop_Defect = payoff_matrix[0][1][0]
        self.opponent_opposite = None
        self.play = None
        self.deviation = 2
        self.my_first_move = None
        self.my_second_move = None
        self.switch = True
        self.switch2 = True
        self.is_me = True

    def move(self):
        if self.games_played == 0:
            self.my_first_move = True if self.Defect_Defect < self.Coop_Coop else False
            self.play = self.my_first_move
        elif self.games_played == 1 or self.games_played == 2:
            self.my_second_move = False if self.Defect_Defect < self.Coop_Coop else True
            self.play = self.my_second_move
        else:
            if self.opponent_first_move == self.opponent_second_move == self.opponent_third_move:
                if self.opponent_defect >= self.games_played - self.deviation:
                    self.constant_defect()
                if self.opponent_defect <= self.deviation:
                    self.constant_coop()
                else:
                    self.unknown_strategy()
            elif self.opponent_second_move == self.my_first_move and self.opponent_third_move == self.my_second_move:
                if self.copy_counter >= self.games_played - self.deviation:
                    self.opponent_tft()
                else:
                    self.unknown_strategy()
            elif self.opponent_second_move != self.my_first_move and self.opponent_third_move != self.my_second_move:
                if self.copy_counter <= self.games_played + self.deviation:
                    self.opponent_reverse_tft()
                else:
                    self.unknown_strategy()
            elif self.opponent_first_move == self.my_first_move and\
                    self.opponent_second_move == self.opponent_third_move == self.my_second_move:
                self.playing_against_self()
            else:
                self.unknown_strategy()
        return self.play

    def playing_against_self(self):
        if self.is_me:
            if self.switch:
                if self.my_last_move == self.opponent_last_move:
                    if self.Coop_Coop * 2 >= self.Defect_Defect * 2 and\
                            self.Coop_Coop * 2 >= self.Coop_Defect + self.Defect_Coop:
                        self.play = False
                    elif self.Defect_Defect * 2 >= self.Coop_Defect + self.Defect_Coop:
                        self.play = True
                    else:
                        self.switch = False
                        self.synchronise()
                else:
                    self.is_me = False
                    self.unknown_strategy()
            else:
                self.synchronise()
        else:
            self.unknown_strategy()

    def synchronise(self):
        if self.my_last_move == self.opponent_last_move:
            if self.switch2:
                self.play = random.choice([True, False])
            else:
                self.is_me = False
                self.unknown_strategy()
        else:
            self.switch2 = False
            self.play = False if self.my_last_move else True

    def constant_defect(self):
        self.play = True if self.Defect_Defect >= self.Coop_Defect else False

    def constant_coop(self):
        self.play = True if self.Defect_Coop >= self.Coop_Coop else False

    def tft(self):
        self.play = self.opponent_last_move if random.choices([True, False], weights=[19, 1])[0]\
            else self.opponent_opposite

    def opponent_tft(self):
        if self.Coop_Defect + self.Defect_Coop >= 2 * self.Coop_Coop and\
                self.Coop_Defect + self.Defect_Coop >= 2 * self.Defect_Defect:
            self.play = False if self.my_last_move else True
        elif self.Coop_Coop >= self.Defect_Defect:
            self.play = False
        else:
            self.play = True

    def opponent_reverse_tft(self):
        if self.Coop_Coop + self.Defect_Defect >= 2 * self.Coop_Defect and\
                self.Coop_Coop + self.Defect_Defect >= 2 * self.Defect_Coop:
            self.play = False if self.my_last_move else True
        elif self.Defect_Coop >= self.Coop_Defect:
            self.play = True
        else:
            self.play = False

    def unknown_strategy(self):
        if 10 <= self.games_played <= 30:
            if self.copy_counter >= self.games_played - self.deviation + 1:
                self.opponent_tft()
            elif self.copy_counter <= self.deviation - 1:
                self.opponent_reverse_tft()
            elif self.opponent_defect >= self.games_played - self.deviation + 1:
                self.constant_defect()
            elif self.opponent_defect <= self.deviation - 1:
                self.constant_coop()
            else:
                self.tft()
        elif self.games_played > 30:
            if self.copy_counter >= self.games_played - self.deviation:
                self.opponent_tft()
            elif self.copy_counter <= self.deviation:
                self.opponent_reverse_tft()
            elif self.opponent_defect >= self.games_played - self.deviation:
                self.constant_defect()
            elif self.opponent_defect <= self.deviation:
                self.constant_coop()
            else:
                self.tft()
        else:
            self.tft()

    def record_last_moves(self, my_last_move, opponent_last_move):
        self.games_played += 1
        self.opponent_last_move = opponent_last_move
        self.my_second_to_last_move = copy.copy(self.my_last_move)
        self.my_last_move = my_last_move
        self.opponent_opposite = False if opponent_last_move else True
        if opponent_last_move:
            self.opponent_defect += 1
        if opponent_last_move == self.my_second_to_last_move:
            self.copy_counter += 1
        if self.games_played == 1:
            self.opponent_first_move = opponent_last_move
        if self.games_played == 2:
            self.opponent_second_move = opponent_last_move
        if self.games_played == 3:
            self.opponent_third_move = opponent_last_move
        if self.games_played % 10 == 0:
            self.deviation += 1
