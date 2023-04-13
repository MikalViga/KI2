

from matplotlib import pyplot as plt
from anet import ANET
from mcts import MonteCarloTreeSearch
from hex import Hex
import parameters as params


class TOPP:

    def __init__(self) -> None:
        self.agents = [ANET("my_code/"+str(i)) for i in params.topp_models_filenames]
        self.agent_names = params.topp_models_filenames
        self.num_games = params.num_games
        self.stastistics = [[[] for i in range(len(self.agents))] for j in range(len(self.agents))]
        self.stastistics2 = [0 for i in range(len(self.agents))]
    
    #def update_s

    def simulate_game(self, agent1, agent2) -> int:
        game = Hex()
        while True:
            move1 = agent1.choose_from_probabilities(game.get_game_state())
            game.do_action(move1)
            game.print_board()
            if game.is_final_state():
                print(self.agent_names[self.agents.index(agent1)]," wins")
                return 1
            move2 = agent1.choose_from_probabilities(game.get_game_state())
            game.do_action(move2)
            
            game.print_board()
            if game.is_final_state():
                print(self.agent_names[self.agents.index(agent2)]," wins")
                return 2
    
    def simulate_games(self) -> None:
        start_turn = 1
        for i in range(len(self.agents)):
            for j in range(i+1, len(self.agents)):
                start_turn = 1
                for k in range(self.num_games):
                    print("game", k, "of", self.num_games, "between", self.agent_names[i], "and", self.agent_names[j])
                    if start_turn == 1:
                        print("starting turn:", self.agent_names[i])
                        simulated_game = self.simulate_game(self.agents[i], self.agents[j])
                        start_turn = 1
                        self.stastistics[i][j].append(simulated_game)
                        self.stastistics[j][i].append(3-self.stastistics[i][j][-1])
                        if simulated_game == 1:
                            self.stastistics2[i] += 1
                        else:
                            self.stastistics2[j] += 1
                    else:
                        print("starting turn:", self.agent_names[j])
                        simulated_game = self.simulate_game(self.agents[j], self.agents[i])
                        start_turn = 2
                        self.stastistics[j][i].append(simulated_game)
                        self.stastistics[i][j].append(3-self.stastistics[j][i][-1])
                        if simulated_game == 1:
                            self.stastistics2[j] += 1
                        else:
                            self.stastistics2[i] += 1
    
    def print_statistics(self) -> None:
        for i in range(len(self.agents)):
            for j in range(i+1, len(self.agents)):
                print("agent", i, "vs", j, ":", self.stastistics[i][j].count(1), ":", self.stastistics[i][j].count(2))
    
    #a function that shows the total win rate of each agent for the whole tournament in a graph
    def show_total_win_rate(self) -> None:
        number = (len(self.agents)-1)*self.num_games
        stats_list = []
        for i in range(len(self.agents)):
            stats = self.stastistics2[i]/number
            print("agent", i, ":", stats)
            stats_list.append(stats)
        plt.bar(range(len(self.agents)), stats)
        #plt.show()