from addressbook import *
import mysql.connector

conn = mysql.connector.connect(user='cadmin',password='secret',database='contacts', host='127.0.0.1')
curs = conn.cursor()

def loaddatas(contacts):
	curs.execute("select * from user_info");
	for each in curs.fetchall():
		contacts.append({"firstname":each[0], "lastname": each[1], "phoneno": each[2],"status": "old"});

def saveindb(contacts):
	for each in contacts:
		if each["status"] == "new":
			curs.execute("insert into user_info values('"+each['firstname']+"','"+each['lastname']+"','"+each['phoneno']+"')");
			conn.commit()
		elif each["status"] == "upd":
			curs.execute("update user_info set firstname = '"+each['firstname']+"', lastname = '"+each['lastname']+"' where phoneno = '"+each['phoneno']+"'");
			conn.commit()
		elif each["status"] == "del":
			curs.execute("delete from user_info where phoneno = '"+each['phoneno']+"'");
			conn.commit()

contacts = []
loaddatas(contacts)
while True:
	print ('-' * 67)
	print ('\t\t\tContacts - Address Book')
	print ('-' * 67)
	viewcontacts(contacts)
	print ('1.New\t2.Update\t3.Delete\t4.Save\t0.Exit')
	ch = int(input("Select Choice = "))
	if ch == 1:
		insertcontacts(contacts)
	elif ch == 2:
		phone = input("Phone no to update = ")
		updatecontacts(contacts, phone)
	elif ch == 3:
		phone = input("Phone no to update = ")
		deletecontacts(contacts, phone)
	elif ch == 4:
		saveindb(contacts)
		contacts = []
		loaddatas(contacts)
	else:
		saveindb(contacts)
		print ('Modules Ends')
		break

conn.close()