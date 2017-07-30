""" find hcf of two numbers.
    
    ex. 
        define function hcf(num1, num2) with 2 parameters.
        def lcm(num1, num2):
            return lcm
        return lcm # do not use print

        input two numbers, out hcf of two.
        num1 = int(input())
        num2 = int(input())
        
"""

def hcf(x,y):
    # write code here
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller+1):
        if((x % i == 0) and(y%i == 0)):
            hcf = i
    return hcf

# test code 
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))

print("The HCF of ",num1, "and", num2,"is", hcf(num1,num2))
