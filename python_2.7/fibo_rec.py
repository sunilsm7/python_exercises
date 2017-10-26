def fib(n):
	new_list = []
	""" Fibonacci series using recursion """
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)


result = fib(8)
print(result)
