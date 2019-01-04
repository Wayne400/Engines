import sqlite3

conn = sqlite3.connect('hornet_register.db')
cursor = conn.cursor()
sql = "select * from hornets"
results = cursor.execute(sql)
all_hornets = results.fetchall()
for hornet in all_hornets:
   print hornet