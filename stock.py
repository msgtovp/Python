items = [
{'code': 'P001', 'name': 'shampoo', 'price': 125.00, 'quantity': 10, 'manufacturer': 'Hindustan', 'expirydate': '12-12-2016' }
]
def viewitems(stock):
	print ('CODE\tNAME\tPRICE\t\tQUANT\tMANF.\t\tEXP.DATE')
	for each in stock:
		print (each['code']+'\t'+each['name']+'\tRs.'+str(each['price'])+'\t'+str(each['quantity'])+'\t'+each['manufacturer']+'\t\t'+each['expirydate'])

def insertitems(stock):
	item = {}
	item['code'] = input('item code = ')
	item['name'] = input('item name = ')
	item['price'] = float(input('item price = '))
	item['quantity'] = int(input('item quantity = '))
	item['manufacturer'] =  input('item manufacturer = ')
	item['expirydate'] =  input('item expirydate = ')
	stock.append(item)

print ('*'*75)
viewitems(items)
print ('*'*75)
ch = int(input('choice'))
if(ch == 1):
	insertitems(items)
	viewitems(items)
