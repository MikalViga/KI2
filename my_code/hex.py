from disjoint_set import DisjointSet
import numpy as np
from game import Game
import parameters as params


class Hex(Game):

    opposite_player = {
        1: -1,
        -1: 1
    }

    def __init__(self, game_state: tuple[int,...] = None) -> None:
        if game_state is not None:
            self.game_state = game_state
            self.player_id = game_state[0]
            self.size = int(len(game_state[1:])**0.5)
            self.board = [[game_state[1:][i*self.size+j] for j in range(self.size)] for i in range(self.size)]
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
                    if self.board[i][j] == -1:
                        for (x,y) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1), (i+1,j-1),(i-1,j+1)]:
                            if(x>=0 and x<self.size and y>=0 and y<self.size and self.board[x][y] == self.board[i][j]):
                                self.ds_blue.union((i,j), (x,y))  
        if game_state is None:
            self.size = params.board_size
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
            print("Illegal move",(i,j))
            print(self.board)
            print(self.player_id)
            print(self.game_state)
            return "Illegal move"
        if self.board[i][j] != 0:
            print("Illegal move",(i,j))
            print(self.board)
            print(self.player_id)
            print(self.game_state)
            print("Illegal move",(i,j))
            return "Illegal move"
        if player == 1:
            ds = self.ds_red
            self.board[i][j] = 1
        else:
            ds = self.ds_blue
            self.board[i][j] = -1
        for (x,y) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1), (i+1,j-1),(i-1,j+1)]:
            if x>=0 and x<self.size and y>=0 and y<self.size and self.board[x][y] == self.board[i][j]:
                ds.union((i,j),(x,y))
        if self.is_final_state():
            return self.get_game_state(), self.get_reward()
        self.player_id = self.opposite_player[self.player_id]
        return self.get_game_state(), 0
    
    def is_final_state(self) -> bool:
        self.get_game_state()
        return self.ds_red.find(self.top_node) == self.ds_red.find(self.bottom_node) or self.ds_blue.find(self.west_node) == self.ds_blue.find(self.east_node)
    
    #prints board with the connections between the nodes
    def print_board(self) -> str:
        s = ""#+"Player " + str(self.player_id) + " to move \n"
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 1:
                    s += "R "
                elif self.board[i][j] == -1:
                    s += "B "
                else:
                    s += ". "
            s += "\n"
        print(s)
    
    #print the board in a diamond structrure 
    def print_board_diamond(self) -> str:
        print("Player " + str(self.player_id) + " to move \n")        
        a = np.array(self.board)
        b = [np.diag(a[-1:-a.shape[0]-1:-1,:], i).tolist() for i in range(-a.shape[0]+1,a.shape[0])]
        for i in b:
            print(str(i).center(50), sep=" ")
        

    def print_board_diamond1(self) -> None:
        print("Player" + str(self.player_id) + " to move \n")
        print(self.get_game_state())
        brettet = self.get_game_state()[1:]
        a = np.array(brettet)
        
        d = {0: "▢", 1: "R", -1: "B"}
        a = np.vectorize(d.get)(a.astype(int))
        
        i = 1
        
        for j in range(self.size*2-1):
            b = a[:i]
            a = a[i:]
            
            b = np.ndarray.tolist(b)
            if i != 1:
                k = 1
                while k < len(b):
                    b.insert(k, '⎯')
                    k = (k+2)
            
            diagon = []
            if j < self.size-1:
                i += 1
                k = 0
                while k < len(b):
                    diagon.append("⟋ ⟍")
                    k = (k+2)
            else: 
                i -=1
                k = 1
                while k < len(b):
                    diagon.append("⟍ ⟋")
                    k = (k+2)

            c = " ".join(b)
            print(*str(c).center(20))
        
            c = " ".join(diagon)    
            print(*str(c).center(20))

    def print_diamond2(self) -> None:
        a = np.array(self.board)
        b = [np.diag(a[-1:-a.shape[0]-1:-1,:], i).tolist() for i in range(-a.shape[0]+1,a.shape[0])]
        for i in range(len(b)):
            s = ""
            for j in range(len(b[i])):
                if b[i][j] == 1:
                    s += "R"
                elif b[i][j] == -1:
                    s += "B"
                else:
                    s += "▢"
                if j != len(b[i])-1:
                    s += " - "
            print(s.center(50), sep=" ")
            if i <self.size-1:
                print((("/ " + "\\ ")*len(b[i])).center(50), sep=" ")
            else:
                print((("\\ " + "/ ")*(len(b[i])-1)).center(50), sep=" ")
            


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
    
    #A function that returns an array of all actions. Valid actions are equal to 1, invalid are equal to 0.
    def get_action_mask(self) -> list[int]:
        return [1 if self.board[i][j] == 0 else 0 for i in range(self.size) for j in range(self.size)]