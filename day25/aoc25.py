import networkx as nx

f = open("input.txt").read().splitlines()

graph = nx.Graph()

for line in f:
    pattern, connections = line.split(":")
    pattern, connections = pattern.strip(), connections.strip()

    for connection in connections.split(" "):
        graph.add_edge(pattern, connection)

graph.remove_edges_from(nx.minimum_edge_cut(graph))

first, second = nx.connected_components(graph)

print(len(first) * len(second))