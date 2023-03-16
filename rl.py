from nim import Nim
from mcts import MCTNode, MonteCarloTreeSearch

class RL:

    def __init__(self) -> None:
        self.game = Nim()
        self.rpbuffer = dict()

    def simulate(self) -> None:
        self.game.reset()
        tree = MonteCarloTreeSearch((1,6))
        while not self.game.is_final_state():
            for i in range(1000):
                tree.work_down_tree(tree.get_root())
            self.rpbuffer[self.game.get_game_state()] = tree.get_normalized_action_probabilities()
            game_state = self.game.do_action(tree.get_best_action())[0]
            tree = MonteCarloTreeSearch(game_state)
            print(self.rpbuffer)
            wait = input("Press enter to continue")

