queue = []

def nqueue(qu, elem):
	qu.append(elem)

def dqueue(qu):
	return qu.pop(0)

def peekrearqueue(qu):
	if(len(qu) == 0):
		return None;
	return qu[-1]

def peekfrontqueue(qu):
	if(len(qu) == 0):
		return None;
	return qu[0]

while(True):
	print ('1.NQ\n2.DQ\n3.Peek Front\n4.Peek Rear\n5.Traverse')
	ch = int(input("Choice = "))
	if (ch == 1):
		elem = int(input("Enter the element = "))
		nqueue(queue, elem)
	elif (ch == 2):
		print (dqueue(queue))
	elif (ch == 3):
		print (peekfrontqueue(queue))
	elif (ch == 4):
		print (peekrearqueue(queue))
	elif (ch == 5):
		print (queue)
	else:
		break
