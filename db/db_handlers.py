import sqlite3
import json
from db.db_config import db_file_name


class DataBase:
    db_name = None
    db_connection = None
    cursor = None

    def __init__(self):
        print('__ Initialization __')
        try:
            self.db_name = db_file_name
            self.db_connection = sqlite3.connect(self.db_name)
            print('[INFO]  DB is successfully connected')
            self.cursor = self.db_connection.cursor()

            exist_query = """SELECT name FROM sqlite_master WHERE type='table' and name='folders' or name='graphs'"""
            self.cursor.execute(exist_query)
            result = self.cursor.fetchall()
            print(result)
            if not result:
                self.create_basic_tables()

            self.cursor.close()
            print('[INFO]  Cursor is closed')
        except sqlite3.Error as error:
            print('[ERROR] Connection error ', error)
        finally:
            if self.db_connection:
                self.db_connection.close()
                print('[INFO]  Connection is closed')

    def __enter__(self):
        try:
            self.db_connection = sqlite3.connect(self.db_name)
            print('[INFO]  DB is connected')
            self.cursor = self.db_connection.cursor()
            print('[INFO]  Cursor is open')
        except sqlite3.Error as error:
            print('[ERROR] Connection error ', error)

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.db_connection.commit()
            print('[INFO]  Commit')
            self.cursor.close()
            print('[INFO]  Cursor is close')
        except sqlite3.Error as error:
            print('[ERROR] Connection error ', error)
        finally:
            if self.db_connection:
                self.db_connection.close()
                print('[INFO]  Connection is closed')

    def create_basic_tables(self):
        try:
            create_folders_table_query = """
                                CREATE TABLE IF NOT EXISTS folders(
                                id integer PRIMARY KEY AUTOINCREMENT,
                                name text NOT NULL)"""
            self.cursor.execute(create_folders_table_query)
            print('[INFO]  Table Folders is successfully created')

            add_folder_query = """INSERT INTO folders (id, name) VALUES (1, 'All')"""
            self.cursor.execute(add_folder_query)

            create_graphs_table_query = """
                                CREATE TABLE IF NOT EXISTS graphs(
                                id integer PRIMARY KEY AUTOINCREMENT,
                                name text NOT NULL,
                                folder_id integer NOT NULL DEFAULT 1,
                                graph text NOT NULL,
                                nodes_number integer NOT NULL,
                                max_flow integer NOT NULL, 
                                set_a text NOT NULL,
                                set_b text NOT NULL,
                                cut text NOT NULL,
                                rev_cut text NOT NULL,
                                FOREIGN KEY (folder_id) REFERENCES folders (id))"""
            self.cursor.execute(create_graphs_table_query)
            print('[INFO]  Table Graphs is successfully created')

            self.db_connection.commit()
            print('[INFO]  Commit')
        except sqlite3.Error as error:
            print('[ERROR] Connection error ', error)

    def get_graphs(self, folder_id):
        try:
            get_data_query = F"""SELECT id, name, nodes_number, max_flow  FROM graphs WHERE folder_id={folder_id}"""
            self.cursor.execute(get_data_query)
            res = self.cursor.fetchall()
            return db_value_to_data(res)
        except sqlite3.Error as error:
            print('[ERROR] Select error ', error)

    def get_graph(self, graph_id=None):
        try:
            get_data_query = F"""SELECT * FROM graphs WHERE id={graph_id}"""
            self.cursor.execute(get_data_query)
            res = self.cursor.fetchall()
            return db_value_to_data(res)[0]
        except sqlite3.Error as error:
            print('[ERROR] Select error ', error)

    def get_graph_net(self, folder_id):
        try:
            get_data_query = F"""SELECT graph FROM graphs WHERE folder_id={folder_id}"""
            self.cursor.execute(get_data_query)
            res = self.cursor.fetchall()
            # print(res)
            return db_value_to_data(res)
        except sqlite3.Error as error:
            print('[ERROR] Get error ', error)

    def get_folders(self):
        try:
            get_data_query = """SELECT * FROM folders"""
            self.cursor.execute(get_data_query)
            res = self.cursor.fetchall()
            return db_value_to_data(res)
        except sqlite3.Error as error:
            print('[ERROR] Select error ', error)

    def add_graph(self, name, folder=1, *args):
        all_data = [name, folder]
        for arg in args:
            all_data.append(arg)
        values = graph_data_to_db_value(all_data)
        try:
            add_graph_query = f"""INSERT INTO graphs (name, folder_id, graph, nodes_number, set_a, set_b, cut, rev_cut, max_flow)
                                    VALUES {values}"""
            self.cursor.execute(add_graph_query)
            print('[INFO] Graph was added')
        except sqlite3.Error as error:
            print('[ERROR] Add error ', error)

    def add_folder(self, data):
        values = data_to_db_value(data)
        try:
            self.cursor.execute('INSERT INTO folders (name) VALUES(?)', values)
        except sqlite3.Error as error:
            print('[ERROR] Insert error ', error)

    def delete_graph(self, graph_id):
        try:
            delete_graph_query = f"""DELETE FROM graphs WHERE id={graph_id}"""
            self.cursor.execute(delete_graph_query)
            print('[INFO] Graph was deleted')
        except sqlite3.Error as error:
            print('[ERROR] Delete error ', error)

    def delete_folder(self, folder_id):
        try:
            delete_folder_query = f"""DELETE FROM folders WHERE id={folder_id}"""
            delete_graphs_query = f"""DELETE FROM graphs WHERE folder_id={folder_id}"""
            self.cursor.execute(delete_folder_query)
            print('[INFO] Folder was deleted')
            self.cursor.execute(delete_graphs_query)
            print('[INFO] Graphs were deleted')
        except sqlite3.Error as error:
            print('[ERROR] Delete error ', error)

# End of class


def data_to_json(data):
    return json.dumps(data) if isinstance(data, (dict, list)) else data


def json_to_data(data):
    if isinstance(data, str):
        try:
            return json.loads(data)
        except json.decoder.JSONDecodeError:
            return data
    return data


def data_to_db_value(params):
    query = [data_to_json(item) for item in params.split(' ')]
    print(query)
    return tuple(query)


def graph_data_to_db_value(params):
    query = [data_to_json(item) for item in params]
    print(query)
    return tuple(query)


def db_value_to_data(db_value):
    result = [[json_to_data(item) for item in row] for row in db_value]
    return result
