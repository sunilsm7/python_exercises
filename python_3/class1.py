class Person:
	# constructor or initializer
	def __init__(self, name):
		self.name = name # name is data field also commonly known as instance variables

	# method which returns a string
	def whoami(self):
		return "You are " + self.name

p1 = Person('tom') # now we have created a new perosn object p1
print(p1.whoami())
print(p1.name)
p1.name = 'jerry'
print(p1.name)