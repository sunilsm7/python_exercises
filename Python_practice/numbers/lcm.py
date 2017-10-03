""" find lcm of two numbers.
    
    ex. 
        define function lcm(num1, num2) with 2 parameters.
        def lcm(num1, num2):
            return lcm
        return lcm # do not use print

        input two numbers, out lcm of two.
        num1 = int(input())
        num2 = int(input())
        
"""
def lcm(x,y):
    # write code here
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater %y == 0)):
            lcm = greater

            break
        greater +=1
        print(greater)
    return lcm


# check the code 
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))

print("The LCM of ",num1, "and", num2,"is", lcm(num1,num2))
