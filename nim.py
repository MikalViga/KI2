


class Nim:

    opposite_player = {
        1: 2,
        2: 1
    }

    def __init__(self, state: tuple[int,int] = None) -> None:
        self.__max_stones = 3
        self.__player_id = 1
        self.__board = 12
        self.reset(state)
    

    
    def reset(self, state : tuple[int,int] = None) -> tuple[int,int]:
        if state is None:
            self.__player_id = 1
        else:
            self.__player_id = state[0]
            self.__board = state[1]
        return self.__get_state()

    def __get_state(self) -> tuple[int, int]:
        return (self.__player_id, self.__board)
    
    
    def do_action(self, action: int) -> tuple[int,int]:
        if action > self.__board:
            print("Illegal action")
            raise ValueError("Illegal action")
        if action > self.__max_stones:
            print("Illegal action")
            raise ValueError("Illegal action")
        self.__board -= action
        if self.is_final_state():
            return False
        self.__player_id = self.opposite_player[self.__player_id]
        return self.__get_state()

    def get_reward(self) -> int:
        return 1 if self.__player_id == 1 else -1


    def is_final_state(self) -> bool:
        return self.__board == 0
    def get_player_id(self) -> int:
        return self.__player_id
    def get_board(self) -> int:
        return self.__board
    def get_max_stones(self) -> int:
        return self.__max_stones
    def get_legal_actions(self) -> tuple[int,...]:
        return [i for i in range(1, min(self.__board, self.__max_stones)+1)]

    def __str__(self) -> str:
        return f"player: {self.__player_id}, board: {self.__board}"