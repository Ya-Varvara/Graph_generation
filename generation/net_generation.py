from random import random, randint, choice, shuffle
from generation.algorithms import random_sum, random_flow, FordFulkerson
from generation.graph_draw import draw_graph
from collections import deque
from generation.test import ex2

# TODO Рефакторинг всего кода
# TODO Сохранять планарные графы
# TODO Настроить БД для хранения графов
# TODO Настроить выборку из БД


def generate(nodes: int, min_weight=1, max_weight=60) -> None:
    # Высчитываем средний вес и 10% от диапазона для задания максимального потока
    k = (max_weight - min_weight)//10
    avg = (max_weight - min_weight)//2
    # Генерируем базу
    base = generate_graph_base(nodes)
    print(base)
    # Генерируем сильно связный граф
    while True:
        make_strongly_connected(base)
        if is_strongly_connected(base):
            break
    print(base)
    # Задаем разрез и определяем подмножества вершин и обратные ребра разреза, проверяем на то, чтобы списки ребер были не пустные
    while True:
        cutA, cutB, cut, r_cut = make_cut(base)
        if cut and r_cut:
            break
    print(base)
    print('Множество А = ', cutA, "\nМножество В = ", cutB, "\nРебра = ", cut, "\nОбратные ребра =", r_cut)
    # Задаем максимальный поток на графе
    net, max_flow = make_flow(base, cut, r_cut, avg-k, avg+k)
    print(net)
    print(max_flow)
    # Определяем пропускные способности
    make_throughput(net, cut, min_weight, max_weight)
    print(net)
    # Рисуем граф
    draw_graph(net)


def generate_graph_with_p(n: int, p: float) -> dict:
    """Генерирует рандомный орграф в виде словаря с некоторой вероятностью p

    :param n: количество вершин
    :param p: вероятность существования ребра между этими двумя вершинами
    :return: dict
    """
    graph = {i: [] for i in range(n)}
    while True:
        # print(is_weakly_connected(graph))
        # print(graph)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if round(random(), 3) <= p:
                    graph[i].append(j)
        if is_weakly_connected(graph):
            break
        else:
            graph = {i: [] for i in range(n)}
    return graph


def generate_graph_base(n: int) -> dict:
    """Генерирует слабо связную базу графа

    :param n: количество вершин
    :return: dict
    """
    graph = {i: [] for i in range(n)}
    while True:
        w = (n + 1) // 2 if n < 11 else n // 3
        window = [i for i in range(1, w + 1)]
        first = 1
        last = w
        for x in graph:
            if x == n - 1:
                break
            k = randint(1, 2)
            wx = window.copy()
            shuffle(wx)
            while k:
                if not wx:
                    break
                a = wx.pop(0)
                if a != x and (a not in graph[x]) and (x not in graph[a]):
                    graph[x].append(a)
                    k -= 1
            if x == first + (last - first + 1) // 3 and last < n - 1:
                window.remove(first)
                first += 1
                last += 1
                window.append(last)
        if is_weakly_connected(graph):
            break
        else:
            print("!")
            graph = {i: [] for i in range(n)}
    return graph


def is_strongly_connected(graph: dict) -> bool:
    """Проверка на сильную связность графа

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
    """Проверка на связность графа

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


def count_edges(graph: dict) -> tuple:
    """Считает у каждого узла кол-во входящих и исходящих ребер

    :param graph: Граф
    :return: 2 Массива - один с кол-вом входящих ребер, второй - с кол-вом исходящих ребер
    """
    res_in = [0] * len(graph)
    res_out = [0] * len(graph)
    for key, value in graph.items():
        res_out[key] = len(value)
        for node in value:
            res_in[node] += 1
    return res_in, res_out


