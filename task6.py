import sqlite3
def delete_product(product_id):
    conn=sqlite3.connect('shop.db')
    c=conn.cursor()
    c.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()
    print('Product deleted')
delete_product(3)