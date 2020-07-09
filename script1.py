import psycopg2


def create_table():
    con = psycopg2.connect("dbname = 'database1' user='postgres' password='Mysql#123' host='localhost' port = '5432' ")
    cur = con.cursor()
    cur.execute("CREATE TABLE if NOT EXISTS data(item TEXT, quantity integer, prices REAL)")
    con.commit()
    con.close()


def insert(item, quantity, price):
    con = psycopg2.connect("dbname = 'database1' user='postgres' password='Mysql#123' host='localhost' port = '5432' ")
    cur = con.cursor()
    # cur.execute("INSERT INTO data VALUES('%s','%s','%s')" %(item, quantity, price))
    cur.execute("INSERT INTO data VALUES(%s,%s,%s)", (item, quantity, price))
    con.commit()
    con.close()


# insert("Beer", 50, 5.5)


def view():
    con = psycopg2.connect("dbname = 'database1' user='postgres' password='Mysql#123' host='localhost' port = '5432' ")
    cur = con.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    con.close()
    return rows


def delete(item):
    con = psycopg2.connect("dbname = 'database1' user='postgres' password='Mysql#123' host='localhost' port = '5432' ")
    cur = con.cursor()
    cur.execute("DELETE FROM data WHERE item=%s", (item,))
    con.commit()
    con.close()


def update(quantity, price, item):
    con = psycopg2.connect("dbname = 'database1' user='postgres' password='Mysql#123' host='localhost' port = '5432' ")
    cur = con.cursor()
    cur.execute('UPDATE data SET quantity=%s, prices=%s WHERE item=%s', (quantity, price, item))
    con.commit()
    con.close()


# insert("Wine", 20, 15.5)
# create_table()
# delete('Wine')
# update(30, 15.5, 'Beer')
#
print(view())
