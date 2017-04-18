import mysql.connector
conn = mysql.connector.connect(user='cadmin',password='secret',database='contacts', host='127.0.0.1')
curs = conn.cursor()
curs.execute("select * from user_info")
print (curs.rowcount)
print (curs.fetchall())
print (curs.rowcount)

conn.commit()
conn.close()