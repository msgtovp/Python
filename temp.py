import mysql.connector
conn = mysql.connector.connect(user='cadmin',password='secret',database='contacts', host='127.0.0.1')
curs = conn.cursor()
fname = input("Enter Username=")
phone = input("Enter Password=")
st = "SELECT * FROM USER_INFO WHERE FIRSTNAME = '"+fname+"' AND PHONENO = '"+phone+"'"
curs.execute(st);
print(curs.fetchall())
conn.commit()
conn.close()