import pyodbc
try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Nemuel\Documents\Database3.accdb;')
    print("Database is connected")

    record = connection.cursor()

    name = 'Nemuel Rico Palomo'
    add = "Bataan"
    contactnumber = '789'
    birthdate1 = '05/07/1999'
    semgrade = 90
    user_id = 6

    record.execute('update Table1 SET Fullname=? WHERE id=?', (name, user_id))
    record.execute('update Table1 SET Address=? WHERE id=?', (add, user_id))
    record.execute('update Table1 SET Birthdate=? WHERE id=?', (birthdate1, user_id))
    record.execute('update Table1 SET Sem=? WHERE id=?', (semgrade, user_id))
    record.execute('update Table1 SET Contact=? WHERE id=?', (contactnumber, user_id))
    record.commit()
    print("Database is updated!")

except pyodbc.Error as e:
    print("Error in Connection")
