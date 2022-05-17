import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Nemuel\Documents\Database3.accdb;')

    user_id = 6
    record = connection.cursor()
    record.execute('delete from Table1 WHERE id=?', (user_id))
    record.commit()
    print("Data is deleted")


except pyodbc.Error as e:
    print("Error in Connection...")