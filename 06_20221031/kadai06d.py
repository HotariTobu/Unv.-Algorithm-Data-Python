from operator import itemgetter

import matplotlib.pyplot as plt
import networkx as nx

def printnum(G):
    print('num of nodes:', G.number_of_nodes())
    print('num of edges:', G.number_of_edges())

n = int(input())
m = int(input())
lines = [input().split() for _ in range(m)]
E = [(int(token) for token in line) for line in lines]

E.sort(key=itemgetter(2))

T = nx.Graph()

for e in E:
    if not nx.has_path(T, e[0], e[1]):
        T.add_edge(e[0], e[1], weight=e[2])

weights = [e['weight'] for e in T.edges]
weight = sum(weights)
print(weight)

printnum(T)
nx.draw_networkx(T)
plt.show()