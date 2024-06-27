import sqlite3

class Database:
    def __init__(self, path="./levels.db", **kwargs):
        self.path = path
        self.schemas = {}
        for schema_name, schema in kwargs.items():
            self.schemas[schema_name] = schema
    
    def __enter__(self):
        self.conn = sqlite3.connect(self.path)
        return self.conn
    
    def __exit__(self, *args):
        self.conn.close()

    def get_level(self, grid_size, level_nr):
        with self as db:
            cursor = db.cursor()
            
            if not level_nr == "*":
                cursor.execute("SELECT * FROM ? WHERE Level_nr=?", (grid_size, level_nr))
            else:
                cursor.execute("SELECT * FROM ?", (grid_size,))
            

            return cursor.fetchall()