import sqlite3


def initialize_db():
    conn = sqlite3.connect('bot_database.dp')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXIST users (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             user_id INTEGER NOT NULL, 
             username TEXT,
             first_name TEXT,
             last_name TEXT
             )
             
       ''')
    conn.commit()
    conn.close()

