from generation.net_generation import generate_graph_base, make_strongly_connected
from generation.graph_draw import draw_graph

gr1 = generate_graph_base(9)
print(gr1)
print(make_strongly_connected(gr1))
draw_graph(gr1)
# gr2 = generate_graph_with_p(9, 0.5)
# print(gr2)
