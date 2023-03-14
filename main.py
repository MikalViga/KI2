from nim import Nim
from mcts import MCTNode, MonteCarloTreeSearch

tree = MonteCarloTreeSearch([1,10])

for i in range(100):
    tree.traverse(tree.get_root())

print(tree.get_root().get_children())


#A function returns all the children of a node