import mysql.connector
conn = mysql.connector.connect(user='cadmin',password='secret',database='contacts', host='127.0.0.1')
curs = conn.cursor()
curs.execute('create table if not exists log(id int, name varchar(256))');
conn.commit()
conn.close()