import mysql.connector

eli = mysql.connector.connect(
    host = "localhost",
    user = 'abc',
    password = 'password'
)

cur = eli.cursor()
#cur.execute("USE fsds_db")
cur.execute("select * from fsds_db.fsds1")

for i in cur:
    print(i)