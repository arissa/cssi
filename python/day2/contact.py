class Contact (object):
	def __init__(self, name, phone, email):
		self.name = name
		self.phone = phone
		self.email = email

	def to_string(self):
		return 'Name: %s; Phone: %s; Email: %s' %(self.name, self.phone, self.email)