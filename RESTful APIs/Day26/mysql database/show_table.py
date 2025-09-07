import mysql.connector

mydb=mysql.connector.connect(host='localhost', user='root', password='Amit@123', database='MyDB')

#printing the connection status
print(mydb.is_connected())

cur=mydb.cursor()

# Sql SELECT query to show the table
show_table_query = """SELECT * FROM person
"""
# SEND REQUEST & EXECUTE REQUEST
cur.execute(show_table_query)


# Fetch all rows from the executed query
rows = cur.fetchall()
# Print the rows
for row in rows:
    print(row)


cur.close()
mydb.close()