li = []

def pushstack(li, elem):
	li.append(elem)

def popstack(li):
	return li.pop()

def stackisempty(li):
	if(len(li) == 0):
		return True
	return False

def peek(li):
	if(len(li) == 0):
		return '(';
	return li[-1]

def optprec(ch):
	if (ch == ')'):
		return 7
	elif (ch == '%' or ch == '*' or ch == '/'):
		return 6
	elif (ch == '+' or ch == '-'):
		return 5
	elif (ch == '&'):
		return 4
	elif (ch == '^'):
		return 3
	elif (ch == '|'):
		return 2
	elif (ch == '('):
		return 1
	else:
		return 0

exp = input('Enter Infix : ')
itr = 0;
out = [];

while( itr < len(exp)):
	if(exp[itr] == '('):
		pushstack(li, exp[itr])
	elif (exp[itr].isdigit()):
		pushstack(out, exp[itr])
	elif (exp[itr] == ')'):
		while(peek(li) != '(' ):
			pushstack(out, popstack(li))
		popstack(li)
	else:
		while(optprec(peek(li)) >= optprec(exp[itr])):
			pushstack(out, popstack(li))
		pushstack(li, exp[itr])
	itr += 1

while (stackisempty(li) == False):
	pushstack(out, popstack(li))

print (out)