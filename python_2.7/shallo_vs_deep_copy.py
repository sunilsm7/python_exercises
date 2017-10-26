# Python code to demonstrate copy operations

# importing "copy" for copy operations
import copy

# initializing list 1
li1 = [1, 2, [3,5], 4]

# using copy to shallow copy 
li2 = copy.copy(li1)

# original elements of list
print ("The original elements before shallow copying")
for i in range(0,len(li1)):
	print (li1[i], end= " ")

print("\r")

# adding and element to new list
li2[0] = 17 # change will be not reflected in original list
li2[2][0] = 7 # change will be reflected in original list

# checking if change is reflected
print ("The original elements after shallow copying")
for i in range(0,len( li1)):
	print (li1[i], end= " ")
