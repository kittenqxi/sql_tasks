import sqlite3
def update_price(product_id, new_price):
    conn=sqlite3.connect('shop.db')
    c=conn.cursor()
    c.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
    conn.commit()
    conn.close()
    print('Product price updated')
update_price(2, 30.00)    