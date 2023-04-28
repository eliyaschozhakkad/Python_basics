import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)

mycursor = mydb.cursor()



mycursor.execute("SELECT * FROM ineuron.fsds")

for i in mycursor:
    print(i)

mycursor.execute("SELECT * FROM ineuron.fsds WHERE firstname = 'nuh' AND studentid = 124")
for i in mycursor:
    print(i)

mycursor.execute("UPDATE ineuron.fsds SET firstname = 'nuha' WHERE studentid = 124")
mydb.commit()

mycursor.execute("UPDATE ineuron.fsds SET class = 'mysql'")
mydb.commit()

mycursor.execute("DELETE FROM ineuron.fsds WHERE lastname = 'p'")
mydb.commit()

mycursor.execute("SELECT MIN(studentid) FROM ineuron.fsds") 
for i in mycursor:
    print(i)

mycursor.execute("SELECT MAX(studentid) FROM ineuron.fsds") 
for i in mycursor:
    print(i)

mycursor.execute("SELECT COUNT(*) FROM ineuron.fsds")
for i in mycursor:
    print(i)

mycursor.execute("UPDATE ineuron.fsds SET class = 'sql' WHERE studentid BETWEEN 123 AND 124")
mydb.commit()

mycursor.execute("UPDATE ineuron.fsds SET class = 'mongodb' WHERE studentid BETWEEN 125 AND 127")
mydb.commit()

mycursor.execute("SELECT COUNT(*),class FROM ineuron.fsds GROUP BY class")
for i in mycursor:
    print(i)

mycursor.execute("DROP TABLE ineuron.fsds")
mydb.commit()

mycursor.execute("DROP DATABASE ineuron")
mydb.commit()