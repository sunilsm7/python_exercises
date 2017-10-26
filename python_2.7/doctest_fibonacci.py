import doctest

def fib(n):
	"""calculates fibonacci series iteratively
		>>> fib(0)
		0
		>>> fib(1)
		1
		>>> fib(15)
		610
		>>> fib(10)
		55

	"""
	a, b = 0, 1
	for i in range(n):
		a, b = b, a + b
	return a


if __name__ == "__main__":
	doctest.testmod()
	print('ok')
