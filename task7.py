import sqlite3
def get_total_stock_value():
    conn=sqlite3.connect('shop.db')
    c=conn.cursor()
    c.execute('SELECT SUM(price*quantity) FROM products')
    result=c.fetchone()
    print('Total = ', *result)
    conn.close()
get_total_stock_value() 