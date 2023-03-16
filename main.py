from nim import Nim
from mcts import MCTNode, MonteCarloTreeSearch

tree = MonteCarloTreeSearch((1,6))

for i in range(1000):
    tree.work_down_tree(tree.get_root())

#print("The best action is to remove ", tree.get_best_action(), " stones")
for i in tree.get_liste():
    print("gamestate", i.get_game_state(),"parentState",i.parent.get_game_state(), " visits: ", i.get_visits(), " q_value: ", i.get_q_value(), " uct_value: ", i.get_uct_value())

print(len(tree.get_liste()))
for action, child in tree.get_root().get_children().items():
    print("Action: ", action, " visits: ", child.get_visits(), " q_value: ", child.get_q_value(), " uct_value: ", child.get_uct_value(), "percentage wins", child.get_q_value()/child.get_visits())
print(tree.get_normalized_action_probabilities())
print(tree.get_best_action())