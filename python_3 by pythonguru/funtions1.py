def sum(start, end):
	if(start > end):
		print("start should be less than end")
		return
	result = 0
	for i in range(start, end + 1):
		result +=i
	return result

s = sum(1,10)
print(s)