items = []
itr = 100
def viewitems(stock):
	print ('*'*75)
	print ('CODE\tNAME\tPRICE\t\tQUANT\tMANF.\t\tEXP.DATE')
	print ('*'*75)
	for each in stock:
		print (each['code']+'\t'+each['name']+'\tRs.'+str(each['price'])+'\t'+str(each['quantity'])+'\t'+each['manufacturer']+'\t\t'+each['expirydate'])

def insertitems(stock):
	item = {}
	global itr;
	item['code'] = 'P'+str(itr)
	itr += 1
	item['name'] = input('item name = ')
	item['price'] = float(input('item price = '))
	item['quantity'] = int(input('item quantity = '))
	item['manufacturer'] =  input('item manufacturer = ')
	item['expirydate'] =  input('item expirydate = ')
	stock.append(item)

viewitems(items)
ch = int(input('choice'))
if(ch == 1):
	insertitems(items)
	viewitems(items)
	insertitems(items)
	viewitems(items)
