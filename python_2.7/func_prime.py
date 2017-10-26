def is_prime(num):
    '''
    Naive method of checking for primes. 
    '''
    for n in range(2,num):
        if num % n == 0:
            return 'not prime'
            break
    else: # If never mod zero, then prime
        return 'prime'

num = int(input('Enter a number:'))
result = is_prime(num)
print(result)