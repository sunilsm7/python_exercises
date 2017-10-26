from copy import deepcopy

list1 = ['a','b',['c','d','e']]
list2 = deepcopy(list1)

list2[2][1] = 'x'
list2[0] = 'z'

print(list1)
print(list2)
