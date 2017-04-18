import mysql.connector
conn = mysql.connector.connect(user='cadmin',password='secret',database='contacts', host='127.0.0.1')
curs = conn.cursor()
fname = input("Enter First Name = ")
lname = input("Enter Last Name = ")
phone = input("Enter Phone = ")
curs.execute('insert into user_info values(%s,%s,%s)',(fname,lname,phone));
fname = input("Enter First Name = ")
lname = input("Enter Last Name = ")
phone = input("Enter Phone = ")
curs.execute('insert into user_info values(%(fsname)s,%(lsname)s,%(phonen)s)',{"fsname":fname,"lsname":lname,"phonen":phone});
conn.commit()
conn.close()