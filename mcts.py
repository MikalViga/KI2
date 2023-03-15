from __future__ import annotations
import math
import random
from nim import Nim

class MCTNode:

    def __init__(self, game_state: tuple[int,int], parent: MCTNode = None) -> None:
        self.parent = parent
        self.game_state = game_state
        self.children = dict()
        self.visits = 1
        self.q_value = 0
        self.uct_value = 1

    def get_children(self) -> dict[int, MCTNode]:
        return self.children

    def get_game_state(self) -> tuple[int,int]:
        return self.game_state
    
    def get_visits(self) -> int:
        return self.visits
    
    def get_q_value(self) -> int:
        return self.q_value

    def get_uct_value(self) -> int:
        if self.parent is None:
            return 0
        self.uct_value = 5 * (2 * math.log(self.parent.visits) / self.visits) ** 0.5 
        return self.uct_value

    def get_win_percentage(self) -> float:
        return self.q_value/self.visits
    def add_child(self, action: int, child: MCTNode) -> None:
        self.children[action] = child

    #prints game state and and the state of the children
    def __str__(self) -> str:
        string="\n"
        for action, child in self.children.items():
            string+="Action: "+str(action)+" "+str(child.get_uct_value())+"\n"
        return f"game state: {self.game_state}, children: {string}"


class MonteCarloTreeSearch:

    def __init__(self, game_state) -> None:
        self.root = MCTNode(game_state)
        self.liste=[]
    
    def expand_node(self, node: MCTNode) -> None:
        if node.get_game_state() != False:
            if node.children == {}:
                for action in Nim(node.get_game_state()).get_legal_actions():
                    print("Action: ", action, "game state: ", node.get_game_state())
                    game = Nim(node.get_game_state())
                    game_state, reward = game.do_action(action)
                    child = MCTNode(game_state, node)
                    node.add_child(action, child)
                    self.liste.append(child)
    
    def rollout(self, node: MCTNode) -> int:
        game = Nim(node.get_game_state())
        reward = 0
        while not game.is_final_state():
            state, reward = game.do_action(random.choice(game.get_legal_actions()))
        return reward

    def backpropagate(self, node: MCTNode, reward: int) -> None:
        node.visits += 1
        node.q_value += reward
        if node.parent is not None:
            node.q_value += reward
            self.backpropagate(node.parent, reward)

    def tree_policy(self, node: MCTNode) -> MCTNode:
        #node.visits += 1
        print("player", node.get_game_state()[0])
        if Nim(node.game_state).is_final_state():
            self.backpropagate(node, Nim(node.game_state).get_reward())
            print("leaf is final state")
            return node
        if node.children == {}:
            return node
        else:
            best_node = node.children[1]
            for action, child in node.children.items():
                if node.get_game_state()[0] == 1:
                    if child.get_uct_value() + child.get_win_percentage() > best_node.get_uct_value() + best_node.get_win_percentage():
                        best_node = child
                else:
                    if child.get_uct_value() - child.get_win_percentage() < best_node.get_uct_value() - best_node.get_win_percentage():
                        best_node = child
            return self.tree_policy(best_node)
        

    def work_down_tree(self, node: MCTNode) -> None:
        leaf_node = self.tree_policy(node)
        self.expand_node(leaf_node)
        print(leaf_node)
        childnodes = list(leaf_node.children.values())
        if  len(childnodes) > 0:
            print("We roll out")
            child = random.choice(childnodes)
            reward = self.rollout(child)
            self.backpropagate(child, reward)


        # for action, child in leaf_node.children.items():
        #     reward = self.rollout(child)
        #     self.backpropagate(child, reward)

    def get_root(self) -> MCTNode:
        return self.root
    
    def get_best_action(self) -> int:
        return max(self.root.children.items(), key=lambda x: x[1].q_value)[0]

    def get_liste(self) -> list[MCTNode]:
        return self.liste