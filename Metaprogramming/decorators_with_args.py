# You want to write a decorator function that takes arguement

from functools import wraps
import logging


def logged(level, name=None, message=None):
    """Add logging to a function

    Args:
        level (str): the logging level,
        name (str, optional): Defaults to None. name is the logger name
        message (str, optional): Defaults to None. Log message
        If the name and message aren't specified ,
        the default to the function's module and name
    """

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            print(func.__name__, logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorate


# Example of use case
@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, "example")
def spam():
    print("spam!")
