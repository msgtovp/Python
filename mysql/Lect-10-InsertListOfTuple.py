import mysql.connector
conn = mysql.connector.connect(user='cadmin',password='secret',database='contacts', host='127.0.0.1')
curs = conn.cursor()
qry = "insert into user_info values(%s,%s,%s)"
data = [('Vijay','Prakash','9876543210'),('Steve','Jobs','9876543211')]
curs.executemany(qry, data)
conn.commit()
qry = "insert into user_info values(%(fname)s,%(lname)s,%(phone)s)"
data = [{"fname":'Shiva',"lname":'Sakthi',"phone":'9876543222'},{"fname":'Guido van',"lname":'Rossum',"phone":'9876543212'}]
curs.executemany(qry, data)
conn.commit()
conn.close()