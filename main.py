from generation.net_generation import generate
from db.db_handlers import DataBase
from db.db_config import db_file_name

db = DataBase(db_file_name)
n = 12
with db:
    db.add_graph("test_1", 1, generate(n))