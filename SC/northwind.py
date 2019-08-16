import sqlite3

#Create a connection.

conn = sqlite3.connect('northwind_small.sqlite3')

#What are the ten most expensive items 
#(per unit price) in the database?

curs1 = conn.cursor()

query1 = """
SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""

ten_most_expensive = curs1.execute(query1).fetchall()

print("The ten most expensive items are:", ten_most_expensive)

#What is the average age of an employee at the time of their hiring? 
#(Hint: a lot of arithmetic works with dates.)

curs2 = conn.cursor()

query2 = 'SELECT AVG(HireDate - BirthDate) FROM Employee;'

avg_age = curs2.execute(query2).fetchall()

print("The average age of an employee at the time of their hiring is:", avg_age)

#(Stretch) How does the average age of employee at hire vary by city?

curs3 = conn.cursor()

query3 = 'SELECT AVG(HireDate - BirthDate), City FROM Employee GROUP BY City;'

avg_age_by_city = curs3.execute(query3).fetchall()

print("The average age of an employee at the time of their hiring by city is:", avg_age_by_city)

#What are the ten most expensive items (per unit price) 
#in the database and their suppliers?

#Need Product and Supplier tables.

curs4 = conn.cursor()

query4 = """
SELECT ProductName, UnitPrice, CompanyName
FROM Product
LEFT JOIN Supplier
ON Product.SupplierID = Supplier.ID
ORDER BY UnitPrice DESC
LIMIT 10;
"""

ten_most_expensive_supplier = curs4.execute(query4).fetchall()

print("The ten most expensive items and their suppliers are:", ten_most_expensive_supplier)

#What is the largest category 
#(by number of unique products in it)?

#Need Product and Category tables.

curs5 = conn.cursor()

query5 = """
SELECT CategoryName, COUNT(DISTINCT Product.ID)
FROM Category
LEFT JOIN Product
ON Category.ID = Product.CategoryID
GROUP BY CategoryID
ORDER BY COUNT(DISTINCT Product.ID) DESC
LIMIT 1;
"""

largest_category = curs5.execute(query5).fetchall()

print("The largest category by unique products is:", largest_category)

#(Stretch) Who's the employee with the most territories? 
#Use TerritoryId (not name, region, or other fields) 
#as the unique identifier for territories.

#Need Employee and Territory tables.

curs6 = conn.cursor()

query6 = """
SELECT EmployeeID, LastName, FirstName, COUNT(DISTINCT TerritoryID)
FROM Employee AS e, Territory AS t,
EmployeeTerritory AS et
WHERE e.ID = et.EmployeeID AND
t.ID = et.TerritoryID
GROUP BY EmployeeID
ORDER BY COUNT(DISTINCT TerritoryID) DESC
LIMIT 1;
"""

emp_most_territories = curs6.execute(query6).fetchall()

print("The employee with the most territories is:", emp_most_territories)