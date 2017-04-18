import mysql.connector
conn = mysql.connector.connect(user='cadmin',password='secret',database='contacts', host='127.0.0.1')
curs = conn.cursor()
curs.execute("insert into log values(1,'Vijay')");
conn.commit()
conn.close()