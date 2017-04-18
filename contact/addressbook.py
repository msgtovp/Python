def insertcontacts(contacts):
	print ('-' * 67)
	print ('\t\t\tInsert Module')
	print ('-' * 67)
	phone = input("Phone No. = ")
	fname = input("First Name = ")
	lname = input("Last Name = ")
	contacts.append({"firstname":fname, "lastname":lname, "phoneno":phone,"status": "new"})
	print ("Inserted Success")
	print ('-' * 67)

def viewcontacts(contacts):
	print ("{0:20} | {1:20} | {2:20}|".format("FirstName","LastName","PhoneNo."))
	print ('-' * 67)
	for each in contacts:
		if each["status"] not in ("del",):
			print ("{firstname:20} | {lastname:20} | {phoneno:20}|".format(**each))
	print ('-' * 67)
	print ('\n'*2)

def updatecontacts(contacts, phoneno):
	print ('-' * 67)
	print ('\t\t\tUpdate Module')
	print ('-' * 67)
	for each in contacts:
		if(each["phoneno"] == phoneno):
			each["status"] = "upd"
			fname = each["firstname"]
			lname = each["lastname"]
			print('1.FirstName\t2.LastName\t*.Exit')
			ch = int(input("\tEnter Choice = "))
			if(ch == 1):
				fname = input("\tFirst Name = ")
			elif(ch == 2):
				lname = input("\tLast Name = ")
			each["firstname"] = fname
			each["lastname"] = lname
			print ("Exist: Updated Success")
			print ('-' * 67)
			return True
	print ("Doen't Exist: Update Failed")
	print ('-' * 67)
	return False

def deletecontacts(contacts, phoneno):
	print ('-' * 67)
	print ('\t\t\tDelete Module')
	print ('-' * 67)
	for each in contacts:
		if(each["phoneno"] == phoneno):
			each["status"] = "del"
			print ("Exist: Deleted Success")
			print ('-' * 67)
			return True
	print ("Doen't Exist: Delete Failed")
	print ('-' * 67)
	return False