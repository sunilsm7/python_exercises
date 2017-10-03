# automorphic number

num = int(int(input("Enter a number:")))

square  = num ** 2
v = pow(10, len(str(num)))

if square % v == num:
    print(num, " is an Automorphic number.")
else:
    print(num, " is not an Automorphic number.")