import numpy as np

# 入力の高速化
import sys
input = sys.stdin.readline

# 入力
N = int(input())
scores = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]

# NumPy 配列への変換
scores_np = np.array(scores)

# keisan() 関数の削減と NumPy の使用
answer = []
for i in range(Q):
    L, R = queries[i]
    total1 = np.sum(scores_np[L-1:R, 1][scores_np[L-1:R, 0] == 1])
    total2 = np.sum(scores_np[L-1:R, 1][scores_np[L-1:R, 0] == 2])
    answer.append([str(total1), str(total2)])

# 出力
for row in answer:
    print(" ".join(row))
