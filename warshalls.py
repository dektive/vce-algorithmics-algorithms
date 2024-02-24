import networkx as nx
from graph_algorithms_reg.test_graphs import complex_graph, test_graph_for_warshalls
import numpy as np

def graph2adjacencymatrix(graph):
    return nx.to_numpy_array(graph).tolist()

def graph2binaryadjacencymatrix(graph):
    adm = graph2adjacencymatrix(graph)
    for row_no, row in enumerate(adm):
        for elem_no, elem in enumerate(row):
            if elem != 0.0:
                adm[row_no][elem_no] = 1.0

    return adm

def warshalls(adjacency_matrix):
    n = len(adjacency_matrix) # number of nodes

    for k in range(n):
        for i in range(n):
            for j in range(n):
                print("k: ", k, " i: ", i, " j: ", j)
                adjacency_matrix[i][j] = adjacency_matrix[i][j] or (adjacency_matrix[i][k] and adjacency_matrix[k][j])
                # checks if its either already a one, or if all of those around it are ones
    return adjacency_matrix

o = graph2binaryadjacencymatrix(test_graph_for_warshalls())
n = warshalls(graph2binaryadjacencymatrix(test_graph_for_warshalls()))
from pprint import pprint
pprint(o)
pprint(n)