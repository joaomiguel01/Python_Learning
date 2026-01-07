import sqlite3

def get_connection(db_path="flights.db"):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn
