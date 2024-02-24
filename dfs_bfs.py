from queue import Queue, PriorityQueue
import matplotlib.pyplot as plt
def DFS(graph, snode, vis=None):
    if vis is None:
        vis = []

    vis.append(snode)
    for node in list(graph[snode]):
        if node not in vis:
            DFS(graph=graph, snode=node, vis=vis)

    return vis


def BFS(graph, snode, vis=None, tvis=None):
    if vis is None:
        vis = []
    if tvis is None:
        tvis = Queue()

    if not snode in vis:
        vis.append(snode)
    available_nodes = [i for i in list(graph[snode]) if i not in vis]

    if not available_nodes:
        return
    else:
        for i in available_nodes:
            tvis.put(i)

    while not tvis.empty():
        next = tvis.get()
        BFS(graph=graph, snode=next, vis=vis, tvis=tvis)

    return vis


def djikstras(graph, start_node, target_node=None):
    dist = {float('infinity') for node in graph.nodes}
    dist[start_node] = 0

    Q = PriorityQueue()
    Q.put((0, start_node))

    while not Q.empty():
        weight, vertex = Q.get()

        for neighbour in graph[vertex]:
            distance_to_neighbour = graph[vertex][neighbour]['weight']

            if distance_to_neighbour + weight < dist[neighbour]:
                dist[neighbour] = distance_to_neighbour + weight

                Q.put((dist[neighbour], neighbour))

    return dist

def plot_graph(graph, spl=False):
    if spl:
        pos = nx.spring_layout(graph)
    else:
        pos = nx.get_node_attributes(graph, 'pos')
    edges = nx.get_edge_attributes(graph,'weight')

    nx.draw(graph, pos, with_labels=True)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edges)
    plt.show()

if __name__ == '__main__':
    import networkx as nx
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
    djikstras()