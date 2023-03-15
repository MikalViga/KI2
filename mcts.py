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
        self.uct_value = 0.00001

    def get_children(self) -> dict[int, MCTNode]:
        return self.children

    def get_game_state(self) -> tuple[int,int]:
        return self.game_state

    def add_child(self, action: int, child: MCTNode) -> None:
        self.children[action] = child
    
    def update(self, reward: int) -> None:
        self.visits += 1
        self.q_value += reward
        if self.parent is not None:
            self.uct_value = self.q_value / self.visits + 2 * (2 * math.log(self.parent.visits) / self.visits) ** 0.5

    #prints game state and children
    def __str__(self) -> str:
        return f"game state: {self.game_state}, children: {self.children}"
    

class MonteCarloTreeSearch:

    def __init__(self, game_state) -> None:
        self.root = MCTNode(game_state)
        self.counter=0
        self.counter2=0
    
    def expand_node(self, node: MCTNode) -> None:
        if node.get_game_state() != False:
            self.counter2+=1
            for action in Nim(node.get_game_state()).get_legal_actions():
                game = Nim(node.get_game_state())
                if game.is_final_state():
                    print("Final state")
                else:
                    child = MCTNode(game.do_action(action), node)
                    node.add_child(action, child)
    
    def rollout(self, node: MCTNode) -> int:
        if node.get_game_state() == False:
            return 0
        game = Nim(node.get_game_state())
        while not game.is_final_state():
            game.do_action(random.choice(game.get_legal_actions()))
        return game.get_reward()
    
    def backpropagate(self, node: MCTNode, reward: int) -> None:
        node.update(reward)
        if node.parent is not None:
            self.backpropagate(node.parent, reward)
    
    # def select(self, node: MCTNode) -> MCTNode:
    #     if node.children == {}:
    #         return node
    #     else:
    #         for action, child in node.children.items():
    #             child.uct_value = child.q_value / child.visits + 2 * (2 * math.log(node.visits) / child.visits) ** 0.5
    #         return self.select(max(node.children.items(), key=lambda x: x[1].uct_value)[1])
    
    def select(self, node: MCTNode) -> MCTNode:
        best_node = node.get_children().get(1)
        for action, child in (node.get_children().items()):
            if child.uct_value > best_node.uct_value:
                best_node = child
        return best_node


    def traverse(self, node: MCTNode) -> MCTNode:
        print("Går inn  ",self.counter, "gang")
        self.counter+=1
        if node.children == {}:
            self.expand_node(node)
            if len(node.children) == 0:
                self.backpropagate(node,0)
            else:
                childnode = random.choice(list(node.children.values()))
                reward = self.rollout(childnode)
                self.backpropagate(childnode, reward)
        else:
            print(node.get_children())
            childnode = self.select(node)
            self.traverse(childnode)

    def get_root(self) -> MCTNode:
        return self.root
    
    def get_best_action(self) -> int:
        print(self.counter2, "ganger expandert")
        return max(self.root.children.items(), key=lambda x: x[1].q_value)[0]
