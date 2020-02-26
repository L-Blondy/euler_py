from math import sqrt
from utils import chrono
from primes import getPrimes, isPrime, sieve
from itertools import product

primes, isP = sieve(1000000)


def getK(n):
    sum_divisors = 0
    len_divisors = 0
    N = n

    for p in primes:
        if p > n**0.5 and n != 1:
            len_divisors += 1
            sum_divisors += n
            break

        while n % p == 0:
            n //= p
            sum_divisors += p
            len_divisors += 1
    return len_divisors + N-sum_divisors


@chrono
def loop(kBound):
    highest_K = 0
    tot = 0

    for n in range(4, 1000000):

        if isP[n]:
            continue

        k = getK(n)
        if k > highest_K:
            highest_K = k
            tot += n
        if k >= kBound:
            return tot


print(loop(12))
# print(getK(10))
