import sqlite3
 
table_connect = sqlite3.connect('billing.db')
curs = table_connect.cursor()

# curs.execute("""CREATE TABLE customer(
#              first_name text,
#              last_name text,
#              product text,
#              stock_amount int
# )""")

# curs.execute("INSERT INTO customer VALUES ('Ram','Shankar','Juice',23)")
# curs.execute("INSERT INTO customer VALUES ('Immanel','Jackson','Bread',35)")
# curs.execute("INSERT INTO customer VALUES ('Ahmed','Suhai','Tea',100)")

curs.execute("SELECT * FROM customer")
print(curs.fetchall())

table_connect.commit()
table_connect.close()