def make_strongly_connected(graph: dict) -> None:
    """На выходе получаем сильно связный граф

    :param graph: Граф слабой связности
    :return: Ничего не возвращается, граф изменяется
    """

    def update_edges(source_node: int, destination_node: int) -> None:
        graph[source_node].append(destination_node)
        edges_out[source_node] += 1
        edges_in[destination_node] += 1

    edges_in, edges_out = count_edges(graph)
    n = len(graph) - 1
    w = (n + 1) // 2
    zero_in = [i for i in edges_in if not edges_in[i] and i]
    zero_out = [i for i in edges_out if not edges_out[i] and i < w - 1]
    if edges_out[0] < randint(2, 4):
        flag = False
        for node in zero_in:
            if node <= w and node not in graph[0]:
                update_edges(0, node)
                flag = True
                if edges_in[node] > 1:
                    zero_in.remove(node)
            if flag:
                break
        for x in range(1, w + 1):
            if flag:
                break
            if edges_in[x] < 3 and x not in graph[0]:
                update_edges(0, x)
                flag = True
    if edges_in[n] < randint(2, 4):
        flag = False
        for node in zero_out:
            if node >= w and node not in graph[n]:
                update_edges(node, n)
                flag = True
                if edges_out[node] > 1:
                    zero_out.remove(node)
            if flag:
                break
        for x in range(w, n):
            if flag:
                break
            if edges_out[x] < 3 and n not in graph[x]:
                update_edges(x, n)
                flag = True
    while zero_out:
        x = zero_out.pop(0)
        k = randint(2, 3)
        while k:
            for node in zero_in:
                if abs(node - x) <= w and x not in graph[node] and node not in graph[x]:
                    update_edges(x, node)
                    if edges_in[node] > 1:
                        zero_in.remove(node)
                    k -= 1
                if not k:
                    break
            for i in range(1, n):
                if not k:
                    break
                if x != i and abs(i - x) <= w and x not in graph[i] and i not in graph[x]:
                    update_edges(x, i)
                    k -= 1
            break
    while zero_in:
        x = zero_in.pop(0)
        k = randint(2, 3)
        while k:
            for i in range(1, n - 1):
                if not k:
                    break
                if x != i and abs(i - x) <= w and len(graph[i]) <= randint(2, 3) and x not in graph[i] and i not in \
                        graph[x]:
                    update_edges(i, x)
                    k -= 1
            break
    for x in graph:
        if edges_out[x] == 1:
            k = randint(1, 2) if x < n - 1 else 1
            if x + k not in graph[x]:
                graph[x].append(x + k)
    # return graph


def make_flow(base: dict, cut: list, reversed_cut: list, min_flow=20, max_flow=40) -> tuple:
    """Расставляет поток в графе

    :param max_flow: Верхняя граница максимального потока
    :param min_flow: Нижняя граница максимального потока
    :param base: граф, в котором нужно провести поток
    :param cut: ребра, входящие в разрез
    :param reversed_cut: ребра, входящие в обратный разрез
    :return: граф с потоком, максимальный поток
    """

    def edge_balance(node) -> bool:
        out_flow = sum(graph[node].values())
        in_flow = 0
        for x in graph:
            if node in graph[x]:
                in_flow += graph[x][node]
        return True if in_flow == out_flow else False

    graph = {x: {y: 0 for y in base[x]} for x in base}
    done = []
    buf = deque()
    n = len(graph) - 1
    flow = randint(min_flow, max_flow)
    input_flow = [0] * len(graph)

    def update_flow(node, fl) -> bool:
        nodes = set(graph[node]) - set(done)
        if nodes:
            f = random_flow(len(nodes), fl)
            for x in nodes:
                k = f.pop()
                graph[node][x] += k
                input_flow[x] += k
        else:
            k = choice(list(graph[node].keys()))
            graph[node][k] += fl
            input_flow[k] += fl
            update_flow(k, fl)
        return True

    def add_flow(node):
        if node == n:
            return
        done.append(node)
        if node == 0:
            f = random_flow(len(graph[node]), flow)
        else:
            z = list(filter(lambda y: (node, y) in reversed_cut, list(graph[node].keys())))
            f = random_flow(len(graph[node]) - len(z), input_flow[node])
        for x in graph[node]:
            if (node, x) in reversed_cut:
                graph[node][x] = 0
                continue
            fl = f.pop()
            if x in done:
                if not update_flow(x, fl):
                    f[0] += fl
                    fl = 0
            elif x not in buf:
                buf.append(x)
            graph[node][x] = fl
            input_flow[x] += fl
        while buf:
            add_flow(buf.popleft())
        return

    add_flow(0)
    return graph, flow


