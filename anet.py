

import random

from nim import Nim


class ANET:

    def __init__(self) -> None:
       pass

    def choose_random_action(self, state: tuple[int,int]) -> tuple[int,...]:
        return random.choice(Nim(state).get_legal_actions())