import logging

from functools import wraps

logging.basicConfig(level=logging.DEBUG)

def timed(original_function):
    import time

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        time_start = time.time()
        result = original_function(*args, **kwargs)
        time_elapsed = (time.time() - time_start) / 1000

        logging.info( "Execution time {}{} is {} seconds".format(original_function.__name__,args,time_elapsed) )
        return result

    return wrapper

def logged(original_function):
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        logging.debug( "Entering {}{}".format(original_function.__name__,args) )
        result = original_function(*args, **kwargs)
        logging.debug( "Exiting {} = {}".format(original_function.__name__,result) )
        return result
    
    return wrapper

# Solution 1 - Explicitly wrap function 

# logged_add = logged(add)
# logged_sub = logged(sub)

# logged_add(3,5)
# logged_sub(4,3)

# Solution 2 - Use decorator-like syntax 

# Using decorators is equivalent to
# augmented_add = logged( timed( add ))
# augmented_add(2,3)

@logged
@timed
def add(a,b):
    return a+b

@logged
@timed
def sub(a,b):
    return a-b

add(3,5)
sub(4,3)

