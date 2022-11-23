import matplotlib.pyplot as plt
import networkx as nx

def printnum(G):
    print('num of nodes:', G.number_of_nodes())
    print('num of edges:', G.number_of_edges())

def numstr(G):
    return ['nodes', G.number_of_nodes(), 'edges', G.number_of_edges()]

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

print('input graph:', *numstr(G))

while True:
    rv = None
    for v in G:
        if G.degree(v) < 2:
            rv = v
            break
    
    if rv is None:
        break

    G.remove_node(rv)

print('output graph:', *numstr(G))

# printnum(G)
# nx.draw_networkx(G)
# plt.show()