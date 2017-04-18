import mysql.connector
conn = mysql.connector.connect(user='cadmin',password='secret',database='contacts', host='127.0.0.1')
curs = conn.cursor()
curs.execute("select firstname from user_info")
print (curs.description)
conn.close()