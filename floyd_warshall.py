def floyd_warshall(graph):
    array = {}
    nodes = list(graph.nodes)
    for node in nodes:
        sub_array = {}
        for _node in nodes:
            sub_array[_node] = float('infinity')
        array[node] = sub_array

    for i in nodes:
        array[i][i] = 0

    for edge in graph.edges:
        init = edge[0]
        end = edge[1]
        weight = graph[init][end]['weight']
        array[init][end] = weight

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if array[i][j] > array[i][k] + array[k][j]:
                    array[i][j] = array[i][k] + array[k][j]

    return array
