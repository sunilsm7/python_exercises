# prime numbers upto n

num = int(input("Enter a number:"))
print("\n Prime numbers: ")
for i in range(1, (num+1)):
    flag =0
    for j in range(2, i):
        if i%j == 0:
            flag = 1
            break
    if(flag == 0):
        print(i, end = ' ')

