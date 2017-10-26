
# create another example generator which calculates fibonacci numbers:

def gen_fibo(n):
	''' generate fibonacci series upto n'''
	a,b = 0,1
	for i in range(n):
		yield a
		a , b= b, a+b

# for num in gen_fibo(8):
# 	print(num)
