import networkx as nx
import matplotlib.pyplot as plt
def test_digraph():
    G = nx.DiGraph()

    G.add_node("S", pos=(1, 1.4))
    G.add_node("E", pos=(1.3, 1.6))
    G.add_node("D", pos=(1.3, 1.2))
    G.add_node("C", pos=(1.5, 1.4))
    G.add_node("B", pos=(1.5, 1.2))
    G.add_node("A", pos=(1.2, 2))

    G.add_edge("S", "E", weight=8)
    G.add_edge("S", "A", weight=10)
    G.add_edge("A", "C", weight=2)
    G.add_edge("E", "D", weight=1)
    G.add_edge("D", "A", weight=4)
    G.add_edge("D", "C", weight=1)
    G.add_edge("C", "B", weight=2)
    G.add_edge("B", "A", weight=1)

    return G

def test_graph():
    G = nx.Graph()
    G.add_node("S", pos=(1, 1.4))
    G.add_node("E", pos=(1.3, 1.6))
    G.add_node("D", pos=(1.3, 1.2))
    G.add_node("C", pos=(1.5, 1.4))
    G.add_node("B", pos=(1.5, 1.2))
    G.add_node("A", pos=(1.2, 2))

    G.add_edge("S", "E", weight=8)
    G.add_edge("S", "A", weight=10)
    G.add_edge("A", "C", weight=2)
    G.add_edge("E", "D", weight=1)
    G.add_edge("D", "A", weight=4)
    G.add_edge("D", "C", weight=1)
    G.add_edge("C", "B", weight=2)
    G.add_edge("B", "A", weight=1)
    return G


def test_graph_negative():
    G = nx.DiGraph()
    G.add_node("S", pos=(1, 1.4))
    G.add_node("E", pos=(1.3, 1.6))
    G.add_node("D", pos=(1.3, 1.2))
    G.add_node("C", pos=(1.5, 1.4))
    G.add_node("B", pos=(1.5, 1.2))
    G.add_node("A", pos=(1.2, 2))

    G.add_edge("S", "E", weight=8)
    G.add_edge("S", "A", weight=10)
    G.add_edge("A", "C", weight=2)
    G.add_edge("E", "D", weight=1)
    G.add_edge("D", "A", weight=4)
    G.add_edge("D", "C", weight=-1)
    G.add_edge("C", "B", weight=-2)
    G.add_edge("B", "A", weight=1)
    return G

def complex_graph():
    G = nx.Graph()
    G.add_node("S", pos=(1, 1.4))
    G.add_node("E", pos=(1.3, 1.6))
    G.add_node("D", pos=(1.3, 1.2))
    G.add_node("C", pos=(1.5, 1.4))
    G.add_node("B", pos=(1.5, 1.2))
    G.add_node("A", pos=(1.2, 2))
    G.add_node("H", pos=(1.2, 1.1))

    G.add_edge("S", "E", weight=8)
    G.add_edge("S", "A", weight=10)
    G.add_edge("A", "C", weight=2)
    G.add_edge("E", "D", weight=1)
    G.add_edge("D", "A", weight=4)
    G.add_edge("D", "C", weight=1)
    G.add_edge("C", "B", weight=2)
    G.add_edge("B", "A", weight=1)
    G.add_edge("S", "C", weight=2)
    G.add_edge("H", "B", weight=2)
    G.add_edge("H", "D", weight=3)
    G.add_edge("B", "D", weight=3)
    return G

def test_graph2():
    G = nx.Graph()

    G.add_node("A", pos=(1.6, 1))
    G.add_node("B", pos=(1.4, 1.2))
    G.add_node("C", pos=(1.8, 1.2))
    G.add_node("D", pos=(1.2, 1.4))
    G.add_node("E", pos=(1.3, 1.4))
    G.add_node("F", pos=(1.4, 1.4))
    G.add_node("G", pos=(1.5, 1.4))

    G.add_edge("A", "B", weight=0.5)
    G.add_edge("A", "C", weight=9.8)
    G.add_edge("B", "D", weight=2.4)
    G.add_edge("B", "E", weight=3.5)
    G.add_edge("C", "F", weight=8.1)
    G.add_edge("C", "G", weight=4.5)

    return G

def test_graph_for_warshalls():
    G = nx.DiGraph()

    G.add_node("A", pos=(1.6, 1))
    G.add_node("B", pos=(1.4, 1.2))
    G.add_node("C", pos=(1.8, 1.2))
    G.add_node("D", pos=(1.2, 1.4))

    G.add_edge("A", "B", weight=1.0)
    G.add_edge("D", "A", weight=1.0)
    G.add_edge("D", "C", weight=1.0)
    G.add_edge("B", "D", weight=1.0)


    return G


def plot_graph(graph, spl=False):
    if spl:
        pos = nx.spring_layout(graph)
    else:
        pos = nx.get_node_attributes(graph, 'pos')
    edges = nx.get_edge_attributes(graph,'weight')

    nx.draw(graph, pos, with_labels=True)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edges)
    plt.show()