#Game
import tensorflow as tf


board_size = 5



#RL
epsilon = 1
epsilon_decay = 0.95
learning_rate = 0.001
num_layers = 3
num_neurons = 64
activation_function = 'relu'
optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate) #SGD, Adagrad, Adadelta, Adam, Adamax, Nadam, RMSprop


#RL training
save_interval = 20
search_games = 300
search_seconds = 4
max_buffer_size = 500

#Simulation
num_cached_anets = 5
num_games = 300
topp_models_filenames = ["0_4.h5", "140_4.h5"]
thinking_depth = 40




token = "498243c4cc984c1d9f59cdbc42cfb501"