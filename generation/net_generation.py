from random import random, randint, choice


def generate_graph_with_p(n: int, p: float) -> dict:
    """
    Генерирует рандомный орграф в виде словаря с некоторой вероятностью p

    :param n: количество вершин
    :param p: вероятность существования ребра между этими двумя вершинами
    :return: dict
    """
    graph = {i: [] for i in range(n)}
    while True:
        # print(is_weakly_connected(graph))
        # print(graph)
        for i in range(n-1):
            for j in range(i+1, n):
                if round(random(), 3) <= p:
                    graph[i].append(j)
        if is_weakly_connected(graph):
            break
        else:
            graph = {i: [] for i in range(n)}
    return graph


def generate_graph_base(n: int) -> dict:
    """
    Генерирует рандомный орграф с определенными условиями в виде словаря
    :param n: количество вершин
    :return: dict
    """
    graph = {i: [] for i in range(n)}
    while True:
        # print(is_weakly_connected(graph))
        w = 2*n//3 if n < 10 else n//2
        window = [i for i in range(1, w)]
        first = 1
        last = w
        for x in graph:
            if x == n-1:
                break
            k = randint(1, 2)
            while k:
                a = choice(window)
                if a != x and (a not in graph[x]) and (x not in graph[a]):
                    graph[x].append(a)
                    k -= 1
            if x == first+(last-first+1)//3 and last < n-1:
                window.remove(first)
                first += 1
                last += 1
                window.append(last)
        if is_weakly_connected(graph):
            break
        else:
            graph = {i: [] for i in range(n)}
    # print(graph)
    return graph


def is_strongly_connected(graph: dict) -> bool:
    """
    Проверка на сильную связность графа
    :param graph: граф в виде словаря
    :return: bool
    """
    buf = []
    done = set()
    buf.extend(graph[0])
    done.add(0)
    while buf:
        node = buf.pop(0)
        if node not in done:
            done.add(node)
            buf.extend(graph[node])
    if len(done) == len(graph):
        return True
    return False


def is_weakly_connected(graph: dict) -> bool:
    """
    Проверка на связность графа
    :param graph: граф в виде словаря
    :return: bool
    """
    done = set()
    buf = []
    for key, value in graph.items():
        if key in done or done & set(value) or not done:
            done.add(key)
            done |= set(value)
        else:
            s = set(value)
            s.add(key)
            buf.append(s)
    while buf:
        k = buf.pop()
        if done & set(k):
            done |= k
    return True if len(done) == len(graph) else False


def count_edges(graph: dict) -> dict:
    """
    Считает у каждого узла кол-во входящих и исходящих ребер
    :param graph: Граф
    :return: Список вида: {номер ребра: [кол-во входящих ребер, кол-во исходящих ребер]}
    """
    res = {i: [0, 0] for i in graph}
    for key, value in graph.items():
        res[key][1] = len(value)
        for x in value:
            res[x][0] += 1
    return res


def make_strongly_connected(graph: dict) -> dict:
    """
    На выходе получаем сильно связный граф
    :param graph: Граф слабой связности
    :return:
    """
    def update_edges(source_node: int, destination_node: int) -> None:
        graph[source_node].append(destination_node)
        edges[source_node][1] += 1
        edges[destination_node][0] += 1

    edges = count_edges(graph)
    n = len(graph) - 1
    w = (n+1)// 2
    zero_in = [i for i in edges if not edges[i][0] and i]
    zero_out = [i for i in edges if not edges[i][1] and i < w-1]
    count = 0
    if edges[0][1] < 2:
        k = randint(2, 4)
        x = 1
        while edges[0][1] < k:
            count += 1
            if zero_in and zero_in[0] <= w:
                update_edges(0, zero_in.pop(0))
            elif x <= w:
                if edges[x][0] == 1 and x not in graph[0]:
                    update_edges(0, x)
                x += 1
            elif edges[0][1] < 2:
                node = randint(1, w)
                if node not in graph[0]:
                    update_edges(0, node)
            if count > 20:
                break
    if edges[n][0] < 2:
        k = randint(2, 4)
        x = n-1
        while edges[n][0] < k:
            if zero_out and zero_out[-1] > w:
                update_edges(zero_out.pop(), n)
            elif x > w:
                if edges[x][1] == 1 and n not in graph[x]:
                    update_edges(x, n)
                x -= 1
            elif edges[n][0] < 2:
                node = randint(w, n-1)
                if n not in graph[node]:
                    update_edges(node, n)
            else:
                break
    while zero_out:
        x = zero_out.pop(0)
        k = randint(1, 2)
        while k:
            if zero_in:
                if abs(zero_in[0] - x) <= w and x not in graph[zero_in[0]] and zero_in[0] not in graph[x]:
                    update_edges(x, zero_in.pop(0))
                    k -= 1
            else:
                for i in range(1, n):
                    if not k:
                        break
                    if x != i and abs(i - x) <= w and x not in graph[i] and i not in graph[x]:
                        update_edges(x, i)
                        k -= 1
    while zero_in:
        x = zero_in.pop(0)
        k = randint(1, 2)
        while k:
            for i in range(1, n-1):
                if not k:
                    break
                if x != i and abs(i - x) <= w and len(graph[i]) < 3 and x not in graph[i] and i not in graph[x]:
                    update_edges(i, x)
                    k -= 1
    return graph

