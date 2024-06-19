#inserting data into the table
import sqlite3

conn = sqlite3.connect('test.db')
print("Success")

conn.execute("INSERT INTO TEACHERS VALUES (1,'James','kariuki',45,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES (2,'Fiona','Nkatha',18,70000.00)")
conn.execute("INSERT INTO TEACHERS VALUES (3,'Vivy','Twinn',18,60000.00)")
conn.execute("INSERT INTO TEACHERS VALUES (4,'Lewis','kariuki',27,50000.00)")
conn.execute("INSERT INTO TEACHERS VALUES (5,'Victor','Loishoru',19,560000.00)")
conn.execute("INSERT INTO TEACHERS VALUES (6,'Frank','Loipari',15,90000.00)")

conn.commit()
print("Successfully inserted records")

conn.close()