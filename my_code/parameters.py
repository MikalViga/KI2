#Game
import tensorflow as tf


board_size = 5



#RL
epsilon = 1
epsilon_decay = 0.95
learning_rate = 0.001
num_layers = 3
num_neurons = 64
activation_function = 'relu' #relu, tanh, sigmoid, selu, elu, softplus, softsign, hard_sigmoid, linear
optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate) #SGD, Adagrad, Adadelta, Adam, Adamax, Nadam, RMSprop

#MCTS
actual_games = 1000
search_seconds = 5

#RL training
num_cached_anets = 5
save_interval = 50 #actual_games/num_cached_anets
max_buffer_size = 512


#other
num_cached_anets = 5

#Simulation
num_games = 1
topp_models_filenames = ["c850_4.h5", "d850_5.h5"]
thinking_depth = 40




token = "498243c4cc984c1d9f59cdbc42cfb501"