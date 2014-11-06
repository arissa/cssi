speed = int(raw_input('Enter speed: '))
mood = raw_input('Enter mood: ')

if speed >= 80:
	print 'License and registration please.'
	if mood == 'terrible' or speed >= 100:
		print 'You have the right to remain silent.'
	elif mood == bad and speed >= 90:
		print 'I am going to have to write you a ticket.'
	else:
		print 'Let\'s try to keep it under 80, ok?'
