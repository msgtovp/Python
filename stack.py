stack = []

def pushstack(st, elem):
	st.append(elem)

def popstack(st):
	return st.pop()

def peekstack(st):
	if(len(st) == 0):
		return None;
	return st[-1]

while(True):
	print ('1.Push\n2.Pop\n3.Peek\n4.Traverse')
	ch = int(input("Choice = "))
	if (ch == 1):
		elem = int(input("Enter the element = "))
		pushstack(stack, elem)
	elif (ch == 2):
		print (popstack(stack))
	elif (ch == 3):
		print (peekstack(stack))
	elif (ch == 4):
		print (stack[::-1])
	else:
		break
