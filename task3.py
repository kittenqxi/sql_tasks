import sqlite3
conn=sqlite3.connect('shop.db')
c=conn.cursor()
c.execute('SELECT id, name, price, quantity FROM products')
products=c.fetchall()
for i in products:
    print(*i)
    conn.close()