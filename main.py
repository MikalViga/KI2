from nim import Nim
from mcts import MCTNode, MonteCarloTreeSearch

tree = MonteCarloTreeSearch([1,10])

for i in range(1000):
    tree.traverse(tree.get_root())

print("The best action is to remove ", tree.get_best_action(), " stones")

print("The number of times the root node was visited is ", tree.get_root().visits)