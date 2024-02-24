import networkx as nx

G = nx.DiGraph()


def pageRank(G, d, iterations:int=5):
    values = []
    list_of_nodes = G.nodes
    for node in list_of_nodes:
        values[node] = 1/len(list_of_nodes)

    for i in range(iterations):
        for node in list_of_nodes:
            outgoing = node.out_degree
            for edge