import sqlite3


# Connect to the database
conn = sqlite3.connect('passwords.db')
c = conn.cursor()

# Create the table if it doesn't already exist
c.execute('''CREATE TABLE IF NOT EXISTS passwords
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT,
              website TEXT,
              password TEXT,
              created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

# Insert a new password into the database
# username = ""
# website = "example.com"
# password = ""
# c.execute("INSERT INTO passwords (username, website, password) VALUES (?, ?, ?)", (username, website, password))
conn.commit()

# Retrieve a password from the database
# c.execute("SELECT password FROM passwords WHERE username=? AND website=?", (username, website))
# result = c.fetchone()
