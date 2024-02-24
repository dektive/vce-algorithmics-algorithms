import networkx as nx


def prims(graph):
    nodes = list(graph.nodes)
    starting_node = nodes[0]

    visited = [starting_node]
    sp_tree = nx.Graph()
    sp_tree.add_node(starting_node)

    while set(visited) != set(nodes):
        all_edges_in_visited = []
        for i in visited:
            for z in list(graph.edges(i)):
                all_edges_in_visited.append(z)

        available_edges = {edge: graph[edge[0]][edge[1]]['weight'] for edge in all_edges_in_visited}
        filtered_edges = available_edges.copy()
        for i in available_edges:
            if i[1] in visited:
                filtered_edges.pop(i)

        minimum_edge = min(filtered_edges, key=filtered_edges.get)
        init_node = minimum_edge[0]
        end_node = minimum_edge[1]

        if end_node not in visited:
            sp_tree.add_node(end_node)
            sp_tree.add_edge(init_node, end_node, weight=available_edges[minimum_edge])

            visited.append(end_node)
    return sp_tree
