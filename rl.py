from nim import Nim
from hex import Hex
from mcts import MCTNode, MonteCarloTreeSearch
import numpy as np
import parameters as params


import tensorflow as tf
from keras.models import Sequential
from keras.layers import Input, Dense
from anet import ANET


class RL:

    def __init__(self) -> None:
        self.game = Hex()
        self.rpbuffer = np.empty((0,self.game.get_board_size()**2 + 1 + len(self.game.get_all_actions())), dtype=np.float64)
        self.model: Sequential = self.build_model() 
        self.anet = ANET()

    def simulate(self) -> None:
        for i in range(1):
            print(i, "-----------------")
            tree = MonteCarloTreeSearch(anet=ANET())
            self.game = Hex()
            while not self.game.is_final_state():
            
                for i in range(300):
                    tree.work_down_tree(tree.get_root())
                distribution = []
                #print([i[0] for i in tree.get_normalized_action_probabilities()])
                #if the the one action from get_all_actions() is in the action in get_normalized_action_probabilities() then the value of the action is added to the distribution list
                for action in self.game.get_all_actions():
                    if action in [i[0] for i in tree.get_normalized_action_probabilities()]:
                        distribution.append(tree.get_normalized_action_probabilities()[[i[0] for i in tree.get_normalized_action_probabilities()].index(action)][1])
                    else:
                        distribution.append(0.0)
                #print(distribution)
                self.rpbuffer = np.append(self.rpbuffer, np.array([self.game.get_game_state() + tuple(distribution)]), axis=0)
                game_state = self.game.do_action(tree.get_best_action())[0]
                print("Game state: ", game_state)
                print("not_final_state: ")
                tree = MonteCarloTreeSearch(game_state, anet=ANET())
        #print(self.rpbuffer)
            self.fit(self.rpbuffer)
        #save the rpbuffer to a file
        self.anet.save_model(self.rpbuffer, "hex_5_300_10_32_1_128_64_1_64_1_32_1_16_1_8_")

    def build_model(self) -> Sequential:
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Dense(128, activation='relu', input_shape=(self.game.get_board_size()**2 + 1,)))
        model.add(tf.keras.layers.Dense(64, activation='relu'))
        model.add(Input(shape=(self.game.get_board_size()**2 + 1,)))
        model.add(Dense(len(self.game.get_all_actions()), activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model 

    def fit(self, rpbuffer: np.ndarray) -> None:
        X, Y = rpbuffer[:,:-len(self.game.get_all_actions())], rpbuffer[:,-len(self.game.get_all_actions()):]
        self.model.fit(X, Y, epochs=10, batch_size=32, verbose=1)
        print(self.model.predict(X))
        print(len(self.rpbuffer))
