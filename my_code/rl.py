from nim import Nim
from hex import Hex
from mcts import MCTNode, MonteCarloTreeSearch
import numpy as np
import parameters as params
import time 

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Input, Dense
from anet import ANET


class RL:

    def __init__(self) -> None:
        self.game = Hex()
        self.rpbuffer = np.empty((0,self.game.get_board_size()**2 + 1 + len(self.game.get_all_actions())), dtype=np.float64)
        self.anet = ANET() #ANET(filepath="my_code/305_3.h5")
        self.games = 15
        self.seconds = 4

    def simulate(self) -> None:
       
        for i in range(self.games):
            print("game", i, "started")
            tree = MonteCarloTreeSearch(anet=ANET())
            self.game = Hex()
            self.anet.reset_epsilon()
            while not self.game.is_final_state():
                t_end = time.time() + self.seconds
                runs = 0
                while time.time() < t_end and runs < 1000:
                    tree.work_down_tree(tree.get_root())
                    if runs % 100 == 0:
                        print("Runs: ", runs)
                    runs+=1
                distribution = []
                for action in self.game.get_all_actions():
                    if action in [i[0] for i in tree.get_normalized_action_probabilities()]:
                        distribution.append(tree.get_normalized_action_probabilities()[[i[0] for i in tree.get_normalized_action_probabilities()].index(action)][1])
                    else:
                        distribution.append(0.0)
                self.rpbuffer = np.append(self.rpbuffer, np.array([self.game.get_game_state() + tuple(distribution)]), axis=0)
                game_state = self.game.do_action(tree.get_best_action())[0]
                tree = MonteCarloTreeSearch(game_state, anet=ANET())
            self.anet.fit(self.rpbuffer)
        self.anet.save_model(self.rpbuffer, "my_code/"+str(self.games)+"_"+str(self.seconds))

