import numpy as np
H, W = list(map(int,input().split()))
num_list = []
for _ in range(H):
    num_list.append(list(map(int,input().split())))

result = np.zeros((H, W))

def tasu(i, j, num_list, H, W):
    total = 0
    for a in range(W):
        total += num_list[i][a]
    for b in range(H):
        total += num_list[b][j]
    total -= num_list[i][j]
    return total

for i in range(H):
    for j in range(W):
        result[i][j] = tasu(i,j,num_list,H,W)

result = result.astype(int)
result = result.astype(str)

for row in result:
    print(" ".join(row))



