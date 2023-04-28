import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "abc",
    password = "password"
)

mycursor = mydb.cursor()
mycursor.execute("""INSERT INTO ineuron.fsds VALUES (123,'eliyas','ch','2022-11-11','sql','fsds'),
 (124,'nuh','ch','2022-11-11', 'sql','fsds'),
(125,'henna','pk','2022-11-11', 'sql','fsds'),
(126,'fasalu','p','2022-11-11', 'sql','fsds')
""")

mydb.commit()

mycursor.execute("SELECT * FROM ineuron.fsds")

for i in mycursor:
    print(i)

mycursor.execute("SELECT studentid, firstname, class from ineuron.fsds")

for i in mycursor:
    print(i)

mycursor.execute("SELECT * FROM ineuron.fsds WHERE studentid = 126")

for i in mycursor:
    print(i)