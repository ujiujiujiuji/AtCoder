N = int(input())
data = [[0,0,0]]
for i in range(N):
    data.append(list(map(int,input().split())))
flag = True

for i in range(N):
    delta_t = data[i+1][0] - data[i][0]
    distance = abs(data[i][1] - data[i+1][1]) + abs(data[i][2] - data[i+1][2])
    if not (distance <= delta_t and (delta_t - distance) % 2 == 0):
        flag = False

if flag:
    print("Yes")
else:
    print("No")



