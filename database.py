import sqlite3 # loads database library

#The db has only 1 table called "users: with info -> pk, name, email, password (hashed)

conn=sqlite3.connect("hireready.db") # connects to the db file,if it doesn't exist it'll be created
cursor=conn.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS users(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 email TEXT UNIQUE NOT NULL,
                 password_hash TEXT NOT NULL
               )
''')
conn.commit() # saves the changes to the db
conn.close() # closes the connection to the db

# function to add user to the db

def add_user(name, email, password_hash):

    conn = sqlite3.connect("hireready.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users(name, email, password_hash)
            VALUES (?, ?, ?)
            """,
            (name, email, password_hash)
        )
        conn.commit()
        return True
    
    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()

# build login

def get_user(email):
    conn = sqlite3.connect("hireready.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM users
        WHERE email = ?
        """,
        (email,)
    )
    user = cursor.fetchone()
    conn.close()
    return user

