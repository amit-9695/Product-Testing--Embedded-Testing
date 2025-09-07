import mysql.connector

mydb=mysql.connector.connect(host='localhost', user='root', password='Amit@123', database='MyDB')

#printing the connection status
print(mydb.is_connected())

cur=mydb.cursor()

create_table_query="""
CREATE TABLE person(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT
    
)
"""

# Inserting value query
insert_data_query="""
INSERT INTO person (name, age) VALUES
('John Doe', 30),
('Jane Smith', 25),
('Alice Johnson', 28)
"""

# SEND REQUEST & EXECUTE REQUEST
cur=mydb.cursor()
cur.execute(create_table_query)
mydb.commit()

cur.execute(insert_data_query)
mydb.commit()

cur.close()
mydb.close()
