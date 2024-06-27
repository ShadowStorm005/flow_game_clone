import sqlite3

conn = sqlite3.connect('levels.db')

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS 5x5
            (Level_nr INTEGER,
            Green TEXT,
            Red TEXT,
            Blue TEXT,
            Yellow TEXT,
            Purple TEXT)
''')
cur.execute('''CREATE TABLE IF NOT EXISTS 6x6
            (Level_nr INTEGER,
            Green TEXT,
            Red TEXT,
            Blue TEXT,
            Yellow TEXT,
            Purple TEXT,
            Orange TEXT)
''')
cur.execute('''CREATE TABLE IF NOT EXISTS 7x7
            (Level_nr INTEGER,
            Green TEXT,
            Red TEXT,
            Blue TEXT,
            Yellow TEXT,
            Purple TEXT,
            Orange TEXT,
            Pink TEXT)
''')

cur.close()
conn.close()
