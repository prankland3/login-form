import sqlite3

DB_NAME = "database.db"
conn = sqlite3.connect(DB_NAME)

cur = conn.cursor()

# Create the table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    firstname TEXT NOT NULL, 
    lastname TEXT NOT NULL, 
    username TEXT NOT NULL, 
    email TEXT NOT NULL, 
    password TEXT NOT NULL, 
    user_logo BLOB NOT NULL 
)
""")

# Check if the table was created successfully
cur.execute("""
SELECT name FROM sqlite_master WHERE type='table' AND name='users'
""")
table_exists = cur.fetchone()

if table_exists:
    print("The 'users' table was created successfully.")
else:
    print("Failed to create the 'users' table.")

conn.commit()
cur.close()
conn.close()