import numpy as np
H,W,N = list(map(int,input().split()))

pos =np.array([1,1,0])
def white_direction_control(pos):
    if pos[2] == 0:
        pos[2] = 1
    elif pos[2] == 1:
        pos[2] = 2
    elif pos[2] == 2:
        pos[2] = 3
    else:
        pos[2] = 0

def black_direction_control(pos):
    if pos[2] == 0:
        pos[2] = 3
    elif pos[2] == 1:
        pos[2] = 0
    elif pos[2] == 2:
        pos[2] = 1
    else:
        pos[2] = 2

def proceed(pos):
    if pos[2] == 0:
        if pos[0] == 1:
            pos[0] = H
        else:
            pos[0] -= 1
    elif pos[2] == 1:
        if pos[1] == W:
            pos[1] = 1
        else:
            pos[1] += 1
    elif pos[2] == 2:
        if pos[0] == H:
            pos[0] = 1
        else:
            pos[0] += 1
    else:
        if pos[1] == 1:
            pos[1] = W
        else:
            pos[1] -= 1

grid = np.full((H, W), '.', dtype=str)

for i in range(N):
    if grid[pos[0]-1][pos[1]-1] == ".":
        grid[pos[0]-1][pos[1]-1] = "#"
        white_direction_control(pos)
        proceed(pos)
    else:
        grid[pos[0]-1][pos[1]-1] = "."
        black_direction_control(pos)
        proceed(pos)


for row in grid:
    print(''.join(row))