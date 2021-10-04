import sqlite3

#connect to database

conn=sqlite3.connect('movies.db')

#create a cursor

c =conn.cursor()

#Query the database

c.execute("SELECT rowid, * FROM movies")

items = c.fetchall()

print("Number\t| Movie Name\t\t\t| Lead Actor\t\t| Lead Actress\t\t\t| Year of Release| Director")
print("-------------------------------------------------------------------------------------------------------------------------------")

for item in items:
    print(str(item[0]) + "\t|"+ str(item[1]) + "\t|" + str(item[2]) + "\t|" + str(item[3]) + "\t|"+ str(item[4]) + "\t\t |" + str(item[5]))



#commit our commnd

conn.commit()

#close our connection

conn.close()