# *args example

def sum(*args):
	s = 0
	for i in args:
		s += i
	print("sum is ", s)

sum(1, 2, 3)

# **kwargs example

def my_func(**kwargs):
	for i,j in kwargs.items():
		print(i,j)

my_func(name='tim', sport='football', roll=19)

# Using *args and **kwargs in function call

def my_three(a, b, c):
	print(a, b, c)

a = [1,2,3]
my_three(*a) # here list is broken into three elements


def my_two(a, b):
	print(a, b)

a = {'a': "one", 'b': "two", 'c': "three" }
my_two(**a)