import numpy as np

state = tuple([1,2,3,4])
#a tuple where the distrubution of the state is 0.1
target_distribution = tuple([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])

traning_data = np.array([state + target_distribution], dtype=np.float64)
print(traning_data)