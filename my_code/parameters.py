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
save_interval = 50
actual_games = 1000
search_seconds = 5
max_buffer_size = 512

#Simulation
num_cached_anets = 5
num_games = 75
topp_models_filenames = ["c950_4.h5", "c400_4.h5", "c100_4.h5", "c0_4.h5"]
thinking_depth = 40




token = "498243c4cc984c1d9f59cdbc42cfb501"