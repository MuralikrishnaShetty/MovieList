import sqlite3

# connect to database

conn = sqlite3.connect('movies.db')

#create a cursor

c = conn.cursor()

#create a table

c.execute("""CREATE TABLE movies (
            name text,
            lead_actor text,
            lead_actress text,
            year_of_release integer,
            director text
            ) """)

#Adding records into the table

an =[
    ('Pyaar Ka Punchnama         ','Kartik Aaryan        ','Nushrratt Bharuccha     ',2011,'Luv Ranjan'),
    ('Pyaar Ka Punchnama 2       ','Kartik Aaryan        ','Nushrratt Bharuccha     ',2015,'Luv Ranjan'),
    ('Guest iin London           ','Kartik Aaryan        ','Kriti Kharbanda         ',2017,'Ashwni Dhir'),
    ('Luka Chuppi                ','Kartik Aaryan        ','Kriti Sanon             ',2019,'Laxman Utekar'),
    ('Googly                     ','Yash                 ','Krithi Kharbanda        ',2013,'Pavan Wadeyar'),
    ('Gajakesari                 ','Yash                 ','Amulya                  ',2014,'Krishna'),
    ('Mr and Mrs Ramachari       ','Yash                 ','Radika Pandit           ',2014,'Santhosh Anandram'),
    ('K.G.F Chapter 1            ','Yash                 ','Srinidhi Shetty         ',2018,'Prashanth Neel'),
    ('Santhu Straight Forward    ','Yash                 ','Radika Pandit           ',2016,'Mahesh Rao'),
    ('Red                        ','Ram Pothineni        ','Malvika Sharma          ',2021,'Kishore Tirumala'),
    ('Hello Guru Prema Kosame    ','Ram Pothineni        ','Anupama Parameswaran    ',2018,' Trinadha Rao Nakkina'),
    ('Kirik Party                ','Rakshit Shetty       ','Rashmika Mandanna       ',2016,'Rishab Shetty')
    ]

c.executemany("INSERT INTO movies VALUES (?,?,?,?,?)",an)

print("update done")


#commit our commnd

conn.commit()

#close our connection

conn.close()