def make_cut(graph: dict) -> tuple:
    """Делает разрез в графе

    :param graph: граф
    :return: Граф изменяется, если потребуется. Возвращаются вершины, входящие в А и В, прямые ребра, обратные ребра
    """
    source = 0
    sink = len(graph) - 1
    buf = []
    A = [source]
    if len(graph[source]) > 3:
        for x in graph[source]:
            if random() > 0.3:
                A.append(x)
                buf.extend(graph[x])
    else:
        for x in graph[source]:
            A.append(x)
            buf.extend(graph[x])
    while buf:
        x = buf.pop()
        if random() > 0.5 and x not in A and x <= sink // 2:
            A.append(x)
    cutA = set(A)
    cutB = set(graph.keys()) - cutA
    cut = []
    reverse_cut = []
    flag = False
    k = 0
    for node in cutA:
        for x in graph[node]:
            if x in cutB:
                cut.append((node, x))
    if not cut:
        flag = True
        k = randint(2, 4)
    for node in cutB:
        for x in graph[node]:
            if x in cutA:
                if flag:
                    k -= 1
                    cut.append((x, node))
                    graph[x].append(node)
                    graph[node].remove(x)
                    if not k:
                        flag = False
                else:
                    reverse_cut.append((node, x))
                if not set(graph[node]) - cutA:
                    nodes = list(cutB)
                    nodes.remove(node)
                    graph[node].append(nodes[0])
    if not reverse_cut:
        k = randint(1, 2)
        A = sorted(list(cutA))
        B = sorted(list(cutB))
        while k:
            graph[B[0]].append(A[len(A) - 1])
            reverse_cut.append((B.pop(0), A.pop()))
            k -= 1
    return cutA, cutB, cut, reverse_cut


def make_throughput(graph: dict, cut_edges: list, min_weight=1, max_weight=60) -> None:
    """Функция расставляет пропускные способности ребер

    :param graph: граф
    :param cut_edges: ребра, входящие в разрез
    :param min_weight: минимальный вес ребра
    :param max_weight: максимальный вес ребра
    :return: Граф изменяется, ничего не возвращается
    """
    for x in graph:
        for y in graph[x]:
            if (x, y) in cut_edges:
                continue
            f = graph[x][y]
            add = 0
            if min_weight <= f < max_weight:
                add = randint(1, max_weight-f+1)
            elif f < min_weight:
                add = randint(min_weight-f+1, max_weight-f+1)
            graph[x][y] += add
    return


# def add_weights(graph: dict, wmin=5, wmax=70) -> dict:
#     """
#
#     :param wmax:
#     :param wmin:
#     :param graph:
#     :return:
#     """
#     new_graph = {x: {y: 0 for y in graph[x]} for x in graph}
#     cutA, cutB, cut, r_cut = make_cut(graph)
#     print('Множество А = ', cutA, "\nМножество В = ", cutB, "\nРебра = ", cut, "\nОбратные ребра =", r_cut)
#     window = round((wmax - wmin + 1) * 0.10)
#     avg = (wmax - wmin) // 2
#     max_flow = 0
#     input_flow = [0] * len(new_graph)
#
#     def add_next(x):
#         if x == len(new_graph) - 1:
#             return
#         w = random_sum(len(new_graph[x]), input_flow[x])
#         buf = []
#         for y in new_graph[x]:
#             if not new_graph[x][y]:
#                 f = w.pop()
#                 new_graph[x][y] = f
#                 input_flow[y] += f
#                 buf.append(y)
#         for y in buf:
#             add_next(y)
#         return
#
#     for x, y in cut:
#         flow = randint(avg - 3 * window, avg)
#         new_graph[x][y] = flow
#         input_flow[y] += flow
#         max_flow += flow
#         add_next(y)
#     for x, y in r_cut:
#         flow = randint(avg - 3 * window, avg)
#         new_graph[x][y] = flow
#     for node in cutA:
#         for x in new_graph[node]:
#             if not new_graph[node][x]:
#                 flow = randint(avg, avg + 2 * window)
#                 new_graph[node][x] = flow
#     print("Граф с весами\n", new_graph)
#     print(max_flow)
#     return new_graph
# ex3 = {0: [4, 1, 3], 1: [2, 4, 3], 2: [4], 3: [2, 4], 4: [5, 6, 3], 5: [6, 3], 6: [8, 11], 7: [9], 8: [7, 10], 9: [8, 10], 10: [11, 9], 11: []}
# print(ex3)
# cutA, cutB, cut, r_cut = make_cut(ex3)
# print(ex3)
# print(cutA, cutB, cut, r_cut)
