import sqlite3
from sqlite3 import Error
from sqlite3.sqlite_connection import create_connection

def create_table(con):
    """Create the table with given columns"""
    try:
        cur=con.cursor()
        cur.execute('''CREATE TABLE employees(
        id INTEGER PRIMARY KEY,
        name TEXT,
        surname TEXT,
        department TEXT,
        position TEXT,
        salary REAL,
        date TEXT);''')
        con.commit()
        print('The table is created successfully')
    except Error:
        print(Error)
        
create_table(create_connection())
         