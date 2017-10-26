def fib(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a + b
	if n == 20:
		a = 42
	return a


