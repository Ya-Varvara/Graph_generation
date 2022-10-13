def dict_to_list(gr: dict) -> list:
    """
    Преобразует граф типа словарь в тип двумерный массив

    :param d: граф типа словарь
    :return: двумерный массив
    """
    new = []
    for x in gr:
        new.append([0]*len(gr))
        for y in gr[x]:
            new[x][y] = gr[x][y]
    return new


def FordFulkerson(gr: dict) -> tuple:
    """
    Алгоритм находит максимальный поток и минимальный разрез

    :param gr:
    :return: Максимальный поток, список вершин, входящих в левую часть, список вершин, входящих в правую часть
    """
    graph = dict_to_list(gr) if isinstance(gr, dict) else gr
    source = 0
    sink = len(graph) - 1
    # print(graph)

    def BFS(graph, s, t):
        # Return True if there is node that has not iterated.
        visited = [False] * len(graph)
        queue = [s]
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind in range(len(graph[u])):
                if visited[ind] is False and graph[u][ind] > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return True if visited[t] else False

    parent = [-1] * (len(graph))
    max_flow = 0
    while BFS(graph, source, sink):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
        parent = [-1] * (len(graph))
    parent[0] = 0
    A = [i for i in range(len(parent)) if parent[i] != -1]
    B = [i for i in range(len(parent)) if parent[i] == -1]
    return max_flow, A, B

# C = [[0, 25, 47, 14, 21, 0, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 13],
#      [0, 0, 0, 0, 0, 48, 7, 23, 0, 0, 0, 0],
#      [0, 0, 27, 0, 0, 0, 0, 20, 0, 0, 0, 0],
#      [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 43, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0],
#      [0, 0, 0, 0, 0, 16, 0, 5, 31, 0, 0, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 52, 0],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 0, 38],
#      [0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 60],
#      [0, 0, 0, 0, 0, 0, 23, 0, 0, 35, 0, 39],
#      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# flow, cutA, cutB = FordFulkerson(C)
# print(flow, cutA, cutB)
