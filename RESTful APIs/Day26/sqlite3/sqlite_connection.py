import sqlite3
from sqlite3 import Error

def create_connection():
    # Creating a connection with sqlite database
    try:
        db= sqlite3.connect('example.db')
        return db
    except Error:
        print("Error while connecting to database")
        
db_connection = create_connection()
if db_connection:
    print("Connection to SQLite DB successful")
else:
    print("Failed to connect to SQLite DB")