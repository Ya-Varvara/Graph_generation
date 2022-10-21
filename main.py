from generation.net_generation import generate_graph_base, make_strongly_connected, is_strongly_connected, make_cut, \
    generate
from generation.algorithms import FordFulkerson
from generation.graph_draw import draw_graph
from random import sample, shuffle, randint, choice

# gr1 = generate_graph_base(15)
# print("Сгенерированная база\n", gr1)
# gr2 = make_strongly_connected(gr1)
# print("Граф без весов\n", gr2)
# # gr2 = add_weights(gr2)
# # print(FordFulkerson(gr2))
# draw_graph(gr2)


# def g_base(n: int) -> dict:
#     graph = {i: [] for i in range(n)}
#     print(graph)
#     bonded = []
#     buf = []
#     w = n + 1 // 2 if n < 11 else n // 3
#
#     def make_window(node) -> list:
#         f = node - w // 2
#         l = node + w // 2
#         while f < 1:
#             f += 1
#         while l > n - 1:
#             l -= 1
#         res = [i for i in range(f, l+1)]
#         shuffle(res)
#         return res
#
#     def make_link(node):
#         if node == n - 1:
#             return
#         bonded.append(node)
#         window = make_window(node)
#         k = randint(1, 2)
#         while k:
#             x = window.pop()
#             if node != x and x not in graph[node] and node not in graph[x]:
#                 graph[node].append(x)
#                 if x not in buf:
#                     buf.append(x)
#                 k -= 1
#         while buf:
#             make_link(buf.pop(0))
#
#     make_link(0)
#     return graph


generate(25)
