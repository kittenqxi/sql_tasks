import sqlite3
conn=sqlite3.connect('shop.db')
c=conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
price REAL NOT NULL,
quantity INTEGER DEFAULT 0
)
''')
conn.commit()
conn.close()
print('Database and table created')