t = 1

def increment():
	global t
	#global = 100 this is error
	t =100
	t = t + 1
	print("inside function",t)

increment()
print("outside function",t)