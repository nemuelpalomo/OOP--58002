import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Nemuel\Documents\Database1.accdb;')

    user_id = 6
    record = connection.cursor()
    record.execute('delete from tblInventor WHERE id=0')
    record.execute('delete from tblInventor WHERE id=1')
    record.execute('delete from tblInventor WHERE id=2')
    record.execute('delete from tblInventor WHERE id=3')
    record.execute('delete from tblInventor WHERE id=4')
    record.execute('delete from tblInventor WHERE id=5')
    record.execute('delete from tblInventor WHERE id=6')
    record.execute('delete from tblInventor WHERE id=7')
    record.execute('delete from tblInventor WHERE id=8')
    record.execute('delete from tblInventor WHERE id=9')
    record.execute('delete from tblInventor WHERE id=10')
    record.execute('delete from tblInventor WHERE id=11')
    record.execute('delete from tblInventor WHERE id=12')
    record.execute('delete from tblInventor WHERE id=13')
    record.execute('delete from tblInventor WHERE id=14')
    record.execute('delete from tblInventor WHERE id=15')
    record.execute('delete from tblInventor WHERE id=16')
    record.execute('delete from tblInventor WHERE id=17')
    record.execute('delete from tblInventor WHERE id=18')
    record.execute('delete from tblInventor WHERE id=19')
    record.execute('delete from tblInventor WHERE id=20')
    record.execute('delete from tblInventor WHERE id=21')
    record.commit()
    print("Data is deleted")


except pyodbc.Error as e:
    print("Error in Connection...")