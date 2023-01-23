import networkx as nx

G = nx.les_miserables_graph()

print(max(G.degree(n) for n in G))