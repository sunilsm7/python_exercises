"""
    Write function fibonacci
    input: number
"""

def fibonacci(num):
    result = []
    a, b = 0, 1
    while a < num:
        result.append(a)
        a, b = b, a+b
    return result

data = int(input("Enter the upper limit:"))
print(fibonacci(data))
