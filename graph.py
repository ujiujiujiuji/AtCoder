import networkx as nx
import matplotlib.pyplot as plt
N = int(input())
L = []
for _ in range(N-1):
    L.append(list(map(int,input().split())))


# 空の有向グラフを作成
G = nx.DiGraph()

for i in range(1,N): #1からN−１まで
    G.add_node(i)
    G.add_edge(i, i+1, weight = L[i-1][0])
    G.add_edge(i, L[i-1][2], weight = L[i-1][1])




# ノードやエッジの情報を出力
print("Nodes:", G.nodes())
print("Edges:", G.edges(data=True))

nx.draw(G, with_labels=True)
plt.show()
