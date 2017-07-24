"""
    for loop
"""
def sum_List(my_list):
    count = 0
    for number in my_list:
        count = count + number
    return count
     
assert sum_List([1,2,3]) == 6
assert sum_List([1,2,3,4]) == 10

print(sum_List([1,2]))