import networkx as nx

G = nx.Graph()

G.add_edge('a', 'b', weight=2)
G.add_edge('b', 'c', weight=4)
G.add_edge('a', 'c', weight=10)
G.add_edge('c', 'd', weight=6)
G.add_edge('b', 'd', weight=2)
G.add_edge('b', 'e', weight=5)
G.add_edge('e', 'f', weight=8)
G.add_edge('d', 'f', weight=8)

from itertools import islice
from networkx.classes.function import path_weight

def k_shortest_paths(G, source, target, k, weight=None):
    return list(islice(nx.shortest_simple_paths(G, source, target, weight='weight'), k))

for path in k_shortest_paths(G, 'a','f', 3):
    print(path, path_weight(G, path, weight="weight"))