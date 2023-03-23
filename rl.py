from nim import Nim
from hex import Hex
from mcts import MCTNode, MonteCarloTreeSearch
import numpy as np

class RL:

    def __init__(self) -> None:
        self.game = Hex()
        self.rpbuffer = np.empty((self.game.get_board_size()**2 + 1 + len(self.game.get_all_actions())), dtype=np.float64)

    def simulate(self) -> None:
        tree = MonteCarloTreeSearch()
        while not self.game.is_final_state():
            for i in range(1000):
                tree.work_down_tree(tree.get_root())
            distribution = []

            #if the the one action from get_all_actions() is in the action in get_normalized_action_probabilities() then the value of the action is added to the distribution list
            for action in self.game.get_all_actions():
                if action in tree.get_normalized_action_probabilities():
                    distribution.append(tree.get_normalized_action_probabilities()[action])
                else:
                    distribution.append(0.0)

            
            
    
            self.rpbuffer = np.append(self.rpbuffer, np.array(self.game.get_game_state() + tuple(distribution)), axis=0)
            game_state = self.game.do_action(tree.get_best_action())[0]
            tree = MonteCarloTreeSearch(game_state)
            #print(self.rpbuffer)
            
        