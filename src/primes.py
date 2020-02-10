from math import sqrt

# naive solution that counts all multiples


def find_primes(num):
    primes = []
    for i in range(2, num):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
            print(is_prime, i, j)
        if is_prime is True:
            primes.append(i)
    return primes

# sieve of eratosthenes


def sieve(n):
    primes = [True for i in range(n)]
    primes[0] = primes[1] = False

    for i in range(2, int(sqrt(n))):
        for j in range(i * i, n, i):
            primes[j] = False
    return [i for i in range(n) if primes[i] is True]


print(sieve(20))
