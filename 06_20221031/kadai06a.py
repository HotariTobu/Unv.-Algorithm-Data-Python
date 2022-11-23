import matplotlib.pyplot as plt
import networkx as nx

def printnum(G):
    print('num of nodes:', G.number_of_nodes())
    print('num of edges:', G.number_of_edges())

G = nx.read_adjlist('facebook_adj.txt', nodetype=int)
print('ADJ')
printnum(G)

G = nx.read_edgelist('facebook_edge.txt', nodetype=int)
print('EDGE')
printnum(G)

# nx.draw_networkx(G)
# plt.show()