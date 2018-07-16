import sqlite3
connection = sqlite3.connect("higgsEXO.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM request") 
print("fetchall:")
result = cursor.fetchall() 
for r in result:
    print(r)
cursor.execute("SELECT * FROM request") 
print("\nfetch one:")
res = cursor.fetchone() 
print(res)
