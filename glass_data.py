import mysql.connector

with open("glass.data") as fd:
    ls = []
    for i in fd:
        ls.append(i)
col = str(ls[0]).split(',')
print(col)
col[-1] = col[-1].rstrip()
data = ls[1:]
for i in range(len(data)):
    data[i] = data[i].rstrip()

client = mysql.connector.connect(
    host  = "localhost",
    user = "abc",
    password = "password",
    database="glass"
)

print(client.is_connected())

cur = client.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS glass ")
try:
    cur.execute("CREATE TABLE IF NOT EXISTS new (index_no INT)")
except mysql.connector.Error as e:
        print(f"Error executing query: {e}")


print(col)
for i in col:
    if i == 'index':
        continue
    print(i)
    
    query = f"ALTER TABLE new ADD COLUMN {i} FLOAT"
    print(query)
    try:
        cur.execute(query)
    except mysql.connector.Error as e:
        print(f"Error executing query {query}: {e}")

#print(data)

for i in data:
    query = f"INSERT INTO new VALUES ({i})"
    #
    try:
        cur.execute(query)
    except mysql.connector.Error as e:
        print(f"Error executing query {query}:{e}")
    
client.commit()


cur.execute("SELECT * FROM new")
for i in cur:
    print(i)