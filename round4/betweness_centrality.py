import netowrkx as nx

G = nx.Graph()

G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('B', 'D')
G.add_edge('B', 'E')
G.add_edge('C', 'D')
G.add_edge('D', 'E')

print(nx.betweenness_centrality(G))