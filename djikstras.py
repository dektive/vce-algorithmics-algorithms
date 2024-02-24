from queue import PriorityQueue
def djikstras_algorithm(graph, starting_node, end_node=None):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[starting_node] = 0

    priority_queue = PriorityQueue()
    priority_queue.put((0, starting_node))

    paths = {starting_node: starting_node}
    while priority_queue.qsize() > 0:
        current_distance, current_vertex = priority_queue.get()
        if current_distance > distances[current_vertex]:  # checks to see if its an 'improvement'
            continue

        for neighbor in graph[current_vertex]:
            weight = graph[current_vertex][neighbor]['weight']

            distance = current_distance + weight  # adding the weight of the neighbour to the current weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_vertex] + neighbor

                if (end_node is not None) and (end_node == neighbor):
                    return (distance, neighbor)

                priority_queue.put((distance, neighbor))

    return distances, paths


def diameter(graph):
    for i in graph.nodes:
        paths = djikstras_algorithm(graph, i)[1]
        print(max(paths.values(), key=len))
