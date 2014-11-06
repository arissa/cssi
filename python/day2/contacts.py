import contact

alice = contact.Contact('Alice', '415-555-1234', 'alice@gmail.com')
bob = contact.Contact('Bob', '609-555-0987', 'bob@yahoo.com')

contacts = [alice,bob]
for c in contacts:
	print c.to_string()
#for k,v in phone_numbers.items():
#	info = all_contact_info[k]

	#print 'Name %s; Phone: %s; Email: %s' % (k.capitalize(), v, email_addresses[k])
	#print info[0]
	#print info[1]