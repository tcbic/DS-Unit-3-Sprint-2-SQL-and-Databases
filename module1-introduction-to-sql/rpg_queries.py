import sqlite3

#Load the data.
conn = sqlite3.connect('rpg_db.sqlite3')

#Write queries to explore the data.

#1) How many total Characters are there?

#Create a cursor object.
curs1 = conn.cursor()

#Write the query.

query1 = 'SELECT COUNT(*) FROM charactercreator_character;'

#Execute the query.

curs1.execute(query1)

#2) How many of each specific subclass?

#Create a cursor object.
curs2 = conn.cursor()

#Write the query.

#Execute the query.

#3) How many total items?