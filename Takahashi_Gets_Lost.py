H, W, N = list(map(int, input().split()))
T = input()
rand_or_sea = []
for _ in range(H):
    rand_or_sea.append(input())

def judge(i, j, direction, rand_or_sea):
    if direction == "L":
        if rand_or_sea[i][j-1] == ".":

            return True
        else:
            return False
    if direction == "R":
        if rand_or_sea[i][j+1] == ".":

            return True
        else:
            return False
    if direction == "U":
        if rand_or_sea[i-1][j] == ".":

            return True
        else:
            return False
    if direction == "D":
        if rand_or_sea[i+1][j] == ".":

            return True
        else:
            return False
        
def move(i,j,direction):
    if direction == "L":
        return i, j-1
    if direction == "R":
        return i, j+1
    if direction == "U":
        return i-1, j
    if direction == "D":
        return i+1, j

        

count = 0
for i in range(1,H-1):
    for j in range(1,W-1):
        ii = i
        jj = j
        whether_N = 0
        if rand_or_sea[ii][jj] == ".":
                for k in range(N):
                    direction = T[k]
                    if judge(ii, jj, direction, rand_or_sea):
                        ii, jj = move(ii, jj, direction)
                        whether_N += 1
                    else:
                        break
                if whether_N == N:
                    count += 1




print(count)