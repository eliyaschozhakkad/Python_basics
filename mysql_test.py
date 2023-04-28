import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = 'abc',
    password = 'password'
)

print(mydb.is_connected())
#print(mydb)

cur = mydb.cursor()
#print(cur)
cur.execute("SHOW DATABASES")
for i in cur:
    print(i)