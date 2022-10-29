import sqlite3


def create_db(db_file_name: str) -> None:
    db = sqlite3.connect(db_file_name)
    c = db.cursor()
    # ========================================
    # CREATE TABLES
    c.execute("""
        CREATE TABLE IF NOT EXISTS folders (
            id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
            name text NOT NULL,
            description text)
        """)

    c.execute("""select count(*) from folders""")
    count = c.fetchall()
    if count[0][0] == 0:
        c.execute("""INSERT INTO folders VALUES (1, 'Все графы', 'Все графы')""")
        db.commit()
    c.execute("""
        CREATE TABLE IF NOT EXISTS graphs (
            id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
            name text,
            folder integer DEFAULT 1,
            data text NOT NULL,
            max_flow integer NOT NULL,
            cut text NOT NULL,
            seta text NOT NULL,
            setb text NOT NULL,
            FOREIGN KEY (folder) REFERENCES folders(id))
        """)
    db.commit()

    # print(c.fetchall())
    db.close()
    return

