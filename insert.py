import pyodbc
import datetime

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Nemuel\Documents\Database1.accdb;')

    record = connection.cursor()

    # Inventor Names data array

    inventors = [('placeholder'),
                 ('Herman Hollerith'),
                 ('Nikola Tesla'),
                 ('Tim Berners-Lee'),
                 ('James Dyson'),
                 ('Hedy Lamarr'),
                 ('Benjamin Franklin'),
                 ('John Logie Baird'),
                 ('Johannes Gutenberg'),
                 ('Eli Whitney'),
                 ('Alexander Graham Bell')]

    # Inventions data array
    invention = ['placeholder',
                 'Tabulating Machine',
                 'Tesla coil',
                 'World Wide Web',
                 'Ballbarrow',
                 'Signal Hopping',
                 'Lightning rod, iron furnace stove',
                 'Mechanical Television',
                 'Printing Press Ink',
                 'Cotton Gin',
                 'Telephone'
                 ]

    # Datetime data array

    date = ['placeholder',
            (datetime.datetime(1890, 12, 1)),
            (datetime.datetime(1891, 12, 1)),
            (datetime.datetime(1989, 12, 1)),
            (datetime.datetime(1974, 12, 1)),
            (datetime.datetime(1941, 6, 1)),
            (datetime.datetime(1752, 12, 1)),
            (datetime.datetime(1925, 3, 25)),
            (datetime.datetime(1440, 1, 1)),
            (datetime.datetime(1793, 10, 28)),
            (datetime.datetime(1876, 3, 7))]

    description = ['placeholder',
                   """invented a punch-card tabulation machine system for statistical computation. Herman Hollerith's 
                   great breakthrough was his use of electricity to read, count, and sort punched 
                   cards whose holes represented data gathered by the census-takers.""",

                   """Due to overwhelming public demand, we had to add Nikola Tesla to this list. 
                   Tesla was a genius and much of his work was stolen by other inventors.""",

                   """Tim Berners-Lee is an English engineer and computer scientist who is often credited with inventing the World Wide Web, 
                   a network that most people use to access the internet.""",

                   """Sir James Dyson is a British inventor and industrial designer who revolutionized vacuum cleaning 
                   with the invention of the Dual Cyclone, the first bagless vacuum cleaner.""",

                   """"""
                   ]


    # Inserting Inventor IDs
    data1 = []
    for i in range(1, 11):
        data1.append((i, f"{inventors[i]}", f"{invention[i]}", f"{date[i]}"))
    print(data1)

    for d in data1:
        record.execute("insert into tblInventor (ID, Inventors, Invention, [Date of Invention]) values(?, ?, ?, ?)", d)

    record.commit()
    print("Data is inserted")


except pyodbc.Error as e:
    print("Error in Connection...")