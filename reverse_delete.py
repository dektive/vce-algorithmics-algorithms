import networkx as nx
from queue import PriorityQueue

def reverse_delete(graph):
    sp_tree = graph.copy()
    prioritised_weights = PriorityQueue()
    list_of_edges = nx.get_edge_attributes(sp_tree,'weight')
    for edge in list_of_edges:
        weight = list_of_edges[edge]
        prioritised_weights.put((-weight, edge))

    while True:
        priority, tuple_edge = prioritised_weights.get()
        st_node, end_node = tuple_edge

        sp_tree.remove_edge(st_node, end_node)
        if not nx.is_connected(sp_tree):
            sp_tree.add_edge(st_node, end_node, weight=-priority)

        if prioritised_weights.empty():
            break

    return sp_tree
