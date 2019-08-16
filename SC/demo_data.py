import sqlite3

#Create a connection and cursor.

conn_a = sqlite3.connect('demo_data.sqlite3')
curs1 = conn_a.cursor()

#Create demo table.

create_demo_table = """
CREATE TABLE demo (
s CHAR,
x INTEGER, 
y INTEGER
);
"""

curs1.execute(create_demo_table)

#Insert data into data table.

insert_data1 = """
INSERT INTO demo (s, x, y)
VALUES ('g', 3, 9);
"""

curs1.execute(insert_data1)

insert_data2 = """
INSERT INTO demo (s, x, y)
VALUES ('v', 5, 7);
"""

curs1.execute(insert_data2)

insert_data3 = """
INSERT INTO demo (s, x, y)
VALUES ('f', 8, 7);
"""

curs1.execute(insert_data3)

curs1.close()

conn_a.commit()

#Create another connection.

conn_b = sqlite3.connect('demo_data.sqlite3')

#Count how many rows you have - it should be 3!

curs2 = conn_b.cursor()

query1 = 'SELECT COUNT(*) FROM demo;'

a_1 = curs2.execute(query1).fetchall()

print(a_1)

#How many rows are there where both x and y are at least 5?

curs3 = conn_b.cursor()

query2 = 'SELECT COUNT(*) FROM demo WHERE x >=5 AND y >=5;'

a_2 = curs3.execute(query2).fetchall()

print(a_2)

#How many unique values of y are there 
# (hint - COUNT() can accept a keyword DISTINCT)?

curs4 = conn_b.cursor()

query3 = 'SELECT COUNT(DISTINCT y) FROM demo;'

a_3 = curs4.execute(query3).fetchall()

print(a_3)