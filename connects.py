#Connect to the .accdb database

import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Nemuel\Documents\Database1.accdb;')
    print("Database1.accdb is now connected")



except pyodbc.Error as e:
    print("Error in Connection, Please check your code and the correct file extension path.")