import sqlite3
conn=sqlite3.connect('MitMorn.db')
print("Open database Successfully")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (1,'ERICK',30,'eMobilis','Male')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (2,'PURITY',20,'Kenya high','Female')")

conn.commit()
print("Recodrs addded successfull")
conn.close()