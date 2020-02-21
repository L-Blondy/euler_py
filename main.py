import sys
from utils import chrono


@chrono
def countTo(bound):
    c = 0
    for i in range(bound):
        c += 1
    return c


countTo(1000000)
