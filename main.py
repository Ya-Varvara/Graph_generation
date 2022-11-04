# from generation.net_generation import generate, check_graph_flow, generate_graph_base, make_strongly_connected, make_flow, make_cut, make_cut_2
# from db.db_handler import add_graph
# from generation.algorithms import FordFulkerson
# from generation.graph_draw import draw_graph
import sqlite3

db_file_name = 'graph.db'
db = sqlite3.connect(db_file_name)
c = db.cursor()
c.execute("""DROP TABLE graphs""")
c.execute("""DROP TABLE folders""")
db.commit()
c.close()

# n = 12
#
# graph = generate_graph_base(n)
# draw_graph(graph)
# make_strongly_connected(graph)
# draw_graph(graph)
