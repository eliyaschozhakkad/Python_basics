import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE ineuron.fsds (studentid INT, firstname VARCHAR(50), lastname VARCHAR(50), registrationdate DATE,class VARCHAR(20), course VARCHAR(50))")