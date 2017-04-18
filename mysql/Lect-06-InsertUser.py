import mysql.connector
conn = mysql.connector.connect(user='cadmin',password='secret',database='contacts', host='127.0.0.1')
curs = conn.cursor()
ids = input("Enter Your id = ")
name = input("Enter Your Name = ")
curs.execute("insert into log values("+ids+",'"+name+"')");
conn.commit()
print ("Success - Saved");
conn.close()