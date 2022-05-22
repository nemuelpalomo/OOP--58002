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
                 ('Alexander Graham Bell'),
                 ('Palomo, The Coders')]

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
                 'Telephone',
                 "Lab-9"
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
            (datetime.datetime(1876, 3, 7)),
            (datetime.datetime(2022, 5, 22))]

    description = ['placeholder',
                   """invented a punch-card tabulation machine system for statistical computation. Herman Hollerith's 
great breakthrough was his use of electricity to read, count, and sort punched cards whose holes represented data gathered by the census-takers.""",

                   """Due to overwhelming public demand, we had to add Nikola Tesla to this list. 
Tesla was a genius and much of his work was stolen by other inventors.""",

                   """Tim Berners-Lee is an English engineer and computer scientist who is often credited with inventing the World Wide Web, 
a network that most people use to access the internet.""",

                   """Sir James Dyson is a British inventor and industrial designer who revolutionized vacuum cleaning 
with the invention of the Dual Cyclone, the first bagless vacuum cleaner.""",

                   """Hedy Lamarr is often recognized as an early Hollywood starlet, with film credits such as "Algiers" and "Boom Town." As an inventor, 
Lamarr made significant contributions to radio and technology and systems.""",

                   """Benjamin Franklin was known for being an iconic statesman and a Founding Father. But among his many other accomplishments was the invention of the lightning rod, 
the iron furnace stove or Franklin Stove, bifocal glasses, and the odometer.""",

                   """John Logie Baird is remembered as the inventor of mechanical television (an earlier version of television). 
Baird also patented inventions related to radar and fiber optics.""",

                   """Johannes Gutenberg was a German goldsmith and inventor best known for the Gutenberg press, 
an innovative printing machine that used movable type.""",

                   """Eli Whitney invented the cotton gin in 1794. The cotton gin is a machine that separates seeds, 
hulls, and other unwanted materials from cotton after it has been picked.""",

                   """In 1876 at the age of 29, Alexander Graham Bell invented his telephone. Among one of his first innovations after the telephone was the "photophone," 
a device that enabled sound to be transmitted on a beam of light.""",

            "These are the 10 list of some inventors during the 19th century that made an impact in our today's world"
                   ]




    # Inserting Inventor IDs
    data1 = []
    for i in range(1, 12):
        data1.append((i, f"{inventors[i]}", f"{invention[i]}", f"{date[i]}", f"{description[i]}"))
    print(data1)

    for d in data1:
        record.execute("insert into tblInventor (ID, Inventors, Invention, [Date of Invention], Description) values(?, ?, ?, ?, ?)", d)


    record.commit()
    print("Data is inserted")


except pyodbc.Error as e:
    print("Error in Connection...")