import mysql.connector

eli = mysql.connector.connect(
    host = "localhost",
    user = 'abc',
    password = 'password'
)

cur = eli.cursor()

#cur.execute("CREATE DATABASE fsds_db")
cur.execute("USE fsds_db")
#cur.execute("CREATE TABLE fsds1 (name VARCHAR(40),roll_no INT,mail_id VARCHAR(50))")

cur.execute("INSERT INTO fsds1 VALUES('eliyas',1234,'eliyasch@gmail.com')")
eli.commit()
