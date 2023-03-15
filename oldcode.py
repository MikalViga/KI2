#RHIS IS OLD CODE, NOT USED IN THE PROJECT

# def expand_node(self, node: MCTNode) -> None:
#         if node.get_game_state() != False:
#             self.counter2+=1
#             if len(Nim(node.get_game_state()).get_legal_actions()) == 0: 
#                 print("DENNNNNNENENENNENENENENENEN overgår alt")
#             for action in Nim(node.get_game_state()).get_legal_actions():
#                 game = Nim(node.get_game_state())
#                 if game.is_final_state():
#                     print("Final state")
#                 else:
#                     child = MCTNode(game.do_action(action), node)
#                     node.add_child(action, child)
    
#     def rollout(self, node: MCTNode) -> int:
#         print("Rollout: ", node.get_game_state())
#         if node.get_game_state() == False:
#             return 0
#         game = Nim(node.get_game_state())
#         while not game.is_final_state():
#             game.do_action(random.choice(game.get_legal_actions()))
#         print("Reward2222: ", game.get_reward())
#         return game.get_reward()
    
#     def backpropagate(self, node: MCTNode, reward: int) -> None:
#         node.update(reward)
#         if node.parent is not None:
#             self.backpropagate(node.parent, reward)
    
    
#     def select(self, node: MCTNode) -> MCTNode:
#         best_node = node.get_children().get(1)
#         for action, child in (node.get_children().items()):
#             if child.uct_value > best_node.uct_value:
#                 best_node = child
#         return best_node


#     def traverse(self, node: MCTNode) -> MCTNode:

#         self.counter+=1
#         if node.children == {}:
#             self.expand_node(node)
#             if len(node.children) == 0:
#                 self.backpropagate(node,0)
#             else:
#                 childnode = random.choice(list(node.children.values()))
#                 reward = self.rollout(childnode)
#                 self.backpropagate(childnode, reward)
#         else:
#             childnode = self.select(node)
#             self.traverse(childnode)

#     def get_root(self) -> MCTNode:
#         return self.root
    
#     def get_best_action(self) -> int:
#         print(self.counter2, "ganger expandert")
#         return max(self.root.children.items(), key=lambda x: x[1].q_value)[0]
