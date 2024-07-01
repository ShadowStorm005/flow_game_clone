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
                cursor.execute(f"SELECT * FROM {grid_size} WHERE Level_nr=?", 
                               (level_nr,))
            else:
                cursor.execute("SELECT * FROM ?", (grid_size,))
            

            return cursor.fetchall()
    
    def get_answer(self, grid_size, level_nr):
        with self as db:
            cursor = db.cursor()
            
            if not level_nr == "*":
                cursor.execute(f"SELECT * FROM {grid_size} WHERE Level_nr=?", 
                               (level_nr,))
            else:
                cursor.execute("SELECT * FROM ?", (grid_size,))
            

            return cursor.fetchall()

    def insert_level(self, grid_size, level_nr, color_cords):
        with self as db:
            cursor = db.cursor()

            if grid_size == "grid_5x5":
                cursor.execute(f"INSERT INTO {grid_size} VALUES (?, ?, ?, ?, ?, ?)", 
                               (level_nr, color_cords[0], color_cords[1], color_cords[2], color_cords[3], color_cords[4]))
            elif grid_size == "grid_6x6":
                cursor.execute(f"INSERT INTO {grid_size} VALUES (?, ?, ?, ?, ?, ?, ?)", 
                               (level_nr, *color_cords))
            elif grid_size == "grid_7x7":
                cursor.execute(f"INSERT INTO {grid_size} VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                               (level_nr, *color_cords))

            db.commit()
    
    def remove_level(self, grid_size, level_nr):
        with self as db:
            cursor = db.cursor()

            cursor.execute(f"DELETE FROM {grid_size} WHERE Level_nr=?", 
                           (level_nr,))
            db.commit()
    
    def update_level(self, grid_size, level_nr, color_cords):
        with self as db:
            cursor = db.cursor()

            if grid_size == "grid_5x5":
                cursor.execute(f"""UPDATE {grid_size} SET Green=?, Red=?, Blue=?, Yellow=?, Purple=? 
                               WHERE Level_nr=?""", 
                               (*color_cords, level_nr))
            elif grid_size == "grid_6x6":
                cursor.execute(f"""UPDATE {grid_size} SET Green=?, Red=?, Blue=?, Yellow=?, Purple=?, Orange=? 
                               WHERE Level_nr=?""", 
                               (*color_cords, level_nr))
            elif grid_size == "grid_7x7":
                cursor.execute(f"""UPDATE {grid_size} SET Green=?, Red=?, Blue=?, Yellow=?, Purple=?, Orange=?, Pink=? 
                               WHERE Level_nr=?""", 
                               (*color_cords, level_nr))
            db.commit()
    
    