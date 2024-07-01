import sqlite3

conn = sqlite3.connect('./levels.db')

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS grid_5x5
            (Level_nr INTEGER,
            Green LIST,
            Red LIST,
            Blue LIST,
            Yellow LIST,
            Purple LIST)
''')
cur.execute('''CREATE TABLE IF NOT EXISTS grid_6x6
            (Level_nr INTEGER,
            Green LIST,
            Red LIST,
            Blue LIST,
            Yellow LIST,
            Purple LIST,
            Orange LIST)
''')
cur.execute('''CREATE TABLE IF NOT EXISTS grid_7x7
            (Level_nr INTEGER,
            Green LIST,
            Red LIST,
            Blue LIST,
            Yellow LIST,
            Purple LIST,
            Orange LIST,
            Pink LIST)
''')

cur.close()
conn.close()
