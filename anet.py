import random

import numpy as np
import parameters as params
from nimKI import Nim
from hexKI import Hex
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Input, Dense




class ANET:

    def __init__(self) -> None:
        self.game = Hex()
        self.model: Sequential = self.build_model()


    def choose_random_action(self, state: tuple[int,int]) -> tuple[int,...]:
        #print("Chooseing random action")
        return random.choice(Hex(state).get_legal_actions())

    def choose_greedy_action(self, state: tuple[int,int]) -> tuple[int,...]:
        game = Hex(state)
        valid_actions = game.get_action_mask()
        #print("Start predict")
        #probs = self.model.predict(np.array([state]))
        #print("End predict")
        #actions = valid_actions * probs
        #print(actions)
        #print(np.argmax(actions))
        return 1#np.argmax(actions)
    

    def build_model(self) -> Sequential:
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Dense(128, activation='relu', input_shape=(self.game.get_board_size()**2 + 1,)))
        model.add(tf.keras.layers.Dense(64, activation='relu'))
        model.add(Input(shape=(self.game.get_board_size()**2 + 1,)))
        model.add(Dense(len(self.game.get_all_actions()), activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model 

    def fit(self, rpbuffer: np.ndarray) -> None:
        X, Y = rpbuffer[:,:-len(self.game.get_all_actions())], rpbuffer[:,-len(self.game.get_all_actions()):]
        self.model.fit(X, Y, epochs=10, batch_size=32, verbose=1)
        print(self.model.predict(X))
        print(len(self.rpbuffer))