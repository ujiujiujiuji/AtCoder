N = int(input())
A_list = list(map(int,input().split()))
ST_list = []
for _ in range(N-1):
    ST_list.append(list(map(int,input().split())))

def exchange(koukanmoto, A_list, ST_list, count):
    cost = ST_list[koukanmoto][0]
    get = ST_list[koukanmoto][1]
    A_list[koukanmoto] -= cost*count
    A_list[koukanmoto+1] += get*count

for i in range(N-1):
    count = A_list[i] // ST_list[i][0]
    exchange(i, A_list, ST_list, count)

print(A_list[N-1])

