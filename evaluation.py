stack = []

def pushstack(st, elem):
	st.append(elem)

def popstack(st):
	return st.pop()

def peekstack(st):
	if(len(st) == 0):
		return None;
	return st[-1]

exp = input("Enter RPN = ")
itr = 0
while itr < len(exp):
	if (exp[itr].isdigit()):
		pushstack(stack, int(exp[itr]))
	elif (exp[itr] in ('+', '-', '*', '/', '%')):
		val1 = popstack(stack)
		val2 = popstack(stack)
		if (exp[itr] == '+'):
			pushstack(stack, val2+val1)
		elif (exp[itr] == '-'):
			pushstack(stack, val2-val1)
		elif (exp[itr] == '*'):
			pushstack(stack, val2*val1)
		elif (exp[itr] == '/'):
			pushstack(stack, val2/val1)
		elif (exp[itr] == '%'):
			pushstack(stack, val2%val1)
	else:
		break
	itr += 1

print (peekstack(stack))
