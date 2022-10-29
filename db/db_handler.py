import sqlite3
from db.db_creator import create_db
import json

file_name = 'graph.db'
create_db(file_name)


def to_json(data) -> str:
    if isinstance(data, dict):
        return json.dumps(data)
    elif isinstance(data, list):
        return json.dumps(str(data))


def add_graph(info: tuple) -> bool:
    gr_name, f, graph, flow, edges, a, b = info
    graph = to_json(graph)
    edges = to_json(edges)
    a = to_json(a)
    b = to_json(b)
    database = sqlite3.connect(file_name)
    c = database.cursor()
    if f:
        string = F"""SELECT id FROM folders WHERE {f} == name"""
        c.execute(string)
        value = c.fetchall()
        if value[0][0]:
            string = F"""INSERT INTO graphs(name, folder, data, max_flow, cut, seta, setb) 
                        VALUES ({gr_name}, {value[0][0]}, {graph}, {flow}, {edges}, {a}, {b})"""
            c.execute(string)
        else:
            return False
    else:
        string = """INSERT INTO graphs (name, data, max_flow, cut, seta, setb) 
                    VALUES ('{}', '{}', {}, '{}', '{}', '{}')""".format(gr_name, graph, flow, edges, a, b)
        c.execute(string)
    database.commit()
    database.close()
    return True


def add_folder(info: tuple) -> bool:
    name, desc = info
    database = sqlite3.connect(file_name)
    c = database.cursor()
    c.execute(f"""INSERT INTO folders(name, description) 
                    VALUES ({name}, {desc})""")
    database.commit()
    database.close()
    return True
