import timeit

result = [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2 and ((x ** 2)-1)/2 == y and y+1 == z]
timeit.Timer('[(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2 and ((x ** 2)-1)/2 == y and y+1 == z]').timeit(number=1)
print(result)

# list = []
# for x in range(1,400):
# 	for y in range(x,400):
# 		for z in range(y,400):
# 			if x**2 + y**2 == z**2:
# 				if ((x ** 2)-1)/2 == y and y+1 == z:
# 					list.append((x,y,z))

# print(list)

# [(3, 4, 5), (5, 12, 13), (7, 24, 25),.....................]