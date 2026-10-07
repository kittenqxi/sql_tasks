import sqlite3
def get_products_cheaper_than(price):
    conn=sqlite3.connect('shop.db')
    c=conn.cursor()
    c.execute('SELECT id, name, price, quantity FROM products WHERE price<?', (price,))
    filt_pr=c.fetchall()
    for i in filt_pr:
        print(*i)
    conn.close
get_products_cheaper_than(100.00)