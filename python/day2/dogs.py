class Pet(object):
	def AddTrick(self, trick):
		self.tricks.append(trick)


class Dog(Pet):
	def __init__(self, name):
		self.name = name
		self.tricks = []
	def Bark(self):
		print '%s says woof' %self.name

class Cat(Pet):
	def __init__(self):
		self.tricks = []

dug = Dog('Dug')
dug.AddTrick('talk')
#print dug.tricks

kitty = Cat()
kitty.AddTrick('climb')
#print kitty.tricks

pets = [dug, kitty]
for pet in pets:
	pet.AddTrick('rollover')
	print pet.tricks