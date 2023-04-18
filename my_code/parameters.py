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
actual_games = 10
search_seconds = 5

#RL training
num_cached_anets = 5
save_interval = 2 #actual_games/num_cached_anets
max_buffer_size = 512
gen_name = "g"

#other
num_cached_anets = 5

#Simulation
num_games = 100
topp_models_filenames = ["f0_5.h5","f0_5.h5"]




token = "498243c4cc984c1d9f59cdbc42cfb501"