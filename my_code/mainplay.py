from nim import Nim
from mcts import MCTNode, MonteCarloTreeSearch
from hex import Hex
from anet import ANET


a=0
game=Hex()
while False:
    tree.game.print_board()
    for i in range(1000):
        a+=1
        tree.work_down_tree(tree.get_root())
    game.do_action(tree.get_best_action())
    
    game.print_board()
    if game.is_final_state():
        print(game.player_id, "wins")
        break
    game.do_action((int(input("action: ")),int(input("action: "))))

    if game.is_final_state():
        print(game.player_id, "wins")
        break
    tree = MonteCarloTreeSearch(game_state = game.get_game_state(), anet=ANET(filepath="my_code/50_3.h5"))
    
while True:
    tree1=MonteCarloTreeSearch(game_state = game.get_game_state())#, anet=ANET(filepath="my_code/0_4.h5"))
    for i in range(400):
        tree1.work_down_tree(tree1.get_root())
    for i in tree1.get_normalized_action_probabilities():
        print(i)
    game.do_action(tree1.get_best_action())
    print("player 1 did", tree1.get_best_action())
    game.print_board()
    if game.is_final_state():
        print("1 wins")
        break


    tree2=MonteCarloTreeSearch(game_state = game.get_game_state())#, anet=ANET(filepath="my_code/305_3.h5"))
    for i in range(400):
        tree2.work_down_tree(tree2.get_root())
    for i in tree2.get_normalized_action_probabilities():
        print(i)
    game.do_action(tree2.get_best_action())
    print("player 2 did", tree2.get_best_action())
    game.print_board()
    if game.is_final_state():
        print("2 wins")
        break

    