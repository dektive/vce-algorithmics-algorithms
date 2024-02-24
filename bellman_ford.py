import networkx as nx

def bellman_ford(graph, starting_node):
    if not graph.is_directed():
        graph = graph.to_directed()
    distances = {node: float('infinity') for node in graph.nodes}
    distances[starting_node] = 0
    all_nodes = list(graph.nodes)
    paths = {starting_node: starting_node}

    for iter_n in range(len(all_nodes)-1):
        for init, end in graph.edges:
            weight = graph[init][end]['weight']
            if (distances[init] + weight) < distances[end]:
                distances[end] = (distances[init] + weight)

                paths[end] = paths[init] + end

    for init, end in graph.edges:
        if distances[end] > distances[init] + graph[init][end]['weight']:
            print("Contains negative cycle!")

    return distances, paths
