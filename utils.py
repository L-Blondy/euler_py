from time import time
from math import ceil


def chrono(fun):
    def with_chrono(*args, **kwargs):
        start = time()
        result = fun(*args, **kwargs)
        elapsed = ceil((time()-start)*1000)
        print(
            "\n==============================",
            "\n{} was executed in {}ms".format(fun.__name__, elapsed),
            "\n=============================="
        )
        return result
    return with_chrono
