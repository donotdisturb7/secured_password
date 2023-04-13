import sqlite3

conn = sqlite3.connect('passwords.db')
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS passwords
             (password_id INTEGER PRIMARY KEY,
              username TEXT,
              website TEXT,
              password TEXT,
              created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')


conn.commit()

