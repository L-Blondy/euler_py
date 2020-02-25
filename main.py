import numpy as np
from math import sqrt
from utils import chrono
<<<<<<< HEAD
from primes import get_primes, get_isPrime
from itertools import product
=======


@chrono
def countTo(bound):
    c = 0
    for i in range(bound):
        c += 1
    return c


countTo(1000000)

//test
>>>>>>> 8e5b859236e4357c7249a0db30c6ab359bdaf195
