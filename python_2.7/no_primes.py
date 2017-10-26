# Calculation of the prime numbers between 1 and 100 using the sieve of Eratosthenes:
noprimes = [j for i in range(2,8) for j in range(i*2, 100, i)]
primes = [x for x in range(2, 100) if x not in noprimes]
print(primes)