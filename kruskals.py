import networkx as nx
from queue import PriorityQueue

def kruskals(graph):
    prioritised_weights = PriorityQueue()
    list_of_edges = nx.get_edge_attributes(graph,'weight')
    for edge in list_of_edges:
        weight = list_of_edges[edge]
        prioritised_weights.put((weight, edge))

    sp_tree = nx.Graph()

    while True:
        priority, to_add = prioritised_weights.get()
        init = to_add[0]
        end = to_add[1]
        nodes = list(sp_tree.nodes)
        init_new, end_new = False, False

        if init not in nodes:
            sp_tree.add_node(init)
            init_new = True

        if end not in nodes:
            sp_tree.add_node(end)
            end_new = True

        sp_tree.add_edge(init, end, weight=priority)
        try:
            nx.find_cycle(sp_tree)
            sp_tree.remove_edge(init, end)
            if init_new:
                sp_tree.remove_node(init)
            if end_new:
                sp_tree.remove_node(end)

        except nx.exception.NetworkXNoCycle:
            continue

        if set(graph.nodes) == set(sp_tree.nodes):
            break

    return sp_tree
