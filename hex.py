from disjoint_set import DisjointSet
from game import Game

class Hex(Game):

    opposite_player = {
        1: 2,
        2: 1
    }

    def __init__(self, game_state: tuple[int,...] = None) -> None:
        if game_state is not None:
            self.game_state = game_state
            #print("game state: ", self.game_state)
            self.player_id = game_state[0]
            self.size = int(len(game_state[1:])**0.5)
            self.board = [[game_state[1:][i*self.size+j] for j in range(self.size)] for i in range(self.size)]
            #print(self.board)
            self.cells = [(i,j) for i in range(self.size) for j in range(self.size)]
            self.top_node =(-1,0)
            self.west_node = (0,-1)
            self.bottom_node = (self.size,0)
            self.east_node = (0,self.size)
            self.ds_red = DisjointSet(self.cells + [self.top_node, self.bottom_node])
            self.ds_blue = DisjointSet(self.cells + [self.west_node, self.east_node])
            for i in range(self.size):
                self.ds_red.union(self.top_node, (0,i))
                self.ds_red.union(self.bottom_node, (self.size-1,i))
                self.ds_blue.union(self.west_node, (i,0))
                self.ds_blue.union(self.east_node, (i,self.size-1))
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j] == 1:
                        for (x,y) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1), (i+1,j-1),(i-1,j+1)]:
                            if(x>=0 and x<self.size and y>=0 and y<self.size and self.board[x][y] == self.board[i][j]):
                                self.ds_red.union((i,j), (x,y))
                    if self.board[i][j] == 2:
                        for (x,y) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1), (i+1,j-1),(i-1,j+1)]:
                            if(x>=0 and x<self.size and y>=0 and y<self.size and self.board[x][y] == self.board[i][j]):
                                self.ds_blue.union((i,j), (x,y))  
        if game_state is None:
            self.size = 7
            self.board = [[0 for i in range(self.size)] for j in range(self.size)]
            self.cells = [(i,j) for i in range(self.size) for j in range(self.size)]
            self.player_id = 1
            self.game_state = self.player_id, *sum(self.board, [])
            self.top_node =(-1,0)
            self.west_node = (0,-1)
            self.bottom_node = (self.size,0)
            self.east_node = (0,self.size)
            self.ds_red = DisjointSet(self.cells + [self.top_node, self.bottom_node])
            self.ds_blue = DisjointSet(self.cells + [self.west_node, self.east_node])
            for i in range(self.size):
                self.ds_red.union(self.top_node, (0,i))
                self.ds_red.union(self.bottom_node, (self.size-1,i))
                self.ds_blue.union(self.west_node, (i,0))
                self.ds_blue.union(self.east_node, (i,self.size-1))
        
        
    def do_action(self, action: tuple[int,int]) -> tuple[tuple[int,...],int]:
        i = action[0]
        j = action[1]
        player = self.player_id
        if i>=self.size or j>=self.size or i<0 or j<0:
            return "Illegal move"
        if self.board[i][j] != 0:
            return "Illegal move"
        if player == 1:
            ds = self.ds_red
            self.board[i][j] = 1
        else:
            ds = self.ds_blue
            self.board[i][j] = 2
        for (x,y) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1), (i+1,j-1),(i-1,j+1)]:
            if x>=0 and x<self.size and y>=0 and y<self.size and self.board[x][y] == self.board[i][j]:
                ds.union((i,j),(x,y))

        if self.is_final_state():
            #print(action, "Player", player, "wins!", self.get_game_state()[0], "turn")
            #print("Player", player, "wins!")
            return self.get_game_state(), self.get_reward()
        self.player_id = self.opposite_player[self.player_id]
        return self.get_game_state(), 0
    
    def is_final_state(self) -> bool:
        self.get_game_state()
        return self.ds_red.find(self.top_node) == self.ds_red.find(self.bottom_node) or self.ds_blue.find(self.west_node) == self.ds_blue.find(self.east_node)
    
    #prints board with the connections between the nodes
    def print_board(self) -> str:
        s = "Player " + str(self.player_id) + " to move \n"
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 1:
                    s += "R "
                elif self.board[i][j] == 2:
                    s += "B "
                else:
                    s += ". "
            s += "\n"
        print(s)
    
    def get_reward(self) -> int:
        return 1 if self.player_id == 1 else -1

    def get_game_state(self)-> tuple[int,...]:
        self.game_state = self.player_id, *self.board
        return self.player_id, *sum(self.board, [])
    
    def get_legal_actions(self) -> list[tuple[int,int]]:
        return [(i,j) for i in range(self.size) for j in range(self.size) if self.board[i][j] == 0]
    
    def get_cells(self) -> list[tuple[int,int]]:
        return self.cells

    def get_ds_red(self) -> DisjointSet:
        return self.ds_red.find(self.bottom_node)

    def get_ds_blue(self) -> DisjointSet:
        return self.ds_blue

    #A function that returns all actions that are legal action if the game just started
    def get_all_actions(self) -> list[tuple[int,int]]:
        return [(i,j) for i in range(self.size) for j in range(self.size)]

    def get_board_size(self) -> int:
        return self.size