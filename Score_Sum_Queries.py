import numpy as np
N = int(input())
scores = []


for _ in range(N):
    scores.append(list(map(int,input().split())))

Q = int(input())

queries = []
for _ in range(Q):
    queries.append(list(map(int,input().split())))

answer = []


def keisan(L,R,scores):
    total1 = 0
    total2 = 0
    for i in range(L-1,R):
        if scores[i][0] == 1:
            total1 += scores[i][1]
        else:
            total2 += scores[i][1]
    return [str(total1), str(total2)]

for i in range(Q):
    L = queries[i][0]
    R = queries[i][1]
    answer.append((keisan(L,R,scores)))



for row in answer:
    print(" ".join(row))








