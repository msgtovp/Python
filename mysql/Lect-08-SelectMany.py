import mysql.connector
conn = mysql.connector.connect(user='cadmin',password='secret',database='contacts', host='127.0.0.1')
curs = conn.cursor()
curs.execute("select * from log");
dbdata = curs.fetchmany(1)
for i in dbdata:
	print (str(i[0])+" ==> "+i[1])

conn.close()