def enterage(age):
	if age < 0:
		raise ValueError("Only positive integers are allowed")

	if age % 2 == 0:
		print("age is even")
	else:
		print("age is odd")

try:
	num = int(input("enter your age:"))
	enterage(num)

except ValueError as ve:
	#print("Only positive integers are allowed")
	print("Exception:",ve)


except:
	print("something is wrong")