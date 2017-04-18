import mysql.connector
conn = mysql.connector.connect(user='admin',password='secret',database='contacts', host='127.0.0.1')
print (conn.get_server_version())
conn.close()