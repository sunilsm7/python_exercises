global_var  = 12

def func():
	local_var = 100
	print(global_var)

func()
#print(local_var) we can't access local_var outside function