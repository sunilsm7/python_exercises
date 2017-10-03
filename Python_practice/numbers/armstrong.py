"""
An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. 
For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371. 

Solution:
input : num
initialize sum = 0 
find the sum of the cube of each digit in num

compare num and sum, if num == sum then it's armstrong number
"""

num = int(input('Enter a number:'))

# initialize sum
sum = 0

# find the sum of  cubes of each digits
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
