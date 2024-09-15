# PrisonnersDilemma
A player of repetitive Prisoner's Dilemma developed in Python

In a three round tournament of 146 students placed 15th in the first, 2nd in the second round and 75th in third round.

Prisoner's Dilemma is a game in which each player chooses whether they want to Cooperate or Defect their opponent. Based on what each player chooses they are awarded points based on a payoff matrix. A payoff matrix may be, for example, (((1, 1), (5, 0)), ((0, 5), (3, 3)) - first number in a pair is the payoff of first player and second is the payoff for second player, first row is the payoff if the first player Cooperates and the second row, if they Defect. Similarly the first column is the payoff if second player Cooparates and second if they Defect. For example, if the first player Cooperates and the second Defects, the first player is awarded 5 points and the second zero.

My player receives a payoff matrix (2D array of pairs) and may receive the number of iterations with the given opponent when initialized (__init__). 

My player's method "select_move" takes no input parameters and returns False if the player Cooperates or True if it Defects.

My player's method "record_last_moves" takes two boolean input parameters, my player's move in last round and the opponent's move in last round. This is so a player can decide on it's strategy as the game progresses.

Both these functions were in the tournament limited by a time limit of one second on the school's server.

My player works on analysing the strategy of it's opponent, unless there is a clear correct strategy (for example always play Defect) based on the payoff matrix. It begins playing the Tit for Tat strategy, mirroring every move of the opponent. As the game progresses the player decides if it's worth it to continue with this strategy or play another one.
