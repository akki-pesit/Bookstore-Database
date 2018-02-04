import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres1997' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres1997' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)",(item,quantity,price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres1997' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(good):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres1997' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(good,))
    conn.commit()
    conn.close()

def update(item,quantity,price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres1997' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()

create_table()
insert('Orange', 10, 5)
print(view())
#delete('Orange')
update('Mango', 12, 18)
print(view())
'''insert("Wine Glass", 5, 8.5)
insert("Water Glass", 10, 5)
insert("Coffee Cup", 5, 10)
update("Coffee Cup", 10, 12.0)
print(view())'''
