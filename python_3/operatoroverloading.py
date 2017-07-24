import math

class Circle:

	def __init__(self, radius):
		self.__radius = radius

	def setRadius(self, radius):
		self.__radius = radius

	def getRadius(self):
		return self.__radius

	def area(self):
		return math.pi * sel.__radius ** 2

	def __add__(self, another_circle):
		return Circle(self.__radius + another_circle.__radius)

	def __mul__(self, another_circle):
		return Circle(self.__radius * another_circle.__radius)

	def __gt__(self, another_circle):
		return self.__radius > another_circle.__radius

	def __lt__(self, another_circle):
		return self.__radius < another_circle.__radius

	def __str__(self):
		return "Circle with radius " + str(self.__radius)

c1 = Circle(4)
print(c1.getRadius())

c2 = Circle(5)
print(c2.getRadius())

c3 = c1 + c2  # this became possible we have overloaded + operator by adding a method __add__
print(c3.getRadius())

print(c1 < c2)
print(c3 > c1)
print(c3)

c4 = c1 * c2
print(c4.getRadius())