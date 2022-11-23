import matplotlib.pyplot as plt
import networkx as nx

def printnum(G):
    print('num of nodes:', G.number_of_nodes())
    print('num of edges:', G.number_of_edges())

v1, v2 = [int(token) for token in input().split()]

E = [
    (1, 2),
    (1, 8),
    (1, 9),
    (2, 3),
    (2, 4),
    (4, 5),
    (6, 7),
    (6, 8),
    (6, 10),
    (8, 9),
    (8, 10),
]

G = nx.Graph()
G.add_edges_from(E)

spath = nx.shortest_path(G, source=v1, target=v2)
print('shortest path', spath)

allpath = nx.all_simple_paths(G, source=v1, target=v2)
print('paths are')
for path in allpath:
    print(path)

# printnum(G)
# nx.draw_networkx(G)
# plt.show()