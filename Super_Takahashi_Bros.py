import networkx as nx
N = int(input())
L = []
for _ in range(N-1):
    L.append(list(map(int,input().split())))


# 空の有向グラフを作成
G = nx.DiGraph()

for i in range(1,N): #1からN−１まで
    G.add_node(i)
    G.add_weighted_edges_from([(i, i+1, L[i-1][0])])
    G.add_weighted_edges_from([(i, L[i-1][2], L[i-1][1])])

length = nx.dijkstra_path_length(G, 1, N)

print(length)


