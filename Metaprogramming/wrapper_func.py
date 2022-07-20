# PROBLEM: You want to put a wrapper layer around a function that adds extra processing

import time
from functools import wraps


def timethis(func):
    """
    Decorator that reports the execution time.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


# Example
@timethis
def countdown(n):
    while n > 0:
        n -= 1


countdown(1000)
