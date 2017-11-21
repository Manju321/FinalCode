"""Using Python 3.6

Ans for 11th Program
Write a program that can make a connection to the a database and execute a SQL query (SELECT * FROM EMPLOYEE), and prints all the employee names (Assume that there is an employee table with columns ID,NAME,ADDRESS) – Pseudo code would suffice.

"""

import MySQLdb   # assuming mysql db

db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='test')
cur = db.cursor()
cur.execute('SELECT * FROM EMPLOYEE')

# print first and second columns for each row
for row in cur.fetchall():
    print(row[0], row[1])

