#  amicable numbers
def amicable_numbers(x,y):
    sum_x = 0
    sum_y = 0
    for i in range(1, x):
        if x % i ==0:
            sum_x += i
    
    for k in range(1, y):
        if y%k == 0:
            sum_y += k
    
    return sum_x == y and sum_y == x

# main body 
num1 = int(input('Enter number 1:'))
num2 = int(input('Enter number 2:'))

# check number is amicable or not

if amicable_numbers(num1, num2):
    print("the numbers are Amicable")
else:
    print("the numbers are not Amicable")