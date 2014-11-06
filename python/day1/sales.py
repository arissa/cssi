price = float(raw_input('Enter the price of the item:'))
if price <= 10:
	discount = price * .1
else:
	discount = price * .2
print 'The price of the item is $%0.2f' %(price - discount)