import numpy as np


board = [[0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
size = 5

def print_diamond2() -> None:
    a = np.array(board)
    b = [np.diag(a[-1:-a.shape[0]-1:-1,:], i).tolist() for i in range(-a.shape[0]+1,a.shape[0])]
    for i in range(len(b)):
        s = ""
        for j in range(len(b[i])):
            if b[i][j] == 1:
                s += "R"
            elif b[i][j] == -1:
                s += "B"
            else:
                s += "O"
            if j != len(b[i])-1:
                s += " - "
        print(s.center(50), sep=" ")
        if i <size-1:
            print((("/ " + "\\ ")*len(b[i])).center(50), sep=" ")
        else:
            print((("\\ " + "/ ")*(len(b[i])-1)).center(50), sep=" ")
        

print_diamond2( )