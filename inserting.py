import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Nemuel\Documents\Database3.accdb;')

    user_id_6 = 6

    record = connection.cursor()
    record.execute("insert into Table1(ID) values (6)")
    record.commit()
    print("Data is inserted")


except pyodbc.Error as e:
    print("Error in Connection...")