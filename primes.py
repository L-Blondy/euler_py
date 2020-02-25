def get_primes(bound):
    notPrime = [0] * (bound + 1)
    notPrime[0] = notPrime[1] = 1
    primes = [2]

    for n in range(3, bound + 1, 2):
        if not notPrime[n]:
            primes += [n]
            for m in range(n**2, bound + 1, n):
                notPrime[m] = 1
    return primes


def get_isPrime(bound):
    isPrime = [1] * (bound + 1)
    isPrime[0] = isPrime[1] = 0

    for n in range(2, bound + 1):
        if isPrime[n]:
            for m in range(n**2, bound + 1, n):
                isPrime[m] = 0
    return isPrime


def sieve(bound):
    notPrime = [0] * (bound + 1)
    notPrime[0] = notPrime[1] = 1
    primes = []

    for n in range(2, bound + 1):
        if not notPrime[n]:
            primes += [n]
            for m in range(n**2, bound + 1, n):
                notPrime[m] = 1
    return primes, notPrime
